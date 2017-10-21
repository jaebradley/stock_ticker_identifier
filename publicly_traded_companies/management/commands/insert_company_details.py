from django.core.management.base import BaseCommand

from publicly_traded_companies.inserters import insert_all_company_details


class Command(BaseCommand):
    help = 'Inserts all company details'

    def handle(self, *args, **options):
        insert_all_company_details()
