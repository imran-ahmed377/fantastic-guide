# Enterprise Rent-a-Car System

A comprehensive Object-Oriented Programming (OOP) implementation of a car rental management system. This project demonstrates key OOP principles including **inheritance**, **abstraction**, **polymorphism**, and **encapsulation** in Python.

## 🎯 Project Overview

Enterprise Rent-a-Car is a backend system designed to manage vehicle rentals, customer accounts, and administrative operations. The system provides a clean, maintainable architecture built with abstract base classes, service layers, and comprehensive business logic for handling rental transactions.

## ✨ Features

- **User Management**: Support for different user roles (Customer and Admin)
- **Vehicle Management**: Inventory management with availability tracking
- **Rental Processing**: Create and manage rental transactions with cost calculations
- **Role-Based Operations**: Different capabilities for customers and administrators
- **Cost Calculation**: Automatic rental cost computation based on duration
- **Vehicle Availability Tracking**: Track vehicle status (available/unavailable)

## 📁 Project Structure

```
enterprise_rent_a_car/
├── main.py                           # Entry point with example usage
├── requirement.txt                   # Project dependencies
├── README.md                         # This file
├── UML_CLASS_DIAGRAM.md             # Class architecture diagram
├── app/
│   ├── __init__.py                  # Package initialization
│   ├── core/                        # Core utilities (reserved for future use)
│   ├── models/                      # Data models and entities
│   │   ├── __init__.py
│   │   ├── user.py                  # Abstract User base class
│   │   ├── vehicle.py               # Abstract Vehicle base class
│   │   ├── customer.py              # Customer subclass
│   │   ├── admin.py                 # Admin subclass
│   │   ├── car.py                   # Car concrete implementation
│   │   └── rental.py                # Rental transaction model
│   ├── services/                    # Business logic and services
│   │   ├── user_service.py.py       # User management service
│   │   ├── vehicle_service.py       # Vehicle management service
│   │   └── rental_service.py        # Rental processing service
│   └── utils/                       # Utility functions (reserved for future use)
└── data/                            # Data storage (reserved for future use)
```

## 🏗️ Architecture & Class Design

### Core Abstractions

#### `User` (Abstract Base Class)
- **Purpose**: Define the common interface for all user types
- **Attributes**:
  - `user_id`: Unique identifier for the user
  - `name`: User's full name
- **Abstract Methods**:
  - `get_role()`: Return the user's role

#### `Vehicle` (Abstract Base Class)
- **Purpose**: Define the common interface for all vehicle types
- **Attributes**:
  - `vehicle_id`: Unique identifier for the vehicle
  - `brand`: Vehicle brand/manufacturer
  - `model`: Vehicle model name
  - `price_per_day`: Daily rental rate
  - `_is_available`: Availability status (private attribute)
- **Abstract Methods**:
  - `calculate_rental_cost(days)`: Calculate total rental cost
- **Concrete Methods**:
  - `mark_available()`: Mark vehicle as available
  - `mark_unavailable()`: Mark vehicle as unavailable

### Concrete Implementations

#### `Customer` (extends User)
- Represents a customer in the rental system
- **Methods**:
  - `get_role()`: Returns 'Customer'
  - `request_rental(rental_service, vehicle, days)`: Request a vehicle rental

#### `Admin` (extends User)
- Represents an administrator in the rental system
- **Methods**:
  - `get_role()`: Returns 'Admin'
  - `add_vehicle(vehicle_service, vehicle)`: Add vehicles to inventory
  - `remove_vehicle(vehicle_service, vehicle)`: Remove vehicles from inventory

#### `Car` (extends Vehicle)
- Concrete vehicle type for standard cars
- **Attributes**:
  - `seats`: Number of seats in the car
- **Methods**:
  - `calculate_rental_cost(days)`: Returns `price_per_day * days`

### Data Models

#### `Rental`
- Represents a rental transaction
- **Attributes**:
  - `_rental_id`: Unique rental identifier
  - `_customer`: Customer making the rental
  - `_vehicle`: Vehicle being rented
  - `_days`: Number of days rented
  - `_total_cost`: Total cost of the rental
- **Methods**:
  - `get_summary()`: Returns rental details as a dictionary

### Service Layer

#### `UserService`
- Manages user registration and retrieval
- **Methods**:
  - `register_user(user)`: Register a new user

#### `VehicleService`
- Manages vehicle inventory
- **Methods**:
  - `add_vehicle(vehicle)`: Add a vehicle to inventory
  - `get_available_vehicles()`: Retrieve all available vehicles
  - `find_vehicle(vehicle_id)`: Find a vehicle by ID

