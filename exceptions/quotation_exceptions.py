
from .main_custome_exception import VkaptureError

class AddQuotationException(VkaptureError):
    ''' Error in add quotation '''

    def __init__(self, message, status_code) -> None:
        super().__init__(message=message, status_code=status_code)


class AddQuotationDaoException(VkaptureError):
    ''' Error in quotaion dao '''

    def __init__(self, message, status_code) -> None:
        super().__init__(message=message, status_code=status_code)