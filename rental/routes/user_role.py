from flask import Blueprint, request, jsonify
# from flask_mysqldb import MySQL
from rental.service.user_role_service import UserRoleService

user_role_blueprint = Blueprint('user_role_routes', __name__)

mysql = None
user_role_service = None

@user_role_blueprint.record_once
def init_app(setup_state):
    global mysql, user_role_service
    mysql = setup_state.app.extensions.get('mysql') or setup_state.app._mysql
    user_role_service = UserRoleService(mysql)

@user_role_blueprint.route('/user-roles', methods=['POST'])
def assign_role():
    data = request.get_json()
    result = user_role_service.assign_role_to_user(data)
    
    if 'error' in result:
        return jsonify(result), 400
    
    return jsonify(result), 201
