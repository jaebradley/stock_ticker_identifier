import csv
import requests
import logging

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
        logging.info('Get or creating exchange: {exchange_name}'.format(exchange_name=exchange_name))
        exchange, created = Exchange.objects.get_or_create(name=exchange_name, nickname=exchange_nickname)
        logging.info('Exchange: {exchange} was created: {created}'.format(exchange=exchange, created=created))


def insert_nasdaq_companies():
    logging.info('Inserting NASDAQ companies')
    insert_companies_for_exchange(exchange=Exchange.objects.get(nickname='NASDAQ'), url=DOWNLOAD_NASDAQ_COMPANIES_URL)


def insert_nyse_companies():
    logging.info('Inserting NYSE companies')
    insert_companies_for_exchange(exchange=Exchange.objects.get(nickname='NASDAQ'), url=DOWNLOAD_NYSE_COMPANIES_URL)


def insert_amex_companies():
    logging.info('Inserting AMEX companies')
    insert_companies_for_exchange(exchange=Exchange.objects.get(nickname='AMEX'), url=DOWNLOAD_AMEX_COMPANIES_URL)


def insert_companies_for_exchange(exchange, url):
    logging.info('Inserting companies for exchange: {exchange} from URL: {url}'.format(exchange=exchange, url=url))
    content = requests.get(url)
    companies = list(csv.reader(content.text.splitlines(), delimiter=','))
    # remove first row which are column headers
    companies.pop(0)
    for row in companies:
        name = row[1]
        ticker = row[0]
        ipo_year = row[5]
        # n/a is the value if no value exists
        if ipo_year == 'n/a':
            ipo_year = None
        else:
            ipo_year = int(ipo_year)
        sector = row[6]
        industry = row[7]
        company, created = Company.objects.get_or_create(exchange=exchange, name=name, ticker=ticker, ipo_year=ipo_year,
                                                         sector=sector, industry=industry)
        logging.info('Company: {company} was created: {created}'.format(company=company, created=created))
