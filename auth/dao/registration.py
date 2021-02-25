from models import UserProfile, User
from config import db_cursor as cursor, db_conn as conn
from exceptions.auth_exception import RegisterUserException, RegisterUserDaoException

class UserDao(object):
    """
    docstring
    """
    def __init__(self):
        pass
    
    def check_user_exists(self, username):
        
        query = "SELECT count(*) FROM auth WHERE username='{}';"
        cursor.execute(query.format(username))
        row = cursor.fetchone()
        if row['count'] > 0:
            return True
        return False
    
    def create_user_and_user_profile(self, user_data, user_profile_data, cursor=None):
        try:
            100/0
            # create or get user ID
            query = """WITH ins as (Insert into auth (username, password, group_id) values ('{username}', '{password}', (SELECT id from "group" WHERE code='{group}')) on conflict (username) do nothing RETURNING *)
                select id from ins union select id from auth where username='{username}'"""
            
            cursor.execute(query.format(**user_data))
            user_profile_data['user_id'] = cursor.fetchone()['id']
            user_profile_query = "Insert into userprofile (user_id, email, mobile_number, is_active) values('{user_id}', '{email}', \
                                '{mobile_number}', {is_active}) ON CONFLICT (user_id) DO NOTHING;".format(**user_profile_data)
            cursor.execute(user_profile_query)
            
            return True
        except Exception as e:
            raise RegisterUserDaoException(message="error in user register dao", status_code=404)
            
        # https://www.psycopg.org/docs/cursor.html