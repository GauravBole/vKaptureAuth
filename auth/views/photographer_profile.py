from exceptions.exception_error import ExceptionError
from exceptions.dao_exceptions import DaoExceptionError
from auth.decorators import authanticate
from auth.services.photographer_profile import PhotographerPortfolio

from flask import Blueprint, jsonify, make_response, redirect, request, url_for
from flask.views import MethodView

photographer_blueprint = Blueprint('photographer_url', __name__, url_prefix='/photographer')
import threading

class PhotographerPortfolioImagesApiView(MethodView):
    decorators = [authanticate]

    def post(self):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        try:
            if request.files:
                post_data = request.files['image']
                photographer_image_service = PhotographerPortfolio()
                user = request.environ['user']
                user_id = user['user_id']
                photographer_image_service.upload_image(image=post_data, user_id=user_id)

                # long_task = threading.Thread(target=photographer_image_service.upload_image, kwargs={"image":post_data, "user_id":user_id})
                # # task = threading.Thread(photographer_image_service.upload_image, kwargs={"image":post_data, "user_id":user_id)]
                # long_task.start()

                response_data['message'] = {'msg': "file uloaded successfully"},
                response_data["status"] = "success"
                response_data["status_code"] =  200
        
            
        except (DaoExceptionError, ExceptionError) as ex:
            response_data['message'] = ex.get_traceback_details()
        except Exception as e:
            print("--------->", e)

        return make_response(jsonify(response_data)), response_data['status_code']


class PhotographerPortfolioVideoApiView(MethodView):
    decorators = [authanticate]

    def post(self):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        try:
            if request.files:
                post_data = request.files['video']
                photographer_image_service = PhotographerPortfolio()
                user = request.environ['user']
                user_id = user['user_id']
                photographer_image_service.upload_video(video=post_data, user_id=user_id)

                # long_task = threading.Thread(target=photographer_image_service.upload_image, kwargs={"image":post_data, "user_id":user_id})
                # # task = threading.Thread(photographer_image_service.upload_image, kwargs={"image":post_data, "user_id":user_id)]
                # long_task.start()

                response_data['message'] = {'msg': "file uloaded successfully"},
                response_data["status"] = "success"
                response_data["status_code"] =  200
        
            
        except (DaoExceptionError, ExceptionError) as ex:
            response_data['message'] = ex.get_traceback_details()
        except Exception as e:
            print("--------->", e)

        return make_response(jsonify(response_data)), response_data['status_code']

      
        
        


photographer_image_api = PhotographerPortfolioImagesApiView.as_view('photographer_image_api')
photographer_video_api = PhotographerPortfolioVideoApiView.as_view('photographer_video_api')

photographer_blueprint.add_url_rule(
    '/add_images/',
    view_func=photographer_image_api,
    methods = ['POST']
)

photographer_blueprint.add_url_rule(
    '/add_videos/',
    view_func=photographer_video_api,
    methods = ['POST']
)
