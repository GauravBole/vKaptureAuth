import psycopg2.extras
import psycopg2
from config import t_host, t_dbname, t_port
from exceptions.dao_exceptions import DaoExceptionError
from exceptions.exception_error import ExceptionError

def atomic_tarnsaction(func):

    def with_connection_(*arges, **kwargs):
        connector = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname)
        db_cursor = connector.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        try:
        
            result = func(*arges, **kwargs, cursor=db_cursor)
            
        except Exception as e:
            connector.rollback()
            raise
            # exception_class = type(e).__name__
            # exception_message = e.message
            # raise eval(f"{exception_class}(message='{exception_message}')")
        else:
            connector.commit()
        finally:
            connector.close()
        return result
    return with_connection_
