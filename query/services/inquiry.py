from query.dao.inquiry import inquiryDao
from query.models import Inquiry, Address, InquiryDetail
from exceptions.exception_error import ExceptionError
from exceptions.dao_exceptions import DaoExceptionError
from pydantic import parse_obj_as
from typing import List
from pydantic import BaseModel, ValidationError, conint

class InquiryService:

    def create_inquiry(self, request_data):
        
        try:
            address_model = Address(**request_data)
            request_data['detail_address'] = address_model
            request_data['status'] = 'Created'
            inquiry_model = Inquiry(**request_data)
            inquiry_dao = inquiryDao()  
            inquiry_dao.create_inquiey(request_date=request_data)
            return True

        except ValidationError as e:
            raise ExceptionError(message=e.errors(), status_code=400)
        
        except ValueError as ve:
            raise ExceptionError(status_code=403, message=(str(ve)))

        except DaoExceptionError as de:
            raise ExceptionError(status_code=403, message=(de.message))

        except Exception as e:
            raise ExceptionError(message="error in login user service", status_code=403)
    

    def get_all_inquires(self):
        try:
            inquiry_dao = inquiryDao()
            all_inquires = inquiry_dao.get_all_inquiry()
            return all_inquires

        except DaoExceptionError as de:
            raise ExceptionError(status_code=403, message=(de.message))

        except Exception as e:
            raise ExceptionError(message="error in list inquiry", status_code=400)

    
