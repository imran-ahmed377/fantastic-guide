# Rental class to represent a rental transaction in the car rental system
class Rental:
    def __init__(self, rental_id, customer, vehicle, days):
        self._rental_id = rental_id  # Initializing the rental_id attribute
        self._customer = customer  # Initializing the customer attribute
        self._vehicle = vehicle  # Initializing the vehicle attribute
        self._days = days  # Initializing the days attribute
        # Calculating the total cost of the rental using the vehicle's method
        self._total_cost = self._vehicle.calculate_rental_cost(days)

    # Method to get a summary of the rental details, including customer name, vehicle model, rental days, and total cost
    def get_summary(self):
        return {
            'customer': self._customer.name,  # Returning the customer's name in the summary
            'vehicle': self._vehicle.model,  # Returning the vehicle's model in the summary
            'days': self._days,  # Returning the number of rental days in the summary
            # Returning the total cost of the rental in the summary
            'total_cost': self._total_cost
        }
