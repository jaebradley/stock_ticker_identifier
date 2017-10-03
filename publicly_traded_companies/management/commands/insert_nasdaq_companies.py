from django.core.management.base import BaseCommand

from publicly_traded_companies.inserters import insert_nasdaq_companies


class Command(BaseCommand):
    help = 'Inserts NASDAQ Companies'

    def handle(self, *args, **options):
        insert_nasdaq_companies()
