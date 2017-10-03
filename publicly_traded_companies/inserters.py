import csv
import requests

from publicly_traded_companies.models import Exchange, Company
from publicly_traded_companies.constants import DOWNLOAD_NASDAQ_COMPANIES_URL, DOWNLOAD_NYSE_COMPANIES_URL, \
    DOWNLOAD_AMEX_COMPANIES_URL


def insert_exchanges():
    exchanges = {
        'National Association of Securities Dealers Automated Quotations': 'NASDAQ',
        'New York Stock Exchange': 'NYSE',
        'American Stock Exchange':  'AMEX'
    }

    for exchange_name, exchange_nickname in exchanges.items():
        Exchange.objects.get_or_create(name=exchange_name, nickname=exchange_nickname)


def insert_nasdaq_companies():
    insert_companies_for_exchange(exchange=Exchange.objects.get(nickname='NASDAQ'), url=DOWNLOAD_NASDAQ_COMPANIES_URL)


def insert_nyse_companies():
    insert_companies_for_exchange(exchange=Exchange.objects.get(nickname='NASDAQ'), url=DOWNLOAD_NYSE_COMPANIES_URL)


def insert_amex_companies():
    insert_companies_for_exchange(exchange=Exchange.objects.get(nickname='AMEX'), url=DOWNLOAD_AMEX_COMPANIES_URL)


def insert_companies_for_exchange(exchange, url):
    content = requests.get(url)
    companies = list(csv.reader(content.text.splitlines(), delimiter=','))
    # remove first row which are column headers
    companies.pop(0)
    for row in companies:
        name = row[1]
        ticker = row[0]
        ipo_year = row[5]
        if ipo_year == 'n/a':
            ipo_year = None
        else:
            ipo_year = int(ipo_year)
        sector = row[6]
        industry = row[7]
        Company.objects.get_or_create(exchange=exchange, name=name, ticker=ticker, ipo_year=ipo_year, sector=sector,
                                      industry=industry)
