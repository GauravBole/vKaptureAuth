from os import environ, path
from dotenv import load_dotenv
import psycopg2.extras
bas_dir = path.abspath(path.dirname(__file__)) 
load_dotenv(path.join(bas_dir, '.env'))
import psycopg2
# TESTING = True
# DEBUG = True
# ENV = "development"
# SECRATE_KEY = environ.get('SECRATE_KEY')
t_host = "localhost"
t_port = "5432"
t_dbname = "vkapture"
# t_user = "gaurav"
# t_pw = "postgres"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname)
db_cursor = db_conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

class Config:
    """Set Flask config variables."""

    FLASK_ENV = 'development'
    TESTING = True
    SECRET_KEY = environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# for more redding use https://hackersandslackers.com/configure-flask-applications/