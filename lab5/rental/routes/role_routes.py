from flask import Blueprint, request, jsonify
# from flask_mysqldb import MySQL
from rental.service.role_service import RoleService

role_blueprint = Blueprint('role_routes', __name__)

mysql = None
role_service = None

@role_blueprint.record_once
def init_app(setup_state):
    global mysql, role_service
    mysql = setup_state.app.extensions.get('mysql') or setup_state.app._mysql
    role_service = RoleService(mysql)

@role_blueprint.route('/users/<int:user_id>/roles', methods=['GET'])
def get_user_roles(user_id):
    """
    Get roles for a specific user
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: List of roles
    """
    return jsonify(role_service.get_user_roles(user_id))

@role_blueprint.route('/users/<int:user_id>/roles', methods=['POST'])
def assign_role(user_id):
    """
    Assign a role to a user
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            role:
              type: string
    responses:
      200:
        description: Role assigned
    """
    data = request.get_json()
    return jsonify(role_service.assign_role(user_id, data))

@role_blueprint.route('/roles/<int:user_role_id>', methods=['DELETE'])
def remove_role(user_role_id):
    return jsonify(role_service.remove_role(user_role_id))

@role_blueprint.route('/roles/<string:role>/users', methods=['GET'])
def get_users_by_role(role):
    return jsonify(role_service.get_users_by_role(role))
