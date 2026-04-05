from .vehicle import Vehicle  # Importing the Vehicle class from the vehicle module


# Defining the Car class that inherits from the Vehicle class
class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, price_per_day, seats):
        # Calling the constructor of the parent class (Vehicle) to initialize common attributes
        super().__init__(vehicle_id, brand, model, price_per_day)
        self.seats = seats  # Initializing the seats attribute specific to the Car class

    def calculate_rental_cost(self, days):
        # Implementing the abstract method to calculate rental cost based on the number of days
        return self.price_per_day * days
