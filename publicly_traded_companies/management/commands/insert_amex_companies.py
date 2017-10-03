from django.core.management.base import BaseCommand

from publicly_traded_companies.inserters import insert_amex_companies


class Command(BaseCommand):
    help = 'Inserts AMEX Companies'

    def handle(self, *args, **options):
        insert_amex_companies()
