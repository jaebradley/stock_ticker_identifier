from django.core.management.base import BaseCommand

from publicly_traded_companies.management.commands import insert_amex_companies, insert_nasdaq_companies, \
    insert_nyse_companies


class Command(BaseCommand):
    help = 'Inserts All Companies'

    def handle(self, *args, **options):
        insert_amex_companies.insert_amex_companies()
        insert_nasdaq_companies.insert_nasdaq_companies()
        insert_nyse_companies.insert_nyse_companies()
