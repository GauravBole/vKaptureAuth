from config import db_cursor as cursor
from validators.mobile_number import validate_mobile_number
from validators.email import validate_email
from auth.dao.registration import UserDao
from utils.password_hashing import PasswordHashing
from models import UserProfile, User
from exceptions.register_user_exception import RegisterUserException
from pydantic import BaseModel, ValidationError, conint

import json
class RgeistrationService:
    
    def validate_registration_data(self, request_data: dict):
        required_fields = ['username', 'password', 'email', 'mobile_number']
        validate_felds = [data for data in required_fields if data not in request_data]
        print(validate_felds)
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
            print("in if")
            raise ValueError("user name allready exists please try another")
        return True
    
    def register_user(self, request_data: dict):
        try:
            self.validate_user(request_data['username'])
            user_profile_data = UserProfile(**request_data)  
            request_data['password'] = PasswordHashing.craete_hash(request_data['password'])
            auth_user_data = User(**request_data)
            user_dao = UserDao()
            user_dao.create_user_and_user_profile(user_data=auth_user_data.dict(), user_profile_data=user_profile_data.dict())
        
        except ValidationError as e:
            raise RegisterUserException(request_data['username'], message=e.errors(), status_code=400)
        except ValueError as ve:
            print("in value errro", ve)
            raise RegisterUserException(request_data['username'], message=(str(ve)), status_code=403)

        
        # validate_user = self.validate_user(username=request_data['username'])
        
        

        
        
        