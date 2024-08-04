import csv

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from reviews.models import Review, Title, Genre, Category, Comment, TitleGenre


DIRECTORY = 'static/data/'
User = get_user_model()


class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = DIRECTORY + kwargs['csv_file']
        with open(csv_file_path, 'r', encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            match kwargs['csv_file']:
                case 'category.csv':
                    for row in csv_reader:
                        Category.objects.create(
                            id=row['id'],
                            name=row['name'],
                            slug=row['slug']
                        )
                case 'genre.csv':
                    for row in csv_reader:
                        Genre.objects.create(
                            id=row['id'],
                            name=row['name'],
                            slug=row['slug']
                        )
                case 'users.csv':
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
                case 'titles.csv':
                    for row in csv_reader:
                        category_obj = Category.objects.get(id=row['category'])
                        Title.objects.create(
                            id=row['id'],
                            name=row['name'],
                            year=row['year'],
                            category=category_obj
                        )
                case 'review.csv':
                    for row in csv_reader:
                        Review.objects.create(
                            id=row['id'],
                            title_id=row['title_id'],
                            text=row['text'],
                            author_id=row['author'],
                            score=row['score'],
                            pub_date=row['pub_date']
                        )
                case 'comments.csv':
                    for row in csv_reader:
                        Comment.objects.create(
                            id=row['id'],
                            review_id=row['review_id'],
                            text=row['text'],
                            author_id=row['author'],
                            pub_date=row['pub_date']
                        )
                case 'genre_title.csv':
                    for row in csv_reader:
                        TitleGenre.objects.create(
                            id=row['id'],
                            title_id=row['title_id'],
                            genre_id=row['genre_id']
                        )
