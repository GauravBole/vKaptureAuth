# from config import db_cursor as cursor
from exceptions.auth_exceptions import LoginUserDaoException
from database_connection.context_manager import DatabaseConnection as db_connection
class UserLoginDao:

    def login_user(self,username: str, password: str, cursor=None):
        try:
            user_login_query = "select count('id'), id, group_id, password from auth where username='{username}' group by id;"
            # print(user_login_query.format(username=username, password=password))
            cursor.execute(user_login_query.format(username=username, password=password))
            row = cursor.fetchone()
            if row and row['count'] > 0:
                return True, row
            return False, None
        except Exception:
            raise LoginUserDaoException(message="error in login user dao", status_code=404)
        