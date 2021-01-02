import psycopg2.extras
import psycopg2
from config import t_host, t_dbname, t_port

class DatabaseConnection(object):

    def __init__(self, connection_username:str=None, connection_password: str=None) -> None:
        self.connection_useranme = connection_username
        self.connection_password = connection_password
        self.connector = None
        self.db_cursor = None

    def __enter__(self):
        # print("in enter")
        self.connector = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname)
        self.db_cursor = self.connector.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print("in exit", exc_val, exc_type, exc_tb)
        if exc_tb is None:
            self.connector.commit()
        else:
            self.connector.rollback()
        self.connector.close()
        
# https://medium.com/opex-analytics/database-connections-in-python-extensible-reusable-and-secure-56ebcf9c67fe