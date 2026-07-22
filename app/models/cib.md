# Table of Contents


# Introduction
I recently completed my Master's in Applied Computing with a specialization in Artificial Intelligence from the University of Windsor. I have experience as a Data Analyst and a Fraud Analytics Consultant, where I worked mainly with SQL and Python for data analysis and predictive modeling, and used SAS for reporting and quick analytics. I also built Tableau dashboards to help stakeholders make data-driven decisions. I'm particularly interested in data analytics, fraud detection, and using data to solve business problems. I'm excited about the opportunity to apply my skills and continue learning in this role.

# Exeevo Experience
**Company Type:** A consulting firm providing fraud analytics services to clients


**Day in a life Overview:**

I reviewed fraud trends and checked any unusual spikes in fraud alerts. I used SQL to pull the latest transaction data and validated data quality. I used Python to investigate fraud patterns, and refined predictive models, and evaluated model performance. 

I used SAS to generate reports and performed ad hoc analytics. I collaborated with fraud analysts to discuss findings, refine fraud rules, and present recommendations for improving fraud detection and minimizing false positives.


**Day in a life:**

| Time | Typical Activities |
|------|---------------------|
| **8:30–9:00 AM** | Review emails, overnight fraud alerts, dashboards, and key fraud metrics. Check if any fraud rules generated unusually high or low alert volumes. |
| **9:00–10:30 AM** | Analyze recent fraud trends using SQL, SAS, or Python. Investigate suspicious patterns such as increases in card fraud, account takeover, or digital banking fraud. |
| **10:30–11:00 AM** | Team meeting with fraud strategy managers, investigators, or product teams to discuss emerging fraud schemes and ongoing initiatives. |
| **11:00 AM–12:30 PM** | Develop or improve fraud detection rules. Test different thresholds or logic to reduce fraud while minimizing false positives that inconvenience customers. |
| **12:30–1:30 PM** | **Lunch** |
| **1:30–3:00 PM** | Build analytical models or perform statistical analysis. Which  includes logistic regression, decision trees, random forests, or optimization techniques to predict fraudulent activity. |
| **3:00–4:00 PM** | Validate model performance. Compare fraud detection rates, false positive rates, financial impact, and customer experience before recommending deployment. |
| **4:00–5:00 PM** | Prepare reports or presentations explaining findings to business stakeholders. Update documentation and plan next analytical tasks. |

---

# Vista Print Experience

**Day in a life Overview:**

I mostly worked with SQL and Python. I used SQL to extract data from the company's data warehouse and Python to clean, analyze, and validate the data. I performed statistical analyses to detect anomalies and ensure data quality. Once the analysis was complete, I update Tableau dashboards so business teams could monitor key metrics like sales, customer behavior, and campaign performance. I also worked closely with cross-functional teams to understand their reporting needs and presented my findings with recommendations.

## Example Project

**Scenario:** VistaPrint launches a **20% off Business Cards** promotion.

| Task | What You Did |
|------|---------------|
| **Extract campaign data** | Used SQL to retrieve customer orders, website traffic, and campaign information. |
| **Analyze campaign performance** | Used Python to calculate conversion rates, revenue, average order value (AOV), and customer segments. |
| **Detect anomalies** | Identified that one region had unusually low conversion due to an incorrect promotional pricing configuration. |
| **Create dashboard** | Built a Tableau dashboard showing sales by region, campaign ROI, conversion rate, and customer demographics. |
| **Present findings** | Recommended fixing the pricing issue and increasing marketing spend in high-performing regions, resulting in better campaign performance. |

---
#########################################################
---

