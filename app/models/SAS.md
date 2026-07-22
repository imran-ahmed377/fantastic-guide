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