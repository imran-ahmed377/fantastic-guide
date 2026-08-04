
# Greetings

Thank you! I'm excited to be here.

# Introduction

I recently completed my Master's in Applied Computing from the University of Windsor, with a specialization in Artificial Intelligence. I have worked as a Data Scientist and Data Analyst Intern, where I used Python, SQL, and machine learning models to predict customer churn. I have also built RAG based AI agent for real-time data analysis. I presented my findings to both technical and non-technical stakeholders. And I am very excited about this opportunity to apply my skills and continue to learn and grow in this role and contribute to CanadaHelps' mission of sparking generosity and powering positive change.

---

# Project 1: Customer Churn Prediction Model

This project focused on predicting customer churn using behavioral data. The goal was to identify customer who were likely to stop using the platform so the organization could target them with retention campaigns before losing them.

I first cleaned and prepared the data using Python and Pandas by handling missing values, and creating new features like usage frequency and recency, and prepared the data for modeling. Then I built and compared several classification models in Scikit-learn, including Logistic Regression, Decision Tree, and Random Forest. I focused on improving recall, which increased by 25% after feature engineering and model tuning.

Finally, I created a Power BI dashboard that highlighted high-risk customer segments and key trends. This allowed the fundraising team to change outreach efforts and make more informed decisions. I'm especially proud of this project because I learned some new techniques and the team really appreciated the dashboard I built.

---

## What I Learned
- **Extreme Class Imbalance**: I learned how to handle extreme class imbalance in the dataset by using techniques like SMOTE and adjusting class weights in the models. 

- **uvicorn**: I learned how to use uvicorn to run a streamlit app locally and deploy it to a server for others to access.

- **Streamlit**: I learned how to use Streamlit to create interactive dashboards for data visualization and model results.

- **Feature Engineering**: I learned how to create new features from existing data, which improved model performance and provided more insights into customer behavior.

- **ROC AUC**: I learned how to use ROC AUC as a performance metric for classification models, which helped me evaluate the models more effectively.

- **Dashboard**: Highlights high-risk customer accounts, compares model performance, and visualizes churn probability, trends, and segment risk. It shows a 71.2% accuracy, 0.745 ROC-AUC, 53.8% recall, and 5.4% overall churn, helping stakeholders prioritize retention actions effectively for better customer retention outcomes.


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


---

# Monitoring Data Drift
Data drift occurs when the input data changes over time, leading to model decay.
*   **Continuous Monitoring**: Watch for statistical shifts in input features.
*   **Regular Retraining**: Schedule model training sessions on new data.
*   **Trigger Alerts**: Automatically notify the team when performance drops below a threshold.

    ## Data Drift Detection Techniques
    1. Compare averages (mean): Check if the average value of a feature has changed.
    2. Compare distributions (histograms): Look at how values are spread, not just the average.
    3. Statistical tests: Example: Kolmogorov-Smirnov (KS) Test Compare two dataset cumulative distribution (CDF) curves at every point, check the difference between them.

# Handling Missing Data
*   **Imputation**: Fill in missing values with mean, median, or mode.
*   **Model-Based Imputation**: Use regression or KNN to predict missing values.
*   **Deletion**: Remove rows or columns with missing values if they are not critical to the analysis.
*   **Flagging**: Create a new feature indicating whether the data was missing.
*   **Domain Knowledge**: Use business understanding to make informed decisions about missing data.

# Libraries Used
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
