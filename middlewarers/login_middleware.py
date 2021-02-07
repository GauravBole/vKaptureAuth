
from werkzeug.wrappers import Request, Response, ResponseStream
from flask import abort, request, make_response, jsonify
import json

from utils.jwt_util import JWTEncodeDecode

class RequestUser:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        jwt_encode_decode = JWTEncodeDecode()
        # if 'Authorization' not in request.headers:
        #     # return make_response(jsonify({"messsage": " Token missing"})), 403
        #     res = Response(json.dumps('Authorization failed'), mimetype='application/json', status=401)
        #     return res(environ, start_response)
        if 'Authorization' in request.headers:
            payload = None
            environ['user'] = None
            data = request.headers['Authorization']
            token = data.replace('Token ','')
            jwt_data = jwt_encode_decode.decode(token=token)
            if jwt_data['success']:
                payload = jwt_data['data']
                environ['user'] = payload
        return self.app(environ, start_response)
