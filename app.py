from flask import Flask
import psycopg2

from auth.views.registration import auth_blueprint
from middlewarers import looger_middleware
from exceptions.register_user_exception import RegisterUserException

from flask import jsonify

app = Flask(__name__)
# app.wsgi_app = looger_middleware.LoggingMiddleware(app.wsgi_app)
app.register_blueprint(auth_blueprint)

# t_host = "localhost"
# t_port = "5432"
# t_dbname = "vcapture"
# t_user = "postgres"
# t_pw = "postgres"
# db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
# db_cursor = db_conn.cursor()

app.config.from_object('config.Config')


