from django.core.management.base import BaseCommand

from publicly_traded_companies.inserters import insert_exchanges


class Command(BaseCommand):
    help = 'Inserts exchanges'

    def handle(self, *args, **options):
        insert_exchanges()
