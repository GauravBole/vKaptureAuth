from query.dao.inquiry import InquiryDao
from query.models import Inquiry, Address, InquiryDetail, InquiryEdit
from exceptions.exception_error import ExceptionError
from exceptions.dao_exceptions import DaoExceptionError
from typing import Counter, List
from pydantic import ValidationError
from database_connection.decorator import atomic_tarnsaction
from database_connection.context_manager import DatabaseConnection as db_connection
from exceptions.inquiry_exceptions import AddInqueryDaoException, AddInqueryException

class InquiryService:

    @atomic_tarnsaction
    def create_inquiry(self, request_data, cursor=None):
        try:

            address_model = Address(**request_data)
            request_data['detail_address'] = address_model
            request_data['status'] = 'Created'
            Inquiry(**request_data)
            inquiry_dao = InquiryDao()
            inquiry_dao.create_inquiey(request_data, cursor=cursor)
            return True
        except (ValueError, AddInqueryDaoException):
            raise
        except Exception:
            raise AddInqueryException(message="error in inquiry add service", status_code=403)
    
    @atomic_tarnsaction
    def get_all_inquires(self, cursor=None):
        try:
            inquiry_dao = InquiryDao()
            all_inquires = inquiry_dao.get_all_inquiry(cursor=cursor)
            return all_inquires

        except DaoExceptionError as de:
            raise ExceptionError(status_code=403, message=(de.message))

        except Exception as e:
            raise ExceptionError(message="error in list inquiry", status_code=400)

    @atomic_tarnsaction
    def edit_inquiry(self, request_data, inquiry_id, cursor=None):
        try:
            address_model = Address(**request_data)
            request_data['detail_address'] = address_model
            inquiry_model = InquiryEdit(**request_data)
            request_data['inquiry_data'] = inquiry_model
            inquiry_dao = InquiryDao()
            inquiry_dao.edit_inquiry(update_data=request_data, inquiry_id=inquiry_id, cursor=cursor)
        except Exception as e:
            raise ExceptionError(message="error in list inquiry", status_code=400)

    def validate_inquiry_id(self, inquiry_id:int):
        pass

    @atomic_tarnsaction
    def send_query(self, photographer_ids: list, inquiry_id: int, cursor=None):
        try:
            inquiry_dao = InquiryDao()
            if not inquiry_dao.is_inquiry_id_exists(inquiry_id=inquiry_id, cursor=cursor):
                raise ValueError("error inquiry id not exists in system")
            inquiry_photographer_set = [(inquiry_id, i) for i in photographer_ids]
            inquiry_dao.send_query(inquiry_photographer_set, cursor=cursor)
        except Exception as e:
            raise ExceptionError(message="error in send inquiry to photographer", status_code=400)
