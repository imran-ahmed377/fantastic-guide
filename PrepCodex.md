# Table of Contents

- [Python OOP Concepts](#python-oop-concepts)
- [Steps of Data Preprocessing for ML Models](#steps-of-data-preprocessing-for-ml-models)
  - [Missing Value Handling](#missing-value-handling)
- [Machine Learning Q&A](#machine-learning-qa)
- [MLOps Q&A](#mlops-qa)
- [SQL](#sql)
- [A/B Testing](#ab-testing)
- [Product & Business](#product--business)
- [Data Science Intro](#data-science-intro)
- [Aspire Ontario](#aspire-ontario)
- [Meallens](#meallens)
- [Retail Pricing Optimization Model](#retail-pricing-optimization-model)
- [Inventory Demand Forecasting System](#inventory-demand-forecasting-system)
- [Questions](#questions)


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
# Table of Contents

- [Python OOP Concepts](#python-oop-concepts)
- [Steps of Data Preprocessing for ML Models](#steps-of-data-preprocessing-for-ml-models)
  - [Missing Value Handling](#missing-value-handling)
- [Machine Learning Q&A](#machine-learning-qa)
- [MLOps Q&A](#mlops-qa)
- [SQL](#sql)
- [A/B Testing](#ab-testing)
- [Product & Business](#product--business)
- [Data Science Intro](#data-science-intro)
- [Aspire Ontario](#aspire-ontario)
- [Meallens](#meallens)
- [Retail Pricing Optimization Model](#retail-pricing-optimization-model)
- [Inventory Demand Forecasting System](#inventory-demand-forecasting-system)
- [Questions](#questions)

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
---

# Data Science Intro

Hi, I’m Imran Ahmed. I’m a data scientist with experience using data and machine learning to help solve business problems.

I build models and dashboards that help teams make better decisions. I mainly work with tools like Python, SQL, TensorFlow, Microsoft Azure and AWS.

What I enjoy most about data science is finding useful insights from data and explaining them in a simple way that helps teams take action.

I’m interested in this role because I’d like to work on bigger data challenges and collaborate with different teams to build impactful solutions.

---

# Aspire Ontario
At Aspire Ontario, I worked on developing an AI assistant for a Pharma CRM platform to help users quickly retrieve business insights using natural language and voice interaction.

The main goal was to reduce the time users spent manually searching through CRM data and reports. I built a RAG-based system where CRM data was processed using Python, Pandas, and NumPy on Azure Machine Learning, and stored in Azure Blob Storage.

For the retrieval layer, I used Azure AI Search as the vector database with the text-embedding-3-small model for embeddings. I implemented hybrid search combining vector similarity and keyword search to improve answer relevance. The retrieved context was then passed to GPT-4o-mini to generate responses with lower latency and cost.

I also integrated voice capabilities using Azure Speech-to-Text and Text-to-Speech so users could interact with the assistant conversationally.

For monitoring and quality evaluation, I tracked metrics like Top-K accuracy, MRR, response precision, recall, and latency using Azure Monitor and Application Insights. I also added confidence thresholds and fallback handling for cases where relevant insights were not found.

The project had a strong business impact — it reduced insight retrieval time by about 40%, improved response relevance, and increased user adoption because of the natural language and voice-enabled experience.

---

# Meallens
I worked on building a smart food assistant that could detect food items from images and recommend recipes in real time. The goal was to create an interactive AI experience where users could simply show food ingredients and get cooking guidance instantly.

I was responsible for developing the end-to-end computer vision pipeline and integrating it with the backend and mobile application. I processed and cleaned over 200GB of food image data using Python, then trained and combined multiple AI models for better accuracy.

For object detection, I used YOLO because it supports fast real-time detection. Then I used SAM/SAM2 for image segmentation to get precise object boundaries, and CLIP for image-text matching and food classification. The pipeline worked like this: YOLO detected the food items, SAM refined the detected regions, CLIP identified the food category, and then the OpenAI API generated recipe suggestions based on the detected ingredients.

I also integrated speech-to-text so users could interact with the assistant using voice commands and receive step-by-step recipe instructions.

On the deployment side, I collaborated with the backend and mobile teams to deploy the system on DigitalOcean and optimize APIs for low-latency responses.

To evaluate performance, I used metrics like Precision, Recall, and mAP for detection accuracy, and I reduced false positives by tuning confidence thresholds and improving the dataset over time.

The final system was a scalable, real-time food detection and recipe assistant that delivered fast and accurate predictions with a smooth voice-enabled user experience, and it was successfully launched as a working prototype.

---

# Retail Pricing Optimization Model
The goal of this project was to help retail business set better product prices to improve revenue and stay competitive.

I noticed that pricing decisions were mostly manual and didn’t always reflect customer demand or market trends. So, I built a machine learning model to predict how price changes would affect sales and revenue.

For the tech stack, I used Python with pandas and NumPy for data cleaning and analysis, XGBoost for the prediction model, and SQL to pull historical sales data. I also used matplotlib and seaborn for visualization.

The model was trained using features like product price, discounts, seasonality, competitor pricing, and past sales trends. I also simulated demand elasticity to understand how sensitive customers were to price changes.

To measure performance, I mainly used RMSE and MAE to compare predicted sales against actual sales. I also tracked revenue prediction accuracy, which improved by about 25% compared to the previous baseline model.

One challenge was overfitting because some products had limited historical data. To fix that, I did feature selection, cross-validation, and hyperparameter tuning. I also cleaned missing and inconsistent pricing data before training the model, which improved stability and accuracy.
## Success Metrics
The model improved revenue prediction accuracy by around 25% compared to the previous baseline, and RMSE and MAE scores were consistently lower during testing.

# Inventory Demand Forecasting System
It was a research project to predict product demand more accurately so the company could manage inventory better and reduce overstock issues.

I built a forecasting system to estimate future demand.

For the tech stack, I used Python and SQL. I used pandas and NumPy for data processing, matplotlib for visualization, and scikit-learn for modeling. For forecasting, I mainly used Facebook Prophet and XGBoost.

The model used historical sales data, seasonal trends, promotions, and channel-wise sales information to predict future demand.

To measure performance, I used metrics like MAE and RMSE to compare predicted demand with actual sales. I also tracked business impact, and the system helped reduce overstock risk by around 20%.

One challenge was inconsistent sales patterns during holidays and promotions, which caused prediction errors. To improve accuracy, I added seasonal features, cleaned missing data, and retrained the model regularly using updated sales data.

## Success Metrics
The forecasting accuracy improved significantly based on lower MAE and RMSE scores. I also compared forecasted demand with actual sales over multiple cycles to confirm the predictions were reliable.




# Questions
- What is your expectation from the new hire in first 3 to 6 months?
- What are the next steps of the hiring process?


# Table of Contents

- [Python OOP Concepts](#python-oop-concepts)
- [Steps of Data Preprocessing for ML Models](#steps-of-data-preprocessing-for-ml-models)
  - [Missing Value Handling](#missing-value-handling)
- [Machine Learning Q&A](#machine-learning-qa)
- [MLOps Q&A](#mlops-qa)
- [SQL](#sql)
- [A/B Testing](#ab-testing)
- [Product & Business](#product--business)
- [Data Science Intro](#data-science-intro)
- [Aspire Ontario](#aspire-ontario)
- [Meallens](#meallens)
- [Retail Pricing Optimization Model](#retail-pricing-optimization-model)
- [Inventory Demand Forecasting System](#inventory-demand-forecasting-system)
- [Questions](#questions)