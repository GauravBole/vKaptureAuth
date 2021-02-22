
from typing import Counter
from exceptions.dao_exceptions import DaoExceptionError


class PhotographerPortfolioDao:

    def upload_image(self, image_path:str, user:int, cursor=None):
        try:
           
            add_image_query = f"insert into portfolio_image (image_path, created_by_id) values ('{image_path}', {user})"
            cursor.execute(add_image_query)
            
        except Exception as e:
            # print(e, "--->")
            raise DaoExceptionError(status_code=401, message="Error in upload video image", detal_message=e)
            
    def upload_video(self, video_path:str, user:int, cursor=None):
        try:
            add_video_query = f"insert into portfolio_video (video_path, created_by_id, source) values ('{video_path}', {user}, 'file')"
            cursor.execute(add_video_query)
            
        except Exception as e:
            raise DaoExceptionError(status_code=401, message="Error in upload video dao", detal_message=e)

    def get_uoloaded_video_count(self, user_id: int, cursor=None):
        total_vedeo_count = 0
        try:
            active_video_count = f"select count(*) from portfolio_video where created_by_id={user_id} and is_active=true"
            cursor.execute(active_video_count)
            total_vedeo_count = cursor.fetchone().get('count', 0)
        except Exception as e:
            raise DaoExceptionError(status_code=401, message="Error in ", detal_message=e)

        return total_vedeo_count


    def get_uoloaded_image_count(self, user_id: int, cursor=None):
        total_image_count = 0
        try:
            active_image_count = f"select count(*) from portfolio_video where created_by_id={user_id} and is_active=true"
            cursor.execute(active_image_count)
            total_image_count = cursor.fetchone().get('count', 0)
        except Exception as e:
            raise DaoExceptionError(status_code=401, message="Error in ", detal_message=e)

        return total_image_count

class PhotographerPorfileDao:
    
    def add_photographer_profile(self, profile_data, address_data, cursor=None):
        try:
            request_data = profile_data.dict()
            request_data.pop('address')
            profile_update_query = ', '.join('{k}={v!a}'.format(k=k, v=str(v)) for k, v in request_data.items())
            add_photographer_profile_query = """insert into photographer_profile (user_id, address_proof, gst_number, gst_proof,
                                                                                location_availability, experties) values ('{user_id}', 
                                                                                '{address_proof}', '{gst_number}', '{gst_proof}', 
                                                                                '{location_availability}',  '{experties}') 
                                                                                ON CONFLICT (user_id) do update set {profile_update_query} RETURNING * """

            request_data['profile_update_query'] = profile_update_query
            cursor.execute(add_photographer_profile_query.format(**request_data))
    
            photographer_profile_data = cursor.fetchone()
            if photographer_profile_data.get('address_id', None):
                address_update = """ update address set {} where id={address_id}""".format(', '.join('{k}={v!a}'.format(k=k, v=str(v)) 
                                                                                            for k, v in address_data.dict().items()), 
                                                                                            address_id=photographer_profile_data['address_id'])
                cursor.execute(address_update)
            else:
                add_address_query = ''' INSERT INTO address (address, city, state_id, district_id, zip_code) values('{address}', '{city}', '{state_id}', 
                                                                                                                   '{district_id}', '{zip_code}') RETURNING id;'''
            
                cursor.execute(add_address_query.format(**address_data.dict()))
                address_id = cursor.fetchone()['id']
                update_photographer_profile_query = """ update photographer_profile set address_id={address_id} 
                                                        where id={profile_id}""".format(address_id=address_id, 
                                                                                        profile_id=photographer_profile_data['id'])
                cursor.execute(update_photographer_profile_query)
            
        except Exception as e:
            raise DaoExceptionError(status_code=401, message="Error in add photographer id", detal_message=e)

    
    