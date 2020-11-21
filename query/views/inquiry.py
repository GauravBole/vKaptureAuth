import re
from flask import Blueprint, request,  make_response, jsonify, url_for, redirect
from flask.views import MethodView
from query.services import InquiryService
# from query.models import Inquiry, Address
inquir_blueprint = Blueprint('inquiry_url', __name__, url_prefix='/inquiry')

class InquiryApiView(MethodView):

    def post(self):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        try:
            post_data = request.form.to_dict()
            create_inquiry_service = InquiryService()
            create_inquiry_service.create_inquiry(request_data=post_data)
            response_data['message'] = "Inquiry Created success fullly"
            response_data['status_code'] = 200
            response_data['status'] = "success"

        except Exception as e:
            response_data['status_code'] = e.status_code
            response_data['message'] = e.dict()
        return make_response(jsonify(response_data)), response_data['status_code']
        

    def get(self):
        inquiry_service = InquiryService()
        inquiry_data = inquiry_service.get_all_inquires()
        return make_response(jsonify(inquiry_data)), 200
        

inquiry_api = InquiryApiView.as_view('inquiry_api')
inquir_blueprint.add_url_rule(
    '/create',
    view_func=inquiry_api,
    methods=['GET', 'POST']

)