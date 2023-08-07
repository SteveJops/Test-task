import sys
import psycopg2

sys.path.insert(0, 'C:\\Users\\steve\\Works Projects\\contact-list-testing\\src')
from settings import Settings


class DataBaseConn:
    """
    class for making connection to database
    """

    __CONNECTION = None

    def __new__(cls) -> __CONNECTION:  # type: ignore
        if cls.__CONNECTION is None:
            cls.__CONNECTION = object.__new__(cls)
        return cls.__CONNECTION

    def make_connection(self) -> __CONNECTION:  # type: ignore
        """
        making connection to db and returning an instance of db connection

        Returns:
            __CONNECTION: connection to db
        """

        self.__CONNECTION = psycopg2.connect(
            host=Settings.DataBase.HOST,
            database=Settings.DataBase.NAME,
            user=Settings.DataBase.USERNAME,
            password=Settings.DataBase.PASSWORD,
            port=Settings.DataBase.PORT,
        )
        return self.__CONNECTION
