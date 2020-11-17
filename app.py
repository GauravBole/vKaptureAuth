from flask import Flask

from auth.views.registration import auth_blueprint
from auth.views.login import login_blueprint
from query.views.inquiry import inquir_blueprint
from middlewarers import looger_middleware

from flask import Flask

app = Flask(__name__)

app.config.from_object('config.Config')
app.secret_key = '!secret'

app.register_blueprint(auth_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(inquir_blueprint)





