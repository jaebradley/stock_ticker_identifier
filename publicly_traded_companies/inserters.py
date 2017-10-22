import csv
import requests
import logging
import time

from publicly_traded_companies.models import Exchange, Company, Industry, Sector
from publicly_traded_companies.constants import DOWNLOAD_NASDAQ_COMPANIES_URL, DOWNLOAD_NYSE_COMPANIES_URL, \
    DOWNLOAD_AMEX_COMPANIES_URL

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def insert_exchanges():
    exchanges = {
        'National Association of Securities Dealers Automated Quotations': 'NASDAQ',
        'New York Stock Exchange': 'NYSE',
        'American Stock Exchange':  'AMEX'
    }

    for exchange_name, exchange_nickname in exchanges.items():
        logger.info('Get or creating exchange: {exchange_name}'.format(exchange_name=exchange_name))
        exchange, created = Exchange.objects.update_or_create(name=exchange_name,
                                                              defaults={'nickname': exchange_nickname})
        logger.info('Exchange: {exchange} was created: {created}'.format(exchange=exchange, created=created))


def insert_nasdaq_companies():
    logger.info('Inserting NASDAQ companies')
    insert_companies_for_exchange(exchange=Exchange.objects.get(nickname='NASDAQ'), url=DOWNLOAD_NASDAQ_COMPANIES_URL)


def insert_nyse_companies():
    logger.info('Inserting NYSE companies')
    insert_companies_for_exchange(exchange=Exchange.objects.get(nickname='NASDAQ'), url=DOWNLOAD_NYSE_COMPANIES_URL)


def insert_amex_companies():
    logger.info('Inserting AMEX companies')
    insert_companies_for_exchange(exchange=Exchange.objects.get(nickname='AMEX'), url=DOWNLOAD_AMEX_COMPANIES_URL)


def insert_companies_for_exchange(exchange, url):
    logger.info('Inserting companies for exchange: {exchange} from URL: {url}'.format(exchange=exchange, url=url))
    content = requests.get(url)

    content.raise_for_status()

    companies = list(csv.reader(content.text.splitlines(), delimiter=','))
    # remove first row which are column headers
    companies.pop(0)
    for row in companies:
        logger.info('Inserting company data: {data}'.format(data=row))
        name = row[1]
        ticker = row[0]
        try:
            company = Company.objects.get(exchange=exchange, ticker=ticker)
            company.name = name
        except Company.DoesNotExist:
            company = Company(exchange=exchange, ticker=ticker, name=name)
        insert_company_details(company)


def insert_company_details(company):
    time.sleep(0.5)
    r = requests.get(url='https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}'.format(ticker=company.ticker),

                     params={
                         'formatted': True,
                         'modules': 'assetProfile'
                     })
    try:
        raw_company_details = r.json()
    except ValueError as e:
        logger.error(e)
        return

    logger.info(raw_company_details)

    if 'quoteSummary' in raw_company_details \
            and 'result' in raw_company_details['quoteSummary'] \
            and raw_company_details['quoteSummary']['result'] is not None \
            and len(raw_company_details['quoteSummary']['result']) == 1 \
            and 'assetProfile' in raw_company_details['quoteSummary']['result'][0]:
        company_details = raw_company_details['quoteSummary']['result'][0]['assetProfile']

        industry, created = Industry.objects.get_or_create(name=company_details.get('industry'))
        sector, created = Sector.objects.get_or_create(name=company_details.get('sector'))

        company.industry = industry
        company.sector = sector

        company.address_line_1 = company_details.get('address1')
        company.address_line_2 = company_details.get('address2')
        company.city = company_details.get('city')
        company.state = company_details.get('state')
        company.country = company_details.get('country')
        company.zip_code = company_details.get('zip')
        company.fax_number = company_details.get('fax')
        company.phone_number = company_details.get('phone')
        company.website_url = company_details.get('website')
        company.employee_count = company_details.get('fullTimeEmployees')
        company.business_summary = company_details.get('longBusinessSummary')

        company.save()
