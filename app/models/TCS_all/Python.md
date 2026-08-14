# Python Basics

# Table of Contents
- [Basic Python Data Structures](#basic-python-data-structures)
  - [1. Variables](#1-variables)
  - [2. Strings](#2-strings)
  - [3. Lists](#3-lists)
  - [4. Tuples](#4-tuples)
  - [5. Dictionaries](#5-dictionaries)
  - [6. Sets](#6-sets)
  - [7. If Statements](#7-if-statements)
  - [8. For Loops](#8-for-loops)
  - [9. While Loops](#9-while-loops)
  - [10. Functions](#10-functions)
  - [11. User Input](#11-user-input)
  - [12. Basic Operators](#12-basic-operators)
  - [Quick Summary](#quick-summary)

- [Python OOP Concepts](#python-oop-concepts)
    - [1️⃣ Classes and Objects](#1️⃣-classes-and-objects)
    - [2️⃣ Methods](#2️⃣-methods)
    - [3️⃣ Variables](#3️⃣-variables)
    - [4️⃣ Encapsulation](#4️⃣-encapsulation)
    - [5️⃣ Inheritance](#5️⃣-inheritance)
    - [6️⃣ Polymorphism](#6️⃣-polymorphism)
    - [7️⃣ Abstraction](#7️⃣-abstraction)
    - [8️⃣ Other Features](#8️⃣-other-features)



# Basic Python Data Structures

Here are some of the most common Python concepts you'll use when starting out.

## 1. Variables

A **variable** stores a value.

```python
name = "Alice"
age = 20
height = 5.7

print(name)
print(age)
print(height)
```

---

## 2. Strings

A **string** is text. You can use single or double quotes.

```python
name = "Alice"
message = 'Hello, world!'

print(name)
print(message)
```

You can combine strings:

```python
first_name = "Alice"
last_name = "Smith"

full_name = first_name + " " + last_name

print(full_name)
```

---

## 3. Lists

A **list** stores multiple values in an ordered collection. Lists can be changed after they are created.

```python
fruits = ["apple", "banana", "orange"]

print(fruits)
print(fruits[0])
print(fruits[1])
```

### Adding an item

```python
fruits.append("mango")

print(fruits)
```

### Removing an item

```python
fruits.remove("banana")

print(fruits)
```

### Looping through a list

```python
for fruit in fruits:
    print(fruit)
```

---

## 4. Tuples

A **tuple** is similar to a list, but you generally cannot change its contents after creating it.

```python
coordinates = (10, 20)

print(coordinates)
print(coordinates[0])
print(coordinates[1])
```

Another example:

```python
colors = ("red", "green", "blue")

for color in colors:
    print(color)
```

**List:** changeable  
**Tuple:** not changeable

---

## 5. Dictionaries

A **dictionary** stores data as **key-value pairs**.

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "Toronto"
}

print(person)
```

Access a value using its key:

```python
print(person["name"])
print(person["age"])
```

### Add or change a value

```python
person["age"] = 26
person["job"] = "Developer"

print(person)
```

### Loop through a dictionary

```python
for key, value in person.items():
    print(key, value)
```

---

## 6. Sets

A **set** is a collection that does not allow duplicate values.

```python
numbers = {1, 2, 3, 4, 4, 5}

print(numbers)
```

The duplicate `4` is automatically removed.

You can add values:

```python
numbers.add(6)

print(numbers)
```

---

## 7. If Statements

An **if statement** allows your program to make decisions.

```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")
```

You can have multiple conditions:

```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
```

---

## 8. For Loops

A **for loop** repeats code for each item in a collection.

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

You can also loop through numbers:

```python
for number in range(5):
    print(number)
```

This prints:

```text
0
1
2
3
4
```

---

## 9. While Loops

A **while loop** keeps running while a condition is true.

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

Output:

```text
1
2
3
4
5
```

---

## 10. Functions

A **function** is a reusable block of code.

```python
def greet():
    print("Hello!")

greet()
```

Functions can accept information called **parameters**:

```python
def greet(name):
    print("Hello", name)

greet("Alice")
greet("Bob")
```

Functions can also return a value:

```python
def add(a, b):
    return a + b

result = add(5, 3)

print(result)
```

Output:

```text
8
```

---

## 11. User Input

`input()` allows the user to enter information.

```python
name = input("What is your name? ")

print("Hello", name)
```

For numbers, convert the input to an integer:

```python
age = int(input("How old are you? "))

print(age)
```

---

## 12. Basic Operators

### Arithmetic

```python
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Whole-number division
print(a % b)   # Remainder
print(a ** b)  # Power
```

### Comparison

```python
x = 10

print(x == 10)  # Equal
print(x != 10)  # Not equal
print(x > 5)    # Greater than
print(x < 20)   # Less than
print(x >= 10)  # Greater/equal
print(x <= 10)  # Less/equal
```

---

## Quick Summary

| Data type | Example | Description |
| --- | --- | --- |
| `str` | `"Hello"` | Text |
| `int` | `10` | Whole number |
| `float` | `3.14` | Decimal number |
| `bool` | `True` | True/False |
| `list` | `[1, 2, 3]` | Ordered, changeable collection |
| `tuple` | `(1, 2, 3)` | Ordered, generally unchangeable collection |
| `dict` | `{"name": "Alice"}` | Key-value pairs |
| `set` | `{1, 2, 3}` | Unique values |

### A small example using several concepts together

```python
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 95}
]

for student in students:
    if student["score"] >= 80:
        print(student["name"], "passed with a good score!")
    else:
        print(student["name"], "passed.")
```

### Find the duplicate in a list

```python
numbers = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9]
duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicates:", duplicates)
```

This example combines **lists, dictionaries, loops, strings, numbers, and if statements**.

# Pandas Basics
## Pandas DataFrame
```python
import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)
```




# Python OOP Concepts

## 1️⃣ Classes and Objects

* **Class** – Blueprint for creating objects.
* **Object (Instance)** – A real entity created from a class.

**Example:**
```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def drive(self):
        return f"Driving a {self.color} {self.brand}"

# Creating objects (instances)
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.drive())  # Output: Driving a Red Toyota
print(car2.drive())  # Output: Driving a Blue Honda
```

---

## 2️⃣ Methods

* **Instance Methods** – Work on object data; first parameter is `self`.
* **Class Methods** – Work on class data; first parameter is `cls`; use `@classmethod`.
* **Static Methods** – Don't use object or class data; utility functions; use `@staticmethod`.
* **Constructors (`__init__`)** – Initialize object data when it's created.
* **Destructors (`__del__`)** – Cleanup before object is deleted.

**Example:**
```python
class Dog:
    species = "Canine"  # Class variable
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):  # Instance method
        return f"{self.name} says Woof!"
    
    @classmethod
    def get_species(cls):  # Class method
        return f"This is a {cls.species}"
    
    @staticmethod
    def is_adult(age):  # Static method
        return age >= 2

# Creating object
dog = Dog("Buddy", 3)
print(dog.bark())  # Output: Buddy says Woof!
print(dog.get_species())  # Output: This is a Canine
print(Dog.is_adult(3))  # Output: True
```

---

## 3️⃣ Variables

* **Instance Variables** – Belong to objects; accessed via `self`.
* **Class Variables** – Shared across all objects of the class.
* **Local Variables** – Exist inside a method; temporary.
* **Global Variables** – Defined outside class/method; accessible globally.

---

## 4️⃣ Encapsulation

* **Private Variables/Methods** – Prefix with `_` or `__` to hide from outside.
* **Public Variables/Methods** – Accessible from anywhere.
* **Getters and Setters** – Methods to access or update private variables.

---

## 5️⃣ Inheritance

* **Single Inheritance** – One class inherits from another.
* **Multiple Inheritance** – A class inherits from multiple classes.
* **Multilevel Inheritance** – Chain of inheritance.
* **Hierarchical Inheritance** – One parent, multiple children.
* **Method Overriding** – Child class replaces parent method.

---

## 6️⃣ Polymorphism

* **Compile-time / Method Overloading** – Same method name, different parameters (Python doesn't support traditional overloading).
* **Run-time / Method Overriding** – Child class changes parent method.
* **Operator Overloading** – Same operator behaves differently for objects.

---

## 7️⃣ Abstraction

* **Abstract Classes** – Cannot instantiate; only subclass.
* **Abstract Methods** – Must be implemented in child class.
* **In Python**, implemented using the `abc` module.

---

## 8️⃣ Other Features

* `self` – Refers to object instance.
* `cls` – Refers to class itself.
* `super()` – Access parent class methods and variables.
* **Composition / Aggregation** – Classes can contain objects of other classes.