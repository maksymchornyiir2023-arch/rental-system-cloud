class UserDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_users(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT user_id, username, email, phone FROM Users")
        rows = cur.fetchall()
        cur.close()
        return rows

    def create_user(self, data):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            INSERT INTO Users (username, email, phone)
            VALUES (%s, %s, %s)
        """, (data['username'], data['email'], data['phone']))
        self.mysql.connection.commit()
        cur.close()

    def update_user(self, user_id, data):
        # First, get the current user data
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT username, email, phone FROM Users WHERE user_id=%s", (user_id,))
        current_user = cur.fetchone()
        
        if not current_user:
            cur.close()
            return False  # User not found
        
        # Update only the fields that are provided
        username = data.get('username', current_user[0])
        email = data.get('email', current_user[1])
        phone = data.get('phone', current_user[2])
        
        # Execute the update with the new values
        cur.execute("""
            UPDATE Users SET username=%s, email=%s, phone=%s
            WHERE user_id=%s
        """, (username, email, phone, user_id))
        
        self.mysql.connection.commit()
        cur.close()
        return True

    def delete_user(self, user_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM Users WHERE user_id=%s", (user_id,))
        self.mysql.connection.commit()
        cur.close()

    def get_user_with_rentals(self, user_id):
        cur = self.mysql.connection.cursor()
        # Get user details
        cur.execute("""
            SELECT user_id, username, email, phone 
            FROM Users 
            WHERE user_id = %s
        """, (user_id,))
        user = cur.fetchone()
        
        if not user:
            cur.close()
            return None, []
        
        # Get rentals for this user
        cur.execute("""
            SELECT rental_id, user_id, car_id, location_id, start_date, end_date
            FROM Rentals 
            WHERE user_id = %s
        """, (user_id,))
        rentals = cur.fetchall()
        cur.close()
        
        return user, rentals


