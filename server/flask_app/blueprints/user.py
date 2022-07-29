from flask import Blueprint, jsonify, request
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

user = Blueprint(name="user", import_name=__name__)

# Create
@user.route("/register", methods=["POST"])
def create_user():
    pw_hash = bcrypt.generate_password_hash(request.json["password"])
    data = {
        "username": request.json["username"],
        "email": request.json["email"],
        "password": pw_hash,
    }
    return jsonify(User.create(data))


# Login
@user.route("/login", methods=["POST"])
def login():
    data = {"email": request.json["email"]}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        output = {"login": "fail", "error": "Invalid email/password"}
        return jsonify(output)
    if user_in_db and not bcrypt.check_password_hash(
        user_in_db.password, request.json["password"]
    ):
        output = {"login": "fail", "error": "Invalid email/password"}
        return jsonify(output)
    output = {"login": "success", "email": user_in_db.email}
    return jsonify(output)


# Read
@user.route("/getByID", methods=["POST"])
def user_by_id():
    data = {"id": request.json["id"]}
    return jsonify(User.get_user_by_id(data)[0])


@user.route("/getAll", methods=["GET"])
def all_users():
    return jsonify(User.get_all_users())


@user.route("/emails", methods=["GET"])
def all_emails():
    return jsonify(User.get_all_emails())


# Delete
@user.route("/delete", methods=["DELETE"])
def delete_user():
    data = {"id": request.json["id"]}
    return jsonify(User.delete_user_by_id(data))
