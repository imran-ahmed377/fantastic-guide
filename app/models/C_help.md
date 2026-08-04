# Table of Contents
- [Greetings](#greetings)
- [Introduction](#introduction)
- [Exp 1: Data Scientist @ Exeevo (Sept 2025 – Apr 2026)](#exp-1-data-scientist--exeevo-sept-2025--apr-2026)
- [Exp 2: Data Analyst Intern @ VistaPrint (June 2024 – Sept 2024)](#exp-2-data-analyst-intern--vistaprint-june-2024--sept-2024)
- [Project 1: Customer Churn Prediction Model](#project-1-customer-churn-prediction-model)
---
- [What is Canada Helps?](#what-is-canada-helps)
- [Why you applied to Canada Helps?](#why-you-applied-to-canada-helps)
- [Work with Ambiguous Data/Problems](#work-with-ambiguous-dataproblems)
- [Messy Datasets](#messy-datasets)
- [Example of A/B Testing](#example-of-ab-testing)
- [Non-technical stakeholders?](#non-technical-stakeholders)
- [Questions](#questions)
---
- [Technical QnA](#technical-qna)
- [Machine Learning](#machine-learning)
- [Statistics](#statistics)
- [Data Visualization](#data-visualization)
- [Monitoring Data Drift](#monitoring-data-drift)
- [Handling Missing Data](#handling-missing-data)
- [Libraries Used](#libraries-used)

  - [1. Overfitting](#1-overfitting)
  - [2. Underfitting](#2-underfitting)
  - [3. What evaluation metrics would you use?](#3-what-evaluation-metrics-would-you-use)
  - [4. What is the difference between Random Forest and Logistic Regression?](#4-what-is-the-difference-between-random-forest-and-logistic-regression)
    - [Random Forest](#random-forest)
    - [Logistic Regression](#logistic-regression)
    - [XGBoost](#xgboost)
    - [K-Means](#k-means)
    - [Linear Regression](#linear-regression)


# Greetings

Thank you! I'm excited to be here.

# Introduction

I recently completed my Master's in Applied Computing from the University of Windsor, with a specialization in Artificial Intelligence. I have worked as a Data Scientist and Data Analyst Intern, where I used Python, SQL, and machine learning models to predict customer churn. I have also built RAG based AI agent for real-time data analysis. I presented my findings to both technical and non-technical stakeholders. And I am very excited about this opportunity to apply my skills and continue to learn and grow in this role and contribute to CanadaHelps' mission of sparking generosity and powering positive change.


# Exp 1: Data Scientist @ Exeevo (Sept 2025 – Apr 2026)
At Exeevo, I worked as a Data Scientist. My main role was to analyze customer and product data to help the team to make better decisions.

For example, I built customer segmentation and churn prediction models, which improved targeting accuracy by 20%, and helped the marketing team reach the right customers. I also analyzed user behavior, and worked with A/B testing to measure the impact of new features, and created Power BI dashboards so stakeholders could easily understand the data.

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
At VistaPrint, I worked as a Data Analyst Intern. I analyzed large datasets with SQL and Python to find trends and identify areas for improvement. For example, I found patterns in marketing and operations data that helped the teams to understand performance.

I also built dashboards and visualizations so the teams could easily track important metrics instead of manually reviewing data. Also, I maintained data quality and documented my work, for others to use. I also regularly shared my findings with both technical and non-technical teams.

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


This project focused on predicting customer churn using behavioral data. The goal was to identify customer who were likely to stop using the platform so the organization could target them with retention campaigns before losing them.

I first cleaned and prepared the data using Python and Pandas by handling missing values, and creating new features like usage frequency and recency, and prepared the data for modeling. Then I built and compared several classification models in Scikit-learn, including Logistic Regression, Decision Tree, and Random Forest. I focused on improving recall, which increased by 25% after feature engineering and model tuning.

Finally, I created a Power BI dashboard that highlighted high-risk customer segments and key trends. This allowed the fundraising team to change outreach efforts and make more informed decisions. I'm especially proud of this project because I learned some new techniques and the team really appreciated the dashboard I built.

## Feature List
    - account_id
    - account_type
    - region
    - product_tier
    - support_level
    - acquisition_channel
    - tenure_months
    - active_users
    - licensed_users
    - logins_30d
    - sessions_30d
    - support_tickets_90d
    - avg_response_time_hours
    - training_completion_pct
    - feature_adoption_pct
    - campaign_engagement_score
    - nps_score
    - monthly_spend
    - contract_value
    - payment_delays_days
    - account_health_score
    - renewal_window_days
    - executive_sponsor
    - churned_last_quarter
    - last_activity_date
    - last_support_date
    - onboarding_date
    - churn_probability
    - churned
    - health_score_bucket
    - activity_per_user
    - support_burden_per_active_user


## What I Learned
- **Extreme Class Imbalance**: I learned how to handle extreme class imbalance in the dataset by using techniques like SMOTE and adjusting class weights in the models. 

- **uvicorn**: I learned how to use uvicorn to run a streamlit app locally and deploy it to a server for others to access.

- **Streamlit**: I learned how to use Streamlit to create interactive dashboards for data visualization and model results.

- **Feature Engineering**: I learned how to create new features from existing data, which improved model performance and provided more insights into customer behavior.

- **ROC AUC**: I learned how to use ROC AUC as a performance metric for classification models, which helped me evaluate the models more effectively.

- **Dashboard**: Highlights high-risk customer accounts, compares model performance, and visualizes churn probability, trends, and segment risk. It shows a 71.2% accuracy, 0.745 ROC-AUC, 53.8% recall, and 5.4% overall churn, helping stakeholders prioritize retention actions effectively for better customer retention outcomes.

---

**Breakdown**
| Section | Answer |
|---------|--------|
| Project Goal | The goal of this project was to identify customer who were likely to stop using the platform so that the organization could target them with retention campaigns before they left. |
| Business Problem | It is more expensive to acquire a new customer than to retain an existing one. The organization wanted a data-driven way to identify at-risk customers and improve retention. |
| My Role | I collected and analyzed customer behavior data, built the prediction model, evaluated its performance, and created dashboards to present the results. |
| Dataset | Historical customer data including usage frequency,  amount, recency of logins, and customer engagement history. |
| Tools Used | Python, Pandas, Scikit-learn, NumPy, Power BI, Jupyter Notebook |
| Data Preparation | Cleaned missing values, removed duplicates, encoded categorical variables, scaled numerical features, and created new features such as average logins and days since last logins. |
| Feature Engineering | Created features like usage frequency, recency, and average login time because these better represented customer behavior and improved model performance. |
| Model Used | Built and compared classification models using Logistic Regression, Decision Tree, and Random Forest, then selected the model with the best performance. |
| Evaluation Metrics | Evaluated the models using Recall, Precision, F1-score, and Accuracy. Since missing a customer who might churn is costly, Recall was the most important metric. |
| Key Result | Improved the model's Recall by 25%, allowing the organization to identify significantly more at-risk customers than the baseline model. |
| Visualization | Built an interactive Power BI dashboard showing high-risk customer segments, churn probability, trends, and key KPIs so stakeholders could easily identify which customers to target. |
| Business Impact | The dashboard helped the team prioritize outreach efforts toward high-risk customers instead of contacting everyone. This made retention campaigns more focused, improved decision-making, and could reduce customer loss while using marketing resources more efficiently. |
| Challenges | The dataset contained missing values and class imbalance because most customers did not churn. I handled this through data cleaning, feature engineering, and model tuning to improve prediction quality. |
| Why I'm Proud of This Project | I'm proud of this project because it combined data cleaning, machine learning, and visualization into one complete solution. Instead of only building a model, I translated the results into a Power BI dashboard that non-technical stakeholders could easily understand and use to make better business decisions. |

---

# Table of Contents
- [Introduction](#introduction)
- [Exp 1: Data Scientist @ Exeevo (Sept 2025 – Apr 2026)](#exp-1-data-scientist--exeevo-sept-2025--apr-2026)
- [Exp 2: Data Analyst Intern @ VistaPrint (June 2024 – Sept 2024)](#exp-2-data-analyst-intern--vistaprint-june-2024--sept-2024)
- [Project 1: Customer Churn Prediction Model](#project-1-customer-churn-prediction-model)
---
- [What is Canada Helps?](#what-is-canada-helps)
- [Why you applied to Canada Helps?](#why-you-applied-to-canada-helps)
- [Work with Ambiguous Data/Problems](#work-with-ambiguous-dataproblems)
- [Messy Datasets](#messy-datasets)
- [Example of A/B Testing](#example-of-ab-testing)
- [Non-technical stakeholders?](#non-technical-stakeholders)
- [Questions](#questions)
---
- [Technical QnA](#technical-qna)
  - [1. Overfitting](#1-overfitting)
  - [2. Underfitting](#2-underfitting)
  - [3. What evaluation metrics would you use?](#3-what-evaluation-metrics-would-you-use)
  - [4. What is the difference between Random Forest and Logistic Regression?](#4-what-is-the-difference-between-random-forest-and-logistic-regression)
    - [Random Forest](#random-forest)
    - [Logistic Regression](#logistic-regression)
    - [XGBoost](#xgboost)
    - [K-Means](#k-means)
    - [Linear Regression](#linear-regression)

---

# What is Canada Helps?
Canada Helps is an online platform that helps people to donnate to registered Canadian charities and it also provides tools for charities to manage their donations and fundraising campaigns. 


# Why you applied to Canada Helps?
I've actually used CanadaHelps to make donations, so I already appreciate the value it provides. What stands out to me most is its mission to spark generosity and power positive change. I like the idea of using data not just to improve a product, but to help more people support charities, and ultimately contribute to a world where everyone can live better lives.



# Work with Ambiguous Data/Problems

I deal with these problems by understanding the business goal, asking the right questions, and breaking the problem into smaller steps. I validate the data, and adjust my approach based on feedback.

**Example:**

For Example, at VistaPrint, when working with marketing data, the business question was not always clearly defined. So, I first discussed with stakeholders what they wanted to understand, such as improving campaign performance. Then, I explored the data using SQL and Python, and checked for missing or incorrect information, and identified useful patterns. Then I shared my findings through dashboards and simple explanations.

# Messy Datasets
Almost every dataset I've worked with at Exeevo required cleaning.

I first explored the data to understand the issues before making changes. Depending on the situation, I imputed missing values, standardized formats, removed duplicates, and investigated outliers rather than automatically deleting them.

I also documented every cleaning step so the analysis remained reproducible.

# Prioritize tasks
I prioritize tasks by understanding the business goals, deadlines, and dependencies. I break down larger tasks into smaller steps, and I use tools like Jira or Trello to track progress. I also communicate with stakeholders to ensure alignment and adjust priorities as needed.


# Non-technical stakeholders?
I deal with non-technical people by explaining data in a simple way and focusing on the business impact rather than technical details. I avoid using complex terms and use visuals like dashboards or charts to make the insights easier to understand.

**Example:**

For example, at VistaPrint, whenever I shared analysis with marketing and operations teams, I did not focus on SQL queries or Python code. I explained what the data showed, such as which campaigns were performing better or there were opportunities to improve. I used dashboards and simple explanations so the teams could quickly understand the insights.


# Example of A/B Testing

**Business Problem:** At Exeevo the product team wants to know if a new onboarding screen increases user engagement.

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








# Questions
- What would success look like in the first 90 days?
  >>> That's great to hear. Thank you for sharing that.

- Are developers encouraged to experiment with new AI tools and workflows?
  >>> That sounds like an environment I'd really enjoy working in. Thanks for sharing.

- What are the next steps of the hiring process?

- What kinds of applications would I be building?
  >>> That's helpful. Could you also tell me a bit about...

---

# Table of Contents
- [Introduction](#introduction)
- [Exp 1: Data Scientist @ Exeevo (Sept 2025 – Apr 2026)](#exp-1-data-scientist--exeevo-sept-2025--apr-2026)
- [Exp 2: Data Analyst Intern @ VistaPrint (June 2024 – Sept 2024)](#exp-2-data-analyst-intern--vistaprint-june-2024--sept-2024)
- [Project 1: Customer Churn Prediction Model](#project-1-customer-churn-prediction-model)
---
- [What is Canada Helps?](#what-is-canada-helps)
- [Why you applied to Canada Helps?](#why-you-applied-to-canada-helps)
- [Work with Ambiguous Data/Problems](#work-with-ambiguous-dataproblems)
- [Messy Datasets](#messy-datasets)
- [Example of A/B Testing](#example-of-ab-testing)
- [Non-technical stakeholders?](#non-technical-stakeholders)
- [Questions](#questions)
---
- [Technical QnA](#technical-qna)
  - [1. Overfitting](#1-overfitting)
  - [2. Underfitting](#2-underfitting)
  - [3. What evaluation metrics would you use?](#3-what-evaluation-metrics-would-you-use)
  - [4. What is the difference between Random Forest and Logistic Regression?](#4-what-is-the-difference-between-random-forest-and-logistic-regression)
    - [Random Forest](#random-forest)
    - [Logistic Regression](#logistic-regression)
    - [XGBoost](#xgboost)
    - [K-Means](#k-means)
    - [Linear Regression](#linear-regression)

---

# Technical QnA

## Data Processing and Cleaning
### Handling Missing Data
*   **Imputation**: Fill in missing values with mean, median, or mode.
*   **Model-Based Imputation**: Use regression or KNN to predict missing values.
*   **Deletion**: Remove rows or columns with missing values if they are not critical to the analysis.
*   **Flagging**: Create a new feature indicating whether the data was missing.
*   **Domain Knowledge**: Use business understanding to make informed decisions about missing data.

## Statistics

- **Mean vs Median**: The mean is the average of all values, while the median is the middle value when the data is sorted.
- **Confidence intervals**: A range of values that is likely to contain the true population parameter with a certain level of confidence.
- **Hypothesis testing**: A statistical method used to make inferences about a population based on sample data.
- **A/B testing**: A method of comparing two versions of a variable to determine which one performs better, often used in marketing and product development.

---

## Machine Learning

- **Overfitting**: High training accuracy caused by noise and random patterns in training data, resulting in low test accuracy.

- **Underfitting**: The model is too simple to capture the underlying patterns. It performs poorly on both training and testing data.

- **Difference between classification and regression**: Classification is used to predict categorical outcomes, while regression is used to predict continuous outcomes.

- **What is overfitting?**: Overfitting occurs when a model learns the training data too well, capturing noise and details that do not generalize to new data, leading to poor performance on unseen data.

- **Cross-validation**: Cross-validation is a technique used to assess the performance of a model by partitioning the data into subsets, training the model on some subsets, and validating it on others. This helps ensure that the model generalizes well to new data.

- **Random Forest vs XGBoost**: Random Forest is an ensemble learning method that combines multiple decision trees, while XGBoost is a gradient boosting algorithm that builds trees sequentially to minimize prediction errors.

- **Feature engineering**: Feature engineering is the process of creating new features or modifying existing ones to improve model performance. This can involve transforming variables, creating interaction terms, or aggregating data.

- **Clustering**: Clustering is an unsupervised learning technique used to group similar data points together based on their features. Common algorithms include K-Means, DBSCAN, and hierarchical clustering.

- **Recommendation systems**: Recommendation systems are algorithms designed to suggest items to users based on their preferences and behavior. They can be content-based, collaborative filtering, or hybrid approaches.

## Evaluation Metrics
    
Regression:

- MAE 
- RMSE

Classification:
- Precision: Out of all predicted positives, how many are actually correct.
- Recall: Out of all actual positives, how many were correctly predicted.
- F1 Score:  The harmonic mean of precision and recall, providing a balance between the two metrics.
- ROC-AUC: Measures the model's ability to distinguish between classes.


## Monitoring Data Drift
Data drift occurs when the input data changes over time, leading to model decay.
*   **Continuous Monitoring**: Watch for statistical shifts in input features.
*   **Regular Retraining**: Schedule model training sessions on new data.
*   **Trigger Alerts**: Automatically notify the team when performance drops below a threshold.

    ### Data Drift Detection Techniques
    1. Compare averages (mean): Check if the average value of a feature has changed.
    2. Compare distributions (histograms): Look at how values are spread, not just the average.
    3. Statistical tests: Example: Kolmogorov-Smirnov (KS) Test Compare two dataset cumulative distribution (CDF) curves at every point, check the difference between them.



## Libraries Used
- **Python**: For data manipulation, analysis, and modeling.
- **Pandas**: For data cleaning and preprocessing.
- **NumPy**: For numerical operations and array handling.
- **Scikit-learn**: For machine learning algorithms and model evaluation.
- **Matplotlib & Seaborn**: For data visualization and plotting.
- **Power BI**: For creating interactive dashboards and visualizations.
- **Streamlit**: For building interactive web applications to showcase model results and dashboards.
- **Uvicorn**: For running the Streamlit app locally and deploying it to a server.
- **SMOTE**: For handling class imbalance in the dataset by generating synthetic samples of the minority class.
- **ROC AUC**: For evaluating the performance of classification models, especially in imbalanced datasets.

---



## 4. What is the difference between Random Forest and Logistic Regression?

### **Random Forest:**
- How it works: 

    Builds many decision trees using random subsets of the data and features, then combines their predictions (majority vote for classification, average for regression).

- When to use it:
    - Classification or regression
        - example: predicting customer churn (classification) or predicting sales revenue (regression)    
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
        - example: predicting whether a customer will churn or not
    - Baseline model
        - example: when you want a simple model to compare against more complex models
    - When interpretability is important
        - example: when you want to understand the relationship between features and the target variable

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
        - example: predicting sales revenue or donation amounts
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

---

# Table of Contents
- [Introduction](#introduction)
- [Exp 1: Data Scientist @ Exeevo (Sept 2025 – Apr 2026)](#exp-1-data-scientist--exeevo-sept-2025--apr-2026)
- [Exp 2: Data Analyst Intern @ VistaPrint (June 2024 – Sept 2024)](#exp-2-data-analyst-intern--vistaprint-june-2024--sept-2024)
- [Project 1: Customer Churn Prediction Model](#project-1-customer-churn-prediction-model)
---
- [What is Canada Helps?](#what-is-canada-helps)
- [Why you applied to Canada Helps?](#why-you-applied-to-canada-helps)
- [Work with Ambiguous Data/Problems](#work-with-ambiguous-dataproblems)
- [Messy Datasets](#messy-datasets)
- [Example of A/B Testing](#example-of-ab-testing)
- [Non-technical stakeholders?](#non-technical-stakeholders)
- [Questions](#questions)
---
- [Technical QnA](#technical-qna)
  - [1. Overfitting](#1-overfitting)
  - [2. Underfitting](#2-underfitting)
  - [3. What evaluation metrics would you use?](#3-what-evaluation-metrics-would-you-use)
  - [4. What is the difference between Random Forest and Logistic Regression?](#4-what-is-the-difference-between-random-forest-and-logistic-regression)
    - [Random Forest](#random-forest)
    - [Logistic Regression](#logistic-regression)
    - [XGBoost](#xgboost)
    - [K-Means](#k-means)
    - [Linear Regression](#linear-regression)