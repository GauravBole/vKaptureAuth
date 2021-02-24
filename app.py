from flask import Flask

from auth.views.registration import auth_blueprint
from auth.views.login import login_blueprint
from auth.views.photographer_profile import photographer_blueprint
from query.views.inquiry import inquiry_blueprint
from quotation.views.quotation import quotation_blueprint
from middlewarers import looger_middleware, login_middleware

from flask import Flask

class App:
    
    def _initialize_blueprints(self, app):
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(login_blueprint)
        app.register_blueprint(inquiry_blueprint)
        app.register_blueprint(quotation_blueprint)
        app.register_blueprint(photographer_blueprint)


    def _initialize_middelware(self, app):
        app.wsgi_app = looger_middleware.LoggingMiddleware(app.wsgi_app)
        app.wsgi_app = login_middleware.RequestUser(app.wsgi_app)


    def create_app(self):
        app = Flask(__name__)
        self._initialize_blueprints(app)
        self._initialize_middelware(app)
        app.config.from_object('config.Config')
        app.secret_key = '!secret'
        return app

app_obj = App()
app = app_obj.create_app()






