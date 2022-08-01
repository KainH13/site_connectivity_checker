from flask_app.config.mysqlconnection import connectToMySQL


class Url_set:
    db = "concheck_db"

    def __init__(self, data):
        self.id = data["id"]
        self.url_set = data["url_set"]
        self.name = data["name"]
        self.users_id = data["users_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO url_sets (url_set, name, users_id) VALUES(%(url_set)s, %(name)s, %(users_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    # Read
    @classmethod
    def get_url_set_by_users_id(cls, data):
        query = "SELECT * FROM url_sets WHERE users_id=%(users_id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_url_sets(cls):
        query = "SELECT * FROM url_sets;"
        return connectToMySQL(cls.db).query_db(query)

    # Update
    @classmethod
    def update_url_set_by_id(cls, data):
        query = (
            "UPDATE url_sets SET url_set=%(url_set)s, name=%(name)s WHERE id=%(id)s;"
        )
        return connectToMySQL(cls.db).query_db(query, data)

    # Delete
    @classmethod
    def delete_url_set_by_id(cls, data):
        query = "DELETE FROM url_sets WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
