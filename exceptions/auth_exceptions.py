from .main_custome_exception import VkaptureError
from flask import jsonify, request
# from app import app
class RegisterUserException(VkaptureError):
    
    # def __init__(self, status_code=None, message="Error In register user"):
        
    #     # self.username = username
    #     self.message = message
    #     self.status_code = status_code
    #     super().__init__(self.message)
        
    # def __str__(self):
    #     return f'{self.message}'

    # def dict(self):
    #     return {"error_message": self.message}

    def __init__(self, message, status_code) -> None:
        super().__init__(message=message, status_code=status_code)
    

        
class RegisterUserDaoException(VkaptureError):
    ''' Exception raise when user registration error accure'''

    def __init__(self, message, status_code) -> None:
        super().__init__(message=message, status_code=status_code)


class LoginUserException(VkaptureError):
    ''' Error in login user '''

    def __init__(self, message, status_code) -> None:
        super().__init__(message=message, status_code=status_code)

class LoginUserDaoException(VkaptureError):
    ''' when error in login user '''

    def __init__(self, message, status_code) -> None:
        super().__init__(message=message, status_code=status_code)
    

