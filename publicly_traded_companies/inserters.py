from publicly_traded_companies.models import Exchange


def insert_exchanges():
    exchanges = {
        'National Association of Securities Dealers Automated Quotations': 'NASDAQ',
        'New York Stock Exchange': 'NYSE',
        'American Stock Exchange':  'AMEX'
    }

    for exchange_name, exchange_nickname in exchanges.items():
        Exchange.objects.get_or_create(name=exchange_name, nickname=exchange_nickname)