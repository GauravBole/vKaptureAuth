from exceptions.exception_error import ExceptionError
from exceptions.dao_exceptions import DaoExceptionError
from auth.decorators import authanticate
from auth.services.photographer_profile import PhotographerPortfolioService, PhotographerPorfileService

from flask import Blueprint, json, jsonify, make_response, redirect, request, url_for
from flask.views import MethodView

photographer_blueprint = Blueprint('photographer_url', __name__, url_prefix='/photographer')
import threading
import json    


class PhotographerPortfolioImagesApiView(MethodView):
    decorators = [authanticate]

    def post(self):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        try:
            if request.files:
                post_data = request.files['image']
                photographer_image_service = PhotographerPortfolioService()
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
            response_data['message'] = e.args[0]


        return make_response(jsonify(response_data)), response_data['status_code']


class PhotographerPortfolioVideoApiView(MethodView):
    decorators = [authanticate]

    def post(self):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        try:
            if request.files:
                post_data = request.files['video']
                photographer_image_service = PhotographerPortfolioService()
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
            response_data['message'] = e.args[0]


        return make_response(jsonify(response_data)), response_data['status_code']

class PhotographerProfileApiView(MethodView):

    def post(self):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        try:
            user = request.environ['user']
            user_id = user['user_id']
            # experties = request.form.getlist('experties')
            post_data = request.form.to_dict()
            post_data['user_id'] = user_id
            post_data['experties'] = set(json.loads(post_data['experties']))
            post_data['location_availability'] = set(json.loads(post_data['location_availability']))

            photographer_profile_service = PhotographerPorfileService()
            photographer_profile_service.add_photographer_profile(request_data=post_data)
            response_data['message'] = {'msg': "profile updated successfully"},
            response_data["status"] = "success"
            response_data["status_code"] =  200
        
        except (DaoExceptionError, ExceptionError) as ex:
            response_data['message'] = ex.get_traceback_details()
        except Exception as e:
            response_data['message'] = e.args[0]
            pass
        return make_response(jsonify(response_data)), response_data['status_code']

            
class PhotographerCameraApiView(MethodView):
    decorators = [authanticate]
    def post(self):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}

        # try:
        user = request.environ['user']
        user_id = user['user_id']
        post_data = request.form.to_dict()
        photographer_profile_service = PhotographerPorfileService()
        photographer_profile_service.add_camera(request_data=post_data, auth_user=user_id)
        response_data['message'] = {'msg': "camera added successfully"},
        response_data["status"] = "success"
        response_data["status_code"] =  200
        
        # except (DaoExceptionError, ExceptionError) as ex:
        #     response_data['message'] = ex.get_traceback_details()
        # except (Exception, ValueError) as e:
        #     response_data['message'] = e.args[0]
        return make_response(jsonify(response_data)), response_data['status_code']
        


photographer_image_api = PhotographerPortfolioImagesApiView.as_view('photographer_image_api')
photographer_video_api = PhotographerPortfolioVideoApiView.as_view('photographer_video_api')
photographer_profile_api = PhotographerProfileApiView.as_view('photographer_profile_api')
photographer_camera_api = PhotographerCameraApiView.as_view('photographer_camera_api')

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

photographer_blueprint.add_url_rule(
    '/photographer_profile/',
    view_func=photographer_profile_api,
    methods = ['POST']
)

photographer_blueprint.add_url_rule(
    '/photographer_camera/',
    view_func=photographer_camera_api,
    methods = ['POST']
)