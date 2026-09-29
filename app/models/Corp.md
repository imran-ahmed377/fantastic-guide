# Corpay Junior Risk Analyst – Interview Prep Guide

---

## Part 1: Your Core Story

Two things to have ready: they may ask what Exeevo does as a business, so be ready to explain it in one true sentence, and your job start (Sept 2025) overlaps your Master's (ending Dec 2025), so expect "Were you working while studying?" A simple answer: "Yes, I started the role while finishing my final term and graduated in December 2025."

### The Story (structure: Company → Problem → What I Did → Projects → Why Corpay)

**Company:** "At Exeevo, I worked as a Junior Risk Analyst on the risk team in Toronto. Our team was responsible for monitoring client payments, funding, and credit exposure, so the company didn't take losses when clients were late or failed to pay."

**Problem:** "Our team had two main problems. First, we needed to keep a close daily eye on client exposures and unpaid funding, because if a client didn't pay, the company took the loss. Second, our credit reports were built manually in Excel. They took about 3 hours every morning, and sometimes the numbers didn't match the source system, so management didn't fully trust them."

**What I did daily:** "Every morning I checked settlement exposures and outstanding funding positions, followed up on anything unpaid, and escalated items that stayed open more than two days. During the day I reviewed limit exceptions and overdraft requests to make sure the right documents and approvals were in place. I also analyzed client financial statements and transaction patterns in Excel and SQL to support credit reviews."

**Main project:** "My biggest project was moving our legacy Excel reports into Power BI. I rebuilt 8 reports, then validated each one against the source system by comparing record counts and totals. I found and fixed discrepancies like duplicate records caused by a table join and a date filter that was cutting off the last day of the month. As a result, the daily report went from about 3 hours to 30 minutes, and managers started using the dashboard every morning."

**Earlier experience:** "Before that, at Vistaprint, I built Excel and SQL reports to track financial and operational metrics, which gave me a strong base in data validation."

**Why Corpay:** "This role is very close to what I've been doing, but in cross-border payments, which adds FX and multiple currencies. I want to grow in payments risk, and Corpay is a leader in that space."

---

## Part 2: Background Questions

### Q1. Tell me about yourself.
Use the story above, shortened to about 90 seconds: education, current role, main project, why Corpay.

*Follow-ups:* "What did a typical day look like?" (Use the "What I did daily" part.) "What are you most proud of?" (The Power BI migration: 8 reports, 3 hours down to 30 minutes.)

### Q2. Why Corpay, and why this role?
"The responsibilities match my experience almost exactly: settlement exposure, limit exceptions, credit reviews, and moving reports to Power BI. Cross-border payments adds a new layer I want to learn, like FX and international funding. Corpay is a large, growing payments company, so it's a great place to build my risk career."

*Follow-up: "What do you know about our Cross-Border business?"* → "It helps businesses send international payments and manage currency risk. Risk matters because Corpay often commits to paying out before a client's funds arrive."

### Q3. Why did you leave Exeevo?
Pick the one that's true for you:

- **If it was a contract:** "My contract ended in August 2026, and I'm looking for a long-term role focused on payments risk."
- **If you chose to leave:** "I learned a lot there, but I want to work at a company where payments and risk are the core business, so I can grow faster in this field."

### Q4. Where do you see yourself in 2–3 years?
"Strong in credit and settlement risk, handling more complex reviews on my own, and helping improve risk reporting and processes."

---

## Part 3: Role-Specific Risk Questions (most important)

### Q5. What is settlement exposure?
"It's the money at risk when we've paid, or committed to pay, on a client's behalf before the client's funds have arrived. If the client doesn't fund, we take the loss."

*Follow-up: "How would you monitor it?"* → "Run a daily report of each client's unsettled amount against their limit. Flag anyone above 80% or over the limit, chase outstanding funding, and escalate items that are aging."

### Q6. Walk me through how you'd review a settlement limit exception.
Remember five steps: **Why, History, Financials, Documents, Recommend.**

"First, I'd find out why the client needs the extra limit: one-off large payment or a trend. Second, I'd check their history: do they fund on time, any bounced payments? Third, I'd look at their financial strength and current utilization. Fourth, I'd confirm the documentation and the right approver are in place. Finally, I'd write a short recommendation (approve, decline, or approve with conditions) and escalate if needed."

*Example to mention:* "For example, a client with a $500,000 limit asked for a one-time increase to $650,000 for a large supplier payment. They had funded on time for 12 months with no bounces, so I recommended approving it for 5 business days only, with manager sign-off."

*Follow-up: "Sales says it's urgent and wants approval now."* → "I understand the client pressure, so I'd work on it right away and tell Sales exactly what's missing. But I wouldn't skip the approval step, because that's the control that protects us."

