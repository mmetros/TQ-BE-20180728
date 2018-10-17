import sqlite3
from flask_restful import Resource, reqparse


class User:
    def __init__(self, name, _id, email, password):
        self.id = _id
        self.name = name
        self.username = email
        self.password = password

    @classmethod
    def find_by_email(cls, email):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        row = cursor.fetchone()
        if row:
            user = cls(row[0], row[1] ,row[2], row[3])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (_id,))
        row = cursor.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('email',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )


    def post(self):
        data = UserRegister.parser.parse_args()

        # if the user already exists
        if User.find_by_email(data['email']):
            return {"message": "This email has already been taken"}
        else:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users VALUES (NULL,?,?,?)", (data['name'], data['email'], data['password']))
            connection.commit()
            connection.close()
            return {"message": "user created succesfully"}, 201
