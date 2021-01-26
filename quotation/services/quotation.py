
from quotation.models import Quotation, QuotationDetails
from quotation.dao import QuotationDAO, quotation
from exceptions.exception_error import ExceptionError
from exceptions.dao_exceptions import DaoExceptionError
from pydantic import ValidationError
from database_connection.decorator import atomic_tarnsaction
from database_connection.context_manager import DatabaseConnection as db_connection

class QuotationService:

    @atomic_tarnsaction
    def create_quotation(self, request_data, cursor=None):
        try:
            quotation_detail_model = QuotationDetails(**request_data)
            request_data['quaotation_details'] = quotation_detail_model
            quotation_dao = QuotationDAO()
            quotation_dao.create_quotation(request_date=request_data, cursor=cursor)
        except ValidationError as e:
            raise ExceptionError(message=e.errors(), status_code=400)
        
        except ValueError as ve:
            raise ExceptionError(status_code=403, message=(str(ve)))

        except DaoExceptionError as de:
            # raise ExceptionError(status_code=403, message=(de.message))
            raise

        except Exception as e:
            print(e)
            raise ExceptionError(message="error in quaotaion service service", status_code=403)
        
    @atomic_tarnsaction
    def can_quote(self, user_id, inquiry_id, cursor=None):
        quotation_dao = QuotationDAO()
        return quotation_dao.can_quote(user_id=user_id, inquiry_id=inquiry_id, cursor=cursor)
    
        