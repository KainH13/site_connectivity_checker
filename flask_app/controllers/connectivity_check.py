from flask import Blueprint, jsonify, request

connectivity_check = Blueprint(name="connectivity_check", import_name=__name__)

@connectivity_check.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from connectivity_check."}
    return jsonify(output)