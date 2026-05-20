## Table of Contents

- [1. Tell us about yourself.](#1-tell-us-about-yourself)

- [2. Why do you want to work at The Globe and Mail?](#2-why-do-you-want-to-work-at-the-globe-and-mail)

- [12. Why should we hire you?](#12-why-should-we-hire-you)

- [3. What experience do you have with SQL?](#3-what-experience-do-you-have-with-sql)


- [6. Tell us about one achievement you’re proud of.](#6-tell-us-about-one-achievement-youre-proud-of)

- [7. How do you make sure your data is accurate?](#7-how-do-you-make-sure-your-data-is-accurate)

- [8. Do you have experience with A/B testing?](#8-do-you-have-experience-with-ab-testing)


- [10. Have you worked with CRM or customer data platforms?](#10-have-you-worked-with-crm-or-customer-data-platforms)

- [Aspire Ontario Experience](#aspire-ontario-job-role)

- [MealLens Experience](#meallens-job-role)

- [Project 1: Customer Segmentation](#project-1-customer-segmentation-and-campaign-analytics-system)


- [Project 2: Subscriber Behavior](#project-2-subscriber-behavior)

- [Questions](#questions)


- [AB Testing](#ab-testing)

## 1. Tell us about yourself.

I am Imran Ahmed, I have experience working with SQL, customer data, and marketing analytics. In my recent role, I built customer segments for marketing campaigns, created dashboards in Tableau and Power BI, and supported A/B testing to improve campaign performance. I enjoy working with data and using it to help businesses make better decisions.

## 2. Why do you want to work at The Globe and Mail?

I like that this role because it combines data, marketing, and customer engagement, which matches my experience and interests. The Globe and Mail is also a well-known and respected company in Canada, so I’d be excited to be part of a team that focuses on data-driven growth and customer experience.

## 12. Why should we hire you?

I have hands-on experience with SQL, marketing analytics, dashboards, and customer segmentation that matches this role well. I’m also detail-oriented, easy to work with, and always willing to learn new tools and processes.


## 3. What experience do you have with SQL?

I use SQL for customer segmentation, reporting, and analyzing campaign data. I’ve worked with Oracle SQL, PL/SQL, PostgreSQL, and Snowflake to create reports, automate workflows, and manage large datasets.

## 6. Tell us about one achievement you’re proud of.

In my recent role, I helped improve campaign targeting accuracy by 35% by building automated customer segments in SQL. I also supported A/B testing that increased conversion rates by 20%.

## 7. How do you make sure your data is accurate?

I double-check my SQL queries, validate data counts, and test outputs before sharing results or launching campaigns. I pay close attention to details because even small mistakes can affect reporting and campaign performance.

## 8. Do you have experience with A/B testing?

Yes. I helped run A/B tests for user engagement campaigns and compared the results to see which version performed better. Then I shared insights with the team to improve future campaigns.



## 10. Have you worked with CRM or customer data platforms?

Yes. I’ve worked with CRM data for customer segmentation, campaign reporting, and audience creation. I also helped maintain data quality and consistency across customer datasets.









## Aspire Ontario Job Role
At Aspire Ontario, I worked as a Data Analyst. My main role was to develop an AI powered CRM software.

I built SQL-based customer database in Oracle SQL. I also created automated queries and reports for regular data extraction and tracking.

I also built dashboards in Power BI. These dashboards showed campaign performance, customer behavior, and retention trends.

I used tools like Oracle SQL, Power BI, Excel. I also worked with CRM and marketing systems to manage customer data.


## MealLens Job Role

At Meallens my main role was to analyze customer and business data to support decision-making.

I created SQL reports for customer engagement and retention analysis. I also built Tableau and Excel dashboards to track performance and automate reporting.

Another important part of my job was cleaning and transforming data to improve accuracy and reliability. I also supported CRM data extraction and customer segmentation for marketing campaigns.

I worked closely with teams to provide insights and make reporting faster and more efficient.



## Project 1: Customer Segmentation and Campaign Analytics System

The project goal was to improve email campaign targeting using customer segmentation.

I used SQL and Python to analyze user behavior data and create customer segments based on engagement and activity patterns. I also used PowerBI to build dashboards for tracking campaign performance like engagement and retention.

The main outcome was improving targeting precision by about 30%. The key success metrics were better segmentation accuracy and improved campaign engagement indicators like clicks and retention trends.

## Project 2: Subscriber Behavior
The main goal was to understand how users were engaging with content and campaigns, and to track their behavior over time.

I used PowerBI to build the dashboard and visualize key metrics. I also used SQL to pull and prepare the data. For some analysis, I used Python to clean and explore user behavior patterns.

The dashboard showed things like user engagement trends, retention, click-through rates, and campaign performance. I also included an A/B testing view to compare different campaign versions.

The main success metrics for the project were:

- Improving decision-making speed by 45% through faster access to insights
- Better understanding of user engagement trends
- More accurate comparison of campaign performance using A/B testing
- Helping teams identify what content or campaigns were performing better

## Questions
- What is your expectation from the new hire in first 3 to 6 months?
- What are the next steps of the hiring process?


---

# A/B Testing
## ⚡ One-line intuition

**A/B testing = “Show two versions to similar users and check if the difference is real or just luck.”**

## 🎯 Scenario

You run an e-commerce app and want to test:

**Does a new checkout button increase purchases?**

---

## 1. Define the hypothesis

Keep it very clear and measurable.

- **Null hypothesis (H₀):** New button does not change conversion rate  
- **Alternative (H₁):** New button increases conversion rate  

**Example:**  
Current conversion = 10%  
You expect → 12%

---

## 2. Choose your metric

Pick one primary metric (don’t overcomplicate).

**Example:**
- Primary: % of users who complete purchase  
- Secondary (optional): revenue per user  

---

## 3. Decide group split (A vs B)

Most common: **50/50 split**

- Group A → old button  
- Group B → new button  

**Why 50/50?**
- Fastest way to get results  
- Balanced comparison  

Sometimes companies use 90/10 for safer rollout, but 50/50 is standard for testing.

---

## 4. Determine sample size (how many users you need)

You need enough users to detect a real difference.

**Key inputs:**
- Baseline = 10%  
- Expected improvement = +2% (to 12%)  
- Confidence level = 95%  
- Power = 80%  

Using a calculator or stats tool:

👉 You’ll need roughly **~4,000–5,000 users per group**

_(You don’t calculate this manually in practice—tools do it.)_

---

## 5. Determine experiment duration

Duration depends on traffic.

**Example:**
- You get 1,000 users/day  
- Need 5,000 per group → 10,000 total  

👉 Duration ≈ **10 days**

**Add buffer:**
- Run at least 1–2 full weeks to capture weekday/weekend behavior  

👉 Final: **2 weeks**

---

## 6. Run the experiment properly

**Rules:**
- Randomly assign users  
- Keep conditions the same (no other changes)  
- Don’t stop early just because results “look good”  

---

## 7. Analyze results

Compare conversion rates using a statistical test like a t-test or proportion test.

**Example result:**
- A = 10%  
- B = 12%  
- (Chance of result is random, low p-value is good) p-value < 0.05 → significant  

👉 New button wins  

---

## 8. Decide rollout strategy

Don’t always go straight to 100%.

**Typical rollout:**
- Step 1: 10% users  
- Step 2: 50% users  
- Step 3: 100% users  

**Why gradual?**
- Catch bugs or unexpected issues  
- Reduce risk  

---

## 🧠 Simple summary (memory version)

- Hypothesis: what you expect to change  
- Metric: what you measure  
- Split: usually 50/50  
- Sample size: enough users to detect change  
- Duration: based on traffic (usually 1–2 weeks min)  
- Run test: random + controlled  
- Analyze: is difference real?  
- Rollout: gradual release  

## Table of Contents

- [1. Tell us about yourself.](#1-tell-us-about-yourself)

- [2. Why do you want to work at The Globe and Mail?](#2-why-do-you-want-to-work-at-the-globe-and-mail)

- [12. Why should we hire you?](#12-why-should-we-hire-you)

- [3. What experience do you have with SQL?](#3-what-experience-do-you-have-with-sql)


- [6. Tell us about one achievement you’re proud of.](#6-tell-us-about-one-achievement-youre-proud-of)

- [7. How do you make sure your data is accurate?](#7-how-do-you-make-sure-your-data-is-accurate)

- [8. Do you have experience with A/B testing?](#8-do-you-have-experience-with-ab-testing)


- [10. Have you worked with CRM or customer data platforms?](#10-have-you-worked-with-crm-or-customer-data-platforms)

- [Aspire Ontario Experience](#aspire-ontario-job-role)

- [MealLens Experience](#meallens-job-role)

- [Project 1: Customer Segmentation](#project-1-customer-segmentation-and-campaign-analytics-system)

- [Project 2: Subscriber Behavior](#project-2-subscriber-behavior)

- [Questions](#questions)


- [AB Testing](#ab-testing)
