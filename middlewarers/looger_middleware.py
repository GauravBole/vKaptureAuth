from werkzeug.wrappers import Request

class LoggingMiddleware(object):
    def __init__(self, app):
        self.app = app
        
    def __call__(self, environ, start_response):
        print("*"*10, Request(environ).headers)
        return self.app(environ, start_response)
    
#  https://medium.com/swlh/creating-middlewares-with-python-flask-166bd03f2fd4