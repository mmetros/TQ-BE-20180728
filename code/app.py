from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from venue import Venues
from user import UserRegister

app = Flask(__name__)
app.secret_key = 'matthew'
api = Api(app)


jwt = JWT(app, authenticate, identity) #/auth


api.add_resource(UserRegister, '/register')
api.add_resource(Venues, '/venues')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
