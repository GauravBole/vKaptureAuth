
# from config import db_cursor as cursor, db_conn as conn
from flask.globals import request
from exceptions.dao_exceptions import DaoExceptionError
from utils.query_number_generator import create_query
from database_connection.decorator import atomic_tarnsaction
import datetime
import psycopg2
class InquiryDao:

    def create_inquiey(self, request_date, cursor=None):
        try:
            request_date['query_id'] = create_query(cursor)
            create_address_query = ''' INSERT INTO address (address, city, state_id, district_id, zip_code) values('{address}', '{city}', '{state_id}', 
                                                                                                                    '{district_id}', '{zip_code}') RETURNING id;'''
            
            cursor.execute(create_address_query.format(**request_date['detail_address'].dict()))
    
            request_date['address_id'] = cursor.fetchone()['id']

            create_inquiry_query = ''' INSERT INTO inquiry (query_id, event_category_id, title, address_id, extra_message, budget, 
                                                            from_time, to_time, created_by_id, status) values('{query_id}', Array {event_category_id}, '{title}', 
                                                                                                        '{address_id}', '{extra_message}', '{budget}', 
                                                                                                        '{from_time}', '{to_time}', '{created_by_id}', '{status}')
            
            
                                    '''
            
            cursor.execute(create_inquiry_query.format(**request_date))
            # conn.commit()  
        except Exception as e:
            # conn.rollback()
            print(e)
            raise DaoExceptionError(status_code=401, message="Error in inquiry creation dao", detal_message=e)
            
      
    def get_all_inquiry(self, cursor=None):
        try:
            address_query = ''' select a.id, s.name, d.name, a.city, a.zip_code from address as a join state as s on a.state_id=s.id join district as d on a.district_id = d.id
                                where a.id = 2 '''
            all_queries = '''select i.id, json_object_agg(ec.name, ec.id), i.query_id, i.title, i.extra_message, i.budget, i.address_id,                           
						i.from_time, i.to_time, i.created_by_id, i.status, address_table.address_id, address_table.address_name,
						address_table.state_name, address_table.district_name, address_table.city, address_table.zip_code from 
						inquiry as i
						left JOIN event_category as ec on ec.id = any (i.event_category_id)
						JOIN (select a.id as address_id, a.address as address_name, s.name as state_name,
										d.name as district_name, a.city as city, a.zip_code as zip_code
										from address as a 
										join state as s on a.state_id=s.id 
										join district as d on a.district_id = d.id) 
										as address_table on address_table.address_id=i.address_id
									group by(i.id, address_table.address_id, address_table.address_name,
								address_table.state_name, address_table.district_name, address_table.city,
							address_table.zip_code)'''

            cursor.execute(all_queries)
            # conn.commit()
            return cursor.fetchall()
        except Exception as e:
            print(e)
            raise DaoExceptionError(status_code=400, message="error in all inquiry ado")


    def edit_inquiry(self, update_data: dict, inquiry_id: int, cursor=None):
        try:
            update_address = 'UPDATE address as a SET {} from inquiry as i where i.id={inquiry_id} and i.address_id=a.id'
            cursor.execute(update_address.format(', '.join('{k}={v!a}'.format(k=k, v=str(v)) for k, v in update_data['detail_address'].dict().items()), 
                                                                                        inquiry_id=inquiry_id)
                                                                                    )   
            inquiry_data =  update_data['inquiry_data'].dict()
            inquiry_data['status'] = 'Edited'
            event_category_ids = update_data['event_category_id']
            
            inquiry_data.pop('event_category_id')
            
            event_category_id = {i for i in event_category_ids}

            inquiry_update_query = 'UPDATE inquiry SET {}, event_category_id={event_category_id!r} where id= {inquiry_id}'.format(', '.join('{k}={v!a}'.format(k=k, v=str(v)) for k, v in inquiry_data.items()), 
                                                                                            inquiry_id=inquiry_id, event_category_id=str(event_category_id))
            cursor.execute(inquiry_update_query)
        except Exception as e:
            print(e)
            raise DaoExceptionError(status_code=400, message="error in edit inquiry dao")

    def is_inquiry_id_exists(self, inquiry_id: int, cursor=None):
        try:
            query = """select exists(select 1 from inquiry where id='{inquiry_id}') AS {exists} """
            
            cursor.execute(query.format(inquiry_id=inquiry_id, exists='exists'))
            
            return cursor.fetchone()['exists']
        except Exception as e:
            raise DaoExceptionError(status_code=400, message="error in find inquiry id")
        
    def is_photographer_exists(self, photographers: list, cursor=None):
        try:
            query = """select exists(select 1 from auth where id in ='{photographers}') AS {exists} """
            cursor.execute(query.format(photographers=photographers, exists='exists'))
            cursor.fetchone()['exists']
            
        except Exception as e:
            pass

    def send_query(self, inquiry_photographer_set: list, cursor=None):
        try:
            
            # query = """WITH ins as (Insert into send_query (inquiry_id, photographer_id) values ('{inquiry_id}', '{photographer_id}') 
            #             on conflict (inquiry_id, photographer_id) DO UPDATE SET is_active = true RETURNING *)"""
                        # select id from ins union select id from send_query where inquiry_id='{inquiry_id}' and photographer_id={photographer_id} """
            # cursor.execute(query.format(photographer_id = photographer_id, inquiry_id = inquiry_id))
            
            query = """Insert into send_query (inquiry_id, photographer_id) values {}
                        on conflict (inquiry_id, photographer_id) DO UPDATE SET is_active = true"""

            args_str = ','.join(['%s'] * len(inquiry_photographer_set))
            sql = query.format(args_str)
            # print(cursor.mogrify(sql, g).decode('utf8'))

            cursor.execute(sql, inquiry_photographer_set)

        except Exception as e:
            raise DaoExceptionError(status_code=400, message="error in send inquiry to photographer")
