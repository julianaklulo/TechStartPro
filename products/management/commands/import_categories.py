import csv
from django.core.management.base import BaseCommand
from products.models import Category


class Command(BaseCommand):
    help = 'Imports categories information to database from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to CSV file")

    def get_category_data(self, file_path):
        with open(file_path) as categories_csv:
            categories_data = csv.reader(categories_csv)
            next(categories_data)  # skip header

            for category in categories_data:
                yield str(category).strip("'[]")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        for category in self.get_category_data(file_path):
            category_data = Category(name=category)
            category_data.save()
            self.stdout.write(
                self.style.SUCCESS(f"Category {category} added successfully!")
            )
