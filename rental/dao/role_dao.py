class RoleDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_user_roles(self, user_id):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT user_role_id, user_id, role
            FROM UsersRoles 
            WHERE user_id = %s
        """, (user_id,))
        roles = cur.fetchall()
        cur.close()
        return roles
    
    def assign_role(self, user_id, role):
        conn = self.mysql.connection
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO UsersRoles (user_id, role)
            VALUES (%s, %s)
        """, (user_id, role))
        conn.commit()
        cur.close()
        
    def remove_role(self, user_role_id):
        conn = self.mysql.connection
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM UsersRoles 
            WHERE user_role_id = %s
        """, (user_role_id,))
        conn.commit()
        cur.close()
        
    def get_users_by_role(self, role):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT u.user_id, u.username, u.email, u.phone, u.created_at
            FROM Users u
            JOIN UsersRoles ur ON u.user_id = ur.user_id
            WHERE ur.role = %s
        """, (role,))
        users = cur.fetchall()
        cur.close()
        return users