### Q7. What is an early release request? What are the risks?
"It's when we release a payment to the beneficiary before the client's funds have fully cleared. The risk is that the client never funds, and we've already paid out. I'd check proof of funding like a wire confirmation, the client's payment history, the amount compared to their limit, and make sure it has proper approval."

### Q8. What is a temporary overdraft?
"It's allowing a client's balance to go negative for a short time. I'd check the reason, amount, how long it lasts, and the repayment date, get it approved, and then follow up to make sure it's actually cleared on time."

### Q9. A client's payment bounces. What do you do?
"First, confirm the bounce and the reason, like insufficient funds. Then notify the relevant teams (Operations, Sales) so they can contact the client, and consider holding further releases until it's resolved. I'd track it until it's fixed and escalate if it ages. Repeated bounces are a red flag, and I'd recommend reviewing the client's limit."

### Q10. What are CLIAB balances?
This is likely Corpay's internal term for client liability balances (amounts clients owe that haven't been settled). If you haven't used this exact term, it's safe to say:

"I understand it as client liability balances, amounts clients owe us. I'd want to learn exactly how Corpay defines and tracks it, but the monitoring approach would be the same: track, age, follow up, escalate."

### Q11. When would you escalate an issue?
"When the amount is large, when an item stays unresolved past our timeline, when I see a pattern like repeated bounces, or when a client stops responding. I'd rather escalate early with clear facts than late."

---

## Part 4: Financial Statement Analysis

### Q12. What ratios would you look at in a credit review?
Remember **LLPCW**: Liquidity, Leverage, Profitability, Cash flow, Working capital.

| Area | Ratio | Formula | Good sign |
|---|---|---|---|
| Liquidity | Current ratio | Current Assets ÷ Current Liabilities | Above 1 |
| Liquidity | Quick ratio | (Current Assets − Inventory) ÷ Current Liabilities | Above 1 |
| Leverage | Debt-to-equity | Total Debt ÷ Equity | Lower is safer |
| Profitability | Net margin | Net Income ÷ Revenue | Positive, stable |
| Cash flow | Operating cash flow | From cash flow statement | Positive |
| Working capital | Working capital | Current Assets − Current Liabilities | Positive |

*Quick example:* "If a company has $2M current assets and $1M current liabilities, the current ratio is 2.0 and working capital is $1M. That's healthy."

*Follow-up: "What are red flags?"* → "Falling revenue, negative operating cash flow, rising debt, current ratio below 1, and receivables growing faster than sales."

### Q13. A company is profitable but has low cash. Why?
"Profit isn't cash. Their cash may be stuck in unpaid customer invoices or inventory. That's why I always check the cash flow statement, not just the income statement."

### Q14. How would you structure a credit review or exception summary?
Remember **4 parts**: "Overview of the client and the request, key risks, mitigating factors, and my recommendation. Short and clear so a manager can decide quickly."

*Example:* "Client requests a limit increase from $500K to $650K for one supplier payment. Risk: utilization would reach 100%. Mitigants: 12 months of on-time funding, no bounces, current ratio of 1.8. Recommendation: approve for 5 business days with manager sign-off."

---

## Part 5: Technical Questions with Simple Code

### SQL (they said "basic SQL," so keep it simple)

#### Q15. Find clients who are over their limit.
```sql
SELECT client_id, client_name, exposure, settlement_limit
FROM client_exposure
WHERE exposure > settlement_limit;
```

#### Q16. Total unsettled exposure per client, highest first.
```sql
SELECT client_id, SUM(amount) AS total_exposure
FROM transactions
WHERE status = 'UNSETTLED'
GROUP BY client_id
ORDER BY total_exposure DESC;
```

#### Q17. Add a risk flag based on limit utilization.
```sql
SELECT client_id, exposure, settlement_limit,
       exposure * 100.0 / settlement_limit AS utilization_pct,
       CASE
           WHEN exposure > settlement_limit THEN 'BREACH'
           WHEN exposure > 0.8 * settlement_limit THEN 'WATCH'
           ELSE 'OK'
       END AS risk_flag
FROM client_exposure;
```

#### Q18. Clients with 2 or more bounced payments in the last 30 days.
```sql
SELECT client_id, COUNT(*) AS bounced_count, SUM(amount) AS bounced_amount
FROM payments
WHERE status = 'BOUNCED'
  AND payment_date >= DATEADD(day, -30, GETDATE())
GROUP BY client_id
HAVING COUNT(*) >= 2;
```

#### Q19. How do you validate a report against the source system?
Two simple checks. First, compare totals:
```sql
SELECT 'Source' AS system, COUNT(*) AS records, SUM(amount) AS total
FROM source_transactions WHERE txn_date = '2026-09-28'
UNION ALL
SELECT 'Report', COUNT(*), SUM(amount)
FROM report_transactions WHERE txn_date = '2026-09-28';
```

Second, find records missing from the report:
```sql
SELECT s.transaction_id
FROM source_transactions s
LEFT JOIN report_transactions r
       ON s.transaction_id = r.transaction_id
WHERE r.transaction_id IS NULL;
```

