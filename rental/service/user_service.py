from rental.dao.user_dao import UserDAO
from rental.domain.rental_dto import RentalDTO
from rental.domain.user_dto import UserDTO

class UserService:
    def __init__(self, mysql):
        self.dao = UserDAO(mysql)

    def get_all_users(self):
        rows = self.dao.get_all_users()
        return [UserDTO(*row).to_dict() for row in rows]

    def create_user(self, data):
        self.dao.create_user(data)
        return {'message': 'User created successfully'}

    def update_user(self, user_id, data):
        self.dao.update_user(user_id, data)
        return {'message': 'User updated successfully'}

    def delete_user(self, user_id):
        self.dao.delete_user(user_id)
        return {'message': 'User deleted successfully'}
    
    def get_user_with_rentals(self, user_id):
        user_data, rental_rows = self.dao.get_user_with_rentals(user_id)
        
        if not user_data:
            return None
        
        user = UserDTO(*user_data).to_dict()
        rentals = [RentalDTO(*row).to_dict() for row in rental_rows]
        
        user['rentals'] = rentals
        return user
