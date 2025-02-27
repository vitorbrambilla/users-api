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