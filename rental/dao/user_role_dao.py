class UserRoleDAO:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def assign_role_to_user_by_names(self, username, role_name):
        """
        Assigns a role to a user using their names instead of IDs
        """
        cur = self.mysql.connection.cursor()
        
        # Find user by username
        cur.execute("SELECT user_id FROM Users WHERE username = %s", (username,))
        user_result = cur.fetchone()
        if not user_result:
            cur.close()
            return {'error': f'User {username} not found'}
        
        user_id = user_result[0]
        
        # Check if relationship already exists
        cur.execute(
            "SELECT * FROM UsersRoles WHERE user_id = %s AND role = %s", 
            (user_id, role_name)
        )
        
        if cur.fetchone():
            cur.close()
            return {'message': f'User {username} already has role {role_name}'}
        
        # Create the relationship
        cur.execute(
            "INSERT INTO UsersRoles (user_id, role) VALUES (%s, %s)",
            (user_id, role_name)
        )
        
        self.mysql.connection.commit()
        cur.close()
        
        return {'message': f'Role {role_name} assigned to user {username} successfully'}
