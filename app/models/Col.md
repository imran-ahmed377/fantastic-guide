# Exeevo Experience as Supply Chain Data Analyst
## 1. Power BI dashboards

**The bullet:** Built Power BI dashboards tracking 12 logistics KPIs, cutting weekly manual reporting effort by 8 hours

**What it means:** You built **dashboards** (one screen of charts and numbers that update automatically) in **Power BI** (Microsoft software that turns raw data into visual reports). They tracked 12 **logistics KPIs** (the main numbers used to judge how well goods are being moved and stored). Before this, someone made these reports **manually** (by hand, copying and pasting numbers into Excel).

**Example:** Every Monday, an analyst spent a full day downloading files from different systems, pasting them into Excel, making charts, and emailing them to managers. After your dashboard, the data refreshes on its own, and managers open a link to see the numbers anytime. The 12 KPIs might include on-time delivery %, cost per shipment, **truck fill rate** (how full trucks are when they leave), **transit time** (days from pickup to delivery), and damage claims. Saving 8 hours a week equals one full workday, or about 400 hours a year.

## 2. SAP and TMS data with SQL

**The bullet:** Extracted and modelled SAP and TMS shipment data using SQL, improving cost visibility across 40+ lanes

**What it means:** You **extracted** (pulled out) data from **SAP** (company-wide business software that records orders, invoices, and costs) and **TMS** (Transportation Management System, software that plans and tracks shipments). You then **modelled** it (organized and connected data from different sources so it fits together correctly) using **SQL** (a coding language used to pull and combine data from databases). This improved **cost visibility** (the ability to clearly see where money is being spent) across 40+ **lanes** (specific routes between two locations).

**Example:** TMS knew *which truck* went from Toronto to Calgary and *when*. SAP knew *how much the company paid* for it. But the two systems didn't talk to each other, so nobody could easily answer "What does each route cost us?" You matched the two using the shipment number. Now managers could see that Toronto to Calgary costs $4,200 per truckload, while a similar-distance route costs only $3,500, which raises the question of why.

## 3. Carrier scorecards

**The bullet:** Developed carrier performance scorecards driving on-time delivery from 87% to 94% in two quarters

**What it means:** You created **scorecards** (report cards) for **carriers** (outside trucking companies hired to move goods). These measured how well each one performed. Within **two quarters** (6 months, since one quarter is 3 months), on-time delivery went from 87% to 94%.

**Example:** Out of every 1,000 shipments, 87% on time means 130 were late. At 94%, only 60 were late, so that's 70 fewer late deliveries per 1,000. Your scorecard ranked carriers side by side. One carrier saw it was last in the ranking during a **QBR** (Quarterly Business Review, a regular meeting to discuss a carrier's performance). Knowing that future business depended on their score, they added more drivers on busy days and improved.

**Interview tip:** The carriers improved their own performance, so be clear about *your* part: you built the measurement, spotted the problems, and gave the team the evidence to push carriers. An interviewer may ask, "What exactly did you do to cause that improvement?"

## 4. Python automation

**The bullet:** Automated recurring data pipelines in Python, reducing reconciliation errors by 30% across monthly reporting

**What it means:** You **automated** (made the computer do it instead of a person) **recurring** (repeated every month) **data pipelines** (a series of steps that collects data, cleans it, and delivers it to a report) using **Python** (a programming language). This cut **reconciliation** errors by 30%. Reconciliation means checking that two sets of numbers match.

**Example:** Every month, the team compared 5,000 carrier invoices against shipment records to make sure the company wasn't overcharged. Done by hand, mistakes happened: rows copied twice, dates in different formats, missed lines. Your Python script did the same steps the same way every time. If there used to be 50 errors a month, there were now about 35.

**Interview tip:** Be ready to explain how you counted errors before and after. Numbers like "30%" often get a "how did you measure that?" question.

## 5. Cost-to-serve analysis

**The bullet:** Delivered cost-to-serve analysis identifying $1.2M in annual freight savings opportunities for senior leadership

**What it means:** **Cost-to-serve** is the total cost of delivering to a specific customer, region, or product, including transport, handling, and more. You used this to find $1.2 million per year in possible **freight** (shipping) savings and presented it to **senior leadership** (top executives).

