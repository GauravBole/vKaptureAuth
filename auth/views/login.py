from flask import Blueprint, request,  make_response, jsonify, url_for, redirect
from flask.views import MethodView

from config import db_cursor as cursor
from config import oauth

from utils.jwt_util import JWTEncodeDecode

from auth.services.login import LoginService

login_blueprint = Blueprint('login_url', __name__)


@login_blueprint.route('/auth/google_login')
def login():
    redirect_uri = url_for('login_url.auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@login_blueprint.route('/auth/google_auth')
def auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    print(user)
    return redirect('/')


@login_blueprint.route('/')
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
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail",  'data': {}, "status_code": 501}
        try:
            post_data = request.form.to_dict()
            username = post_data.get("username") or None
            password = post_data.get('password') or None
            login_service_obj = LoginService()
            user_data = login_service_obj.login_user(request_data={"username": username, "password": password})
            print(user_data)
            response_data['message'] = "success" 
            response_data["status"] = "success"
            response_data["status_code"] = 200
            response_data['data'] = user_data
        except Exception as e:
            response_data['status_code'] = e.status_code
            response_data['message'] = e.dict()
            
        return make_response(jsonify(response_data)), response_data['status_code']
        

login_view = LoginApi.as_view('login_api')
login_blueprint.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST']
)
        
        

