from flask import Blueprint, request, Response, make_response, jsonify
from flask.views import MethodView

from config import db_cursor as cursor
from utils.jwt_util import JWTEncodeDecode
import json

auth_blueprint = Blueprint('login_url', __name__)


@auth_blueprint.route('/')
def index():
    # cur = db_cursor.execute('select * from auth;')
    # print(cur)
    # array_row = cur.fetchone()
    # print(array_row)
    query1 = "select * from auth"
    cursor.execute(query1)
    print(cursor.fetchone())
    query = "SELECT * FROM auth WHERE username=%s"
    cursor.execute(query, ('gaurav',))
    row = cursor.fetchone()
    print(row)

    return "Thiss is an example app check"

class LoginApi(MethodView):
    def __init__(self):
        self.JWTEncodeDecode = JWTEncodeDecode()
        
    def get(self):
        pass
    
    def post(self):
        post_data = request.form.to_dict()
        username = post_data.get("username") or None
        password = post_data.get('password') or None
        user_query = "SELECT * FROM auth WHERE username=%s"
        cursor.execute(user_query, (username,))
        user = cursor.fetchone()
        token = self.JWTEncodeDecode.encode(user['id'])
        if username is None or password is None:
            return make_response(jsonify({"error": 404, "message": "username and password required"})), 404
        if user is None:
            return make_response(jsonify({"status": "fail", "message": "user not found"})), 404
        

login_view = LoginApi.as_view('login_api')
auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST']
)
        