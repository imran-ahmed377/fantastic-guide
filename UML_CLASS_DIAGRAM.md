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

    class Customer {
        +get_role()
        +request_rental(rental_service, vehicle, days)
    }

    class Admin {
        +get_role()
        +add_vehicle(vehicle_service, vehicle)
        +remove_vehicle(vehicle_service, vehicle)
    }

    class MainCar {
        +vehicle_id
        +brand
        +model
        +price_per_day
        +is_available
    }

    class RentalService {
        <<not implemented>>
        +process_rental(customer, vehicle, days)
    }

    class VehicleService {
        <<not implemented>>
        +add_vehicle(vehicle)
        +remove_vehicle(vehicle)
    }

    AppModelsCar --|> Vehicle : inherits
    Customer --|> User : inherits
    Admin --|> User : inherits

    Customer ..> RentalService : uses
    Admin ..> VehicleService : uses

    note for AppModelsCar "Represents app/models/car.py::Car"
    note for MainCar "Represents main.py::Car (script-local class)"
```

## Notes

- `app/models/rental.py` is currently empty.
- `app/services/rental_service.py` is currently empty.
- `RentalService` and `VehicleService` in the diagram are inferred from method calls in user models and are not implemented as classes yet.
