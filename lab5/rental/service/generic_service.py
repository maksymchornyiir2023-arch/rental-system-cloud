from rental.dao.generic_dao import GenericDAO

class GenericService:
    def __init__(self, mysql):
        self.dao = GenericDAO(mysql)
    
    def insert_into_table(self, table_name, data):
        """
        Insert data into any table
        
        Args:
            table_name (str): Name of the table to insert into
            data (dict): Dictionary with column names as keys and values to insert
        
        Returns:
            dict: Response with message and inserted record ID
        """
        # Validate table name to prevent SQL injection
        valid_tables = ['Users', 'Rentals', 'Cars', 'CarModels', 'Locations', 'UsersRoles']
        if table_name not in valid_tables:
            return {'error': 'Invalid table name'}
        
        last_id = self.dao.insert_into_table(table_name, data)
        return {
            'message': f'Record inserted successfully into {table_name}',
            'id': last_id
        }
    
    def batch_insert_noname_records(self, table_name, column_name, start_num=1, count=10):
        """
        Service method to insert multiple records with 'Noname+№' format
        
        Args:
            table_name (str): Name of the table to insert into
            column_name (str): The column to insert the Noname values into
            start_num (int): Starting number for Noname sequence
            count (int): Number of records to insert (default: 10)
        
        Returns:
            dict: Response with message and inserted record IDs
        """
        # Validate table name to prevent SQL injection
        valid_tables = ['Users', 'Rentals', 'Cars', 'CarModels', 'Locations', 'UsersRoles']
        if table_name not in valid_tables:
            return {'error': 'Invalid table name'}
            
        # Map tables to their required columns
        required_columns = {
            'Users': ['username', 'email'],
            'Rentals': ['user_id', 'car_id', 'location_id', 'start_date', 'end_date'],
            'Cars': ['model_id', 'license_plate'],
            'CarModels': ['manufacturer', 'model_name'],
            'Locations': ['name', 'address', 'capacity'],
            'UsersRoles': ['user_id', 'role']
        }
        
        # Check if the column exists in the table
        if column_name not in required_columns.get(table_name, []):
            return {'error': f'Column {column_name} is not valid for table {table_name}'}
        
        inserted_ids = self.dao.batch_insert_noname_records(table_name, column_name, start_num, count)
        
        return {
            'message': f'Successfully inserted {count} records into {table_name}',
            'inserted_ids': inserted_ids
        }
    def calculate_aggregate(self, table_name, column_name, operation):
        """
        Service method to calculate aggregate values on a column
        
        Args:
            table_name (str): Name of the table
            column_name (str): Name of the column to aggregate
            operation (str): One of 'MAX', 'MIN', 'SUM', 'AVG'
            
        Returns:
            dict: Response with the calculated value
        """
        # Validate table name to prevent SQL injection
        valid_tables = ['Users', 'Rentals', 'Cars', 'CarModels', 'Locations', 'UsersRoles']
        if table_name not in valid_tables:
            return {'error': 'Invalid table name'}
        
        try:
            # Use the stored procedure
            result = self.dao.call_aggregate_procedure(table_name, column_name, operation)
            return {
                'table': table_name,
                'column': column_name,
                'operation': operation.upper(),
                'result': result
            }
        except Exception as e:
            return {'error': str(e)}

    def create_dynamic_tables_and_distribute_data(self, parent_table_name):
        """
        Service method to create dynamic tables and distribute data
        
        Args:
            parent_table_name (str): Name of the parent table
            
        Returns:
            dict: Information about the created tables and distribution
        """
        # Validate table name to prevent SQL injection
        valid_tables = ['Users', 'Rentals', 'Cars', 'CarModels', 'Locations', 'UsersRoles']
        if parent_table_name not in valid_tables:
            return {'error': 'Invalid table name'}
        
        try:
            result = self.dao.create_dynamic_tables_and_distribute_data(parent_table_name)
            return {
                'message': f'Successfully created dynamic tables and distributed data from {parent_table_name}',
                'tables': result
            }
        except Exception as e:
            return {'error': str(e)}
