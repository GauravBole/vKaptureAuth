from flask.views import MethodView
from flask import Blueprint, request,  make_response, jsonify, url_for, redirect
from exceptions.dao_exceptions import DaoExceptionError
from exceptions.exception_error import ExceptionError
from auth.decorators import authanticate, privilege_required, can_quote

from quotation.services import QuotationService

quotation_blueprint = Blueprint('quotation_url', __name__, url_prefix='/quotation')

class QuotationApiView(MethodView):

    decorators = [can_quote, authanticate]
    
    def post(self):
        response_data = {"success": True, "status_code": 200}
    
        user = request.environ['user']
        user_id = user['user_id']
        quotation_service = QuotationService()
        post_data = request.form.to_dict()
        post_data['photographer_id'] = user_id
        quotation_service.create_quotation(request_data= post_data)
        response_data['message'] = "Quotaion Added success fullly"
        return make_response(jsonify(response_data)), response_data['status_code']
        



quotation_api = QuotationApiView.as_view('quotation_api')
quotation_blueprint.add_url_rule(
    '/add',
    view_func=quotation_api,
    methods=['POST'],
)