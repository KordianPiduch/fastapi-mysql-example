"""
module: instance
description: Class Instance for CRUD operation in MySQL DB

"""

import logging
import mysql.connector
from ..exceptions import MySqlBaseException

LOGGER = logging.getLogger("instance")

class Instance():
    def __init__(self, host: str, port: int, user: str, password: str, database: str = None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password 
        self.database = database
        self.connection = None

        try:
            self.connection = self.create_db_connection(**self.connection_parameters)
        except MySqlBaseException as err:
            LOGGER.error(err)

    @property
    def connection_parameters(self):
        return {
            'host': self.host,
            'port': self.port,
            'user': self.user,
            'password': self.password,
            'database': self.database,
        }

    def create_db_connection(self, **kwargs):
        try:   
            connection = mysql.connector.connect(**kwargs)
            LOGGER.info("MySQL DB connection successful")
        except mysql.connector.Error as err:
            raise MySqlBaseException(err)
        return connection

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()   
            LOGGER.info("query successful")
        except mysql.connector.Error as err:
            LOGGER.error(f"Error: {err}")

    def read_query(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            LOGGER.error(f"Error: {err}")
