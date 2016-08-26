from django.core.management.base import BaseCommand, CommandError
from ...utils import fetch_csv

class Command(BaseCommand):
    help = 'Downloads the CSV file and loads data in DB'

    def handle(self, *args, **kwargs):
        csv_file = fetch_csv()
        self.stdout.write(self.style.SUCCESS(csv_file))
