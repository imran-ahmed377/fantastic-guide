# Table of Contents

- [Introduction](#introduction)
- [Aspire Experience (Data Engineer)](#aspire-experience-data-engineer)
- [Meallens Experience (Machine Learning)](#meallens-experience-machine-learning)
- [Project 1: Enterprise ML Monitoring Platform](#project-1-enterprise-ml-monitoring-platform)
- [Project 2: Retail Data Lakehouse Architecture](#project-2-retail-data-lakehouse-architecture)
- [Zapier](#zapier)
- [Data Pipeline you built](#data-pipeline-you-built)
- [Machine Learning Model Deploy](#machine-learning-model-deploy)
- [Model Monitoring After Deployment](#model-monitoring-after-deployment)
- [Azure Service Used](#azure-service-used)
- [Handle Data Quality Issue in ETL](#handle-data-quality-issue-in-etl)
- [Questions](#questions)


# Introduction
I’m a Data Engineer with experience working on Machine Learning and AI-based applications. I completed my Master’s in Applied Computing with a focus on Artificial Intelligence from the University of Windsor.

In my recent role at Aspire Ontario, I worked mainly on building and maintaining data pipelines on Azure that processed over half a million records anually. I also improved data quality, optimized data workflows, and helped deploy machine learning models into production.

I enjoy building systems that are functional, scalable and intelligent, and I am very excited to contribute my expertise to a team where I can continue solving challenging problems, building impactful products, and learn from the experienced engineers.




# Aspire Experience (Data Engineer)
At Aspire Ontario, I contributed to building AI-driven solutions for a CRM platform named Exeevo.

I worked on developing an AI-powered voice assistant for the CRM system. I used Azure services like Azure Data Factory, Azure Databricks, and Azure OpenAI integrations to process customer data and support real-time voice interactions.

I built data pipelines, prepared structured customer data, and ensured the AI system had clean and reliable inputs. I also helped integrate the backend data workflows with the AI assistant so it could respond accurately and quickly.

The **impact** was improved customer support efficiency and faster access to CRM information through voice commands, reducing manual search effort for users. It also made the CRM system more interactive and easier to use for non-technical teams.

# Meallens Experience (Machine Learning)
At Meallens, I worked on building scalable data systems and supporting machine learning workflows.

I designed and implemented a data lake architecture using Azure Data Lake and Delta Lake, which helped centralize and organize large volumes of structured and unstructured data. I also built distributed data processing jobs using PySpark for high-volume analytics use cases.

On the ML side, I worked on automating model training and deployment workflows using TensorFlow and MLflow, which made releases more consistent and efficient.

I also helped set up CI/CD pipelines using Jenkins and GitLab, which reduced deployment failures by about 25%.

Overall, my work improved data organization, made ML deployments smoother, and helped the team deliver analytics solutions faster and more reliably.

# Project 1: Enterprise ML Monitoring Platform
I worked on an ML monitoring platform that tracked model performance after deployment and detected issues like data drift and accuracy drops.

I used Azure Databricks and PySpark to process prediction data and generate monitoring metrics. Azure Data Factory handled scheduling, while Docker and Kubernetes helped scale the monitoring services.

One challenge was processing large volumes of prediction data without impacting performance. I optimized the Spark workloads and used batch processing to keep the system efficient.

The platform automatically flagged unusual model behavior and alerted the team early. This reduced manual monitoring and helped identify when models needed retraining.


# Project 2: Retail Data Lakehouse Architecture
I worked on a Retail Data Lakehouse project on Azure that brought together data from multiple retail systems into a single platform for analytics and reporting.

I used Azure Data Lake for storage, Azure Data Factory for data ingestion, and Azure Databricks with PySpark for data processing and transformations. I also built SCD pipelines to maintain historical data accurately.

One challenge was managing large volumes of historical data while keeping reports fast. I improved performance through query optimization, partitioning, and efficient data modeling.

The solution created a scalable and reliable data platform. It improved data consistency, reduced dashboard load times by around 45%, and made historical reporting easier for business teams.

# Zapier
I have worked on an Automated Lead Capture and Follow-Up System project using Zapier. The goal was to reduce manual work and make sure every new lead gets a quick response.

When a customer fills out a form on the Google Forms, Zapier automatically starts the workflow. First, the lead information is saved in Google Sheets.

Then, a notification is sent to the Slack channel so the team know a new lead has arrived. After that, the system automatically sends a personalized welcome email to the customer through Gmail. If a lead meets certain criteria, Zapier automatically assigns that lead to the high-priority for faster follow-up.


# Data Pipeline you built
At Aspire Ontario, I built data pipeline using Azure Data Factory and Azure Databricks.

Azure Data Factory was used to schedule and run the workflow. It extracted data from multiple source systems and loaded it into Azure Data Lake. Then, Azure Databricks ran PySpark jobs to clean, transform, and validate the data.

I also implemented data quality checks to identify missing or invalid records before loading the data into the curated layer. The processed data was then made available for reporting and machine learning use cases.

One **challenge** was that the pipeline was taking longer than expected as data volume increased. I optimized the PySpark transformations and improved partitioning in Databricks, which reduced the processing time by about 40%.

This pipeline provided reliable and high-quality data for business reporting and analytics while reducing manual effort.

# Machine Learning Model Deploy
At Aspire Ontario, I worked with data scientists to deploy a predictive machine learning model that helped identify customers who were likely to need additional support services.

My role was to prepare the data pipeline, create reliable feature datasets, and help move the model from development into production. We used Azure Databricks and PySpark for data processing, and MLflow for model tracking and deployment.

Once the model was approved, I containerized it using Docker and deployed it as a service for real-time predictions. I also set up monitoring to track model performance, prediction latency, and data quality.

After deployment, the model was able to generate predictions automatically without manual intervention, making it easier for the business team to take timely action. This improved the speed and consistency of the decision-making process.

# Model Monitoring After Deployment
After a model is deployed, I monitor both the model's performance and the health of the deployment.

In one project, we used MLflow to track model versions and performance metrics. I monitored metrics such as prediction accuracy, inference latency, and error rates. I also compared new prediction data with the training data to detect data drift or changes in data patterns.

Using Azure Databricks and PySpark, I built automated monitoring jobs that generated daily reports and alerts when metrics crossed predefined thresholds.

For example, if model accuracy dropped significantly or prediction response times increased, the team would be notified so we could investigate quickly.

I also worked on an ML monitoring platform that tracked model drift, accuracy, and latency. This helped us identify issues early and decide when a model needed retraining or further investigation.

# Azure Service Used
I have mainly worked with Azure Data Factory, Azure Databricks, Azure Data Lake, Azure Synapse Analytics, and MLflow on Azure.

A typical workflow started with Azure Data Factory, which was used to schedule and orchestrate data movement from source systems. The data was stored in Azure Data Lake, which acted as our central storage layer.

Next, Azure Databricks processed the data using PySpark. This included data cleaning, transformation, validation, and feature engineering. The processed data was then stored back in the lake in a structured format.

For reporting and analytics, the curated data was made available through Azure Synapse Analytics, where business users and analysts could access it efficiently.

For machine learning projects, we used MLflow to track experiments, manage model versions, and support deployment.

Together, these services created an end-to-end platform that automated data ingestion, processing, analytics, and machine learning workflows while remaining scalable and reliable.

# Handle Data Quality Issue in ETL
I handle data quality issues by adding checks at multiple stages of the ETL pipeline.

In my work at Aspire Ontario, I used PySpark validation rules inside Azure Databricks to check for missing values, duplicate records, and incorrect data formats before processing.

If issues were found, I either cleaned the data automatically (like filling or removing invalid records) or sent them to a quarantine layer for review.

I also implemented data quality monitoring jobs that ran daily and logged metrics like completeness and accuracy. These were tracked using Azure Data Factory and Databricks notebooks.

When a major issue occurred, I would trace it back to the source system using pipeline logs and fix the transformation logic or ingestion rules.

Finally, I added alerts so the team would be notified early if data quality dropped, which helped prevent bad data from reaching reporting or machine learning systems.

# Data Preprocessing

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

# Missing Value Handling

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

# Monitoring Data Drift
Data drift occurs when the input data changes over time, leading to model decay.
*   **Continuous Monitoring**: Watch for statistical shifts in input features.
*   **Regular Retraining**: Schedule model training sessions on new data.
*   **Trigger Alerts**: Automatically notify the team when performance drops below a threshold.

    ### Data Drift Detection Techniques
    1. Compare averages (mean): Check if the average value of a feature has changed.
    2. Compare distributions (histograms): Look at how values are spread, not just the average.
    3. Statistical tests: Example: Kolmogorov-Smirnov (KS) Test Compare two dataset cumulative distribution (CDF) curves at every point, check the difference between them.

# Questions
- What is your expectation from the new hire in first 3 to 6 months?
- What is the team size?
- What are the next steps of the hiring process?
