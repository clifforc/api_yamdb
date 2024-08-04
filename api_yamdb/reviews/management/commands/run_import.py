from django.core import management
from django.core.management.base import BaseCommand


FILES = ['category.csv', 'genre.csv', 'users.csv', 'titles.csv',
         'genre_title.csv', 'review.csv', 'comments.csv']


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for csv_file in FILES:
            management.call_command('import_CSV', csv_file)
