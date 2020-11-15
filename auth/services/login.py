
from auth.dao.login import UserLoginDao
from auth.dao.user_profile import UserProfileDao
from utils.password_hashing import PasswordHashing
from exceptions.exception_error import ExceptionError
from exceptions.dao_exceptions import DaoExceptionError
class LoginService:

    def login_user(self, request_data: dict):
        try:
            user_login_dao_obj = UserLoginDao()
            check_passwoed = False        
            is_login, user_data = user_login_dao_obj.login_user(username=request_data['username'], password=request_data['password'])
            if is_login:
                check_passwoed = PasswordHashing.decode_hash(request_data['password'], user_data['password'])
                
            if check_passwoed:
                user_profile_dao_obj = UserProfileDao()
                user_profile = user_profile_dao_obj.get_user_info_from_user_id(user_id=user_data['id'])
                return user_profile
            if is_login is False or check_passwoed is False:
                raise ValueError("invalid user username and pass word")
        except ValueError as ve:
            raise ExceptionError(status_code=403, message=(str(ve)))

        except DaoExceptionError as de:
            raise ExceptionError(status_code=403, message=(de.message))

        except Exception as e:
            raise ExceptionError(message="error in login user service", status_code=403)