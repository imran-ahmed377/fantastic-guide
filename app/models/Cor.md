
## Table of Contents

- [Introduction](#introduction)
- [Aspire Ontario Exp (Data Science Software Developer)(Sept 2025 – Present)](#aspire-ontario-exp-data-science-software-developersept-2025--present)
- [Vista Print Exp (Software Developer Intern) (Jan 2023 – Dec 2024)](#vista-print-exp-software-developer-intern-jan-2023--dec-2024)
- [Project 1: Real-Time Analytics Platform on GCP](#project-1-real-time-analytics-platform-on-gcp)
- [Project 2: ML Model Deployment Pipeline](#project-2-ml-model-deployment-pipeline)
---
- [About this company?](#about-this-company)
- [Why Leave Current Job?](#why-leave-current-job)
- [Why are you interested?](#why-are-you-interested)
- [What you will learn from this Job?](#what-you-will-learn-from-this-job)
- [Unclear Requirement](#unclear-requirement)
- [Non-Technical People.](#non-technical-people)
- [Multiple Task/Project?](#multiple-taskproject)
- [RAG Hallucination](#rag-hallucination)
- [Comfortable Learning New Tech?](#comfortable-learning-new-tech)
- [What's your biggest weakness?](#whats-your-biggest-weakness)
- [Describe a difficult bug.](#describe-a-difficult-bug)
- [Questions](#questions)




# Introduction

Hi, I'm a Data Scientist with a strong background in data analysis, machine learning, and statistical modeling. I enjoy working with data to solve real-world business problems and convert complex datasets into clear, actionable insights. I'm proficient in Python, SQL, and data visualization tools like Power BI and Tableau, and I have experience building predictive models and automating analytical workflows. What motivates me most is using data to support smarter decisions and create measurable business value. I'm always eager to learn new technologies and collaborate with teams to develop innovative, data-driven solutions.


# Aspire Ontario Exp (Data Science Software Developer)(Sept 2025 – Present)
At Aspire Ontario, I build data products that are used in analytics and AI. I collaborate with the data scientists, analysts, and business teams to understand what their needs are and then build production-grade solutions to meet those needs. For example, if the marketing team wants a dashboard displaying information on customer trends, I build an Airflow pipeline using Python to gather and process the data from various sources and load it to BigQuery, then model data using Looker for their use. When the data science team builds a machine learning algorithm, I would deploy this in FastAPI on Cloud Run, and making it accessible to other applications.



# Vista Print Exp (Software Developer Intern) (Jan 2023 – Dec 2024)

At Vista Print, I worked with data scientists, software engineers, and business units to ensure they received good quality data. For example, in case the business unit decided to study customer purchasing trends, I created data pipelines using Apache Beam and Dataflow for collecting, cleaning, and transforming data before loading it to BigQuery. I also built REST APIs to expose the transformed data for use by other systems and worked with the data science unit to operationalize machine learning solutions.


# Project 1: Real-Time Analytics Platform on GCP

The goal of this project was to process user activity in real time so business teams could monitor customer behavior without waiting for batch reports.

I built a streaming data pipeline using Pub/Sub to receive events, Dataflow to process and transform the data, and BigQuery to store it for analysis. Then I deployed backend services on Cloud Run so other applications could access the processed data through APIs.

For example, if a customer visited a website or made a purchase, that event was sent through the pipeline, processed within seconds, and became available on dashboards for the business team. I also configured auto-scaling on Cloud Run, so the system could handle traffic spikes without downtime.

# Project 2: ML Model Deployment Pipeline
One project I worked on was an ML Model Deployment Pipeline. The goal was to automate the process of taking a trained machine learning model and deploying it into production safely and efficiently.

I used MLflow to track different model versions and Vertex AI to automate model training, validation, and deployment. Once a model passed the validation tests, it was automatically deployed. I also implemented A/B testing, where a small percentage of users received predictions from the new model while the rest continued using the current model. We monitored the performance, and if the new model performed better, it was rolled out to everyone. If not, the system automatically rolled back to the previous version.

This made the deployment process faster, reduced manual work, and ensured that new models could be released with minimal risk.






## Table of Contents

- [Introduction](#introduction)
- [Aspire Ontario Exp (Data Science Software Developer)(Sept 2025 – Present)](#aspire-ontario-exp-data-science-software-developersept-2025--present)
- [Vista Print Exp (Software Developer Intern) (Jan 2023 – Dec 2024)](#vista-print-exp-software-developer-intern-jan-2023--dec-2024)
- [Project 1: Real-Time Analytics Platform on GCP](#project-1-real-time-analytics-platform-on-gcp)
- [Project 2: ML Model Deployment Pipeline](#project-2-ml-model-deployment-pipeline)
---
- [About this company?](#about-this-company)
- [Why Leave Current Job?](#why-leave-current-job)
- [Why are you interested?](#why-are-you-interested)
- [What you will learn from this Job?](#what-you-will-learn-from-this-job)
- [Unclear Requirement](#unclear-requirement)
- [Non-Technical People.](#non-technical-people)
- [Multiple Task/Project?](#multiple-taskproject)
- [RAG Hallucination](#rag-hallucination)
- [Comfortable Learning New Tech?](#comfortable-learning-new-tech)
- [What's your biggest weakness?](#whats-your-biggest-weakness)
- [Describe a difficult bug.](#describe-a-difficult-bug)
- [Questions](#questions)



# About this company?
Corus Entertainment is one of Canada's leading media and content companies. It owns well-known TV, radio, news, and streaming brands such as Global TV, Global News, and STACKTV.


# Why Leave Current Job?
I've learned a lot in my current role, especially about building data pipelines, deploying machine learning models, and working on GCP. Now I'm looking for a new challenge where I can work on larger-scale data products, collaborate with a bigger team, and continue growing as a Data Science Software Developer. This role at Corus aligns well with my experience and long-term career goals.


# Why are you interested?
This role matches my experience in Python, GCP, ETL pipelines, APIs, and ML deployment. I'm looking for an opportunity where I can continue building production-ready data solutions while working closely with data scientists.


# What you will learn from this Job?
I think I'll gain experience building data products at a larger scale and learn more about designing production systems that support analytics and AI across the business. I'm also excited to work with experienced engineers and data scientists, improve my software architecture skills, and deepen my knowledge of MLOps and cloud technologies.


# Unclear Requirement
When the requirements are not clear, I ask questions to understand what the goal is. Then I confirm my understanding with the stakeholders or my team to make sure we're on the same page. If I need to make any assumptions, I write them down and ask for confirmation. I continue working on the parts that are clear. This helps avoid mistakes and reduces the chance of doing the work again.


# Non-Technical People.
I worked with users who weren't technical. When explaining something to a non-technical user, I avoid technical jargon and focus on the business impact rather than the technology behind it. I try to use simple language, relatable examples, and break the explanation into small steps.



# Multiple Task/Project?

I first understand which tasks have the highest business impact.

Then I break larger work into smaller milestones and communicate progress regularly.


# RAG Hallucination

Hallucination is when the AI confidently gives an answer that sounds right but isn't actually true or grounded in real data. 
A few ways I addressed this in my project:

- Grounding with RAG — instead of letting the model answer from memory alone, I made sure it only answered based on retrieved, real ticket data. This alone removes a lot of hallucination risk.

- Prompt engineering — I wrote prompts that explicitly instructed the model to say 'not enough information' rather than guess, if it couldn't find a good match.

- Testing and iteration — I tested outputs against known cases to check accuracy before rolling it out, and documented what worked so the prompt patterns were reusable and reliable going forward.

Basically, the goal isn't to fully eliminate hallucination — it's to reduce the risk and make sure a human is still in the loop for anything important."


# Comfortable Learning New Tech?

I am very comfortable. I expect continuous learning to be part of the job because technology evolves quickly, especially in the AI sector.

When I find something new, I usually build a small proof of concept first, read the documentation, and then apply it to a real project.

# What's your biggest weakness?

Earlier in my career, I sometimes spent too much time trying to find the perfect solution before moving forward.

I've learned that delivering a solid first version, gathering feedback, and iterating usually leads to better outcomes."

# Describe a difficult bug.

I once had an issue where an API worked locally but failed in production due to environment variable configuration.

I reproduced the issue, checked the deployment logs, compared the environments, identified the missing configuration, and added validation to prevent similar issues in the future.



# Questions
- What would success look like in the first 3-6 months?
  >>> That's great to hear. Thank you for sharing that.
- What kinds of applications would I be building?
  >>> That's helpful. Could you also tell me a bit about...
- Are developers encouraged to experiment with new AI tools and workflows?
  >>> That sounds like an environment I'd really enjoy working in. Thanks for sharing.
- What are the next steps of the hiring process?



## Table of Contents

- [Introduction](#introduction)
- [Aspire Ontario Exp (Data Science Software Developer)(Sept 2025 – Present)](#aspire-ontario-exp-data-science-software-developersept-2025--present)
- [Vista Print Exp (Software Developer Intern) (Jan 2023 – Dec 2024)](#vista-print-exp-software-developer-intern-jan-2023--dec-2024)
- [Project 1: Real-Time Analytics Platform on GCP](#project-1-real-time-analytics-platform-on-gcp)
- [Project 2: ML Model Deployment Pipeline](#project-2-ml-model-deployment-pipeline)
---
- [About this company?](#about-this-company)
- [Why Leave Current Job?](#why-leave-current-job)
- [Why are you interested?](#why-are-you-interested)
- [What you will learn from this Job?](#what-you-will-learn-from-this-job)
- [Unclear Requirement](#unclear-requirement)
- [Non-Technical People.](#non-technical-people)
- [Multiple Task/Project?](#multiple-taskproject)
- [RAG Hallucination](#rag-hallucination)
- [Comfortable Learning New Tech?](#comfortable-learning-new-tech)
- [What's your biggest weakness?](#whats-your-biggest-weakness)
- [Describe a difficult bug.](#describe-a-difficult-bug)
- [Questions](#questions)


