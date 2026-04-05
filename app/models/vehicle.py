# Importing the ABC (Abstract Base Class) and abstractmethod from the abc module
from abc import ABC, abstractmethod


class Vehicle(ABC):  # Defining an abstract class named Vehicle that inherits from ABC
    def __init__(self, vehicle_id, brand, model, price_per_day):
        self.vehicle_id = vehicle_id  # Initializing the vehicle_id attribute
        self.brand = brand  # Initializing the brand attribute
        self.model = model  # Initializing the model attribute
        self.price_per_day = price_per_day  # Initializing the price_per_day attribute
        self._is_available = True  # Initializing the _is_available attribute to True

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass  # Abstract method to calculate rental cost, to be implemented by subclasses

    def mark_unavailable(self):
        self._is_available = False  # Method to mark the vehicle as unavailable

    def mark_available(self):
        self._is_available = True  # Method to mark the vehicle as available
