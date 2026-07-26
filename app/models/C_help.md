# Introduction

# Exp 1: Data Scientist @ Exeevo (Sept 2025 – Apr 2026)
At Exeevo, I worked as a Data Scientist. My main role was to analyze customer and product data to help the business make better decisions.

For example, I built customer segmentation and churn prediction models, which improved targeting accuracy by 20%, helping the marketing team reach the right customers. I also analyzed user behavior, designed A/B tests to measure the impact of new features, and created Power BI dashboards so stakeholders could easily understand the data. I worked closely with the product and marketing teams to support data-driven business decisions.

**Day in Life @ Exeevo:**
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

# Exp 2: Data Analyst Intern @ VistaPrint (June 2024 – Sept 2024)
At VistaPrint, I worked as a Data Analyst Intern. I analyzed large datasets with SQL and Python to find trends and identify areas for improvement. For example, I found patterns in marketing and operations data that helped the teams to understand performance and make better decisions.

I also built dashboards and visualizations so the teams could easily track important metrics instead of manually reviewing data. Also, I maintained data quality and documented my work, for others to use. Also I regularly shared my findings with both technical and non-technical teams.

**Day in Life @ Vista Print:**

| Time | Activity | Tools Used |
|------|----------|------------|
| 9:00 – 9:15 AM | Check emails, review tasks, and attend the daily team stand-up | Outlook, Microsoft Teams |
| 9:15 – 11:00 AM | Query and explore marketing or operations data to answer business questions | SQL, Python |
| 11:00 – 12:00 PM | Clean and validate data to ensure accuracy before analysis | Python (Pandas), SQL |
| 12:00 – 1:00 PM | Lunch | — |
| 1:00 – 2:30 PM | Create or update dashboards for business teams | Power BI or Tableau, Excel |
| 2:30 – 3:15 PM | Analyze trends and summarize insights | Python, Excel |
| 3:15 – 4:00 PM | Meet with marketing or operations teams to explain findings and answer questions | Microsoft Teams, PowerPoint |
| 4:00 – 5:00 PM | Document work, update reports, and plan tasks for the next day | Confluence/SharePoint, Excel, Teams |


# Project 1: Customer Churn Prediction Model


This project focused on predicting customer churn using donor behavioral data. The goal was to identify donors who were likely to stop donating so the organization could target them with retention campaigns before losing them.

I first cleaned and prepared the data using Python and Pandas by handling missing values, creating new features like donation frequency and recency, and preparing the data for modeling. Then I built and compared several classification models in Scikit-learn, including Logistic Regression, Decision Tree, and Random Forest. Since missing a donor who might churn is more costly than incorrectly flagging one, I focused on improving recall, which increased by 25% after feature engineering and model tuning.

Finally, I created a Power BI dashboard that highlighted high-risk donor segments and key trends. This allowed the fundraising team to prioritize outreach efforts and make more informed decisions. I'm especially proud of this project because it combined data analysis, machine learning, and visualization to solve a real business problem and produce insights that stakeholders could easily use.

**Breakdown**
| Section | Answer |
|---------|--------|
| Project Goal | The goal of this project was to identify donors who were likely to stop donating (churn) so that the organization could target them with retention campaigns before they left. |
| Business Problem | It is more expensive to acquire a new donor than to retain an existing one. The organization wanted a data-driven way to identify at-risk donors and improve retention. |
| My Role | I collected and analyzed donor behavior data, built the prediction model, evaluated its performance, and created dashboards to present the results. |
| Dataset | Historical donor data including donation frequency, donation amount, recency of donations, and donor engagement history. |
| Tools Used | Python, Pandas, Scikit-learn, NumPy, Power BI, Jupyter Notebook |
| Data Preparation | Cleaned missing values, removed duplicates, encoded categorical variables, scaled numerical features, and created new features such as average donation amount and days since last donation. |
| Feature Engineering | Created features like donation frequency, recency, lifetime donation value, and average donation amount because these better represented donor behavior and improved model performance. |
| Model Used | Built and compared classification models using Logistic Regression, Decision Tree, and Random Forest, then selected the model with the best performance. |
| Evaluation Metrics | Evaluated the models using Recall, Precision, F1-score, and Accuracy. Since missing a donor who might churn is costly, Recall was the most important metric. |
| Key Result | Improved the model's Recall by 25%, allowing the organization to identify significantly more at-risk donors than the baseline model. |
| Visualization | Built an interactive Power BI dashboard showing high-risk donor segments, churn probability, donation trends, and key KPIs so stakeholders could easily identify which donors to target. |
| Business Impact | The dashboard helped the fundraising team prioritize outreach efforts toward high-risk donors instead of contacting everyone. This made retention campaigns more focused, improved decision-making, and could reduce donor loss while using marketing resources more efficiently. |
| Challenges | The dataset contained missing values and class imbalance because most donors did not churn. I handled this through data cleaning, feature engineering, and model tuning to improve prediction quality. |
| Why I'm Proud of This Project | I'm proud of this project because it combined data cleaning, machine learning, and visualization into one complete solution. Instead of only building a model, I translated the results into a Power BI dashboard that non-technical stakeholders could easily understand and use to make better business decisions. |


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


**Business Problem:** Product team wants to know if a new onboarding screen increases user engagement.

**Hypothesis:** The new onboarding screen will increase the 7-day user retention rate.

| Step | Activity | Tools Used | Example |
|------|----------|------------|---------|
| 1 | Understand the business problem | Jira, Confluence, Slack, Meetings | Product Manager asks if the new onboarding improves retention. |
| 2 | Define success metric | SQL, Excel | Primary KPI = 7-day retention. Secondary KPI = Session duration. |
| 3 | Form hypothesis | Documentation (Confluence/Word) | H0: No difference. H1: New onboarding increases retention. |
| 4 | Identify eligible users | SQL | Select only new users who signed up during the experiment period. |
| 5 | Randomly split users | SQL, Product Platform (or application logic) | Group A = Old onboarding (50%). Group B = New onboarding (50%). |
| 6 | Launch experiment | Product Team, Feature Flag Tool (e.g., LaunchDarkly/Optimizely if available) | Only Group B sees the new onboarding screen. |
| 7 | Collect experiment data | SQL, Data Warehouse | Store user IDs, retention, clicks, sessions, conversions. |
| 8 | Analyze results | Python (Pandas, SciPy, Statsmodels) | Perform a two-proportion z-test or t-test to compare retention rates. |
| 9 | Visualize results | Power BI, Matplotlib, Seaborn | Dashboard shows retention for both groups and confidence intervals. |
| 10 | Present recommendation | Power BI, PowerPoint | "Retention increased from 42% to 48% (p < 0.05). Recommend rolling out the new onboarding." |

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