
from typing import Counter
from exceptions.dao_exceptions import DaoExceptionError


class PhotographerProfileDao:

    def upload_image(self, image_path:str, user:int, cursor=None):
        try:
           
            add_image_query = f"insert into portfolio_image (image_path, created_by_id) values ('{image_path}', {user})"
            cursor.execute(add_image_query)
            
        except Exception as e:
            # print(e, "--->")
            raise DaoExceptionError(status_code=401, message="Error in upload video image", detal_message=e)
            
    def upload_video(self, video_path:str, user:int, cursor=None):
        try:
            add_video_query = f"insert into portfolio_video (video_path, created_by_id, source) values ('{video_path}', {user}, 'file')"
            cursor.execute(add_video_query)
            
        except Exception as e:
            raise DaoExceptionError(status_code=401, message="Error in upload video dao", detal_message=e)

    def get_uoloaded_video_count(self, user_id: int, cursor=None):
        total_vedeo_count = 0
        try:
            active_video_count = f"select count(*) from portfolio_video where created_by_id={user_id} and is_active=true"
            cursor.execute(active_video_count)
            total_vedeo_count = cursor.fetchone().get('count', 0)
        except Exception as e:
            raise DaoExceptionError(status_code=401, message="Error in ", detal_message=e)

        return total_vedeo_count


    def get_uoloaded_image_count(self, user_id: int, cursor=None):
        total_image_count = 0
        try:
            active_image_count = f"select count(*) from portfolio_video where created_by_id={user_id} and is_active=true"
            cursor.execute(active_image_count)
            total_image_count = cursor.fetchone().get('count', 0)
        except Exception as e:
            raise DaoExceptionError(status_code=401, message="Error in ", detal_message=e)

        return total_image_count

    
            
    