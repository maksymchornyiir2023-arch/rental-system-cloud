from rental.dao.rental_dao import RentalDAO
from rental.domain.rental_dto import RentalDTO
from rental.domain.user_dto import UserDTO

class RentalService:
    def __init__(self, mysql):
        self.dao = RentalDAO(mysql)

    def get_rentals_by_user_id(self, user_id):
        rows = self.dao.get_rentals_by_user_id(user_id)
        return [RentalDTO(*row).to_dict() for row in rows]
        
    def get_all_rentals_with_details(self):
        rentals_data = self.dao.get_all_rentals_with_details()
        result = []
        
        for rental, user, car in rentals_data:
            rental_dict = RentalDTO(*rental).to_dict()
            rental_dict['user'] = UserDTO(*user).to_dict() if user else None
            rental_dict['car'] = self._car_to_dict(car) if car else None
            result.append(rental_dict)
            
        return result
    
    def get_rental_with_details(self, rental_id):
        rental_data = self.dao.get_rental_with_details(rental_id)
        
        if not rental_data or not rental_data[0]:
            return None
            
        rental, user, car = rental_data
        rental_dict = RentalDTO(*rental).to_dict()
        rental_dict['user'] = UserDTO(*user).to_dict() if user else None
        rental_dict['car'] = self._car_to_dict(car) if car else None
        
        return rental_dict
        
    def create_rental(self, data):
        self.dao.create_rental(data)
        return {'message': 'Rental created successfully'}
        
    def _car_to_dict(self, car):
        if not car:
            return None
        return {
            'car_id': car[0],
            'model': car[1],         # This is now model_name from CarModels
            'manufacturer': car[2],  # This is manufacturer from CarModels
            'year': car[3],          # This is NULL for now
            'license_plate': car[4]  # This remains the same
        }
