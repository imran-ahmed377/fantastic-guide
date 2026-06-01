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
Sure. I recently completed my Master's in Applied Computing with a specialization in Artificial Intelligence from the University of Windsor.

I have over 2 years of experience in Data Engineering and Machine Learning. Most recently, I worked as a Data Engineer at Aspire Ontario, where I built and maintained data pipelines on Azure that processed over 2 million records every day. I also improved data quality processes, optimized data workflows, and helped deploy machine learning models into production.

Before that, I worked at Meallens as a Machine Learning and Data Engineering Developer. There, I helped build data lake solutions, created automated machine learning workflows, and supported large-scale data processing projects.

Overall, my experience has focused on building reliable data systems, improving data quality, and helping organizations make better decisions using data. I enjoy working with cross-functional teams and solving data-related challenges that create business value.

# Aspire Experience (Data Engineer)
At Aspire Ontario, I contributed to building AI-driven solutions for a CRM platform.

One of my key projects was developing an AI-powered voice assistant for the CRM system. I used Azure services like Azure Data Factory, Azure Databricks, and Azure OpenAI integrations to process customer data and support real-time voice interactions.

My role included building data pipelines, preparing structured customer data, and ensuring the AI system had clean and reliable inputs. I also helped integrate the backend data workflows with the assistant so it could respond accurately and quickly.

The impact was improved customer support efficiency and faster access to CRM information through voice commands, reducing manual search effort for users. It also made the CRM system more interactive and easier to use for non-technical teams.

# Meallens Experience (Machine Learning)
At Meallens, I worked on building scalable data systems and supporting machine learning workflows.

I designed and implemented a data lake architecture using Azure Data Lake and Delta Lake, which helped centralize and organize large volumes of structured and unstructured data. I also built distributed data processing jobs using PySpark for high-volume analytics use cases.

On the ML side, I worked on automating model training and deployment workflows using TensorFlow and MLflow, which made releases more consistent and efficient.

I also helped set up CI/CD pipelines using Jenkins and GitLab, which reduced deployment failures by about 25%.

Overall, my work improved data organization, made ML deployments smoother, and helped the team deliver analytics solutions faster and more reliably.

# Project 1: Enterprise ML Monitoring Platform
I built an Enterprise ML Monitoring Platform to track model performance after deployment and detect issues like drift and performance drop.

I used Azure Databricks and PySpark to process prediction logs and calculate metrics like accuracy, latency, and data drift. The pipeline was scheduled using Azure Data Factory, and results were stored in the data lake for reporting. We also used Docker and Kubernetes to deploy monitoring services in a scalable way.

One key challenge was handling large volumes of real-time prediction data efficiently without slowing down the system. I solved this by optimizing Spark jobs and batching the monitoring calculations.

The result was a system that could automatically detect anomalies in model behavior and alert the team early. This helped reduce manual monitoring effort and made it easier to identify when a model needed retraining or investigation.

# Project 2: Retail Data Lakehouse Architecture
I built a Retail Data Lakehouse Architecture on Azure to unify structured and unstructured retail data for analytics and reporting.

We used Azure Data Lake as the central storage layer and Delta Lake for managing structured tables with versioning. Data ingestion and orchestration were handled using Azure Data Factory, while Azure Databricks with PySpark was used for data cleaning, transformations, and building SCD (Slowly Changing Dimension) pipelines.

One key challenge was handling large-scale historical data efficiently while keeping reporting fast. To solve this, I optimized Spark queries, used proper partitioning, and implemented SCD logic to maintain accurate historical records.

The result was a scalable lakehouse system that improved data consistency and reduced dashboard latency by about 45%. It also made historical reporting more reliable and easier for business users to access.

# Zapier
I have worked on an Automated Lead Capture and Follow-Up System project using Zapier. The goal was to reduce manual work and make sure every new lead gets a quick response.

When a customer fills out a form on the Google Forms, Zapier automatically starts the workflow. First, the lead information is saved in Google Sheets.

Then, a notification is sent to the Slack channel so the team know a new lead has arrived. After that, the system automatically sends a personalized welcome email to the customer through Gmail. If a lead meets certain criteria, Zapier automatically assigns that lead to the high-priority for faster follow-up.


# Data Pipeline you built
At Aspire Ontario, I built a data pipeline that processed over 2 million records daily using Azure Data Factory and Azure Databricks.

Azure Data Factory was used to schedule and orchestrate the workflow. It extracted data from multiple source systems and loaded it into Azure Data Lake. Then, Azure Databricks ran PySpark jobs to clean, transform, and validate the data.

I also implemented data quality checks to identify missing or invalid records before loading the data into the curated layer. The processed data was then made available for reporting and machine learning use cases.

One challenge was that the pipeline was taking longer than expected as data volume increased. I optimized the PySpark transformations and improved partitioning in Databricks, which reduced the processing time by about 40%.

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

# Questions
- What is your expectation from the new hire in first 3 to 6 months?
- What is the team size?
- What are the next steps of the hiring process?
