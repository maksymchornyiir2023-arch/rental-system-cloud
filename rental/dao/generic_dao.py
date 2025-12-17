class GenericDAO:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def insert_into_table(self, table_name, data):
        """
        Performs parameterized insertion into any table
        
        Args:
            table_name (str): Name of the table to insert into
            data (dict): Dictionary with column names as keys and values to insert
        
        Returns:
            int: ID of the inserted record
        """
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())
        
        conn = self.mysql.connection
        cur = conn.cursor()
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        cur.execute(query, values)
        last_id = cur.lastrowid
        conn.commit()
        cur.close()
        
        return last_id

    def batch_insert_noname_records(self, table_name, column_name, start_num=1, count=10):
        """
        Inserts multiple records into a table with 'Noname+№' format values
        
        Args:
            table_name (str): Name of the table to insert into
            column_name (str): The column to insert the Noname values into
            start_num (int): Starting number for Noname sequence
            count (int): Number of records to insert (default: 10)
        
        Returns:
            list: List of inserted record IDs
        """
        inserted_ids = []
        conn = self.mysql.connection
        cur = conn.cursor()
        
        for i in range(start_num, start_num + count):
            value = f"Noname{i}"
            
            # Handle different tables with their required columns
            if table_name == 'Users':
                if column_name == 'username':
                    # For Users table, also generate an email when username is provided
                    query = "INSERT INTO Users (username, email) VALUES (%s, %s)"
                    email = f"noname{i}@example.com"
                    cur.execute(query, (value, email))
                elif column_name == 'email':
                    # Generate a username when email is provided
                    query = "INSERT INTO Users (username, email) VALUES (%s, %s)"
                    username = f"user{i}"
                    cur.execute(query, (username, value))
            elif table_name == 'CarModels':
                if column_name == 'model_name':
                    # For CarModels, we need manufacturer too
                    query = "INSERT INTO CarModels (model_name, manufacturer) VALUES (%s, %s)"
                    manufacturer = f"Company{i}"
                    cur.execute(query, (value, manufacturer))
                elif column_name == 'manufacturer':
                    # Generate model_name when manufacturer is provided
                    query = "INSERT INTO CarModels (manufacturer, model_name) VALUES (%s, %s)"
                    model_name = f"Model{i}"
                    cur.execute(query, (value, model_name))
            elif table_name == 'Locations':
                if column_name == 'name':
                    # For Locations, we need address and capacity
                    query = "INSERT INTO Locations (name, address, capacity) VALUES (%s, %s, %s)"
                    address = f"Address{i}"
                    capacity = 10 + i
                    cur.execute(query, (value, address, capacity))
                elif column_name == 'address':
                    # Generate name and capacity when address is provided
                    query = "INSERT INTO Locations (name, address, capacity) VALUES (%s, %s, %s)"
                    name = f"Location{i}"
                    capacity = 10 + i
                    cur.execute(query, (name, value, capacity))
            else:
                # Default case - just insert into the specified column
                # This works for tables with default values for other columns
                query = f"INSERT INTO {table_name} ({column_name}) VALUES (%s)"
                cur.execute(query, (value,))
                
            inserted_ids.append(cur.lastrowid)
        
        conn.commit()
        cur.close()
        
        return inserted_ids
    
    def call_aggregate_procedure(self, table_name, column_name, operation):
        """
        Calls the CalculateAggregate stored procedure
        
        Args:
            table_name (str): Name of the table
            column_name (str): Name of the column to aggregate
            operation (str): One of 'MAX', 'MIN', 'SUM', 'AVG'
        
        Returns:
            float/int: The result of the aggregate operation
        """
        # Normalize the operation to uppercase
        operation = operation.upper()
        
        # Validate the operation
        valid_operations = ['MAX', 'MIN', 'SUM', 'AVG']
        if operation not in valid_operations:
            raise ValueError(f"Operation must be one of {', '.join(valid_operations)}")
        
        cur = self.mysql.connection.cursor()
        
        # Make sure the procedure exists
        self.create_aggregate_procedure()
        
        # Call the procedure
        cur.execute("CALL CalculateAggregate(%s, %s, %s)", (table_name, column_name, operation))
        result = cur.fetchone()[0]
        cur.close()
        
        return result
    

    def create_aggregate_procedure(self):
        """
        Creates a stored procedure that calculates aggregate values
        """
        conn = self.mysql.connection
        cur = conn.cursor()
        
        # First drop the procedure if it exists
        cur.execute("DROP PROCEDURE IF EXISTS CalculateAggregate")
        
        # Create the procedure
        procedure_sql = """
        CREATE PROCEDURE CalculateAggregate(
            IN p_table_name VARCHAR(100),
            IN p_column_name VARCHAR(100),
            IN p_operation VARCHAR(10)
        )
        BEGIN
            SET @sql = CONCAT('SELECT ', p_operation, '(', p_column_name, ') AS result FROM ', p_table_name);
            PREPARE stmt FROM @sql;
            EXECUTE stmt;
            DEALLOCATE PREPARE stmt;
        END
        """
        
        cur.execute(procedure_sql)
        conn.commit()
        cur.close()
    def create_dynamic_tables_and_distribute_data(self, parent_table_name):
        """
        Dynamically creates two tables with timestamp names, copies the structure of the parent table,
        and randomly distributes rows from the parent table to these new tables.
        """
        import time
        import random
        import re
        
        # Generate timestamp for table names
        timestamp = int(time.time())
        table1_name = f"{parent_table_name}_copy1_{timestamp}"
        table2_name = f"{parent_table_name}_copy2_{timestamp}"
        
        conn = self.mysql.connection
        cur = conn.cursor()
        
        try:
            # Get the structure of the parent table
            cur.execute(f"SHOW CREATE TABLE {parent_table_name}")
            create_table_sql = cur.fetchone()[1]
            
            # Use regex to properly replace the table name, regardless of case or backticks
            # This pattern finds "CREATE TABLE `anycase_tablename`" and replaces it
            pattern = re.compile(r'CREATE\s+TABLE\s+`?([^`\s]+)`?', re.IGNORECASE)
            
            # Replace with the new table names
            create_table1_sql = pattern.sub(f"CREATE TABLE `{table1_name}`", create_table_sql, 1)
            create_table2_sql = pattern.sub(f"CREATE TABLE `{table2_name}`", create_table_sql, 1)
            
            # Create the new tables
            cur.execute(create_table1_sql)
            cur.execute(create_table2_sql)
            
            # Get all rows from the parent table
            cur.execute(f"SELECT * FROM {parent_table_name}")
            rows = cur.fetchall()
            
            # Get column names
            cur.execute(f"SHOW COLUMNS FROM {parent_table_name}")
            columns = [column[0] for column in cur.fetchall()]
            columns_str = ', '.join([f"`{col}`" for col in columns])
            
            # Count of rows distributed to each table
            table1_count = 0
            table2_count = 0
            
            # Distribute rows randomly
            for row in rows:
                # Prepare placeholders for the values
                placeholders = ', '.join(['%s'] * len(row))
                
                # Randomly choose which table to insert into
                target_table = table1_name if random.choice([True, False]) else table2_name
                
                # Insert the row
                insert_query = f"INSERT INTO {target_table} ({columns_str}) VALUES ({placeholders})"
                cur.execute(insert_query, row)
                
                # Update counts
                if target_table == table1_name:
                    table1_count += 1
                else:
                    table2_count += 1
            
            conn.commit()
            
            return {
                'parent_table': parent_table_name,
                'table1': {
                    'name': table1_name,
                    'rows_count': table1_count
                },
                'table2': {
                    'name': table2_name,
                    'rows_count': table2_count
                },
                'total_rows_distributed': table1_count + table2_count
            }
            
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
