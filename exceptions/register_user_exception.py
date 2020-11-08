
from flask import jsonify, request
# from app import app
class RegisterUserException(Exception):
    
    def __init__(self, username, status_code=None, message="Error In register user"):
        
        self.username = username
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.message} {self.username}' 
    
    def dict(self):
        return {"error_message": self.message}
    

        
class RegisterUserDaoException(Exception):
    pass

# @app.errorhandler(RegisterUserException)
# def handle_bad_request(error):
#     """Catch BadRequest exception globally, serialize into JSON, and respond with 400."""
#     payload = dict(error.payload or ()) 
#     payload['status'] = error.status
#     payload['message'] = error.message
#     return jsonify(payload), 400