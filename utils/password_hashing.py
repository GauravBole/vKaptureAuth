from passlib.hash import sha256_crypt

class PasswordHashing:
    
    @staticmethod
    def craete_hash(password:str):
        return sha256_crypt.encrypt(password)
    
    @staticmethod
    def decode_hash(password:str, hashed_password:str):
        return sha256_crypt.verify(password, hashed_password)
    
# https://pythonprogramming.net/password-hashing-flask-tutorial/
    