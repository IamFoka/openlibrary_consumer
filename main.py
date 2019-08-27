# -*- coding: utf-8 -*-
"""Main module

This module makes the communication between the other modules
"""

import argparse

from loguru import logger
from open_library import OpenLibrary
from mongo_collection import MongoCollection

# argparse setup
PARSER = argparse.ArgumentParser()
PARSER.add_argument('--manual-info', '-m', nargs=3,
                    metavar=('<query>', '<pages_number>', 'page_limit'))

OPTIONS = PARSER.parse_args()

def main(query='lord', pages_number=64, page_limit=1000):
    '''Main function

    Args:
        query (str): keyword used on the open_library request
        pages_number (int): number of pages to the open_library request
        page_limit (int): item quantity per page on the open_library request
    '''

    # mongodb name setup
    db_name = 'guilherme_test'
    collection_name = 'test'

    collection = MongoCollection(db_name, collection_name)

    library = OpenLibrary(query, int(pages_number), int(page_limit))
    # downloads all the requested data, and inserts it on the mongodb database
    library.download_data(collection)

    # ranks and show the result of the top 10 more recurrent words
    collection.rank_titles()

# parse option call
if OPTIONS.manual_info:
    logger.debug('manual info flag')
    main(*OPTIONS.manual_info)
else:
    main()
