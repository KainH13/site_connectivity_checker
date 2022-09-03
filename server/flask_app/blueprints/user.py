import json
import os
from datetime import datetime, timedelta
import jwt
from flask import Blueprint, jsonify, request
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.config.jwt_helper import auth_required

bcrypt = Bcrypt(app)

user = Blueprint(name="user", import_name=__name__)

# Create
@user.route("/register", methods=["POST"])
def register():
    """
    Register a new user
    json body is expected to contain {
        email: required(string),
        password: required(string)
        confirmPassword: required(string)
    }
    """

    # validations
    data = request.get_json(force=True)
    email = data.get("email", None)
    password = data.get("password", None)
    confirmPassword = data.get("confirmPassword", None)

    if None in [email, password]:
        return (
            jsonify({"error": "Email and password are required to create an account"}),
            400,
        )

    if password != confirmPassword:
        return (jsonify({"error": "Passwords do not match"}), 400)

    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400

    # checks that a user with this email does not already exist
    all_emails = set(User.get_all_emails())
    email = request.json["email"]
    if email in all_emails:  # using a set gives O(1) lookup time complexity
        return (
            jsonify(
                {
                    "error": "An account with that email already exists. Please create an account with a unique email"
                }
            ),
            401,
        )

    # hashes password, sets up data and creates the user record
    pw_hash = bcrypt.generate_password_hash(request.json["password"])
    data = {
        "email": email,
        "password": pw_hash,
    }
    user_id = User.create(data)

    # creates jwt token
    result = User.get_user_by_id({"id": user_id})
    user = result[0]
    token = jwt.encode(
        {"id": user_id, "exp": datetime.now() + timedelta(days=1)},
        os.environ.get("JWT_SECRET"),
        algorithm="HS256",
    )

    return jsonify({"user": user, "token": token}), 201


# Login
@user.route("/login", methods=["POST"])
def login():
    """
    Authenticate an existing user
    json body is expected to contain {
        email: required(string),
        password: required(string)
    }
    """
    data = request.get_json(force=True)
    email = data.get("email", None)
    password = data.get("password", None)

    # validation
    if None in [email, password]:
        return jsonify({"error": "Email and password are required to login."}), 400

    user = None
    try:
        user = User.get_by_email({"email": email})[0]
    except TypeError:
        return jsonify({"error": "Incorrect email or password."}), 401
    except IndexError:
        return jsonify({"error": "Incorrect email or password."}), 401

    if not bcrypt.check_password_hash(user["password"], password):
        return jsonify({"error": "Incorrect email or password."}), 401

    # create jwt token
    token = jwt.encode(
        {"id": user["id"], "exp": datetime.now() + timedelta(days=1)},
        os.environ.get("JWT_SECRET"),
        algorithm="HS256",
    )

    return jsonify({"user": user, "token": token}), 200


# Read
@user.route("/getByID", methods=["POST"])
def user_by_id():
    data = {"id": request.json["id"]}
    return jsonify(User.get_user_by_id(data))


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