**Day in a life:**
| Time | What I Did | Tools Used | Business Purpose |
|------|-------------|------------|------------------|
| **9:00 AM** | Checked the status of overnight data pipelines and reviewed data quality reports. Investigated any missing or unusual data. | SQL, Python | Ensure stakeholders receive accurate and complete data. |
| **9:30 AM** | Queried sales, customer, and marketing data from the data warehouse for ongoing analysis requests. | SQL | Extract relevant data for reporting and business analysis. |
| **10:30 AM** | Cleaned and transformed data using Python. Removed duplicates, handled missing values, and prepared datasets for analysis. | Python (Pandas) | Produce reliable datasets for analysis and dashboards. |
| **11:30 AM** | Performed statistical analysis to identify anomalies, such as unexpected drops in sales, duplicate orders, or abnormal customer behavior. | Python (NumPy, SciPy), SQL | Improve data quality and identify potential business issues. |
| **1:00 PM** | Built or updated Tableau dashboards showing sales trends, customer acquisition, campaign performance, and operational KPIs. | Tableau | Provide business teams with interactive dashboards for decision-making. |
| **2:00 PM** | Met with marketing, operations, or product teams to understand new reporting requirements or answer questions about existing dashboards. | Teams/Zoom, Tableau | Translate business needs into analytical solutions. |
| **3:00 PM** | Worked on ad hoc analysis, such as evaluating the performance of a recent marketing campaign or identifying top-selling products. | SQL, Python | Help business teams make data-driven decisions. |
| **4:00 PM** | Prepared reports or presentations summarizing key findings and recommendations for managers and stakeholders. | Tableau, PowerPoint, Excel | Clearly communicate insights and recommended actions. |
| **5:00 PM** | Optimized SQL queries or Python scripts, documented analysis, and planned tasks for the next day. | SQL, Python | Improve efficiency and maintain reusable analytical workflows. |

---



---

# Salary Expectations?
I'm looking for a base salary in the $80,000–90,000 range, but I'm flexible based on the overall compensation package.


# Questions
- What would success look like in the first 90 days?
  >>> That's great to hear. Thank you for sharing that.
- What kinds of applications would I be building?
  >>> That's helpful. Could you also tell me a bit about...
- Are developers encouraged to experiment with new AI tools and workflows?
  >>> That sounds like an environment I'd really enjoy working in. Thanks for sharing.
- What are the next steps of the hiring process?


---

# 1. SAS Enterprise Guide (SAS EG) — Data Access, Analysis, Reporting, and Rule Development

SAS Enterprise Guide (SAS EG) would be your **daily workhorse** for querying data, exploring fraud patterns, creating datasets, and producing analytical outputs.

## Typical Uses in This Job

### A. Extracting and Preparing Fraud Data

You would use SAS EG to connect to company's data repositories and pull information such as:

- Credit/debit card transactions
- Online banking activity
- Customer profiles
- Device information
- Transaction history
- Fraud case outcomes
- Previous fraud alerts

**Example tasks:**

- Identify all transactions flagged as fraud in the last 30 days.
- Join transaction data with customer behavior data.
- Create datasets for modeling.

### Example SAS EG Workflow

```text
Transaction Database
        │
        ▼
SAS EG SQL Query
        │
        ▼
Cleaned Fraud Analysis Dataset
        │
        ▼
Modeling / Reporting
```

---

### B. Investigating Fraud Trends

A fraud analyst might use SAS EG to answer questions like:

> **"Why did fraud losses increase last month?"**

You might analyze:

- Fraud rate by transaction type
- Fraud rate by country
- Fraud rate by merchant category
- Fraud rate by device type
- Time-of-day fraud patterns

#### Example Output

| Segment | Fraud Rate |
|----------|-----------:|
| Mobile banking | 0.8% |
| Online purchases | 1.4% |
| International transactions | 2.3% |

Based on these findings, you could recommend new fraud detection rules.

---

### C. Building Fraud Detection Rules

A major part of the job is **rules management**.

#### Example Rule

```sql
IF transaction_amount > 5000
AND transaction_country != customer_country
THEN create fraud alert
```

You would use SAS EG to test questions such as:

- How many fraud cases would this rule catch?
- How many legitimate customers would be affected?
- How much fraud loss could be prevented?

Typical evaluation metrics include:

- Detection rate
- False positive rate
- Customer impact
- Financial benefit

---

### D. Creating Monitoring Reports and Dashboards

SAS EG can generate reports for fraud managers and stakeholders.

#### Example Daily Fraud Monitoring Report

```text
Total transactions:       10,000,000
Fraud alerts generated:      25,000
Confirmed fraud cases:        2,500
False positives:             22,500
Fraud prevented:           $4.2 million
```

These reports help determine whether fraud strategies are performing effectively.

---

# 2. SAS Enterprise Miner (SAS Miner) — Predictive Modeling and Machine Learning

