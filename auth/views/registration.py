from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from auth.services.registration import RgeistrationService

auth_blueprint = Blueprint('register_url', __name__)


class RegistrationApi(MethodView):
    
    def post(self):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        try:
            post_data = request.form.to_dict()
            registration_service = RgeistrationService()
            registration_service.register_user(post_data)
            response_data['message'] = f'{post_data["username"]} Created success fully' 
            response_data["status"] = "success"
            response_data["status_code"] = 200
        except Exception as e:
            response_data['status_code'] = e.status_code
            response_data['message'] = e.dict()
            
        return make_response(jsonify(response_data)), response_data['status_code']
        


registration_api = RegistrationApi.as_view('register_api')
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=registration_api,
    methods=['GET', 'POST']
)