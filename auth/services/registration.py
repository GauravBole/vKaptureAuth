from config import db_cursor as cursor
from validators.mobile_number import validate_mobile_number
from validators.email import validate_email
from utils.password_hashing import PasswordHashing

class RgeistrationService:
    
    def validate_registration_data(self, request_data: dict):
        required_fields = ['username', 'password', 'email', 'mobile_number']
        validate_felds = [data for data in required_fields in data not in required_fields]
        if len(validate_felds) > 1:
            raise ValueError({"error": "Required {} fields missings".format(validate_felds)})
        
        validate_mobile_number(str(request_data['mobile_number']))
        validate_email(email=request_data['email'])
        request_data['passworf'] = PasswordHashing.craete_hash(request_data['password'])
        return request_data
    
    def register_user(self, request_data: dict):
        validate_data = self.validate_registration_data(request_data=request_data)
        