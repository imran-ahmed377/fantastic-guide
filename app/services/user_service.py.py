# User Service to manage user registration and information
class UserService:
    def __init__(self):
        self.users = []

    # Method to register a new user by adding them to the users list
    def register_user(self, user):
        self.users.append(user)