**Example:** You found that one small customer ordered 3 times a week in tiny amounts. Each delivery cost $180, but the order barely made a profit. You also found many **LTL shipments** (Less Than Truckload, where your goods share a truck with other companies' goods, which is more expensive per box) that could be combined into **FTL shipments** (Full Truckload, one full truck for just your goods, which is cheaper per box). Adding up opportunities like these across customers and routes gave $1.2M.

**Interview tip:** "Identifying opportunities" means you found the savings, not necessarily that the company achieved them. Be honest if asked how much was actually saved.

## 6. Process re-engineering

**The bullet:** Re-engineered two planning processes with stakeholders, reducing end-to-end cycle time by 25%

**What it means:** You **re-engineered** (redesigned from the ground up) two planning processes, working with **stakeholders** (the people involved in or affected by the process). This cut **end-to-end cycle time** (the total time from the start of a task to the finish) by 25%.

**Example:** In the load planning process, orders came in, the planner emailed the warehouse to confirm stock, waited for a reply, got a manager's approval, then booked a truck. The whole thing took 4 hours. You ran a **process mapping** session (drawing every step on a whiteboard to spot waste) with planners and warehouse staff. You found the manager approval was a repeat of a check already done, and the email wait could be replaced by a shared stock report. The process dropped to 3 hours, which is 25% faster. The second process would have its own similar story.

## Project: Carrier Performance Scorecard & Freight Cost Dashboard

In one sentence: You built a report that ranks trucking companies and shows where the company is overpaying for shipping.

1. The carrier scorecard

**The bullet:** Designed Power BI scorecard ranking 20 carriers on cost per mile, on-time rate, and damage claims

**What it means:** You made a scorecard (report card) in Power BI (Microsoft software for charts and dashboards) that compares 20 carriers (trucking companies hired to move goods) on three things: cost per mile (how much each carrier charges for every mile driven), on-time rate (% of deliveries that arrive on time), and damage claims (complaints filed when goods arrive broken).

**Example:** Carrier A charges $2.10 per mile, is on time 95% of the time, and has 2 damage claims. Carrier B charges $2.60 per mile, is on time 84% of the time, and has 11 claims. The scorecard makes it obvious that Carrier B costs more and performs worse.

2. The data behind it

**The bullet:** Modelled 100K+ shipment records in SQL Server, automating monthly refresh and eliminating manual consolidation

**What it means:** You organized over 100,000 shipment records in SQL Server (Microsoft's database system for storing and working with large amounts of data). You set it up so the report refreshes (updates with new data) automatically every month, removing manual consolidation (combining data from different files by hand).

**Example:** Before, someone had to collect separate Excel files from each carrier and region, then copy them into one big sheet every month. Now the database pulls everything together on its own, and the dashboard updates without anyone touching it.

3. Finding overspending

**The bullet:** Surfaced lane-level cost anomalies flagging 9% of total freight spend as renegotiation candidates

**What it means:** You found cost anomalies (costs that look unusually high compared to normal) at the lane level (for specific routes, like Toronto to Montreal). These routes made up 9% of total freight spend (money spent on shipping), and you flagged them as renegotiation candidates (routes where the company should ask carriers for a better price).

**Example:** Most carriers charge about $1,800 to go from Toronto to Montreal, but one charges $2,400 for the same trip. You flag it. If the company spends $10M a year on shipping, 9% means about $900,000 worth of shipments may be priced too high.


# Vista Print Experience: Logistics Analyst (Co-op)

**In one sentence:** During a 4-month work term, you used data to help a printing and shipping site deliver on time, plan staff better, and run more smoothly.

### 1. Fixing late deliveries

**The bullet:** Analyzed outbound shipment data in SQL and Excel, identifying routing gaps that reduced late deliveries 15%

**What it means:** You studied **outbound shipment data** (records of orders leaving the warehouse to go to customers) using **SQL** (a coding language to pull data from databases) and Excel. You found **routing gaps** (weak spots in how shipments were assigned to routes or carriers, causing delays), and fixing them cut late deliveries by 15%.

**Example:** You noticed orders going to rural Ontario were often late because they were sent with a carrier that only picked up once a day at 2 PM. Orders packed after 2 PM waited a full extra day. After switching those orders to a carrier with a later pickup, late deliveries dropped from 200 a month to 170, which is 15% fewer.

### 2. Forecasting daily orders

**The bullet:** Built Excel forecasting model for daily order volumes, improving labour and dock planning accuracy by 20%

**What it means:** You built a **forecasting model** (a spreadsheet that predicts future numbers using past data) to estimate how many orders would come in each day. This improved **labour planning** (deciding how many workers to schedule) and **dock planning** (deciding how many truck loading doors and time slots are needed).

**Example:** Before, supervisors guessed staffing, so some Mondays had 10 extra workers standing around while busy Fridays were short-staffed. Your model used past orders, day of the week, and seasonal patterns (like more business card orders in September). If the old guesses were off by 25% on average and yours were off by 20% less than that, planning became noticeably more accurate.

**Interview tip:** Be ready to explain what "accuracy" meant, for example comparing forecasted orders to actual orders each day.

### 3. Documenting workflows

**The bullet:** Mapped and documented three distribution workflows, standardizing procedures for a 25-person operations team

**What it means:** You **mapped** (drew out every step, usually as a flowchart) three **distribution workflows** (the step-by-step processes for getting orders packed and shipped). You then wrote them down so everyone followed the same **standardized procedures** (one agreed way of doing a task).

**Example:** Three shift leads each handled damaged items differently: one reprinted right away, one waited for approval, one just shipped them anyway. You interviewed them, drew the steps, and wrote one clear guide everyone used. New hires could now learn the process from a document instead of relying on whoever trained them.

### 4. Weekly performance reports

**The bullet:** Produced weekly performance reports on throughput, cost per unit, and carrier compliance for site supervisors

**What it means:** Every week you created reports for **site supervisors** (managers running daily operations) covering three things. **Throughput** is how many orders the site processed in a set time. **Cost per unit** is the average cost to process and ship one order. **Carrier compliance** is whether trucking companies followed the agreed rules, like picking up on time.

**Example:** Your weekly report might show 18,000 orders processed, $3.40 cost per order, and one carrier missing 4 of its 20 scheduled pickups. The supervisor uses this to call that carrier and ask why.