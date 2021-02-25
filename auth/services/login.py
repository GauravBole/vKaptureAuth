
from auth.dao.login import UserLoginDao
from auth.dao.user_profile import UserProfileDao
from utils.jwt_util import JWTEncodeDecode
from utils.password_hashing import PasswordHashing
from exceptions.exception_error import ExceptionError
from exceptions.auth_exceptions import LoginUserDaoException, LoginUserException
from database_connection.decorator import atomic_tarnsaction
class LoginService:

    @atomic_tarnsaction
    def login_user(self, request_data: dict, cursor=None):
        try:
            user_login_dao_obj = UserLoginDao()
            check_passwoed = False
            is_login, user_data = user_login_dao_obj.login_user(username=request_data['username'], password=request_data['password'], cursor=cursor)
            jwt_encoder = JWTEncodeDecode()
            token = jwt_encoder.encode(user_id=user_data['id'], group_id=user_data["group_id"]).decode("utf-8")
            if is_login:
                check_passwoed = PasswordHashing.decode_hash(request_data['password'], user_data['password'])
                
            if check_passwoed:
                user_profile_dao_obj = UserProfileDao()
                user_profile = user_profile_dao_obj.get_user_info_from_user_id(user_id=user_data['id'], cursor=cursor)
                user_profile['tokne'] = token
                return user_profile
            if is_login is False or check_passwoed is False:
                raise ValueError("invalid user username and password")

        except (ValueError, LoginUserDaoException):
            raise 

        except Exception as e:
            print(e)
            raise LoginUserException(message="error in login user service", status_code=403)