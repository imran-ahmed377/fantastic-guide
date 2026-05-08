# Table of Contents

- [Python OOP Concepts](#python-oop-concepts)
- [Steps of Data Preprocessing for ML Models](#steps-of-data-preprocessing-for-ml-models)
  - [Missing Value Handling](#missing-value-handling)
- [Machine Learning Q&A](#machine-learning-qa)
- [MLOps Q&A](#mlops-qa)
- [SQL](#sql)
- [A/B Testing](#ab-testing)
- [Product & Business](#product--business)


# Python Basics


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

    ### Data Drift Detection Techniques
    1. Compare averages (mean): Check if the average value of a feature has changed.
    2. Compare distributions (histograms): Look at how values are spread, not just the average.
    3. Statistical tests: Example: Kolmogorov-Smirnov (KS) Test Compare two dataset cumulative distribution (CDF) curves at every point, check the difference between them.


---


# SQL

## Slow Query to Fast Query
- Add indexes, reduce unnecessary columns, filter early, avoid subqueries if possible, use proper joins, and check execution plans.
---

# A/B Testing
## ⚡ One-line intuition

**A/B testing = “Show two versions to similar users and check if the difference is real or just luck.”**

## 🎯 Scenario

You run an e-commerce app and want to test:

**Does a new checkout button increase purchases?**

---

## 1. Define the hypothesis

Keep it very clear and measurable.

- **Null hypothesis (H₀):** New button does not change conversion rate  
- **Alternative (H₁):** New button increases conversion rate  

**Example:**  
Current conversion = 10%  
You expect → 12%

---

## 2. Choose your metric

Pick one primary metric (don’t overcomplicate).

**Example:**
- Primary: % of users who complete purchase  
- Secondary (optional): revenue per user  

---

## 3. Decide group split (A vs B)

Most common: **50/50 split**

- Group A → old button  
- Group B → new button  

**Why 50/50?**
- Fastest way to get results  
- Balanced comparison  

Sometimes companies use 90/10 for safer rollout, but 50/50 is standard for testing.

---

## 4. Determine sample size (how many users you need)

You need enough users to detect a real difference.

**Key inputs:**
- Baseline = 10%  
- Expected improvement = +2% (to 12%)  
- Confidence level = 95%  
- Power = 80%  

Using a calculator or stats tool:

👉 You’ll need roughly **~4,000–5,000 users per group**

_(You don’t calculate this manually in practice—tools do it.)_

---

## 5. Determine experiment duration

Duration depends on traffic.

**Example:**
- You get 1,000 users/day  
- Need 5,000 per group → 10,000 total  

👉 Duration ≈ **10 days**

**Add buffer:**
- Run at least 1–2 full weeks to capture weekday/weekend behavior  

👉 Final: **2 weeks**

---

## 6. Run the experiment properly

**Rules:**
- Randomly assign users  
- Keep conditions the same (no other changes)  
- Don’t stop early just because results “look good”  

---

## 7. Analyze results

Compare conversion rates using a statistical test like a t-test or proportion test.

**Example result:**
- A = 10%  
- B = 12%  
- (Chance of result is random, low p-value is good) p-value < 0.05 → significant  

👉 New button wins  

---

## 8. Decide rollout strategy

Don’t always go straight to 100%.

**Typical rollout:**
- Step 1: 10% users  
- Step 2: 50% users  
- Step 3: 100% users  

**Why gradual?**
- Catch bugs or unexpected issues  
- Reduce risk  

---

## 🧠 Simple summary (memory version)

- Hypothesis: what you expect to change  
- Metric: what you measure  
- Split: usually 50/50  
- Sample size: enough users to detect change  
- Duration: based on traffic (usually 1–2 weeks min)  
- Run test: random + controlled  
- Analyze: is difference real?  
- Rollout: gradual release  

---

# Product & Business 

1. Translate a business problem into a data science problem? 

- Clarify the goal
- define success metrics, 
- identify target variable, 
- gather relevant data, 
- frame it as a predictive or analytical problem.

2. Tell me about a time your model impacted business decisions.
- Built an A/B test model improving conversion by 5%, 
- leading the team to adopt the new design and increase revenue.

3. How do you handle ambiguity when you had no clear data or direction?
- Clarify goals, 
- Make reasonable assumptions, 
- Explore available data, 
- Prioritize quick experiments, 
- Iterate while aligning with stakeholders for direction.

# Data Science Intro

Hi, I’m Imran Ahmed. I’m a data scientist with about [X years] of experience working with machine learning, statistical analysis, and data visualization to solve business problems.

Currently, I work at Aspire Ontario, where I build predictive models and dashboards that help teams make data-driven decisions. My work has involved tools like Python, SQL, TensorFlow, and cloud platforms such as AWS.

One project I’m particularly proud of was developing a customer churn prediction model that improved retention targeting and increased campaign efficiency by 20%. I enjoy translating complex data into actionable insights that non-technical stakeholders can use.

What interests me about this opportunity is the chance to work on larger-scale data problems and collaborate with cross-functional teams in a product-focused environment.