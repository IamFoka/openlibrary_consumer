# -*- coding: utf-8 -*-
"""MongoDB module

This module is responsable of the creation and accesses of the MongoDB collections
"""

from loguru import logger
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


class MongoCollection:
    """Class that represents the MongoDB collection

    Provides access to all the MongoDB collection methods

    Args:
        db_name (str): the MongoDB database name
        collection_name (str): the MongoDB collection name

    Attributes:
        client: MongoClient instance from pymongo
        database: pymongo's database representation
        collection: pymongo's collection representation
    """
    def __init__(self, db_name, collection_name):
        self.client = MongoClient()

        self.test_connection()

        try:
            self.client.drop_database(db_name)
            logger.info('cleaning database')
        except Exception as exception:
            logger.error(exception)

        self.database = self.client[db_name]
        self.collection = self.database[collection_name]

    def insert_data(self, docs):
        """Method responsable for inserting the JSON data in to the database

        Args:
            docs: JSON data from open_library
        """
        data_list = list(docs)

        _ = self.collection.insert_many(data_list)

    def rank_titles(self):
        """Method responsable for the database query to search the top 10 recurrent words
        """

        # transforms all the words to uppercase
        # splits the titles using space as splitter
        # creates one document per word
        # tests if the word has more than 5 characters
        # aggroups all the words and calculates their quantity
        # sorts the words by quantity, in decrescent way
        # limits the result to 10 items

        top_words = self.collection.aggregate([{"$project": {"title": {"$toUpper": "$title"}}},
                                               {"$project": {
                                                   "words": {"$split": ["$title", " "]}}},
                                               {"$unwind": "$words"},
                                               {"$match": {
                                                   "$expr": {"$gt": [{"$strLenCP": "$words"}, 5]}}},
                                               {"$group": {"_id": "$words",
                                                           "count": {"$sum": 1}}},
                                               {"$sort": {"count": -1}},
                                               {"$limit": 10}])

        logger.info('Most recurrent words top 10 rank:')
        logger.info('---------------------------------')

        # iterates into the result and logs the words info
        for word in top_words:
            logger.info(f'Name: {word["_id"]}, {word["count"]} times')

        logger.info('---------------------------------')

    def create_title_index(self):
        """Method responsable for the title index creation
        """
        try:
            self.collection.create_index('title')
            logger.info('title index created')
        except Exception as exception:
            logger.warning('failed to create title index')
            logger.error(exception)

    def test_connection(self):
        """Method responsable for validating the database connection
        """
        try:
            _ = self.client.server_info()
        except ServerSelectionTimeoutError as exception:
            logger.critical('server is down')
            logger.critical(exception)
