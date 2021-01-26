from os import name
import re
from flask import Blueprint, request,  make_response, jsonify, url_for, redirect
from flask.views import MethodView
from query.services import InquiryService
# from query.models import Inquiry, Address
inquiry_blueprint = Blueprint('inquiry_url', __name__, url_prefix='/inquiry')
from auth.decorators import authanticate, privilege_required
from exceptions.exception_error import ExceptionError
from exceptions.dao_exceptions import DaoExceptionError
class InquiryApiView(MethodView):
    allow = {
       'GET': "view_all_inquiry", 
       'POST': "craete_inquiry",
       'DELETE': "delete_inquiry",
       'PUT': 'edit_inquiry'
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
        inquiry_service = InquiryService()
        inquiry_data = inquiry_service.get_all_inquires()
        return make_response(jsonify(inquiry_data)), 200
    
    def put(self, inquiry_id, *args, **kwargs):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        try:
            inquiry_service = InquiryService()
            put_data = request.form.to_dict()

            inquiry_data = inquiry_service.edit_inquiry(inquiry_id=inquiry_id, request_data=put_data)
            response_data['message'] = "Inquiry Updated success fullly"
            response_data['status_code'] = 200
            response_data['status'] = "success"

        except (ExceptionError, DaoExceptionError) as e:
            response_data['status_code'] = e.code
            response_data['message'] = e.get_traceback_details()
        return make_response(jsonify(response_data)), response_data['status_code']
        
    
class SendQueryPhotographer(MethodView):

    def post(self, *args, **kwargs):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        try:
            inquiry_service = InquiryService()
            post_data = request.form.to_dict()
            photographer_ids = request.form.getlist('photographer_id')
            inquiry_service.send_query(inquiry_id=post_data['inquiry_id'], photographer_ids=photographer_ids)
            response_data['message'] = "Inquiry photographer send success"
            response_data['status_code'] = 200
            response_data['status'] = "success"

        except (ExceptionError, DaoExceptionError) as e:
            response_data['status_code'] = e.code
            response_data['message'] = e.get_traceback_details()
        except ValueError as ve:
            response_data['status_code'] = 400
            response_data['message'] = ve.args[0]
        except Exception as e:
            print(e)
        return make_response(jsonify(response_data)), response_data['status_code']
         
    

inquiry_api = InquiryApiView.as_view('inquiry_api')
send_query_api = SendQueryPhotographer.as_view('send_query_api')

inquiry_blueprint.add_url_rule(
    '/create',
    view_func=inquiry_api,
    
    methods=['GET', 'POST'],
    # options={"name", "inquiry_add"}

)
inquiry_blueprint.add_url_rule(
    '/<int:inquiry_id>',
    view_func=inquiry_api,
    
    methods=['PUT',],
    # options={"name", "inquiry_add"}

)
inquiry_blueprint.add_url_rule(
    '/send_query/',
    view_func=send_query_api,
    
    methods=['POST',],
    # options={"name", "inquiry_add"}

)