from rental.dao.user_role_dao import UserRoleDAO

class UserRoleService:
    def __init__(self, mysql):
        self.dao = UserRoleDAO(mysql)
    
    def assign_role_to_user(self, data):
        username = data.get('username')
        role_name = data.get('role_name')
        
        if not username or not role_name:
            return {'error': 'Username and role name are required'}
        
        return self.dao.assign_role_to_user_by_names(username, role_name)
