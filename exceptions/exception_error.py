import sys
from typing import KeysView
class ExceptionError(Exception):
    
    # def __init__(self, status_code=None, message="Error In register user"):
        
    #     self.message = message
    #     self.status_code = status_code
    #     super().__init__(self.message)
        
    # def __str__(self):
    #     return f'{self.message}' 
    
    # def dict(self):
    #     return {"error_message": self.message}
    

    def __init__(self, *args: object, **kwargs:object) -> None:
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None
        self.message = kwargs.get('message', None)
        self.code = kwargs.get("code")
        self.level = kwargs.get("level")
        # self.detail = kwargs.get('detail')
        exc_type, exc_value, exc_traceback = sys.exc_info()
        self.traceback_details = {
                         'filename': exc_traceback.tb_frame.f_code.co_filename,
                         'lineno'  : exc_traceback.tb_lineno,
                         'name'    : exc_traceback.tb_frame.f_code.co_name,
                         'type'    : exc_type.__name__,
                         'message' : str(exc_value)
                        }


    def get_traceback_details(self):
        print("--------->"*10,)
        return self.traceback_details
