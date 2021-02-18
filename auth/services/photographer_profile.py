from auth.dao import photographer_profile
from auth.dao.photographer_profile import PhotographerProfileDao
from database_connection.decorator import atomic_tarnsaction
from exceptions.dao_exceptions import DaoExceptionError
from exceptions.exception_error import ExceptionError

from utils.s3_upload import AWSFileUpload

class PhotographerPortfolio:


    def validate_uploaded_image(self, user_id, cursor=None):
        try:
            photographer_profile_dao = PhotographerProfileDao()
            image_count = photographer_profile_dao.get_uoloaded_image_count(user_id=user_id, cursor=cursor)
            if image_count > 5:
                raise ValueError("you excid maximum limit of images count")
        except Exception as e:
            raise

  
    def validate_uploaded_video(self, user_id, cursor=None):
        try:
            photographer_profile_dao = PhotographerProfileDao()
            image_count = photographer_profile_dao.get_uoloaded_video_count(user_id=user_id, cursor=cursor)
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
            photographer_profile_dao = PhotographerProfileDao()
            photographer_profile_dao.upload_image(image_path=file_url, user=user_id, cursor=cursor)
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
            photographer_profile_dao = PhotographerProfileDao()
            photographer_profile_dao.upload_video(video_path=file_url, user=user_id, cursor=cursor)
           
        except DaoExceptionError as de:
            raise
        except Exception as e:
            raise ExceptionError(message="error in upload image service")