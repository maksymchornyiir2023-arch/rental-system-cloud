from flask import Blueprint, request, jsonify
from flask_mysqldb import MySQL
from rental.service.rental_service import RentalService

rental_blueprint = Blueprint('rental_routes', __name__)

mysql = MySQL()
rental_service = None

@rental_blueprint.record_once
def init_app(setup_state):
    global mysql, rental_service
    mysql = setup_state.app.extensions.get('mysql') or setup_state.app._mysql
    rental_service = RentalService(mysql)

@rental_blueprint.route('/rentals', methods=['GET'])
def get_all_rentals():
    return jsonify(rental_service.get_all_rentals_with_details())

@rental_blueprint.route('/rentals/<int:rental_id>', methods=['GET'])
def get_rental(rental_id):
    return jsonify(rental_service.get_rental_with_details(rental_id))

@rental_blueprint.route('/rentals', methods=['POST'])
def create_rental():
    data = request.get_json()
    return jsonify(rental_service.create_rental(data))
