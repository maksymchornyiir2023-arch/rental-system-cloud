from rental.dao.role_dao import RoleDAO
from rental.domain.role_dto import RoleDTO
from rental.domain.user_dto import UserDTO

class RoleService:
    def __init__(self, mysql):
        self.dao = RoleDAO(mysql)
    
    def get_user_roles(self, user_id):
        roles = self.dao.get_user_roles(user_id)
        return [RoleDTO(*role).to_dict() for role in roles]
    
    def assign_role(self, user_id, role_data):
        self.dao.assign_role(user_id, role_data['role'])
        return {'message': f"Role '{role_data['role']}' assigned to user {user_id}"}
    
    def remove_role(self, user_role_id):
        self.dao.remove_role(user_role_id)
        return {'message': 'Role removed successfully'}
    
    def get_users_by_role(self, role):
        users = self.dao.get_users_by_role(role)
        return [UserDTO(*user).to_dict() for user in users]
