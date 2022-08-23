import os
from functools import wraps
from flask import request, jsonify, g
import jwt

from flask_app.models.user import User


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("jwt-access-token", None)
        secret = os.environ.get("JWT_SECRET")
        if token:
            try:
                payload = jwt.decode(token, secret, algorithms=["HS256"])
                user_id = payload["id"]
                if user_id:
                    g.user = User.get_user_by_id({"id": user_id})
                    if g.user == False:
                        return jsonify({"error": "Invalid token"}), 403
            except Exception as e:
                return func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper
