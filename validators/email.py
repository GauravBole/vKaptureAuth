import re
def validate_email(email: str):
    pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if re.search(pattern, email.lower()):
        return email.lower()
    else:
        ValueError({"error": "invalid email"})