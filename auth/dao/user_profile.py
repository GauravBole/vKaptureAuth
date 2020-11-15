
from config import db_cursor as cursor, db_conn as conn
from exceptions.dao_exceptions import DaoExceptionError
class UserProfileDao:

    def get_user_info_from_user_id(self, user_id:int):
        try:
            user_profile_qs = '''select a.username, up.email, up.mobile_number 
                                from auth as a join userprofile as up 
                                on a.id = up.user_id 
                                where a.id={user_id}s;'''
            cursor.execute(user_profile_qs.format(user_id=user_id))
            row = cursor.fetchone()
            return row
        except Exception as e:
            raise DaoExceptionError(message="error in user profile info dao", status_code=400) 
