"""Open Library module

Responsable for the interactions with the Open Library API
"""

import sys
import json
import urllib3

from loguru import logger


class OpenLibrary:
    """Class to represents the Open Library connection

    Args:
        query (str): keyword used on the download request
        pages_number (int): number of pages to the download request
        page_limit (int): item quantity per page on the download request
    """
    def __init__(self, query='lord', pages_number=1, page_limit=100):
        self.url = f'http://openlibrary.org/search.json?q={query}&limit={page_limit}'

        # as range function starts on 1, pages_number must be bigger than 1
        self.pages_number = pages_number + 1

        # PoolManager is responsable for the http requests
        self.http = urllib3.PoolManager()
        logger.info(f'data source: {self.url}&page={pages_number}')

    def download_data(self, collection):
        """Method responsable for download one or more pages from the Open Library API

        Args:
            collection: MongoCollection instance used to persist the data
        """
        logger.info('---------------------------------')
        logger.info('Fetching data...')

        # iterates over the pages number
        for page in range(1, self.pages_number):
            try:
                response = self.http.request('GET', f'{self.url}&page={page}')
                logger.info(f'page {page} request response: {response.status}')
            except Exception as exception:
                logger.error(exception)
                sys.exit()

            if response.status != 200:
                logger.error(
                    f'page {page} request response: {response.status}')
                continue

            data = json.loads(response.data)
            # extracts only the needed information
            docs = data['docs']

            # persists the data
            collection.insert_data(docs)
        logger.info('---------------------------------')

        collection.create_title_index()
