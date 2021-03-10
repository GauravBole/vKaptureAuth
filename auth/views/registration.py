
from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from auth.services.registration import RgeistrationService


auth_blueprint = Blueprint('register_url', __name__) 
class RegistrationApi(MethodView):
    
    def post(self):
        """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
   
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