#### `RentalService`
- Handles rental transaction processing
- **Methods**:
  - `create_rental(customer, vehicle, days)`: Create a new rental transaction
  - Automatically increments rental IDs and manages vehicle availability

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Installation

1. Clone or download the project:
```bash
cd enterprise_rent_a_car
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## 💻 Usage

### Basic Example

```python
from app.models.customer import Customer
from app.models.admin import Admin
from app.models.car import Car
from app.services.user_service import UserService
from app.services.vehicle_service import VehicleService
from app.services.rental_service import RentalService

# Initialize services
user_service = UserService()
vehicle_service = VehicleService()
rental_service = RentalService()

# Create users
customer1 = Customer(1, "John Doe")
admin1 = Admin(101, "Jane Smith")

# Register users
user_service.register_user(customer1)
user_service.register_user(admin1)

# Create vehicles
car1 = Car(1, "Toyota", "Camry", 50, 5)
car2 = Car(2, "Honda", "Civic", 45, 5)

# Admin adds vehicles to inventory
admin1.add_vehicle(vehicle_service, car1)
admin1.add_vehicle(vehicle_service, car2)

# Get available vehicles
available = vehicle_service.get_available_vehicles()
print(f"Available vehicles: {len(available)}")

# Customer requests a rental
if available:
    rental = rental_service.create_rental(customer1, car1, 5)
    print("Rental created:", rental.get_summary())

# Check remaining available vehicles
available_after = vehicle_service.get_available_vehicles()
print(f"Available vehicles after rental: {len(available_after)}")
```

### Output Example

```
Available vehicles: 2
Rental created: {'customer': 'John Doe', 'vehicle': 'Camry', 'days': 5, 'total_cost': 250}
Available vehicles after rental: 1
```

## 🔑 Key Concepts Demonstrated

### 1. **Abstraction**
- Abstract base classes (`User`, `Vehicle`) define contracts for subclasses
- Implementation details are hidden from consumers

### 2. **Inheritance**
- `Customer` and `Admin` inherit from `User`
- `Car` inherits from `Vehicle`
- Promotes code reuse and consistency

### 3. **Polymorphism**
- Different user roles implement `get_role()` differently
- Different vehicle types can implement `calculate_rental_cost()` differently

### 4. **Encapsulation**
- Private attributes (e.g., `_is_available`, `_rental_id`) hide internal state
- Public methods provide controlled access to data

### 5. **Service Layer Pattern**
- Services handle business logic separately from models
- Improves maintainability and testability

## 📊 Class Relationships

```
User (Abstract)
├── Customer
└── Admin

Vehicle (Abstract)
└── Car

Services:
├── UserService → manages Users
├── VehicleService → manages Vehicles
├── RentalService → manages Rentals

Rental:
├── belongs to Customer
└── involves Vehicle
```

## 🔄 Workflow Example

1. **Admin** registers in the system
2. **Admin** adds cars to vehicle inventory
3. **Customer** registers in the system
4. **Customer** requests a rental for an available vehicle
5. **RentalService** creates a rental transaction
6. Vehicle is marked as unavailable
7. **Customer** receives rental summary with total cost

## 🛠️ Running the Project

Execute the main script:

```bash
python main.py
```

This will run a demonstration with sample cars and their properties.

## 📝 Notes

- The `data/` folder is reserved for future database integration
- The `core/` and `utils/` folders are reserved for additional utility functions
- The system currently stores all data in memory; future versions could integrate with a database
- Vehicle availability is tracked in real-time during rental operations

## 🎓 Educational Value

This project is an excellent resource for learning:
- Object-Oriented Programming principles in Python
- Design patterns (Service Layer, Abstract Factory concepts)
- Class hierarchies and inheritance
- Professional code organization and structure
- Business logic implementation

## 📄 Files Reference

- **UML_CLASS_DIAGRAM.md**: Visual representation of class relationships and architecture
- **PrepCodex.md** & **PrepCodex_v2.md**: Additional documentation (reference materials)

## 🤝 Future Enhancements

- Database integration for persistent storage
- User authentication and authorization
- Advanced vehicle filtering and search
- Rental history and reporting
- Payment processing integration
- Vehicle maintenance tracking
- Additional vehicle types (trucks, motorcycles, etc.)
- Customer review and rating system

## 📞 Support

For questions or issues, refer to the code comments and the UML diagram for architectural understanding.

---

**Created as an Object-Oriented Programming exercise demonstrating best practices in Python development.**