#### Q20. Find duplicate transactions.
```sql
SELECT transaction_id, COUNT(*)
FROM transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;
```

#### Likely SQL follow-ups (one-line answers)
- **WHERE vs HAVING?** WHERE filters rows before grouping; HAVING filters groups after.
- **INNER JOIN vs LEFT JOIN?** INNER keeps only matches; LEFT keeps everything from the left table, even without a match.
- **Why use LEFT JOIN for validation?** It shows records that exist in the source but are missing from the report.

### Excel

#### Q21. Which Excel functions do you use most?
```
Look up a client's limit:
=XLOOKUP(A2, Limits!A:A, Limits!C:C, "Not found")
=VLOOKUP(A2, Limits!A:C, 3, FALSE)

Total unsettled exposure for a client:
=SUMIFS(Txn!D:D, Txn!A:A, A2, Txn!E:E, "Unsettled")

Count bounced payments for a client:
=COUNTIFS(Pay!A:A, A2, Pay!C:C, "Bounced")

Risk flag (C = exposure, D = limit):
=IF(C2>D2, "BREACH", IF(C2>0.8*D2, "WATCH", "OK"))

Utilization % without errors:
=IFERROR(C2/D2, 0)
```

*Follow-up: "XLOOKUP vs VLOOKUP?"* → "XLOOKUP can look left, defaults to exact match, and doesn't break when you insert columns."

*Follow-up: "How would you use a pivot table here?"* → "Put Client in Rows, Exposure in Values as a sum, and Status as a filter, to see exposure by client quickly."

### Power BI

#### Q22. How do you validate a Power BI report?
Remember **4 checks**: "Compare counts and totals to the source for the same date and filters. Check the report filters and slicers. Check table relationships for duplicates. Confirm the data refresh time."

*Follow-up: "You find a mismatch. What next?"* → "I narrow it down by date, then by client, until I find the exact records that differ. Then I fix the cause, document it, and add a check so it doesn't happen again."

#### Q23. Write a simple measure.
```
Utilization % = DIVIDE(SUM(Exposure[Amount]), SUM(Limits[Limit]), 0)

Breach Count = CALCULATE(COUNTROWS(Clients), Clients[Exposure] > Clients[Limit])
```

"DIVIDE is safer than a plain slash because it handles divide-by-zero."

---

## Part 6: Behavioral Questions (answer with Situation → Action → Result)

### Q24. Tell me about a time you found a data discrepancy.
"During the Power BI migration, the dashboard's total exposure was about $48,000 higher than the source system. I compared counts by date, then by client, and found that a join between the transactions table and the client table was creating duplicate rows for clients with two account records. I fixed the relationship, re-validated, and added a daily count check to our process. After that, the reports matched every day."

### Q25. How do you handle competing priorities?
"I do time-sensitive risk items first, like daily exposure and funding follow-ups, because delays can cost money. Then reports, then projects. For example, one morning I had a month-end report due and three unresolved funding items. I cleared the funding follow-ups first, told my manager the report would be two hours later, and delivered it the same day."

### Q26. Tell me about working with another team to solve a problem.
"A client's $25,000 payment bounced because of insufficient funds. I worked with Operations to confirm the details, with Sales to contact the client, and with Compliance to make sure we followed procedure. We held further releases for that client, the client re-sent the funds within two days, and I tracked it until it was fully closed."

### Q27. Tell me about a mistake you made.
"I once sent a daily credit report with the previous day's date filter still applied. I noticed within 15 minutes because the totals looked very different from normal. I sent a corrected version right away and told my manager what happened. Since then, I always reconcile report totals against the source before sending."

### Q28. Someone pushes you to approve something without documents. What do you do?
"I stay polite but firm. I explain what's missing and why it matters, help them get it quickly, and escalate to my manager if there's still pressure."

### Q29. What's your weakness?
"Sometimes I spend too long double-checking details. Now I set a time limit and use checklists, so I stay accurate without slowing down."

---

## Part 7: Questions to Ask Them (pick 2)

1. "What does a typical day look like for this role in the first few months?"
2. "Which reports are you currently moving to Power BI, and what's the biggest challenge there?"
3. "How would you measure success for this role after six months?"

---

## Quick Memory Cheat Sheet

- **Limit exception:** Why, History, Financials, Documents, Recommend
- **Ratios:** LLPCW (Liquidity, Leverage, Profitability, Cash flow, Working capital)
- **Credit summary:** Overview, Risks, Mitigants, Recommendation
- **Power BI validation:** Totals, Filters, Relationships, Refresh
- **Escalate when:** Big amount, Aging, Pattern, No response
- **Your numbers:** 8 reports, 3 hours → 30 minutes, $48K mismatch fixed, $25K bounce resolved in 2 days
- **Key line:** "Profit isn't cash."