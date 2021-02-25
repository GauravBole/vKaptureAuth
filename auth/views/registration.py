
from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from auth.services.registration import RgeistrationService

auth_blueprint = Blueprint('register_url', __name__)


class RegistrationApi(MethodView):
    
    def post(self):
        response_data = {"success": True, "status_code": 200}
        post_data = request.form.to_dict()
        registration_service = RgeistrationService()
        registration_service.register_user(post_data)
        response_data['message'] = f'{post_data["username"]} Created success fully' 
        return make_response(jsonify(response_data)), response_data['status_code']
        

registration_api = RegistrationApi.as_view('register_api')
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=registration_api,
    methods=['GET', 'POST']
)