from flask import Blueprint, request, Response, make_response, jsonify
from flask.views import MethodView

from config import db_cursor as cursor
from utils.jwt_util import JWTEncodeDecode
import json

auth_blueprint = Blueprint('login_url', __name__)


class Registration:
    
    def post(self):
        post_data = request.form.to_dict()
        username = post_data.get('username', None)
        password = post_data.get('password', None)
        email = post_data.get('email', None)
        mobile_number = post_data.get('mobile_number', None)
        