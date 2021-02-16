from flask import Flask

from auth.views.registration import auth_blueprint
from auth.views.login import login_blueprint
from auth.views.photographer_profile import photographer_blueprint
from query.views.inquiry import inquiry_blueprint
from quotation.views.quotation import quotation_blueprint
from middlewarers import looger_middleware, login_middleware

from flask import Flask

app = Flask(__name__)

app.wsgi_app = looger_middleware.LoggingMiddleware(app.wsgi_app)
app.wsgi_app = login_middleware.RequestUser(app.wsgi_app)

app.config.from_object('config.Config')
app.secret_key = '!secret'

app.register_blueprint(auth_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(inquiry_blueprint)
app.register_blueprint(quotation_blueprint)
app.register_blueprint(photographer_blueprint)





