# Introduction

# Exp 1
At Exeevo, I worked as a Data Scientist. My main role was to analyze customer and product data to help the business make better decisions.

For example, I built customer segmentation and churn prediction models, which improved targeting accuracy by 20%, helping the marketing team reach the right customers. I also analyzed user behavior, designed A/B tests to measure the impact of new features, and created Power BI dashboards so stakeholders could easily understand the data. I worked closely with the product and marketing teams to support data-driven business decisions.

Day in Life:
| Time | Activity | Business Purpose |
|------|----------|------------------|
| 9:00 – 9:15 AM | Check emails, Slack, Jira tickets, review priorities | Understand new requests from Product and Marketing teams |
| 9:15 – 9:30 AM | Daily stand-up meeting | Share progress, discuss blockers, align with team |
| 9:30 – 11:00 AM | Query data using SQL and clean data using Python (Pandas, NumPy) | Prepare high-quality data for analysis |
| 11:00 – 12:00 PM | Perform exploratory data analysis (EDA) using Python, Matplotlib, Seaborn | Identify customer behavior and trends |
| 12:00 – 1:00 PM | Lunch | — |
| 1:00 – 2:30 PM | Build machine learning models (Scikit-learn) for segmentation or churn prediction | Improve customer targeting and identify customers likely to leave |
| 2:30 – 3:30 PM | Design or analyze A/B tests | Measure whether a new feature improves business metrics |
| 3:30 – 4:30 PM | Build dashboards using Power BI | Help business teams monitor KPIs and make decisions |
| 4:30 – 5:00 PM | Present findings to Product and Marketing teams | Recommend data-driven actions and next steps |

# Exp 2

# Project 1:

# Project 2:

---

# What is Canada Helps?
Canada Helps is an online platform that helps individuals to donnate to registered Canadian charities and it also provides tools for charities to manage their donations and fundraising campaigns. 


# Why you applied to Canada Helps?
I've actually used CanadaHelps to make donations, so I already appreciate the value it provides. What stands out to me most is its mission to spark generosity and power positive change. I like the idea of using data not just to improve a product, but to help more people support charities, and ultimately contribute to a world where everyone can live better lives.



# Work with Ambiguous Data/Problems


# Messy Datasets
Almost every dataset I've worked with at Exeevo required cleaning.

One project involved missing values, inconsistent formats, duplicate records, and outliers.

I first explored the data to understand the issues before making changes. Depending on the situation, I imputed missing values, standardized formats, removed duplicates, and investigated outliers rather than automatically deleting them.

I also documented every cleaning step so the analysis remained reproducible.

# Example of A/B Testing
Based on real exp

# Non-technical stakeholders?
Based on experience

# 


# Questions

---

# Technical QnA
## 1. Overfitting:
Overfitting occurs when a model learns the training data too well, capturing noise and details that do not generalize to new data. This results in poor performance on unseen data.

## 2. Underfitting:
Underfitting occurs when a model is too simple to capture the underlying patterns in the data, leading to poor performance on both training and unseen data.

## 3. What evaluation metrics would you use?
    
Regression:

- MAE 
- RMSE

Classification:
- Precision: True positive out of all predicted positive cases.
- Recall: True positive out of all actual positive cases.
- F1 Score: The harmonic mean of precision and recall.
- ROC-AUC: Measures the model's ability to distinguish between classes.

## 4. What is the difference between Random Forest and Logistic Regression?

### **Random Forest:**
- How it works: 

    Builds many decision trees using random subsets of the data and features, then combines their predictions (majority vote for classification, average for regression).

- When to use it:
    - Classification or regression
    - Nonlinear relationships
    - Large datasets with many features

- Evaluation metrics:
    - Classification: Accuracy, Precision, Recall, F1-score, ROC-AUC
    - Regression: MAE, RMSE, R²

- Pros:
    - High accuracy
    - Handles nonlinear data
    - Less prone to overfitting than a single decision tree

- Cons:
    - Less interpretable
    - Slower to train
    - Larger memory usage


### **Logistic Regression:**
- How it works: 

    Uses a logistic (sigmoid) function to estimate the probability that an observation belongs to a class.

- When to use it:
    - Binary classification
    - Baseline model
    - When interpretability is important

- Evaluation metrics:
    - Accuracy
    - Precision
    - Recall
    - F1-score
    - ROC-AUC

- Pros:
    - Simple and fast
    - Easy to interpret
    - Outputs class probabilities

- Cons:
    - Assumes a linear relationship
    - Cannot capture complex nonlinear patterns
    - Sensitive to outliers and multicollinearity

---

### **XGBoost:**
- How it works: 

    Builds decision trees sequentially, where each new tree corrects the errors made by previous trees (gradient boosting).

- When to use it:
    - Classification or regression
    - Structured/tabular data
    - High prediction accuracy is needed

- Evaluation metrics:
    - Classification: Accuracy, Precision, Recall, F1-score, ROC-AUC
    - Regression: MAE, RMSE, R²

- Pros:
    - Very high accuracy
    - Handles missing values well
    - Built-in regularization helps reduce overfitting

- Cons:
    - More complex to understand
    - Requires hyperparameter tuning
    - Slower to train than simpler models

---

### **K-Means:**
- How it works: 

    Groups similar data points into **K** clusters by minimizing the distance between each point and its assigned cluster center.

- When to use it:
    - Customer or donor segmentation
    - Pattern discovery
    - Unlabeled datasets

- Evaluation metrics:
    - Silhouette Score
    - Inertia (WCSS)
    - Davies-Bouldin Index

- Pros:
    - Simple and fast
    - Easy to implement
    - Scales well to large datasets

- Cons:
    - Must choose K beforehand
    - Sensitive to outliers
    - Assumes clusters are roughly spherical

### **Linear Regression:**
- How it works: 
    
    Fits the best straight line to model the relationship between input variables and a continuous target variable.

- When to use it:
    - Predict continuous values
    - Understand relationships between variables
    - Baseline regression model

- Evaluation metrics:
    - MAE
    - RMSE
    - R²

- Pros:
    - Simple and easy to interpret
    - Fast to train
    - Good baseline model

- Cons:
    - Assumes a linear relationship
    - Sensitive to outliers
    - Performs poorly on complex nonlinear data