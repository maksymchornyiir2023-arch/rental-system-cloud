from flask import Blueprint, request, jsonify
# from flask_mysqldb import MySQL
from rental.service.user_service import UserService

user_blueprint = Blueprint('user_routes', __name__)

mysql = None
user_service = None

@user_blueprint.record_once
def init_app(setup_state):
    global mysql, user_service
    # Get the mysql instance directly from the app
    mysql = setup_state.app.extensions.get('mysql') or setup_state.app._mysql
    user_service = UserService(mysql)

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    """
    Get all users
    ---
    responses:
      200:
        description: A list of users
    """
    return jsonify(user_service.get_all_users())

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            email:
              type: string
            phone:
              type: string
    responses:
      200:
        description: User created
    """
    data = request.get_json()
    return jsonify(user_service.create_user(data))

@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return jsonify(user_service.update_user(user_id, data))

@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify(user_service.delete_user(user_id))

@user_blueprint.route('/users/<int:user_id>/rentals', methods=['GET'])
def get_user_rentals(user_id):
    return jsonify(user_service.get_user_with_rentals(user_id))
