import sqlite3
from flask_restful import Resource
from flask_jwt import jwt_required, current_identity

class Venues(Resource):

    @jwt_required()
    def get(self):
        # print(current_identity.name)
        # print(current_identity.email)
        # print(current_identity.password)
        # print(current_identity.id)
        return "success"
