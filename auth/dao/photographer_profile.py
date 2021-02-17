
from exceptions.dao_exceptions import DaoExceptionError


class PhotographerProfileDao:

    def upload_image(self, image_path:str, user:int, cursor=None):
        try:
            add_image_query = f"insert into portfolio_image (image_path, created_by_id) values ('{image_path}', {user})"
            cursor.execute(add_image_query)
        except Exception as e:
            # print(e, "--->")
            raise DaoExceptionError(status_code=401, message="Error in inquiry creation dao", detal_message=e)
            
    def upload_video(self, video_path:str, user:int, cursor=None):
        try:
            add_video_query = f"insert into portfolio_video (video_path, created_by_id, source) values ('{video_path}', {user}, 'file')"
            cursor.execute(add_video_query)
        except Exception as e:
            # print(e, "--->")
            raise DaoExceptionError(status_code=401, message="Error in inquiry creation dao", detal_message=e)
    