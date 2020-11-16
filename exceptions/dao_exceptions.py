class DaoExceptionError(Exception):
    
    def __init__(self, status_code=None, message="Error In register user"):
        
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.message}' 
    
    def dict(self):
        return {"error_message": self.message}
    