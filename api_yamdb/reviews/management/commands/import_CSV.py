import csv

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title, TitleGenre


DIRECTORY = 'static/data/'
User = get_user_model()
NAMES_FILE = {
    'category.csv': "self.category(csv_reader)",
    'genre.csv': "self.genre(csv_reader)",
    'users.csv': "self.user(csv_reader)",
    'titles.csv': "self.title(csv_reader)",
    'review.csv': "self.review(csv_reader)",
    'comments.csv': "self.comment(csv_reader)",
    'genre_title.csv': "self.title_genre(csv_reader)"
}


class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def category(self, csv_reader):
        for row in csv_reader:
            Category.objects.create(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )

    def genre(self, csv_reader):
        for row in csv_reader:
            Genre.objects.create(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )

    def user(self, csv_reader):
        for row in csv_reader:
            User.objects.create(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name']
            )

    def title(self, csv_reader):
        for row in csv_reader:
            category_obj = Category.objects.get(id=row['category'])
            Title.objects.create(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category=category_obj
            )

    def review(self, csv_reader):
        for row in csv_reader:
            Review.objects.create(
                id=row['id'],
                title_id=row['title_id'],
                text=row['text'],
                author_id=row['author'],
                score=row['score'],
                pub_date=row['pub_date']
            )

    def comment(self, csv_reader):
        for row in csv_reader:
            Comment.objects.create(
                id=row['id'],
                review_id=row['review_id'],
                text=row['text'],
                author_id=row['author'],
                pub_date=row['pub_date']
            )

    def title_genre(self, csv_reader):
        for row in csv_reader:
            TitleGenre.objects.create(
                id=row['id'],
                title_id=row['title_id'],
                genre_id=row['genre_id']
            )

    def handle(self, *args, **kwargs):
        file_name = kwargs['csv_file']
        csv_file_path = DIRECTORY + file_name
        with open(csv_file_path, 'r', encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            if csv_reader is not None:
                exec(NAMES_FILE[file_name])
