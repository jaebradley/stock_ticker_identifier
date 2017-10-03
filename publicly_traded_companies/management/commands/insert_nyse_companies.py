from django.core.management.base import BaseCommand


from publicly_traded_companies.inserters import insert_nyse_companies


class Command(BaseCommand):
    help = 'Inserts NYSE Companies'

    def handle(self, *args, **options):
        insert_nyse_companies()
