from os import environ, path
from dotenv import load_dotenv
import psycopg2.extras
bas_dir = path.abspath(path.dirname(__file__)) 
load_dotenv(path.join(bas_dir, '.env'))
from flask import current_app as app
from authlib.integrations.flask_client import OAuth

import psycopg2
# TESTING = True
# DEBUG = True
# ENV = "development"
# SECRATE_KEY = environ.get('SECRATE_KEY')
t_host = "localhost"
t_port = "5432"
t_dbname = "vkaptur_2"
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

GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)


oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id= GOOGLE_CLIENT_ID,
    client_secret= GOOGLE_CLIENT_SECRET,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    jwks_uri= "https://www.googleapis.com/oauth2/v3/certs",
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)

# https://github.com/authlib/demo-oauth-client/blob/master/flask-google-login/app.py
# https://github.com/Vuka951/tutorial-code/blob/master/flask-google-oauth2/app.py