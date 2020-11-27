from functools import wraps

from flask import abort, request, make_response, jsonify
from flask.globals import request
from utils.jwt_util import JWTEncodeDecode
import jwt

def authanticate(function):

    @wraps(function)
    def decorated_function(*args, **kwargs):
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