from os import name
import re
from flask import Blueprint, request,  make_response, jsonify, url_for, redirect
from flask.views import MethodView
from query.services import InquiryService
# from query.models import Inquiry, Address
inquir_blueprint = Blueprint('inquiry_url', __name__, url_prefix='/inquiry')
from auth.decorators import authanticate, privilege_required
from exceptions.exception_error import ExceptionError
from exceptions.dao_exceptions import DaoExceptionError
class InquiryApiView(MethodView):
    allow = {
       'GET': "view_all_inquiry", 
       'POST': "craete_inquiry",
       'DELETE': "delete_inquiry",
       }
    decorators = [privilege_required(acl=allow)]
    

    def post(self, *arge, **kwargs):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        try:
            post_data = request.form.to_dict()
            create_inquiry_service = InquiryService()
            create_inquiry_service.create_inquiry(request_data=post_data)
            response_data['message'] = "Inquiry Created success fullly"
            response_data['status_code'] = 200
            response_data['status'] = "success"

        except (ExceptionError, DaoExceptionError) as e:
            response_data['status_code'] = e.code
            response_data['message'] = e.get_traceback_details()
            # response_data['message'] = e.dict()
        return make_response(jsonify(response_data)), response_data['status_code']
        

    def get(self, *arge, **kwargs):
        print(arge, kwargs, "decoretors data")
        inquiry_service = InquiryService()
        inquiry_data = inquiry_service.get_all_inquires()
        return make_response(jsonify(inquiry_data)), 200
        
def login_required():
    print(request.headers.get('Authorization'), "request0000>")

inquiry_api = InquiryApiView.as_view('inquiry_api')
inquir_blueprint.before_request(login_required)
inquir_blueprint.add_url_rule(
    '/create',
    view_func=inquiry_api,
    
    methods=['GET', 'POST'],
    # options={"name", "inquiry_add"}

)