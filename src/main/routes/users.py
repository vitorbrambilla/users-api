from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.users_handler import UsersHandler
from src.errors.error_handler import handle_error

users_route_bp = Blueprint('users_route', __name__)

@users_route_bp.route('/users', methods=['GET'])
def get_users():
    try:
        users_handler = UsersHandler()
        http_response = users_handler.find_all()
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_error(error)
        return jsonify(http_response.body), http_response.status_code

@users_route_bp.route('/users', methods=['POST'])
def create_user():
    try:
        users_handler = UsersHandler()
        http_request = HttpRequest(body=request.json)
        http_response = users_handler.create_user(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_error(error)
        return jsonify(http_response.body), http_response.status_code
    
@users_route_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        users_handler = UsersHandler()
        http_request = HttpRequest(body=request.json)
        http_response = users_handler.update_user(user_id, http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_error(error)
        return jsonify(http_response.body), http_response.status_code
    
@users_route_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        users_handler = UsersHandler()
        http_response = users_handler.delete_user(user_id)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_error(error)
        return jsonify(http_response.body), http_response.status_code