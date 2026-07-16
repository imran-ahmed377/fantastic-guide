# Table of Contents
- [Introduction](#introduction)
- [Aspire Ontario (AI Enablement Specialist) (Sept 2025 - Present)](#aspire-ontario-ai-enablement-specialist-sept-2025---present)
- [Exeevo (AI/ML Analyst Intern) (May 2024 – Dec 2024)](#exeevo-aiml-analyst-intern-may-2024--dec-2024)
- [Project 1: Credit Risk Assessment Model Optimization](#project-1-credit-risk-assessment-model-optimization)
- [Project 2: Collections Efficacy Enhancement](#project-2-collections-efficacy-enhancement)
---
- [Why do you want to leave your current job?](#why-do-you-want-to-leave-your-current-job)
- [Why apply for this job?](#why-apply-for-this-job)
- [What you will learn from this role?](#what-you-will-learn-from-this-role)
- [What is ROC-AUC?](#what-is-roc-auc)
- [How do you explain technical concepts to non-technical people](#how-do-you-explain-technical-concepts-to-non-technical-people)
- [Describe a time you solved a difficult problem](#describe-a-time-you-solved-a-difficult-problem)
- [How do you deal with ambiguity?](#how-do-you-deal-with-ambiguity)
- [Questions](#questions)
---
- [Steps of Data Preprocessing for ML Models](#steps-of-data-preprocessing-for-ml-models)
- [Missing Value Handling](#missing-value-handling)
- [Machine Learning Q&A](#machine-learning-qa)
- [MLOps Q&A](#mlops-qa)
- [Monitoring Model in Production](#monitoring-model-in-production)
- [Monitoring Data Drift](#monitoring-data-drift)

# Introduction
I recently completed my Master's in Applied Computing with a specialization in Artificial Intelligence from the University of Windsor. I've gained hands-on experience working on AI and machine learning projects.

In my current role, I work with data scientists and engineers to support the AI lifecycle by gathering business requirements, analyzing model performance, retraining models and helping them deploy into production. I also use data analytics to measure business impact and improve AI solutions.

During my internship at Exeevo, I built predictive models for customer risk scoring and collaborated with cross-functional teams.

I enjoy solving business problems using AI and working closely with both technical and business teams. And I'm excited about this opportunity at Bell, because it combines AI, analytics, and collaboration to create real business value.

# Aspire Ontario (AI Enablement Specialist) (Sept 2025 - Present)
My role is a mix of business analysis, data analysis, AI operations, and working with different teams. My main goal is to make sure the AI solutions stayed accurate, reliable, and continued to support the business goals.

I monitor the performance of our machine learning models using dashboards and KPIs. 

I reviewed metrics like prediction accuracy and looked for any signs that the models were underperforming because of the changes in the data.

If I see any performance gap, I analyze the data to understand the root cause and document my findings. 

I then collaborated with data scientists to discuss potential improvements, such as retraining the model or adjusting features.

I validate results and ensure the updated models meet technical and business needs before deployment.

I worked closely with the business teams to understand what they needed. Then I explained those requirements in a simple and clear way for the technical team so everyone was on the same page.

When new AI models or updates were ready, I helped test them to make sure they worked properly before and after they went live.

I also tracked how much value these AI projects were bringing to the business. I created reports and dashboards to measure things like prediction accuracy and how much time or effort the business was saving.

## Skills
- **SQL** to query data
- **Power BI** or **Tableau** for dashboards
- **Excel** for ad hoc analysis
- **Python** or **Jupyter Notebooks** for light analysis or model evaluation
- **Azure Machine Learning**, **Databricks**, or **cloud AI platforms**
- **Jira** or **Azure DevOps** for project tracking
- **Confluence** or **SharePoint** for documentation
- **Git** for version control (occasionally)


# Exeevo (AI/ML Analyst Intern) (May 2024 – Dec 2024)
During my internship, I mainly worked on improving machine learning models that helped predict customer risk for collections.

I used SQL and Python to analyze customer data, checked how the models were performing, and looked for any changes that could affect their accuracy over time.

I also worked closely with the business team to understand what they needed and explained those requirements to the data science team in a clear way. Once the models were ready, I helped test and validate them, compared their performance, and suggested retraining them if the results started getting worse.

I also worked with engineers, product teams, and business users to make sure the models were successfully put into use. I created training materials and documentation to help people understand how to use the AI tools.

One project I worked on helped improve the efficiency of early-stage collections by around 20%. It showed how better predictions can help the business make smarter decisions and improve results.
## Skills
- **SQL**
- **Python** (Pandas, scikit-learn, NumPy)
- **Jupyter Notebook**
- **Power BI** or **Tableau**
- **Excel**
- **Git**
- **Jira**
- **Confluence**
- **Azure Machine Learning** (depending on the organization)

# Project 1: Credit Risk Assessment Model Optimization

One project I worked on was improving a credit risk model that predicted whether a customer was likely to miss payments or default on a loan. The goal was to make the predictions more accurate while also making sure the model was fair.

We started by understanding the business problem. I worked with the business team to understand what they considered a default, what level of accuracy they expected, and how the model would be used when making credit decisions.

Next, we prepared the data. We used historical customer information like payment history, credit usage, income, employment, account balances, and any previous defaults. I helped clean the data by filling in or handling missing values, checking for unusual data, and making sure everything was ready for the model.

After that, we created useful features and split the data into training and testing sets. We chose XGBoost because it works really well with structured data and is good at finding patterns in customer information.

Then we trained the model and tried different settings, like the learning rate, tree depth, and the number of trees. We used cross-validation to find the combination that gave the best results.

Once the model was ready, I helped evaluate how well it performed. We looked at several metrics, but the main one was AUC-ROC because it shows how well the model can tell the difference between customers who are likely to default and those who are not. Our final model achieved an AUC-ROC of about 0.85, which was a strong result.

Another important part of the project was checking that the model was fair. We compared its predictions across different customer groups, where it was appropriate and allowed, to make sure it wasn't treating one group unfairly. We looked at things like false positives and false negatives to check for any bias.

If we found any differences, we looked at ways to improve the model. For example, we reviewed the input features, adjusted the decision threshold, or retrained the model to reduce bias while keeping its overall performance strong.

At the end of the project, I documented the results and shared them with both the technical team and the business team. We explained how the model performed, what we found during the fairness checks, and our recommendations for deployment and future monitoring.

My main contribution was helping with data preparation, model evaluation, performance analysis, and fairness testing while working closely with both the data science team and the business stakeholders throughout the project.


# Project 2: Collections Efficacy Enhancement
The goal of this project was to improve collection efficiency by focusing on customers with the highest likelihood of making payments.

My role was analyzing the data, finding useful patterns, validating the recommendations, and sharing the results with both the technical team and the business stakeholders.

I used SQL and Python to analyze historical collections data and looked for patterns in customer repayment behavior. I looked at things like payment history, how many days a payment was overdue, previous collection attempts, and outstanding balances to understand which factors were most useful for predicting whether a customer would repay.

Based on what we found, I worked with the team to build AI recommendations that ranked customer accounts by their likelihood of repayment. The idea wasn't to replace the collection agents but to give them better guidance on which accounts they should prioritize.

We tested the solution by comparing the new AI-assisted process with the existing one. The results were very positive—we saw about an 8% reduction in net bad debt, which showed that better account prioritization could improve collections performance.

# Table of Contents
- [Introduction](#introduction)
- [Aspire Ontario (AI Enablement Specialist) (Sept 2025 - Present)](#aspire-ontario-ai-enablement-specialist-sept-2025---present)
- [Exeevo (AI/ML Analyst Intern) (May 2024 – Dec 2024)](#exeevo-aiml-analyst-intern-may-2024--dec-2024)
- [Project 1: Credit Risk Assessment Model Optimization](#project-1-credit-risk-assessment-model-optimization)
- [Project 2: Collections Efficacy Enhancement](#project-2-collections-efficacy-enhancement)
---
- [Why do you want to leave your current job?](#why-do-you-want-to-leave-your-current-job)
- [Why apply for this job?](#why-apply-for-this-job)
- [What you will learn from this role?](#what-you-will-learn-from-this-role)
- [What is ROC-AUC?](#what-is-roc-auc)
- [How do you explain technical concepts to non-technical people](#how-do-you-explain-technical-concepts-to-non-technical-people)
- [Describe a time you solved a difficult problem](#describe-a-time-you-solved-a-difficult-problem)
- [How do you deal with ambiguity?](#how-do-you-deal-with-ambiguity)
- [Questions](#questions)
---
- [Steps of Data Preprocessing for ML Models](#steps-of-data-preprocessing-for-ml-models)
- [Missing Value Handling](#missing-value-handling)
- [Machine Learning Q&A](#machine-learning-qa)
- [MLOps Q&A](#mlops-qa)
- [Monitoring Model in Production](#monitoring-model-in-production)
- [Monitoring Data Drift](#monitoring-data-drift)

# Why do you want to leave your current job?
I'm looking for an opportunity where I can be involved in understanding business requirements, monitoring model performance and improving AI solutions after deployment, at the same time learning from experienced professionals. And working at a top technology company like Bell is a dream come true.

# Why apply for this job?
I applied for this role because it brings together AI, data analysis, and solving real business problems. I like that the role isn't just about building AI models but also improving them, tracking how they're performing, and collaborating with different teams to make them more effective. On top of that, Bell's focus on innovation and using AI to create a better customer experience is something that really interests me, and I'd love to be part of that.


## What you will learn from this role?
- how AI models are deployed and monitored in a real business environment
- the entire AI lifecycle—from development to deployment and ongoing improvements
- working with experienced professionals and seeing how AI solutions create real business value
- understanding the business context and translating it into technical requirements


# what is ROC-AUC?
ROC-AUC is a metric used to measure how well a classification model can separate different classes. A higher ROC-AUC score means the model is better at distinguishing between positive and negative cases. A score close to 1 is excellent, while 0.5 means the model is performing about the same as random guessing.

# How do you explain technical concepts to non-technical people
- I avoid technical jargon 
- use simple language 
- real-life examples. 
- I focus on the business problem instead of the technical details
- check any questions they have.

# Describe a time you solved a difficult problem.?
In one of my projects, I ran into a situation where the machine learning model just wasn't performing as well as I expected. After looking into it, I realized the main issue was with the data—it had a lot of missing values and duplicate records.

So, I started by cleaning the dataset. I removed the duplicates, handled the missing values, and spent some time exploring the features to better understand what was affecting the model's performance.

Once I retrained the model using the cleaned data, the prediction accuracy improved quite a bit. That experience really showed me how important good-quality data is. Even a great model won't perform well if the data going into it isn't reliable.


# How do you deal with ambiguity?
- I start by asking questions to understand the goal.
- I break down the problem into smaller parts and tackle them one at a time.
- I make sure to communicate with the team and stakeholders to clarify any uncertainties.
- For example, in one project at Exeevo, the requirements were not clear at first. I asked questions to clarify what the business needed, and then I worked with the team to define a clear plan. By breaking the problem down and keeping everyone informed, we were able to move forward successfully.


# Questions
- What would success look like in the first 3-6 months?
  >>> That's great to hear. Thank you for sharing that.
- What kinds of applications would I be building?
  >>> That's helpful. Could you also tell me a bit about...
- Are developers encouraged to experiment with new AI tools and workflows?
  >>> That sounds like an environment I'd really enjoy working in. Thanks for sharing.
- What are the next steps of the hiring process?


# Table of Contents
- [Introduction](#introduction)
- [Aspire Ontario (AI Enablement Specialist) (Sept 2025 - Present)](#aspire-ontario-ai-enablement-specialist-sept-2025---present)
- [Exeevo (AI/ML Analyst Intern) (May 2024 – Dec 2024)](#exeevo-aiml-analyst-intern-may-2024--dec-2024)
- [Project 1: Credit Risk Assessment Model Optimization](#project-1-credit-risk-assessment-model-optimization)
- [Project 2: Collections Efficacy Enhancement](#project-2-collections-efficacy-enhancement)
---
- [Why do you want to leave your current job?](#why-do-you-want-to-leave-your-current-job)
- [Why apply for this job?](#why-apply-for-this-job)
- [What you will learn from this role?](#what-you-will-learn-from-this-role)
- [What is ROC-AUC?](#what-is-roc-auc)
- [How do you explain technical concepts to non-technical people](#how-do-you-explain-technical-concepts-to-non-technical-people)
- [Describe a time you solved a difficult problem](#describe-a-time-you-solved-a-difficult-problem)
- [How do you deal with ambiguity?](#how-do-you-deal-with-ambiguity)
- [Questions](#questions)
---
- [Steps of Data Preprocessing for ML Models](#steps-of-data-preprocessing-for-ml-models)
- [Missing Value Handling](#missing-value-handling)
- [Machine Learning Q&A](#machine-learning-qa)
- [MLOps Q&A](#mlops-qa)
- [Monitoring Model in Production](#monitoring-model-in-production)
- [Monitoring Data Drift](#monitoring-data-drift)

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

# Table of Contents
- [Introduction](#introduction)
- [Aspire Ontario (AI Enablement Specialist) (Sept 2025 - Present)](#aspire-ontario-ai-enablement-specialist-sept-2025---present)
- [Exeevo (AI/ML Analyst Intern) (May 2024 – Dec 2024)](#exeevo-aiml-analyst-intern-may-2024--dec-2024)
- [Project 1: Credit Risk Assessment Model Optimization](#project-1-credit-risk-assessment-model-optimization)
- [Project 2: Collections Efficacy Enhancement](#project-2-collections-efficacy-enhancement)
---
- [Why do you want to leave your current job?](#why-do-you-want-to-leave-your-current-job)
- [Why apply for this job?](#why-apply-for-this-job)
- [What you will learn from this role?](#what-you-will-learn-from-this-role)
- [What is ROC-AUC?](#what-is-roc-auc)
- [How do you explain technical concepts to non-technical people](#how-do-you-explain-technical-concepts-to-non-technical-people)
- [Describe a time you solved a difficult problem](#describe-a-time-you-solved-a-difficult-problem)
- [How do you deal with ambiguity?](#how-do-you-deal-with-ambiguity)
- [Questions](#questions)
---
- [Steps of Data Preprocessing for ML Models](#steps-of-data-preprocessing-for-ml-models)
- [Missing Value Handling](#missing-value-handling)
- [Machine Learning Q&A](#machine-learning-qa)
- [MLOps Q&A](#mlops-qa)
- [Monitoring Model in Production](#monitoring-model-in-production)
- [Monitoring Data Drift](#monitoring-data-drift)