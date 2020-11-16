
from config import db_cursor as cursor, db_conn as conn
from exceptions.dao_exceptions import DaoExceptionError

class inquiryDao:

    def create_inquiey(self, request_date):
        try:
            create_inquiry_query = ''' INSERT INTO inquiry (query_id, event_category_id, title, address_id, extra_message, budget, 
                                                            from_time, to_time, created_by_id) values({},{},{}, {}, {}, {}, {}, {}, {})
            '''
        except Exception as e:
            pass