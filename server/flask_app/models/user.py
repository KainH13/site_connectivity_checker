from flask_app.config.mysqlconnection import connectToMySQL


class User:
    db = "concheck_db"

    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (email, password) VALUES(%(email)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    # Read
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT *  FROM users WHERE email = %(email)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL(cls.db).query_db(query)

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        all_emails = []
        for entry in results:
            all_emails.append(entry["email"])
        return all_emails

    # Update
    @classmethod
    def update_user_by_id(cls, data):
        query = "UPDATE users SET email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    # Delete
    @classmethod
    def delete_user_by_id(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
