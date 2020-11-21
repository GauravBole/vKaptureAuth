
from config import db_cursor as cursor, db_conn as conn
from exceptions.dao_exceptions import DaoExceptionError

class inquiryDao:

    def create_inquiey(self, request_date):
        try:
            create_address_query = ''' INSERT INTO address (address, city, state_id, district_id, zip_code) values('{address}', '{city}', '{state_id}', 
                                                                                                                    '{district_id}', '{zip_code}') RETURNING id;'''
            
            cursor.execute(create_address_query.format(**request_date['detail_address'].dict()))
            
            request_date['address_id'] = cursor.fetchone()['id']
            
            create_inquiry_query = ''' INSERT INTO inquiry (query_id, event_category_id, title, address_id, extra_message, budget, 
                                                            from_time, to_time, created_by_id, status) values('{query_id}', '{event_category_id}', '{title}', 
                                                                                                        '{address_id}', '{extra_message}', '{budget}', 
                                                                                                        '{from_time}', '{to_time}', '{created_by_id}', '{status}')
            
            
                                    '''
            
            cursor.execute(create_inquiry_query.format(**request_date))
            conn.commit()
        except Exception as e:
            conn.commit()
            raise DaoExceptionError(status_code=401, message="Error in inquiry creation dao", detal_message=e)
            
    
            

    

    def get_all_inquiry(self):
        try:
            address_query = ''' select a.id, s.name, d.name, a.city, a.zip_code from address as a join state as s on a.state_id=s.id join district as d on a.district_id = d.id
                                where a.id = 2 '''
            all_queries = ''' select i.id, ec.name, i.query_id, i.title, i.extra_message, i.budget, i.address_id,
                            i.from_time, i.to_time, i.created_by_id, i.status, address_table.address_id, address_table.address_name,
                            address_table.state_name, address_table.district_name, address_table.city, address_table.zip_code from 
                            inquiry as i 
                            JOIN event_category as ec on i.event_category_id = ec.id 
                            JOIN 
                                (select a.id as address_id, a.address as address_name, s.name as state_name, d.name as district_name, a.city as city, a.zip_code as zip_code 
                                from address as a 
                                join state as s on a.state_id=s.id 
                                join district as d on a.district_id = d.id) 
                            as address_table on address_table.address_id=i.address_id'''

            cursor.execute(all_queries)
            conn.commit()
            return cursor.fetchall()
        except Exception as e:
            raise DaoExceptionError(status_code=400, message="error in all inquiry ado")