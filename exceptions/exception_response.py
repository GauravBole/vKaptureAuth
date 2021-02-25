
from .main_custome_exception import VkaptureError
from flask import Blueprint, jsonify
from pydantic import ValidationError

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(VkaptureError)
def handle_error(error):
    success = False
    if hasattr(error, 'message'):
        
        message = error.message
    else:
        message = [str(x) for x in error.args]
    if hasattr(error, 'status_code'):
        status_code = error.status_code
    else:
        status_code = 500

    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response), status_code



@errors.app_errorhandler(Exception)
def handle_unexpected_error(error):
    status_code = 500
    success = False
    print(error)
    response = {
        'success': success,
        'error': {
            'type': 'UnexpectedException',
            'message': 'An unexpected error has occurred.'
        }
    }

    return jsonify(response), status_code


@errors.app_errorhandler(ValidationError)
def handle_pydentic_error(error):
    status_code = 400
    success = False
    error_message = {k.get("loc")[-1]:k.get("msg") for k in error.errors()}

    response = {
        'success': success,
        'error': {
            'type': 'invalid input',
            'message': error_message
        }
    }

    return jsonify(response), status_code