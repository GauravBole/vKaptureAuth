

from quotation.models import Quotation
from exceptions.dao_exceptions import DaoExceptionError


class QuotationDAO:

    def create_quotation(self, request_date, cursor=None):
        try:
            quatation_detail_query = """ Insert Into quotation_detail (photographer_id, quote, message) 
                                        values('{photographer_id}', '{quote}', '{message}') RETURNING id;
                                    """
            cursor.execute(quatation_detail_query.format(**request_date['quaotation_details'].dict()))
        
            request_date['quotation_detail_id'] = cursor.fetchone()['id']

            quotation_query = """ Insert into quotation (inquiry_id, quotation_detail_id) values({inquiry_id}, {quotation_detail_id})"""    
            cursor.execute(quotation_query.format(**request_date))

        except Exception as e:
            # conn.rollback()
            print(e)
            raise DaoExceptionError(status_code=401, message="Error in Quotation creation dao", detal_message=e)
           
