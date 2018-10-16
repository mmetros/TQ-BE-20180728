import slite3

class User:
    def __init__(self, _id, email, password):
        self.id = _id
        self.username = email
        self.password = password

    @classmethod
    def find_by_email(cls, email):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user WHERE email=?", (email,))
        row = cursor.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user WHERE id=?", (_id,))
        row = cursor.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user
