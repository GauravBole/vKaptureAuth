from flask import Blueprint, request,  make_response, jsonify, url_for, redirect
from flask.views import MethodView

photographer_blueprint = Blueprint('photographer_url', __name__, url_prefix='/photographer')
from auth.services.photographer_profile import PhotographerPortfolio
class PhotographerPortfolioImagesApiView(MethodView):
    
    def post(self):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        if request.files:
            post_data = request.files['image']
            photographer_image_service = PhotographerPortfolio()
            photographer_image_service.upload_image(image=post_data)
        print("pppp")


photographer_image_api = PhotographerPortfolioImagesApiView.as_view('photographer_image_api')

photographer_blueprint.add_url_rule(
    '/add_images/',
    view_func=photographer_image_api,
    methods = ['POST']
)