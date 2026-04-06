# UML Class Diagram

```mermaid
classDiagram
    direction TB

    class User {
        <<abstract>>
        +user_id
        +name
        +get_role()*
    }

    class Customer {
        +get_role()
        +request_rental(rental_service, vehicle, days)
    }

    class Admin {
        +get_role()
        +add_vehicle(vehicle_service, vehicle)
        +remove_vehicle(vehicle_service, vehicle)
    }

    class Vehicle {
        <<abstract>>
        +vehicle_id
        +brand
        +model
        +price_per_day
        -_is_available
        +calculate_rental_cost(days)*
        +mark_unavailable()
        +mark_available()
    }

    class AppModelsCar {
        +seats
        +calculate_rental_cost(days)
    }

    class MainCar {
        +vehicle_id
        +brand
        +model
        +price_per_day
        +is_available
    }

    class UserService {
        +users
        +register_user(user)
    }

    class VehicleService {
        +vehicles
        +add_vehicle(vehicle)
        +get_available_vehicles()
        +find_vehicle(vehicle_id)
    }

    class RentalService {
        +rentals
        +_rental_counter
        +create_rental(customer, vehicle, days)
    }

    class Rental {
        <<missing implementation>>
    }

    User <|-- Customer
    User <|-- Admin
    Vehicle <|-- AppModelsCar

    Customer ..> RentalService : uses
    Admin ..> VehicleService : uses
    UserService ..> User : manages
    VehicleService ..> Vehicle : manages
    RentalService ..> Rental : depends on

    note for AppModelsCar "Represents app/models/car.py::Car"
    note for MainCar "Represents main.py::Car (script-local class)"
```

## Notes

- `app/models/customer.py` and `app/models/admin.py` inherit from `User`.
- `app/services/user_service.py.py` defines `UserService`.
- `app/services/vehicle_service.py` defines `VehicleService`.
- `app/services/rental_service.py` defines `RentalService` and imports `Rental` from an empty `app/models/rental.py`.
- `app/models/customer.py` still calls `rental_service.process_rental(...)`, while `RentalService` currently exposes `create_rental(...)`.
