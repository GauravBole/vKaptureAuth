import psycopg2.extras
import psycopg2
from config import t_host, t_dbname, t_port

def atomic_tarnsaction(func):

    def with_connection_(*arges, **kwargs):
        connector = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname)
        db_cursor = connector.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        try:
        
            result = func(*arges, **kwargs, conn=db_cursor)
            
        except Exception as e:
            connector.rollback()
            print("database error", e)
            raise
        else:
            connector.commit()
        finally:
            connector.close()
        return result
    return with_connection_
