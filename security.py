from werkzeug.security import safe_str_cmp
from user import User

def authenticate(email, password):
    return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
