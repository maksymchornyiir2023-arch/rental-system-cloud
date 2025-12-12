class UserDTO:
    def __init__(self, user_id, username, email, phone):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone
        }
