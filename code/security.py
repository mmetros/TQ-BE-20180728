from werkzeug.security import safe_str_cmp
from user import User

def authenticate(email, password):
    # find user by email
    user = User.find_by_email(email)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    print(user_id)
    return User.find_by_id(user_id)
