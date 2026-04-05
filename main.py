class Car:
    def __init__(self, vehicle_id, brand, model, price_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.is_available = True


car1 = Car(1, 'Toyota', 'Camry', 50)
car2 = Car(2, 'Honda', 'Civic', 45)
car3 = Car(3, 'Ford', 'Mustang', 100)


print(f'Car 1: {car1.brand} {car1.model}, Price per day: ${car1.price_per_day}, Available: {car1.is_available}')
print(f'Car 2: {car2.brand} {car2.model}, Price per day: ${car2.price_per_day}, Available: {car2.is_available}')
print(f'Car 3: {car3.brand} {car3.model}, Price per day: ${car3.price_per_day}, Available: {car3.is_available}')