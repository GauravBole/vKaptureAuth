from auth.dao import photographer_profile
from auth.dao.photographer_profile import PhotographerProfileDao
from database_connection.decorator import atomic_tarnsaction
from exceptions.dao_exceptions import DaoExceptionError
from exceptions.exception_error import ExceptionError

from utils.s3_upload import AWSFileUpload

class PhotographerPortfolio:

    @atomic_tarnsaction
    def upload_image(self, image, user_id, cursor=None):
        try:
            file_name = image.filename
            aws_upload = AWSFileUpload(file=image, file_name=file_name)
            file_url = aws_upload.upload_file()
            photographer_profile_dao = PhotographerProfileDao()
            photographer_profile_dao.upload_image(image_path=file_url, user=user_id, cursor=cursor)
            100/0
        except DaoExceptionError as de:
            raise
        except Exception as e:
            raise ExceptionError(message="error in upload image service")