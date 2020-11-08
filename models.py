from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, conint, constr, ValidationError, validator

from validators.email import validate_email
from validators.mobile_number import validate_mobile_number

class User(BaseModel):
    username : str
    password : str
    
class UserProfile(BaseModel):
    user: User = None
    mobile_number : constr(max_length=25)
    email : str
    profile_type: str = "C"
    profiel_pic: str = None
    is_active: bool = True
    
    @validator('email')
    def validate_email(cls, email):
        return validate_email(email=email)
        
    @validator('mobile_number')
    def validate_mobile_number(cls, mobile_number):
        return validate_mobile_number(number=mobile_number)
    