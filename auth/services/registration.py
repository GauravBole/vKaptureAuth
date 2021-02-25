from config import db_cursor as cursor
from validators.mobile_number import validate_mobile_number
from validators.email import validate_email
from auth.dao.registration import UserDao
from utils.password_hashing import PasswordHashing
from models import UserProfile, User
from exceptions.auth_exception import RegisterUserException, RegisterUserDaoException
from pydantic import ValidationError
from database_connection.decorator import atomic_tarnsaction

import json
class RgeistrationService:
    
    def validate_registration_data(self, request_data: dict):
        required_fields = ['username', 'password', 'email', 'mobile_number']
        validate_felds = [data for data in required_fields if data not in request_data]
        if len(validate_felds) > 1:
            raise ValueError({"error": "Required {} fields missings".format(validate_felds)})
        
        validate_mobile_number(str(request_data['mobile_number']))
        validate_email(email=request_data['email'])
        request_data['password'] = PasswordHashing.craete_hash(request_data['password'])
        return request_data
    
    def validate_user(self, username):
        user_dao = UserDao()
        user_exists = user_dao.check_user_exists(username=username)
        if user_exists:
            raise ValueError("user name allready exists please try another")
        return True

    @atomic_tarnsaction
    def register_user(self, request_data: dict, cursor=None):
        try:
            if "password" in request_data:
                request_data['password'] = PasswordHashing.craete_hash(request_data['password'])

            auth_user_data = User(**request_data)
            user_profile_data = UserProfile(**request_data) 
            self.validate_user(request_data['username'])
            user_dao = UserDao()
            user_dao.create_user_and_user_profile(user_data=auth_user_data.dict(), user_profile_data=user_profile_data.dict(), cursor=cursor)
        except (ValueError, RegisterUserDaoException):
            raise
        except Exception:
            raise RegisterUserException(message="error in user register service", status_code=400)
           

        
        
        