import re

def validate_mobile_number(number):
    # mobile_number_pattern = re.compile('[7-9][0-9]{9}')
    if re.match(r'[7-9]\d{9}$', number):
        return number
    else:
        raise ValueError({"error": "invalid mobile number"})