SAS Enterprise Miner is primarily used to build **predictive fraud models**.

Instead of manually creating rules such as:

> "Flag transactions above $5,000"

Machine learning models learn patterns like:

> "Transactions with these 35 characteristics have an 87% probability of being fraudulent."

---

## Typical SAS Miner Workflow

```text
Raw Fraud Data
        │
        ▼
Data Preparation
        │
        ▼
Feature Engineering
        │
        ▼
Model Building
        │
        ▼
Model Validation
        │
        ▼
Fraud Detection Strategy
```

---

## A. Data Preparation

### Transaction Features

| Feature | Example |
|---------|---------|
| Transaction amount | $2,500 |
| Location | Canada |
| Merchant type | Electronics |
| Transaction time | 2:00 AM |
| Device change | Yes |
| Previous fraud history | No |

### Customer Behavior Features

Examples include:

- Average transaction amount
- Number of transactions per day
- Typical spending locations
- Login frequency
- Recent password changes

---

## B. Building Predictive Models

The job posting specifically mentions:

- Logistic regression
- Decision trees
- Random forest
- Neural networks
- Sampling
- Optimization

These are common modeling techniques in SAS Enterprise Miner.

---

### Example: Logistic Regression

#### Goal

Predict:

```text
Fraud = 1
Legitimate = 0
```

The model might learn that fraud probability increases when:

- New device used
- Foreign IP address
- Large transaction
- Unusual merchant category
- Multiple failed login attempts

#### Example Output

```text
Transaction A
--------------
Fraud Probability: 92%

Action:
Send for manual review
```

---

### Example: Decision Tree

SAS Miner might automatically generate decision logic like:

```text
              Transaction Amount > $3000?
                        │
              ┌─────────┴─────────┐
             Yes                 No
              │
     Foreign Location?
              │
        ┌─────┴─────┐
       Yes         No
        │
 High Fraud Risk
```

The fraud team can convert these findings into production rules.

---

### Example: Random Forest

Used when fraud behavior is highly complex.

Instead of relying on one decision tree:

```text
Tree 1 → Fraud Probability: 85%
Tree 2 → Fraud Probability: 92%
Tree 3 → Fraud Probability: 88%

Final Prediction:
Fraud Probability = 88%
```

---

## C. Model Evaluation

Models are evaluated using metrics such as:

### Accuracy Is Not Enough

Fraud is a highly imbalanced problem.

#### Example

```text
1,000,000 Transactions

999,000 Legitimate
1,000 Fraud
```

A model predicting every transaction as legitimate achieves:

> **99.9% Accuracy**

…but provides no fraud detection value.

Instead, analysts focus on more meaningful metrics.

---

### Fraud Detection Rate (Recall)

**Question:**

> "How much fraud did we catch?"

#### Example

```text
Detected Fraud:
850 / 1,000 cases

Recall = 85%
```

---

### False Positive Rate

**Question:**

> "How many legitimate customers were incorrectly flagged?"

#### Example

```text
Fraud Alerts:
50,000

Actual Fraud:
5,000

False Positives:
45,000
```

Too many false positives negatively impact customer experience.

---

# How SAS Enterprise Guide and SAS Miner Work Together

## Project Example: Reduce Credit Card Fraud Losses

### Step 1 — SAS Enterprise Guide

Extract historical data:

```text
Last 12 Months Transactions
            +
Fraud Investigation Results
            +
Customer Behavior Data
```

↓

### Step 2 — SAS Enterprise Guide

Prepare the data:

```text
- Remove duplicates
- Handle missing values
- Create fraud indicators
```

↓

### Step 3 — SAS Enterprise Miner

Build predictive models:

```text
- Logistic Regression
- Decision Tree
- Random Forest
```

↓

### Step 4 — SAS Enterprise Miner

Compare model performance:

```text
Model A
Fraud Detection = 78%

Model B
Fraud Detection = 86%

Model C
Fraud Detection = 89%
```

↓

### Step 5 — SAS Enterprise Guide

Analyze business impact:

```text
Fraud Prevented:
+$5M

False Positives:
-15%

Customer Complaints:
Reduced
```

↓

### Step 6 — Deploy Fraud Strategy

Deploy the selected model and implement new fraud detection rules into the company's fraud monitoring systems.
