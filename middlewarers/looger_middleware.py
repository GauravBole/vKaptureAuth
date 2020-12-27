from werkzeug.wrappers import Request

from werkzeug.wsgi import pop_path_info, peek_path_info

class LoggingMiddleware(object):
    def __init__(self, app):
        self.app = app
        
    def __call__(self, environ, start_response):
        # print("*"*10, Request(environ).headers, "--->",dir(Request(environ)), dir(pop_path_info(environ)))
        g = Request(environ)
        # print(g.path, g.args, g.base_url, g.application, g.url_root, g.data, g.method, g.url)
    
        return self.app(environ, start_response)
    
#  https://medium.com/swlh/creating-middlewares-with-python-flask-166bd03f2fd4