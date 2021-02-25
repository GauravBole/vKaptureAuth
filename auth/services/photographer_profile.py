from auth.decorators import authanticate
from auth.dao import photographer_profile
from auth.dao.photographer_profile import PhotographerPortfolioDao, PhotographerPorfileDao
from query.models import Address
from database_connection.decorator import atomic_tarnsaction
from exceptions.dao_exceptions import DaoExceptionError
from exceptions.exception_error import ExceptionError
from models import PhotographerProfile, CameraSpecification

from utils.s3_upload import AWSFileUpload

class PhotographerPortfolioService:

    def validate_uploaded_image(self, user_id, cursor=None):
        try:
            photographer_portfolio_dao = PhotographerPortfolioDao()
            image_count = photographer_portfolio_dao.get_uoloaded_image_count(user_id=user_id, cursor=cursor)
            if image_count > 5:
                raise ValueError("you excid maximum limit of images count")
        except Exception as e:
            raise

  
    def validate_uploaded_video(self, user_id, cursor=None):
        try:
            photographer_portfolio_dao = PhotographerPortfolioDao()
            image_count = photographer_portfolio_dao.get_uoloaded_video_count(user_id=user_id, cursor=cursor)
            if image_count > 5:
                raise ValueError("you excid maximum limit of video count")
        except Exception as e:
            raise


    @atomic_tarnsaction
    def upload_image(self, image, user_id, cursor=None):
        try:
            file_name = image.filename
            self.validate_uploaded_image(user_id=user_id, cursor=cursor)
            aws_upload = AWSFileUpload(file=image, file_name=file_name)
            file_url = aws_upload.upload_file()
            photographer_portfolio_dao = PhotographerPortfolioDao()
            photographer_portfolio_dao.upload_image(image_path=file_url, user=user_id, cursor=cursor)
        except DaoExceptionError as de:
            raise
        except Exception as e:
            raise ExceptionError(message="error in upload image service")

    @atomic_tarnsaction
    def upload_video(self, video, user_id, cursor=None):
        try:
            file_name = video.filename
            self.validate_uploaded_video(user_id=user_id, cursor=cursor)
            aws_upload = AWSFileUpload(file=video, file_name=file_name)
            file_url = aws_upload.upload_file()
            photographer_portfolio_dao = PhotographerPortfolioDao()
            photographer_portfolio_dao.upload_video(video_path=file_url, user=user_id, cursor=cursor)
           
        except DaoExceptionError as de:
            raise
        except Exception as e:
            raise ExceptionError(message="error in upload image service")

class PhotographerPorfileService:

    @atomic_tarnsaction
    def add_photographer_profile(self, request_data: dict, cursor=None):
        try:
            address_data = Address(**request_data)
            request_data['address'] = address_data
            validated_data = PhotographerProfile(**request_data)
            photographer_profile_dao = PhotographerPorfileDao()
            photographer_profile_dao.add_photographer_profile(profile_data=validated_data, address_data=address_data, cursor=cursor)
        except DaoExceptionError as de:
            raise

        except Exception as e:
            raise ExceptionError(message="exception in add profile service")

    @atomic_tarnsaction
    def add_camera(self, request_data, auth_user, cursor=None):
        try:
            photographer_profile_dao = PhotographerPorfileDao()

            photographer_profile_id = photographer_profile_dao.get_auth_user_photographer_profile_id(auth_user=auth_user, cursor=cursor)
            if photographer_profile_id is None:
                raise ValueError("invalid photographer user id")
            request_data['photographer_id'] = photographer_profile_id
            camera_data = CameraSpecification(**request_data)
            photographer_profile_dao.add_camera(camera_data=camera_data.dict(), cursor=cursor)
            100/0
        except ValueError as ve:
            raise

        except Exception as e:
            raise ExceptionError(message="exception in add camera")
        