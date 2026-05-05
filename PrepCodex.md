# Table of Contents

- [Python OOP Concepts](#python-oop-concepts)
- [Steps of Data Preprocessing for ML Models](#steps-of-data-preprocessing-for-ml-models)
  - [Missing Value Handling](#missing-value-handling)
- [Machine Learning Q&A](#machine-learning-qa)

# Python OOP Concepts

## 1️⃣ Classes and Objects

* **Class** – Blueprint for creating objects.
* **Object (Instance)** – A real entity created from a class.

---

## 2️⃣ Methods

* **Instance Methods** – Work on object data; first parameter is `self`.
* **Class Methods** – Work on class data; first parameter is `cls`; use `@classmethod`.
* **Static Methods** – Don't use object or class data; utility functions; use `@staticmethod`.
* **Constructors (`__init__`)** – Initialize object data when it's created.
* **Destructors (`__del__`)** – Cleanup before object is deleted.

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


# Steps of Data Preprocessing for ML Models

## 1. Data Collection / Ingestion
- **Sources**: API, Database, CSV files

## 2. Data Cleaning
- **Missing Values**: Handling (drop, impute)
- **Duplicates**: Identifying and removing
- **Formatting**: Fixing formats (Dates, casing)
- **Outliers**: Handling outlier values

## 3. Data Integration
- **Joining**: e.g., merging customer data with transaction data

## 4. Data Transformation
- **Normalization/Standardization**: Scaling data
- **Type Conversion**: e.g., converting salary from string to numeric
- **Formatting**: Converting data into usable formats

## 5. Feature Engineering
- **Creation**: Creating new features from existing ones
- **Example**: Extracting the hour of the day from a timestamp

## 6. Data Validation
- **Schema Validation**: Ensuring data adheres to defined structures
- **Null Checks**: Verifying mandatory fields

---

## Missing Value Handling

### 1. Row Drop
- Recommended if a small percentage of values are missing.

### 2. Column Drop
- Recommended if most of the values in a column are missing.

### 3. Mean Imputation
- Replacing missing values with the average (mean) of the column.

### 4. Median Imputation
- Replacing missing values with the median (the middle value).
- *Example*: For dataset `[3, 10, 15, 20]`, the median is `12.5`.

### 5. Mode Imputation
- Replacing missing values with the mode (the most frequent value).

---

# Machine Learning Q&A

## Overfitting
- **Definition**: High training accuracy caused by noise and random patterns in training data, resulting in low test accuracy.

## Underfitting
- **Definition**: The model is too simple to capture the underlying patterns. It performs poorly on both training and testing data.

## Bias and Variance
- **Bias**: Error due to overly simple assumptions (causes **underfitting**).
- **Variance**: Error due to too much complexity (causes **overfitting**).

## Supervised Learning
- **Definition**: Uses labeled data to train the model.
- **Examples**: Classification, Regression.

## Unsupervised Learning
- **Definition**: Uses unlabeled data to find hidden patterns.
- **Examples**: Clustering, Dimensionality Reduction.

## Difference Between Classification & Regression
- **Classification**: Predicts discrete categories (e.g., Spam or Not Spam).
- **Regression**: Predicts continuous numbers (e.g., House prices).

## Cross Validation
- **Definition**: Splitting data into multiple parts and training/testing multiple times to ensure model stability.
- **Example**: K-Fold Cross Validation.

## Regularization
- **Definition**: Adding a penalty term to the model complexity to reduce overfitting. It slightly “punishes” large weights (coefficients), so the model avoids relying too heavily on any one feature.
- Imagine you’re packing a bag:
    - L1 (Lasso): You throw out some items completely → lighter bag
    - L2 (Ridge): You keep everything but reduce weight of each item → more balanced bag

## Precision & Recall
- **Precision**: Out of all predicted positives, how many are actually correct.
- **Recall**: Out of all actual positives, how many were correctly predicted.

## Confusion Matrix
- **Definition**: A table used to evaluate the performance of classification models.

| | Predicted Positive | Predicted Negative |
| :--- | :---: | :---: |
| **Actual Positive** | **TP** (True Positive) | **FN** (False Negative) |
| **Actual Negative** | **FP** (False Positive) | **TN** (True Negative) |

## F1 Score
- **Definition**: The harmonic mean of precision and recall, providing a balance between the two metrics.

## scikit-learn vs XGBoost
- scikit-learn is a general ML library. XGBoost is specialized for fast, high-performance gradient boosting.

## Gradient boosting (high level)
- Build models sequentially. Each new model focuses on correcting errors from the previous ones, combining them into a strong final model.

## Hyperparameters
- Hyperparameters are settings you choose before training the model (not learned automatically).
Examples:

    - Learning rate (how fast the model learns)
    - Number of trees in a model
    - Regularization strength (L1/L2)

### Common tuning methods
#### Grid Search

    Try all combinations of values. Example:
    - Learning rate: [0.01, 0.1]
    - Regularization: [0.1, 1]

    Try:

    (0.01, 0.1)\
    (0.01, 1)\
    (0.1, 0.1)\
    (0.1, 1)

    👉 Best but can be slow

#### Random Search

    Try random combinations instead of all.

    👉 Faster, often works just as well

#### Smarter methods (advanced)
    Bayesian optimization (chooses better values based on past results)

    Imagine baking a cake:

    Hyperparameters: Oven temperature, Baking time

    You try:

    180°C for 30 min
    200°C for 25 min
    170°C for 40 min

    👉 Then taste each cake and pick the best one.



# MLOps Q&A

## Versioning Dataset, Code, and Model
*   **Git**: Used for versioning code.
*   **DVC (Data Version Control)**: Used for versioning datasets and large files.
*   **MLflow**: Used for tracking experiments and versioning models.

---

## MLOps Lifecycle
The standard lifecycle follows these key stages:
1.  **Data Collection**
2.  **Preprocessing**
3.  **Training**
4.  **Evaluation**
5.  **Deployment**
6.  **Monitoring**

---

## Deploying Model into Production
*   **Containerization**: Use **Docker** to package the model and its dependencies.
*   **API Exposure**: Use frameworks like FastAPI or Flask to expose the model via an API.
*   **Orchestration**: Deploy and manage containers using **Kubernetes**.

---

## Monitoring Model in Production
To ensure the model remains reliable, track the following metrics:
*   **Accuracy**: Is the model still making correct predictions?
*   **Latency**: How long does it take for the model to respond?
*   **Errors**: Monitoring for system crashes or failed requests.
*   **Drift**: Monitoring changes in data or model performance over time.
*   **Tools**: Use Dashboards, Logging, and Alerts.

---

## Monitoring Data Drift
Data drift occurs when the input data changes over time, leading to model decay.
*   **Continuous Monitoring**: Watch for statistical shifts in input features.
*   **Regular Retraining**: Schedule model training sessions on new data.
*   **Trigger Alerts**: Automatically notify the team when performance drops below a threshold.

---
    How do you translate a business problem into a data science problem? 

    Tell me about a time your model impacted business decisions. 

    What is data drift and how do you detect it? 

    Experience with APIs or batch vs real-time systems? 

    How do you design an A/B test? 
    
    How do you determine statistical significance? 
    
    How would you test a pricing strategy change? 

    How do you handle ambiguity? 

    Describe a time you had no clear data or direction. 

    How would you allocate inventory across warehouses? 

    How would you predict which books to purchase? 

    How would you recommend products to wholesale customers? 

    How would you optimize pricing across multiple sales channels?

---
# SQL

## Slow Query to Fast Query
- Add indexes, reduce unnecessary columns, filter early, avoid subqueries if possible, use proper joins, and check execution plans.