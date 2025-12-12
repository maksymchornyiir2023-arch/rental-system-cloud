class RentalDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_rentals_by_user_id(self, user_id):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT rental_id, user_id, car_id, location_id, start_date, end_date 
            FROM Rentals 
            WHERE user_id = %s
        """, (user_id,))
        rows = cur.fetchall()
        cur.close()
        return rows
        
    def get_all_rentals_with_details(self):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT 
                r.rental_id, r.user_id, r.car_id, r.location_id, r.start_date, r.end_date,
                u.user_id, u.username, u.email, u.phone,
                c.car_id, cm.model_name, cm.manufacturer, NULL, c.license_plate
            FROM Rentals r
            LEFT JOIN Users u ON r.user_id = u.user_id
            LEFT JOIN Cars c ON r.car_id = c.car_id
            LEFT JOIN CarModels cm ON c.model_id = cm.model_id
        """)
        rows = cur.fetchall()
        cur.close()
        
        # Process the results to separate rental, user, and car data
        result = []
        for row in rows:
            rental = row[0:6]
            user = row[6:10]
            car = row[10:15]
            result.append((rental, user, car))
            
        return result
        
    def get_rental_with_details(self, rental_id):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT 
                r.rental_id, r.user_id, r.car_id, r.location_id, r.start_date, r.end_date,
                u.user_id, u.username, u.email, u.phone,
                c.car_id, cm.model_name, cm.manufacturer, NULL, c.license_plate
            FROM Rentals r
            LEFT JOIN Users u ON r.user_id = u.user_id
            LEFT JOIN Cars c ON r.car_id = c.car_id
            LEFT JOIN CarModels cm ON c.model_id = cm.model_id
            WHERE r.rental_id = %s
        """, (rental_id,))
        row = cur.fetchone()
        cur.close()
        
        if not row:
            return None
            
        rental = row[0:6]
        user = row[6:10]
        car = row[10:15]
        
        return (rental, user, car)
        
    def create_rental(self, data):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            INSERT INTO Rentals (user_id, car_id, location_id, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (data['user_id'], data['car_id'], data['location_id'], 
              data['start_date'], data['end_date']))
        self.mysql.connection.commit()
        cur.close()
