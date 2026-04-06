from app.models.rental import Rental
# RentalService class to handle the processing of rental requests in the car rental system


class RentalService:
    def __init__(self):
        self.rentals = []  # Initializing an empty list to store rental transactions in the system
        self._rental_counter = 1  # Initializing a counter to generate unique rental IDs

    def create_rental(self, customer, vehicle, days):
        if not vehicle._is_available:
            # Raising an exception if the vehicle is not available for rental
            raise Exception('Vehicle not available for rental')

        # Creating a new Rental object with a unique rental ID
        rental = Rental(self._rental_counter, customer, vehicle, days)
        # Incrementing the rental counter for the next rental transaction
        self._rental_counter += 1

        vehicle.mark_unavailable()  # Marking the vehicle as unavailable for rental
        # Adding the rental transaction to the rentals list
        self.rentals.append(rental)
        return rental  # Returning the created rental transaction
