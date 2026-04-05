from .user import User

# Defining a class named Admin that inherits from the User class


class Admin(User):
    def get_role(self):
        return 'Admin'

    # Method for the admin to add a vehicle, which interacts with the vehicle service to add a new vehicle to the system
    def add_vehicle(self, vehicle_service, vehicle):
        vehicle_service.add_vehicle(vehicle)

    # Method for the admin to remove a vehicle, which interacts with the vehicle service to remove an existing vehicle from the system
    def remove_vehicle(self, vehicle_service, vehicle):
        vehicle_service.remove_vehicle(vehicle)
