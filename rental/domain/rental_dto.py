class RentalDTO:
    def __init__(self, rental_id: int, user_id: int, car_id: int, location_id: int, 
                 start_date: str, end_date: str):
        self.rental_id = rental_id
        self.user_id = user_id
        self.car_id = car_id
        self.location_id = location_id
        self.start_date = start_date
        self.end_date = end_date
        
    def to_dict(self):
        return {
            'rental_id': self.rental_id,
            'user_id': self.user_id,
            'car_id': self.car_id,
            'location_id': self.location_id,
            'start_date': self.start_date,
            'end_date': self.end_date
        }
