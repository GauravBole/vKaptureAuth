import re
from flask import Blueprint, request,  make_response, jsonify, url_for, redirect
from flask.views import MethodView
from query.services import InquiryService
# from query.models import Inquiry, Address
inquir_blueprint = Blueprint('inquiry_url', __name__, url_prefix='/inquiry')

class InquiryApiView(MethodView):

    def post(self):
        post_data = request.form.to_dict()
        print(post_data)
        create_inquiry_service = InquiryService()
        create_inquiry_service.create_inquiry(request_data=post_data)
        # Inquiry(post_data)

    def get(self):
        inquiry_service = InquiryService()
        inquiry_data = inquiry_service.get_all_inquires()
        return inquiry_data

inquiry_api = InquiryApiView.as_view('inquiry_api')
inquir_blueprint.add_url_rule(
    '/create',
    view_func=inquiry_api,
    methods=['GET', 'POST']

)