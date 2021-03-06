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

    def _initialize_errorhandlers(self, app):
        '''
        Initialize error handlers
        '''
        from exceptions.exception_response import errors
        app.register_blueprint(errors)
 
    def _initialize_middelware(self, app):
        app.wsgi_app = looger_middleware.LoggingMiddleware(app.wsgi_app)
        app.wsgi_app = login_middleware.RequestUser(app.wsgi_app)
        

    def create_app(self):
        app = Flask(__name__)
        self._initialize_blueprints(app)
        self._initialize_middelware(app)
        self._initialize_errorhandlers(app)
        app.config.from_object('config.Config')
        app.secret_key = '!secret'
        return app

app_obj = App()
app = app_obj.create_app()

from database_connection.decorator import atomic_tarnsaction
from helper.services import state
from helper.services import events
@atomic_tarnsaction
def init_db(cursor=None):
   
    with app.open_resource('helper/sql_commands.sql', mode='r') as f:
        try:
            query = f.read()
            cursor.execute(query)
        except Exception as e:
            
            raise 
    
    print("init db")

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database.')

@app.cli.command('import_state')
def import_state():
    state_service = state.StateService()

    state_service.add_state_from_dictinary()

@app.cli.command('import_events')
def import_events():
    event_service = events.EventService()
    event_service.add_events()


