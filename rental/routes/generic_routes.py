from flask import Blueprint, request, jsonify
# from flask_mysqldb import MySQL
from rental.service.generic_service import GenericService

generic_blueprint = Blueprint('generic_routes', __name__)

mysql = None
generic_service = None

@generic_blueprint.record_once
def init_app(setup_state):
    global mysql, generic_service
    mysql = setup_state.app.extensions.get('mysql') or setup_state.app._mysql
    generic_service = GenericService(mysql)

@generic_blueprint.route('/tables/<string:table_name>/records', methods=['POST'])
def insert_into_table(table_name):
    data = request.get_json()
    result = generic_service.insert_into_table(table_name, data)
    
    if 'error' in result:
        return jsonify(result), 400
    
    return jsonify(result), 201

@generic_blueprint.route('/tables/<string:table_name>/batch-insert', methods=['POST'])
def batch_insert_noname_records(table_name):
    data = request.get_json()
    column_name = data.get('column_name')
    start_num = data.get('start_num', 1)
    count = data.get('count', 10)
    
    if not column_name:
        return jsonify({'error': 'Column name is required'}), 400
    
    result = generic_service.batch_insert_noname_records(
        table_name, column_name, start_num, count
    )
    
    if 'error' in result:
        return jsonify(result), 400
    
    return jsonify(result), 201

@generic_blueprint.route('/tables/<string:table_name>/aggregate', methods=['GET'])
def calculate_aggregate(table_name):
    column_name = request.args.get('column')
    operation = request.args.get('operation')
    
    if not column_name or not operation:
        return jsonify({'error': 'Column name and operation are required'}), 400
    
    result = generic_service.calculate_aggregate(table_name, column_name, operation)
    
    if 'error' in result:
        return jsonify(result), 400
    
    return jsonify(result)



@generic_blueprint.route('/tables/<string:parent_table_name>/dynamic-copy', methods=['POST'])
def create_dynamic_tables(parent_table_name):
    """
    Endpoint to create dynamic tables with the same structure as the parent table
    and randomly distribute data from the parent table
    """
    result = generic_service.create_dynamic_tables_and_distribute_data(parent_table_name)
    
    if 'error' in result:
        return jsonify(result), 400
    
    return jsonify(result), 201
