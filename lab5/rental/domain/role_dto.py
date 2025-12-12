class RoleDTO:
    def __init__(self, user_role_id: int, user_id: int, role: str):
        self.user_role_id = user_role_id
        self.user_id = user_id
        self.role = role
        
    def to_dict(self):
        return {
            'user_role_id': self.user_role_id,
            'user_id': self.user_id,
            'role': self.role
        }
