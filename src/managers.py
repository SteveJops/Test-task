__all__ = ("ApplicationsManager", "TextSearchManager")

import sys
from typing import List, Union
from psycopg2.extras import DictCursor
sys.path.insert(0, 'C:\\Users\\steve\\Works Projects\\contact-list-testing\\src')
from db_connection import DataBaseConn
from models import TextSearch


class BaseManager:
    """
    base class for making queries to db and getting res
    """

    _CONN = DataBaseConn()
    _CONNECTION = _CONN.make_connection()

    def fetch(self, *args) -> Union[List[List[str]], Exception]:
        """
        method to get data for db

        Returns:
            QuerySet: returning data query result as either list nor Exception
        """
        cursor = self._CONNECTION.cursor(cursor_factory=DictCursor)
        try:
            cursor.execute(self._FETCH_QUERY, (*args,))
        except Exception as error:
            self._CONNECTION.rollback()
            print("Here's an error ", error)
            self._CONNECTION.close()
        else:
            data = cursor.fetchall()
            return data
            

    def commit(self, *args) -> None:
        """
        method to make updates into db

        """
        cursor = self._CONNECTION.cursor()
        try:
            cursor.execute(self._FETCH_QUERY, (*args,))
        except Exception as error:
            self._CONNECTION.rollback()
            self._CONNECTION.close()
            print("Here's an error: ", error)
        else:
            self._CONNECTION.commit()


class ApplicationsManager(BaseManager):
    """
    the class which making updates data into db

    Args:
        BaseManager (args): values of fields which gonna be changed

    Returns:
        committed changes
    """

    _FETCH_QUERY = """
    insert into contacts (id, first_name, last_name, email) values(%s, %s, %s, %s)
    on conflict (id) do 
    update set first_name=EXCLUDED.first_name, last_name=EXCLUDED.last_name, email=EXCLUDED.email
    """


class TextSearchManager(BaseManager):
    """
    the class for making a query to search by a word in db

    Args:
        BaseManager (args): word for making a query
    """    
    _FETCH_QUERY = """
    select * from contacts
    where to_tsquery(%s) @@ (to_tsvector(contacts.first_name)||to_tsvector(contacts.last_name)||to_tsvector(contacts.email))
    """
    def fetch(self, word: str) -> List[TextSearch]:
        """
        the method for fetching query to db

        Args:
            word (str): _description_

        Returns:
            List[TextSearch]: _description_
        """        
        data = super().fetch(word)
        return [TextSearch(**text) for text in data]