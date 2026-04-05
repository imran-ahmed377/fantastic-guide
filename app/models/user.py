from abc import ABC, abstractmethod

# Defining an abstract class named User that inherits from ABC


class User(ABC):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    # Defining an abstract method to get the role of the user, which must be implemented by any subclass of User
    @abstractmethod
    def get_role(self):
        pass
