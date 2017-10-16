import logging

import environ
import requests
from django.core.management.base import BaseCommand

# Janky command used to ping Heroku server to make sure it's not sleeping


class Command(BaseCommand):
    help = 'Ensures server is not sleeping'

    def handle(self, *args, **options):
        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        env = environ.Env(DEBUG=(bool, False), )

        url = 'http://{current_site}/exchanges'.format(current_site=env('CURRENT_SITE'))
        r = requests.get(url)
        logging.info('Made request to {url} with response {response}'.format(url=url, response=r.status_code))
