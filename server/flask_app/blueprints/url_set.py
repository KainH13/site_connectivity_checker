import json
from flask import Blueprint, jsonify, request
from flask_app.models.url_set import Url_set

url_set = Blueprint(name="url_set", import_name=__name__)


# Shared functions
def format_url_set(url_set):
    """
    Formats url set for insertion into JSON field via MySQL syntax
    """
    formatted_url_set = "["
    for i in range(len(url_set)):
        formatted_url_set += f'"{url_set[i]}"'
        if i != len(url_set) - 1:
            formatted_url_set += ", "
    formatted_url_set += "]"
    return formatted_url_set


# Create
@url_set.route("/create", methods=["POST"])
def create_url_set():
    url_set = list(request.json["url_set"])
    formatted_url_set = format_url_set(url_set)
    data = {
        "url_set": formatted_url_set,
        "name": request.json["name"],
        "users_id": request.json["users_id"],
    }
    return jsonify(Url_set.create(data))


# Read
@url_set.route("/get_by_users_id", methods=["POST"])
def get_by_users_id():
    data = {"users_id": request.json["users_id"]}
    return jsonify(Url_set.get_url_set_by_users_id(data))


@url_set.route("/get_all", methods=["GET"])
def get_all():
    return jsonify(Url_set.get_all_url_sets())


# Update
@url_set.route("/update", methods=["POST"])
def update_url_set():
    url_set = list(request.json["url_set"])
    formatted_url_set = format_url_set(url_set)
    data = {
        "id": request.json["id"],
        "name": request.json["name"],
        "url_set": formatted_url_set,
    }
    return jsonify(Url_set.update_url_set_by_id(data))


# Delete
@url_set.route("/delete", methods=["DELETE"])
def delete():
    data = {"id": request.json["id"]}
    return jsonify(Url_set.delete_url_set_by_id(data))
