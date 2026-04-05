from .user import User

# Defining a class named Customer that inherits from the User class


class Customer(User):
    def get_role(self):
        return 'Customer'

    # Method for the customer to request a rental, which interacts with the rental service to process the rental request
    def request_rental(self, rental_service, vehicle, days):
        return rental_service.process_rental(self, vehicle, days)
