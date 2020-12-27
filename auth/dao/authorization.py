

from config import db_cursor as cursor, db_conn as conn
from exceptions.dao_exceptions import DaoExceptionError
class AutharizationDAO:

    def group_user_permission(self, group_id: int, permisstion_name: str):

        try:
            group_permission_query = f"select * from group_permission as gp join permission as p on p.id=gp.permission_id where group_id={group_id} and p.code='{permisstion_name}'"
           
            cursor.execute(group_permission_query)
            group_permission_data = cursor.fetchone()
            
            return group_permission_data
        except Exception as e:
            print(e)
            raise DaoExceptionError(message="Error in featch data from user permissions", status_code=403)