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

    class MainCar {
        +vehicle_id
        +brand
        +model
        +price_per_day
        +is_available
    }

    AppModelsCar --|> Vehicle : inherits

    note for AppModelsCar "Represents app/models/car.py::Car"
    note for MainCar "Represents main.py::Car (script-local class)"
```

## Notes

- `app/models/admin.py` is currently empty.
- `app/models/customer.py` is currently empty.
- `app/models/rental.py` is currently empty.
- No associations/compositions are currently implemented between user/rental/vehicle entities.
