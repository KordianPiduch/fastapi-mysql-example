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
        self.exc = None


    def __enter__(self):
        try:
            self.connection = self.create_db_connection(**self._connection_parameters)
        except Exception as exc:
            self.exc = str(exc)
            self.__exit__(exc)
        finally:
            return self
            

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.exc is None:
            self.exc = str(exc_val)
        if self.connection and self.connection.is_connected():
            self.connection.close()
        return True

    @property
    def _connection_parameters(self):
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
            LOGGER.error(f"MySQL Error: {str(err)}")
            raise MySqlBaseException(err)
        return connection

    def execute_query(self, query):
        """
        INSERT INTO
        UPDATE
        DELETE
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()   
            LOGGER.info("query successful")
        except mysql.connector.Error as err:
            LOGGER.error(f"MySQL Error: {str(err)}")
            raise MySqlBaseException(err)
        finally:
            cursor.close()

    def read_query(self, query):
        """
        SELECT
        """
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            LOGGER.error(f"MySQL Error: {str(err)}")
            raise MySqlBaseException(err)
        finally:
            cursor.close()

    def close_connection(self):
        self.connection.close()