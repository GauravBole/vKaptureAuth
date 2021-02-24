from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, conint, constr, ValidationError, validator
from query.models import Address
from validators.email import validate_email
from validators.mobile_number import validate_mobile_number

class User(BaseModel):
    username : str
    password : str
    group: str
class UserProfile(BaseModel):
    user: User = None
    mobile_number : constr(max_length=25)
    email : str
    profiel_pic: str = None
    is_active: bool = True
    
    @validator('email')
    def validate_email(cls, email):
        return validate_email(email=email)
        
    @validator('mobile_number')
    def validate_mobile_number(cls, mobile_number):
        return validate_mobile_number(number=mobile_number)



class PhotographerPortfolioAddImages(BaseModel):
    created_by_id = int
    image = bytes


def broad_exception_handler(e: Exception):
    # TODO 에러를 세분화해서 잡는 것을 추천합니다.

    if isinstance(e, HTTPException):
        message = e.description
        code = e.code

    elif isinstance(e, ValidationError):
        message = json.loads(e.json())
        code = HTTPStatus.BAD_REQUEST

    else:
        message = ""
        code = HTTPStatus.INTERNAL_SERVER_ERROR

        if current_app.debug:
            import traceback

            traceback.print_exc()

    return jsonify({"error": message}), code 


class PhotographerProfile(BaseModel):
    user_id : int
    address : Address
    address_proof : Optional[bytes]
    gst_number : str
    gst_proof : Optional[bytes] 
    location_availability : set
    experties : set
    metadata : dict = {}


class CameraSpecification(BaseModel):
    photographer_id : int
    model : str
    brand : str


    