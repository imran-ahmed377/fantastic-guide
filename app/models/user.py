from abc import ABC, abstractmethod

"""
This module defines the User class, which serves as an abstract 
base class for different types of users in the car rental system. The 
User class includes attributes for user ID and name, as well as an abstract 
method to get the role of the user. Subclasses of User will need to implement 
the get_role method to specify their specific roles (e.g., Customer, Employee).
"""


class User(ABC):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    # Defining an abstract method to get the role of the user, which must be implemented by any subclass of User
    @abstractmethod
    def get_role(self):
        pass
