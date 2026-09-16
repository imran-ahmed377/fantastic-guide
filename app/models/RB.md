# Table of Contents
- [Intro](#intro)
- [AI Engineer (Exeevo Inc) — What the Job Actually Looks Like](#ai-engineer-exeevo-inc-—-what-the-job-actually-looks-like)
  - [1. The Role at a Glance](#1-the-role-at-a-glance)
  - [2. Regression Testing & Test Coverage](#2-regression-testing--test-coverage)
  - [3. AI-Driven Test Optimization](#3-ai-driven-test-optimization)
  - [4. CI/CD Pipeline with Jenkins](#4-cicd-pipeline-with-jenkins)
  - [5. Data Drift Monitoring](#5-data-drift-monitoring)
  - [6. Test Data Management](#6-test-data-management)
  - [7. Cross-Functional Collaboration](#7-cross-functional-collaboration)
  - [8. Interview Prep](#8-interview-prep)



- [Quality Assurance Intern (Vistaprint) — What the Job Actually Looks Like](#quality-assurance-intern-vistaprint-—-what-the-job-actually-looks-like)
- [1. The Role at a Glance](#1-the-role-at-a-glance-1)
  - [2. Selenium + Java Automation](#2-selenium--java-automation)
  - [3. Flaky Tests (The Real Daily Pain)](#3-flaky-tests-the-real-daily-pain)
  - [4. Validating ML Model Outputs](#4-validating-ml-model-outputs)
  - [5. ETL Data Validation in Python](#5-etl-data-validation-in-python)
  - [6. CI/CD Pipeline Monitoring](#6-cicd-pipeline-monitoring)
  - [7. Interview Prep](#7-interview-prep)

-
# Intro

Thank you for giving me the opportunity. I am Imran Ahmed, I have been working as an AI Engineer at Exeevo. I have developed end to end AI solutions and testing framework. 


# AI Engineer (Exeevo Inc) — What the Job Actually Looks Like

---

## 1. The Role at a Glance

### A typical day

| Time | What you're doing |
|---|---|
| Morning | Check dashboards. Did the nightly regression suite pass? Did any drift alert fire overnight? Triage: real problem or noisy alert? |
| Mid-morning | Standup. Say what you're automating and what's blocked. |
| Rest of day | Write tests for new features, fix a Jenkins job that's timing out, ask data scientists "what accuracy do I fail the build at?" |

The recurring theme: **you are the person who decides what "broken" means for something that doesn't have a clean right answer.**

---

## 2. Regression Testing & Test Coverage

> *Resume bullet: Automated regression test suite with PyTest, boosting test coverage from 65% to 90%*

### What is a regression suite?

"Regression" means: something that used to work has gone backwards.

Imagine your app has a login page. It works. Three months later a developer adds "Sign in with Google" and accidentally breaks regular email login. That's a regression — an old feature broke because of new code.

A regression suite is the pile of tests you keep around **forever** that re-check all the old stuff still works:

```python
def test_email_login_works():        # written in January
def test_password_reset_works():     # written in February
def test_google_login_works():       # written in March
```

Nobody deletes these. They run on every change, forever. When your March feature breaks January's login, the January test catches it.

It's not a special kind of test — it's just the accumulated collection of tests, run repeatedly.

### What a regression test looks like

```python
def test_contact_search_returns_results():
    results = search_contacts("Smith")
    assert len(results) > 0
    assert all("Smith" in r.name for r in results)
```

### What is test coverage?

**Coverage = what percentage of your code lines actually get executed when your tests run.**

Say this is your function:

```python
def get_discount(customer):
    if customer.is_premium:          # line 1
        return 0.20                  # line 2
    elif customer.orders > 10:       # line 3
        return 0.10                  # line 4
    else:                            # line 5
        return 0.0                   # line 6
```

And this is your only test:

```python
def test_premium_discount():
    assert get_discount(premium_customer) == 0.20
```

Lines 1 and 2 executed. Lines 3–6 never ran. **Coverage: 33%.**

### Measuring it with pytest-cov

```bash
$ pytest --cov=myapp

Name         Stmts   Miss  Cover   Missing
------------------------------------------
discount.py      6      4    33%   3-6
```

That `Missing` column is your to-do list. It literally tells you which lines nothing tested.

So you write two more tests:

```python
def test_loyal_customer_discount():
    assert get_discount(customer_with_15_orders) == 0.10

def test_new_customer_no_discount():
    assert get_discount(brand_new_customer) == 0.0
```

Now 100%.

### Why 65% → 90% takes months

You do that across a codebase with thousands of functions — read the Missing column, figure out what state a customer has to be in to reach line 47, build that state, write the assertion. Repeat a few hundred times.

### Important caveat

**High coverage does not mean good tests.** This gets 100% coverage and tests nothing:

```python
def test_discount():
    get_discount(premium_customer)    # no assert! just ran the code
```

Coverage tells you *what ran*, not whether you checked the result was correct.

---

## 3. AI-Driven Test Optimization

> *Resume bullet: Designed AI-driven test optimization framework in Python, reducing manual testing effort by 30%*

### The problem

You have 2,000 tests and the full suite takes 3 hours. A developer changes one file. Running all 2,000 tests is wasteful.

### The solution

Look at which files changed and pick only the tests that touch that code:

```python
changed_files = get_git_diff()
tests_to_run = predict_relevant_tests(changed_files)
# 2000 tests -> 180 tests, 3 hours -> 15 minutes
```

### Where the "AI" part comes from

Your company has years of CI runs stored. Each run recorded: what files changed, which tests ran, which tests failed. So you build a table:

| Changed file | Test | Did it fail? |
|---|---|---|
| `payment.py` | `test_checkout` | Yes |
| `payment.py` | `test_checkout` | Yes |
| `payment.py` | `test_login` | No |
| `payment.py` | `test_login` | No |
| `login.py` | `test_login` | Yes |

After thousands of rows, a pattern emerges: when `payment.py` changes, `test_checkout` fails 40% of the time and `test_login` fails 0.1% of the time.

Now train a model on that table:

```python
model.fit(X=changed_files, y=test_failed)

# New commit touches payment.py
predictions = model.predict_proba(["payment.py"])
# test_checkout: 0.40 probability of failing
# test_login:    0.001 probability of failing

tests_to_run = [t for t in all_tests if predictions[t] > 0.05]
```

Run 180 tests instead of 2,000.

### Reality check

Plenty of teams do a simpler version with **no ML at all** — just a static map of "this folder → these tests." The ML version learns the mapping instead of you maintaining it by hand.

### The daily work

Tuning it so it doesn't skip a test that would have caught a real bug.

---

## 4. CI/CD Pipeline with Jenkins

> *Resume bullet: Integrated automated validation into CI/CD pipeline with Jenkins, cutting deployment cycle time by 25%*

### How a Jenkins pipeline works

A pipeline is a list of stages that run top to bottom. **If a stage fails, everything after it never runs.** That's the whole mechanism.

```groovy
pipeline {
    stages {
        stage('Build') {
            steps { sh 'python -m build' }
        }
        stage('Test') {
            steps { sh 'pytest tests/' }              // ← 3 tests fail here
        }
        stage('Deploy') {
            steps { sh './deploy_to_production.sh' }  // ← never runs
        }
    }
}
```

### Why does it stop?

Because `pytest` returns a **non-zero exit code** when tests fail. Jenkins sees non-zero, marks the stage failed, aborts the pipeline.

Prove it to yourself in a terminal:

```bash
$ pytest tests/
$ echo $?
1          # non-zero = failure
```

### What happens next

The build turns red in Jenkins, a Slack message fires, and production still has yesterday's working code on it. Nobody had to intervene — the broken code simply never made it out.

### A fuller validation stage

```groovy
stage('Validate') {
    steps {
        sh 'pytest tests/ --junitxml=results.xml'
        sh 'python check_model_metrics.py'
    }
}
```

### The daily work

You own this pipeline. When it goes red at 4pm on a Friday, you're the one figuring out whether it's a real failure or infrastructure flakiness.

---

## 5. Data Drift Monitoring

> *Resume bullet: Built data drift monitoring system for ML models, improving prediction reliability by 20%*

### What is drift?

A model was trained on data from a certain period. Over time, real-world data shifts, and the model quietly gets worse. **Nothing crashes. There's no error message.**

Classic example: a spam filter trained before scammers started using emoji in subject lines. It was 95% accurate. Now it's 70% accurate and nobody noticed because nothing crashed.

### The basic idea

```python
# Training data: average customer age was 42
# This week's data: average customer age is 58
# -> something changed, alert the team

drift_score = compare_distributions(training_data, live_data)
if drift_score > THRESHOLD:
    send_alert()
```

### The actual libraries

`compare_distributions()` above is pseudocode. Here's what you'd really use.

**SciPy** — the raw statistics, if you want to write it yourself:

```python
from scipy.stats import ks_2samp

statistic, p_value = ks_2samp(training_ages, live_ages)
if p_value < 0.05:
    print("These two samples come from different distributions — drift!")
```

That's the **Kolmogorov-Smirnov test**. It answers one question: do these two sets of numbers look like they came from the same source? Low p-value means no.

For categorical data (country, product type) you'd use a **chi-squared test** instead, also in SciPy. Another common measure is **PSI (Population Stability Index)**, which you often just write by hand in ~10 lines of NumPy.

**Evidently** — higher level, does everything for you:

```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=training_df, current_data=last_week_df)
report.save_html("drift_report.html")
```

Open the HTML and it tells you: "customer_age drifted, transaction_amount drifted, everything else is fine."

> SciPy is the engine. Evidently is the car built around it.

### Tool landscape

| Tool | What it is |
|---|---|
| **Evidently AI** | Open source Python library. Most common starting point. Generates HTML drift reports. |
| **NannyML** | Open source. Estimates performance drop when you don't have labels yet. |
| **Alibi Detect** | Open source. More statistical / research-flavored. |
| **Arize, Fiddler, WhyLabs** | Paid platforms — dashboards, alerting, hosted. |
| **MLflow / SageMaker Model Monitor** | Built into bigger ML platforms. |

### The daily work

Mostly threshold tuning. Set it too sensitive and you get alerts every day and everyone ignores them. Too loose and you miss the real drift.

---

## 6. Test Data Management

> *Resume bullet: Established test data management protocols, increasing data quality accuracy by 22%*

Sounds boring, matters a lot. Exeevo works in life sciences, so their data involves healthcare and pharma customers — **you cannot just copy production data into a test environment.**

So you build the tooling that generates or anonymizes test data:

- Fake but realistic customer records
- Edge cases on purpose: empty fields, weird characters, dates in 1900
- The **same dataset every time**, so a test failure means the code changed, not the data

### The daily work

Someone says "my test passed yesterday and failed today" and you discover their test data got stale.

---

## 7. Cross-Functional Collaboration

> *Resume bullet: Collaborated with cross-functional teams to translate requirements into automation strategy, accelerating delivery by 18%*

This is the meetings bullet.

A product manager says *"users should be able to filter by region."* You translate that into questions:

- What do we test?
- What happens with no results?
- What about a user with no region permissions?
- What does the model do with a region it's never seen?

### The daily work

Asking annoying clarifying questions **before** code gets written, which is cheaper than finding the gap after release.

---

## 8. Interview Prep

The strongest story you can tell from this role is a **drift story**:

> *"The model looked fine — accuracy on the test set was unchanged — but the live data had shifted and predictions were degrading in production. Here's how we caught it."*

That demonstrates you understand something most candidates don't: **a model can fail silently.**

Have one concrete bug story ready too — what the bug was, how you caught it, what would have happened if you hadn't. That lands better than the percentages on the resume.



---


# Quality Assurance Intern (Vistaprint) — What the Job Actually Looks Like

---

## 1. The Role at a Glance

Vistaprint sells custom printed products — business cards, mugs, t-shirts, signs. A customer picks a design, uploads a logo, types their text, and orders it.

Your job is making sure that flow doesn't break, and that nothing wrong gets printed and mailed to a real person.

### A typical day

| Time | What you're doing |
|---|---|
| Morning | Check the overnight test run. Some tests failed. **Triage:** is this a real bug, or did the test break because someone changed a button's ID? Usually the latter. Fix the test, re-run, move on. |
| 10:00 | Standup. Say what you're testing and what's blocked. |
| Mid-morning | Pick up tickets. A developer merged a new feature — you write tests for it. |
| Afternoon | Writing test scripts, filing bugs in Jira, chasing developers on Slack: *"is this expected behavior or a bug?"* |

**Most of QA is three things: triage, writing tests, and asking clarifying questions.**

### What "triage" actually means

You open the failed test report and ask, in this order:

1. Did the app break? → **real bug**, file it in Jira
2. Did the test break? → someone renamed a button, **fix the test**
3. Did neither break? → **flaky test**, it failed for no good reason (see Section 3)

Roughly 70% of morning failures are #2 and #3. That surprises people.

---

## 2. Selenium + Java Automation

> *Resume bullet: Developed automated test scripts using Selenium and Java, reducing manual testing time by 35%*

### What is Selenium?

Selenium is a library that **controls a real browser with code**. It opens Chrome, clicks buttons, types into boxes, and reads what's on the page — exactly like a human, but in 30 seconds instead of 20 minutes.

### The problem it solves

Before automation, a human clicks through the whole checkout flow every release:

```
pick a business card design → upload logo → enter text → add to cart → checkout
```

That takes 20 minutes. And you have to do it for every browser, every release, forever.

### The same flow as code

```java
driver.get("https://vistaprint.ca/business-cards");
driver.findElement(By.id("design-042")).click();
driver.findElement(By.id("text-line-1")).sendKeys("Jane Smith");
driver.findElement(By.id("add-to-cart")).click();

assertEquals("1", driver.findElement(By.id("cart-count")).getText());
```

Line by line:

| Code | What it does |
|---|---|
| `driver.get(...)` | Opens the page |
| `findElement(By.id(...))` | Finds a thing on the page |
| `.click()` | Clicks it |
| `.sendKeys("Jane Smith")` | Types into it |
| `assertEquals(...)` | **Checks the result is right** — this is the actual test |

The last line is the important one. Everything above it is just setup. If the cart doesn't say "1", the test fails.

The "35% reduction" is just: these flows used to be manual, now they're not.

### How you find things on a page — locators

Selenium needs a way to point at a button. Browsers let you inspect the HTML:

```html
<button id="add-to-cart" class="btn btn-primary">Add to Cart</button>
```

So you can find it several ways:

```java
By.id("add-to-cart")                          // best — IDs are unique and stable
By.className("btn-primary")                   // risky — many buttons share classes
By.xpath("//button[text()='Add to Cart']")    // works, but breaks if text changes
By.cssSelector("button.btn-primary")          // common alternative
```

**Prefer `By.id`.** Most of your broken-test mornings come from using a fragile locator that a developer accidentally changed.

---

## 3. Flaky Tests (The Real Daily Pain)

Writing the test is the easy part. The hard part is that the test **passes 9 times and fails once** — for no reason you can see.

### Why it happens

Selenium runs fast. The browser doesn't. Your code clicks "Add to Cart" 50 milliseconds before the button actually appears on screen, and the test explodes.

### The bad fix

```java
Thread.sleep(2000);   // just wait 2 seconds and hope
driver.findElement(By.id("add-to-cart")).click();
```

Two problems: it's **always** slow (even when the page loaded instantly), and 2 seconds still isn't enough on a bad day. Multiply by 200 tests and your suite takes an hour for no reason.

### The good fix — explicit waits

```java
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

WebElement cartButton = wait.until(
    ExpectedConditions.elementToBeClickable(By.id("add-to-cart"))
);
cartButton.click();
```

This means: *"keep checking for up to 10 seconds until the button is actually clickable, then continue immediately."*

Fast page? Continues in 100ms. Slow page? Waits as long as it needs. This one change fixes most flakiness.

### Keeping tests maintainable — the Page Object Model

If 40 tests all contain `By.id("add-to-cart")` and a developer renames that button, you edit 40 files.

Instead, put the locators in one class per page:

```java
public class CartPage {
    private WebDriver driver;

    private By addToCart = By.id("add-to-cart");
    private By cartCount = By.id("cart-count");

    public void addItem() {
        driver.findElement(addToCart).click();
    }

    public String getItemCount() {
        return driver.findElement(cartCount).getText();
    }
}
```

Now your test reads like English:

```java
@Test
public void addingItemUpdatesCart() {
    cartPage.addItem();
    assertEquals("1", cartPage.getItemCount());
}
```

When the button ID changes, you fix **one line in one file**. This is the single most useful pattern in UI automation.

---

## 4. Validating ML Model Outputs

> *Resume bullet: Validated ML model outputs against production data, decreasing defect leakage by 15%*

### What models does Vistaprint have?

Things like:

- **Design recommendation** — "customers like you also bought this template"
- **Image quality check** — is this uploaded logo sharp enough to actually print?

### Why normal testing doesn't work here

Normal code is deterministic. `2 + 2` is always `4`, so you can write `assertEquals(4, add(2,2))`.

A model is **probabilistic**. It outputs "87% confident this logo is print-quality." There's no single right answer to assert on. So you test differently.

### Approach 1 — test the obvious boundaries

Feed it cases where any reasonable model must agree with you:

```python
def test_blurry_logo_is_rejected():
    result = quality_model.check("tests/images/blurry_100x100.png")
    assert result.approved == False      # a 100x100 logo can NEVER print well

def test_high_res_logo_is_approved():
    result = quality_model.check("tests/images/sharp_4000x4000.png")
    assert result.approved == True
```

If the blurry one gets approved, a real customer receives a box of 500 blurry business cards. That's the bug you're preventing.

### Approach 2 — check the overall behavior hasn't shifted

Run a big batch of real production images through the model and compare to last release:

```python
results = [quality_model.check(img) for img in production_sample]  # 1,000 images
approval_rate = sum(r.approved for r in results) / len(results)

# Last release: 92%
assert 0.88 <= approval_rate <= 0.96, f"Approval rate jumped to {approval_rate}"
```

If it drops from 92% to 60%, nothing crashed — but something broke. Maybe a new version of the model shipped, maybe the image preprocessing changed. Either way you caught it before customers did.

### What "defect leakage" means

> **Defect leakage = bugs that escaped QA and were found by customers instead.**

```
Bugs found by QA:        45
Bugs found by customers:  8     ← leakage
Leakage rate = 8 / 53 = 15%
```

Catching the blurry-logo case in testing instead of in a customer's mailbox is exactly how that number goes down.

---

## 5. ETL Data Validation in Python

> *Resume bullet: Built ETL data validation checks with Python, improving data pipeline accuracy by 20%*

### What is ETL?

**E**xtract → **T**ransform → **L**oad. Data gets pulled out of one place, reshaped, and dropped into another.

```
Orders database  →  [clean it up, join tables, calculate totals]  →  Analytics warehouse
```

Business teams then build dashboards on the warehouse: revenue this month, top-selling products, etc.

### Why it needs testing

**Data pipelines fail silently.** No error, no crash, no red alert. The job says "success." The dashboard just quietly shows wrong numbers, and nobody notices for three weeks — until someone makes a business decision based on them.

### The checks you write

These run automatically after every load:

```python
# No duplicates — an order counted twice inflates revenue
assert orders_df["order_id"].is_unique

# No negative prices — usually means a bad currency conversion
assert orders_df["price"].min() >= 0

# No missing customers — a broken join creates orphan rows
assert orders_df["customer_id"].isna().sum() == 0

# Nothing lost in transit — 10,000 rows in should be 10,000 rows out
assert len(orders_df) == source_row_count
```

### A more realistic version

Instead of crashing on the first failure, collect everything and report:

```python
def validate_orders(df, source_row_count):
    failures = []

    if not df["order_id"].is_unique:
        dupes = df["order_id"].duplicated().sum()
        failures.append(f"{dupes} duplicate order IDs")

    if df["price"].min() < 0:
        failures.append(f"negative price found: {df['price'].min()}")

    if len(df) != source_row_count:
        failures.append(f"row mismatch: expected {source_row_count}, got {len(df)}")

    if failures:
        send_slack_alert(failures)
        raise ValueError("Validation failed:\n" + "\n".join(failures))

    print("All checks passed")
```

Now when it trips, someone gets a Slack message the same day instead of a confused executive three weeks later.

### Common check categories

| Category | Example |
|---|---|
| **Uniqueness** | No duplicate order IDs |
| **Completeness** | No nulls in required columns |
| **Range** | Prices ≥ 0, dates not in the future |
| **Row count** | Source rows == destination rows |
| **Referential** | Every `customer_id` exists in the customers table |
| **Freshness** | Most recent record is from today, not last Tuesday |

> Libraries like **Great Expectations** and **Pandera** do all this in a more structured way, but plain `assert` statements are how most teams start.

---

## 6. CI/CD Pipeline Monitoring

> *Resume bullet: Monitored application performance in CI/CD pipeline, reducing post-release incidents by 12%*

### Wiring your tests into the pipeline

Your Selenium tests are useless sitting on your laptop. They need to run automatically on every code change:

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Selenium suite
        run: mvn test
```

### How "the merge is blocked" works

`mvn test` returns a **non-zero exit code** when tests fail. The pipeline sees non-zero, marks the job red, and GitHub refuses to let the pull request merge.

You can see this yourself:

```bash
$ mvn test
$ echo $?
1          # non-zero = failure
```

Nobody has to intervene. Broken code simply can't get in.

### Your role in it

You're the person who gets pinged when the pipeline goes red. Your job is deciding:

- **Test is wrong** → you fix the test
- **Code is wrong** → you push it back to the developer with a Jira ticket
- **Neither** → it's flaky, go back to Section 3

### The "performance monitoring" part

This usually means you added checks that fail the build when a change makes things slow:

```java
@Test
public void homepageLoadsUnderThreeSeconds() {
    long start = System.currentTimeMillis();
    driver.get("https://vistaprint.ca");

    long loadTime = System.currentTimeMillis() - start;
    assertTrue(loadTime < 3000, "Homepage took " + loadTime + "ms");
}
```

Or at the API level:

```python
def test_search_api_is_fast():
    start = time.time()
    response = requests.get("https://api.vistaprint.ca/search?q=business+cards")
    elapsed = (time.time() - start) * 1000

    assert response.status_code == 200
    assert elapsed < 500, f"Search API took {elapsed:.0f}ms"
```

**Why this matters:** slow pages lose sales. A developer adds an innocent-looking database query, the product page goes from 1s to 4s, and conversion quietly drops. This check catches it before release instead of after.

"Post-release incidents" are problems discovered in production after shipping. Catching slowdowns and broken flows in the pipeline is how you get 12% fewer of them.

---

## 7. Interview Prep

The thing interviewers actually probe is:

> **"Tell me about a bug you found and how."**

Have one concrete story ready with four parts:

1. **What the bug was** — "the image quality model was approving logos under 300 DPI"
2. **How you caught it** — "I added boundary tests with deliberately low-res images"
3. **What would have happened** — "customers would have received blurry printed cards and requested refunds"
4. **What changed after** — "we added a resolution floor and a regression test for it"

That lands far better than reciting the percentages on your resume. Nobody follows up on "35%." Everybody follows up on a real bug.

### Likely follow-up questions

| They ask | What they want to hear |
|---|---|
| "How do you handle flaky tests?" | Explicit waits, not `Thread.sleep`. Quarantine and fix rather than re-run until green. |
| "How do you test something with no exact right answer?" | Boundary cases + aggregate behavior comparison (Section 4). |
| "What's the difference between a test failure and a bug?" | Triage: app broke vs. test broke vs. flaky. |
| "What would you test on a checkout page?" | Happy path, empty cart, invalid card, expired session, quantity 0, quantity 9999. |



---



# RBC — AI Quality Engineer
## Interview Question Bank (30-min screen)

---

## 1. Opening

**Q: Tell me about yourself.**

- Follow-up: Why did you leave Exeevo? / Are you currently working?
- Follow-up: Walk me through your Master's — what did you focus on?
- Follow-up: What kind of role are you looking for next?

---

## 2. Test Optimization Framework ⭐

**Q: Walk me through the AI-driven test optimization framework you built.**

- Follow-up: What features did the model use?
- Follow-up: What if your model skips a test that would have caught a real bug?
- Follow-up: How did you measure the 30% reduction?
- Follow-up: How often did you retrain the model?
- Follow-up: How would this scale to a codebase 100x larger?

---

## 3. Data Drift ⭐

**Q: What is data drift, and how did you detect it?**

- Follow-up: What's the difference between data drift and concept drift?
- Follow-up: Which statistical tests did you use, and why those?
- Follow-up: How did you set the alert thresholds?
- Follow-up: What did you do when an alert fired?
- Follow-up: How did you avoid alert fatigue / false positives?
- Follow-up: How did you measure the 20% reliability improvement?

---

## 4. AI Testing Fundamentals

**Q: How is testing an AI system different from testing traditional software?**

- Follow-up: How do you write an assertion when the output isn't deterministic?
- Follow-up: What's a metamorphic or invariance test? Give an example.
- Follow-up: How do you test for bias or fairness in a model?
- Follow-up: What does "test the data, not just the code" mean in practice?

---

## 5. LLM Evaluation ⭐ (gap area — prepare carefully)

**Q: How would you test an LLM-powered feature?**

- Follow-up: What is a golden dataset and how do you build one?
- Follow-up: What is LLM-as-judge? How do you know the judge is right?
- Follow-up: How do you regression-test a prompt change?
- Follow-up: How would you test for prompt injection or PII leakage?
- Follow-up: How do you evaluate a RAG system specifically?
- Follow-up: How would you detect hallucination at scale?

---

## 6. Test Data Management

**Q: Tell me about the test data management protocols you established.**

- Follow-up: How did you handle sensitive or personal data?
- Follow-up: Synthetic data vs. masked production data — when do you use each?
- Follow-up: How did you keep tests independent so they could run in parallel?
- Follow-up: What is Great Expectations and how did you use it?
- Follow-up: How did you version test data alongside test code?

---

## 7. CI/CD & Pipelines

**Q: Walk me through how validation fits into your CI/CD pipeline.**

- Follow-up: What were the actual stages, in order?
- Follow-up: What fails the build vs. what just warns?
- Follow-up: How did you set the model performance gate threshold?
- Follow-up: How did you keep the pipeline from getting slow or flaky?
- Follow-up: How did you handle flaky tests?
- Follow-up: Jenkins vs. GitHub Actions — why did you use which?
- Follow-up: How did Docker and Kubernetes fit in?

---

## 8. Metrics & Critical Thinking

**Q: You took coverage from 65% to 90%. Is coverage a good measure of quality?**

- Follow-up: What metrics would you actually report to leadership?
- Follow-up: How do you show ROI on a testing investment?
- Follow-up: How do you define "quality" for an AI feature?
- Follow-up: What's your definition of escaped defect rate / MTTD?

---

## 9. Experience Level ⭐ (expect this)

**Q: This role calls for 7+ years and building teams. Walk me through your experience level.**

- Follow-up: Have you ever mentored or onboarded anyone?
- Follow-up: Have you had to influence a decision without authority?
- Follow-up: How would you approach building a center of excellence?
- Follow-up: How do you handle working in an ambiguous environment with no existing process?

---

## 10. Financial Services / Regulated Environment

**Q: What's different about QA in a regulated financial environment?**

- Follow-up: What do you know about model risk management / OSFI E-23?
- Follow-up: How do you make a test run auditable?
- Follow-up: What does "independent validation" mean and why does it matter?
- Follow-up: How would you explain a model decision to a non-technical auditor?

---

## 11. Behavioural

**Q: Tell me about a time you found a critical bug late.**

**Q: Tell me about a time you disagreed with a developer or stakeholder.**

**Q: Tell me about a project that didn't go as planned.**

**Q: How do you prioritize when everything is urgent?**

**Q: Tell me about a time you had to explain something technical to a non-technical audience.**

- Follow-up on any of these: What would you do differently now?

---

## 12. Closing

**Q: Why RBC?**

**Q: Why this role specifically?**

**Q: Where do you see yourself in 3 years?**

**Q: Do you have any questions for us?**

---

## Questions to Ask Them (have 3, ask 2)

1. How mature is the AISDLC framework today — is there something in place that needs modernizing, or is this closer to a blank page?
2. What does the team look like right now, and what would the first 90 days ideally look like?
3. Is RBC's AI testing work mostly around predictive models, or is a lot of it LLM-based features?

*Don't ask about salary or work-from-home in a 30-minute screen unless they raise it first.*

---

## Pre-Interview Checklist

- [ ] Rehearse Q1, Q2, and Q9 out loud until smooth — these three carry the interview
- [ ] Know how you measured every number on your resume
- [ ] Resume open on a second screen
- [ ] Camera, mic, and meeting link tested 15 minutes early
- [ ] Have a clean one-sentence answer for why you left Exeevo