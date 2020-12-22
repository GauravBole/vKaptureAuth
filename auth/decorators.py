from functools import wraps

from flask import abort, request, make_response, jsonify
from flask.globals import request
from utils.jwt_util import JWTEncodeDecode
import jwt

def authanticate(function):

    @wraps(function)
    def decorated_function(*args, **kwargs):
        print(args, kwargs)
        jwt_encode_decode = JWTEncodeDecode()
        if 'Authorization' not in request.headers:
            abort(401)
        
        payload = None
        data = request.headers['Authorization']
        token = data.replace('Token ','')
        jwt_data = jwt_encode_decode.decode(token=token)
        if jwt_data['success']:
            payload = jwt_data['data']
            
            kwargs['user_id'] = payload['user_id']

        else:
            return make_response(jsonify(jwt_data)), jwt_data['error']
        
        
        return function(*args, **kwargs)

    return decorated_function


class privilege_required(object):
    def __init__(self, acl):
        self.acl = acl

    
    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            print(args, kwargs, self.acl)
            # print(self.acl, dir(f), f.__name__, request.method)
            # if not g.role in self.acl[request.method]:
            #     abort(403)

            jwt_encode_decode = JWTEncodeDecode()
            if 'Authorization' not in request.headers:
                abort(401)
            
            payload = None
            data = request.headers['Authorization']
            token = data.replace('Token ','')
            jwt_data = jwt_encode_decode.decode(token=token)
            if jwt_data['success']:
                payload = jwt_data['data']
                
                kwargs['user_id'] = payload['user_id']

            else:
                return make_response(jsonify(jwt_data)), jwt_data['error']
            
            
            return f(*args, **kwargs)

            # return f(*args, **kwargs)
        return wrapped_f