from .main_custome_exception import VkaptureError


class AddInqueryException(VkaptureError):
    ''' Error in Add inquiry'''
    def __init__(self, message, status_code) -> None:
        super().__init__(message=message, status_code=status_code)


class AddInqueryDaoException(VkaptureError):
    ''' Error in add inquiry dao '''

    def __init__(self, message, status_code) -> None:
        super().__init__(message=message, status_code=status_code)
        
class SendQeryException(VkaptureError):
    ''' Error in send query photographer '''

    def __init__(self, message, status_code) -> None:
        super().__init__(message=message, status_code=status_code)

class SendQeryDaoException(VkaptureError):
    ''' Error in send query photographer dao '''

    def __init__(self, message, status_code) -> None:
        super().__init__(message=message, status_code=status_code)