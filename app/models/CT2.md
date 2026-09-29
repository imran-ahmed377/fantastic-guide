

### 1. "Tell me about yourself."

> "I'm an AI ModelOps Engineer with a Master's in Applied Computing, specializing in AI, from the University of Windsor. Most recently at Exeevo, I deployed and monitored ML and GenAI solutions in production on Azure. I built CI/CD pipelines for models and agents, set up model and agent registries, and implemented observability with logging and alerting. Before that, I interned at Vistaprint, where I automated data tasks with Python and built monitoring scripts. I really enjoy the platform side of AI, making it easy and safe for teams to get their models and agents into production. That's why this role at Canadian Tire excites me."

**Follow-ups:**

- **"Why did you leave Exeevo?"**
  Keep it positive and short. For example: *"My contract ended in August, and I'm looking for a larger enterprise where I can work on AI platforms at a bigger scale."* Use whatever the real reason is, said positively.
- **"You worked while doing your Master's. How did you manage?"**
  *"I planned my time carefully, and the two supported each other. What I studied, I used at work, and what I saw at work made my courses more practical."*

---

### 2. "Why Canadian Tire? Why this role?"

> "Canadian Tire is a huge enterprise with many brands like Canadian Tire, Sport Chek, Mark's, and Triangle Rewards. That means AI can have a real impact at a large scale. I also like that this role focuses on building the platform, not just one model. Helping many AI teams deploy safely is exactly the work I did at Exeevo, and I want to do it at a bigger scale. The focus on agentic AI is also exciting, because it's the newest area and still being figured out."

**Follow-up:**

- **"What do you know about our AI work?"**
  Before the interview, spend 15 minutes on Canadian Tire's newsroom and LinkedIn for any AI announcements. Mention one specific thing if you find it.

---

### 3. "Walk me through how you deploy a model or AI agent to production."

> "First, the code and config go into Git. A pull request triggers the CI pipeline, which runs unit tests, builds a Docker image, and runs evaluations. For a model, that's accuracy checks. For an LLM agent, it's a test set of prompts with expected answers. If it passes, the version is registered in the registry with its metadata. Then it deploys to a staging environment for integration testing. After approval, it goes to production, usually on Kubernetes or an Azure managed endpoint. Monitoring starts right away."

**Follow-ups:**

- **"How do you roll back?"**
  *"Every version is in the registry and every image is tagged, so rollback means redeploying the previous version through the same pipeline. For risky changes, I prefer a canary or blue-green deployment, sending a small share of traffic to the new version first."*
- **"How do you test an LLM before deploying it? Outputs change every time."**
  *"You can't test for exact matches. Instead, I use an evaluation dataset and score things like groundedness, relevance, and safety, sometimes using another LLM as a judge. I set a minimum score, and if the new version scores lower than the current one, the pipeline stops."*

#### Code example: A simple CI/CD pipeline (GitHub Actions)

This is what "every model goes through the same steps" looks like in real life. Each `job` is a stage.

```yaml
# .github/workflows/deploy.yml
name: Deploy AI Agent

on:
  push:
    branches: [main]          # Run when code is merged to main

jobs:
  test-and-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4                      # 1. Get the code
      - run: pip install -r requirements.txt           # 2. Install packages
      - run: pytest tests/                             # 3. Run unit tests
      - run: python evaluate.py                        # 4. Run LLM evaluation (fails if score is low)
      - run: docker build -t myregistry.azurecr.io/my-agent:${{ github.sha }} .   # 5. Build image
      - run: docker push myregistry.azurecr.io/my-agent:${{ github.sha }}         # 6. Save image

  deploy-staging:
    needs: test-and-build     # Only runs if the step above passed
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying to STAGING..."

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production   # This setting can require a human to click "Approve"
    steps:
      - run: echo "Deploying to PRODUCTION..."
```

**Key idea:** Each image is tagged with the commit ID (`github.sha`), so every version is unique and easy to roll back.

#### Code example: The evaluation "quality gate" (`evaluate.py`)

This shows how the pipeline stops a bad LLM version. Real teams use better scoring (like Azure AI evaluation or an LLM judge), but the idea is the same.

```python
import sys

# A small test set: questions and words the answer SHOULD contain
test_cases = [
    {"question": "What is your return policy?", "must_include": "90 days"},
    {"question": "Do you sell tires?",           "must_include": "yes"},
]

def ask_agent(question):
    # In real life, this calls your deployed agent in the test environment
    return "Yes, you can return items within 90 days."

passed = 0
for case in test_cases:
    answer = ask_agent(case["question"]).lower()
    if case["must_include"].lower() in answer:
        passed += 1

score = passed / len(test_cases)
print(f"Evaluation score: {score:.0%}")

MIN_SCORE = 0.8
if score < MIN_SCORE:
    print("Score too low. Stopping deployment.")
    sys.exit(1)      # Exit code 1 = the pipeline FAILS and stops here
```

**Key idea:** `sys.exit(1)` tells the pipeline "something failed," so nothing bad reaches production.

---

### 4. "What's the difference between traditional MLOps and GenAI or LLMOps?"

> "In traditional MLOps, you usually train your own model, and the main concerns are data drift and accuracy. In GenAI, you often use a foundation model like GPT through Azure OpenAI, so you don't retrain it. Instead, you manage prompts, RAG pipelines, and agent tools. You also monitor new things: token usage, cost, latency, hallucinations, and harmful content. And evaluation is harder, because there's no single 'correct' answer."

**Follow-up:**

- **"What would you monitor for an LLM application?"**
  *"Four groups: system health (latency, errors, uptime), cost (tokens per request, daily spend), quality (groundedness and user feedback like thumbs up/down), and safety (content filter triggers, prompt injection attempts)."*

---

### 5. "Tell me about the observability stack you built."

> "I set up centralized logging, metrics dashboards, and alerts. For example, using Azure Monitor and Application Insights, every model and agent sent logs and traces to one place. I created dashboards for latency, error rates, and token usage, and alerts that notified the on-call person when something crossed a threshold. For agents, tracing was important, because one request can call the LLM several times and use multiple tools. Tracing shows exactly which step failed."

**Follow-ups:**

- **"How do you avoid alert fatigue?"**
  *"I only alert on things that need action, and I set thresholds based on normal behaviour, not guesses. Warning-level issues go to a dashboard or channel instead of paging someone."*
- **"What's the difference between logs, metrics, and traces?"**
  *"Logs are detailed event records. Metrics are numbers over time, like latency. Traces follow a single request through every step and service."*

#### Code example: A health check endpoint (FastAPI)

This is what the monitoring tool "pings" every few minutes. If it doesn't answer, an alert fires.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}     # Monitoring tool expects HTTP 200 + this response
```

#### Code example: Sending a custom metric (token usage) to Azure Monitor

The platform tracks errors and latency automatically. Python adds **custom** metrics, like tokens.

```python
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import metrics

# Connect this app to Application Insights (one line!)
configure_azure_monitor(connection_string="InstrumentationKey=...")

meter = metrics.get_meter("my-agent")
token_counter = meter.create_counter("llm_tokens_used")

# After each LLM call, record how many tokens it used
tokens_used = 850
token_counter.add(tokens_used, {"app": "customer-help-agent"})
```

#### Code example: An alert query in Log Analytics (KQL)

This is the kind of query behind an alert like "more than 20 errors in 5 minutes."

```kusto
requests
| where timestamp > ago(5m)          // Look at the last 5 minutes
| where success == false             // Only failed requests
| summarize failed_count = count()   // Count them
| where failed_count > 20            // Alert fires if this returns a row
```

**Key idea:** You don't write alerting from scratch. You write a small query, and Azure Monitor runs it on a schedule and notifies people.

---

### 6. "Tell me about a production incident and how you fixed it."

*Use a real one if you have it. Here's an example structure:*

> "One of our GenAI services suddenly became very slow, and some requests failed. Our alerts caught the rise in latency and errors. Looking at the logs, I saw many '429 Too Many Requests' errors from the Azure OpenAI endpoint, meaning we'd hit our rate limit because usage had grown. Short term, I added retry with backoff so requests didn't fail right away. Long term, we increased the quota, spread traffic across deployments, and added an alert for rate-limit errors so we'd see it earlier next time. I also wrote a short post-incident review so the team could learn from it."

**Follow-up:**

- **"How do you do root cause analysis?"**
  *"Start with what changed: a deployment, traffic, or config. Check the dashboards to find when it started, then use logs and traces to narrow it down. Fix the immediate issue first, then find the real cause so it doesn't happen again."*

#### Code example: Retry with backoff (the short-term fix for 429 errors)

"Backoff" means: if it fails, wait a little, then try again, waiting longer each time.

```python
import time
from openai import AzureOpenAI, RateLimitError

client = AzureOpenAI(
    azure_endpoint="https://my-openai.openai.azure.com/",
    api_version="2024-06-01",
    # No API key here: in real code, use managed identity (see Section 8)
)

def ask_llm(question, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": question}],
            )
            return response.choices[0].message.content
        except RateLimitError:                 # This is the 429 error
            wait = 2 ** attempt                # Wait 1s, then 2s, then 4s
            print(f"Rate limited. Retrying in {wait} seconds...")
            time.sleep(wait)
    raise Exception("Still failing after retries")
```

**Key idea:** Retrying immediately makes the problem worse. Waiting longer each time gives the service room to recover.

---

### 7. "You established model and agent registries. What's in them and why do they matter?"

> "A registry is one source of truth for everything in production. For models, MLflow stored the version, training data reference, metrics, and stage, like staging or production. For agents, we tracked the owner, which LLM it used, prompt version, tools it could access, evaluation results, and approval status. It matters for governance. If an auditor or manager asks 'what's running, who approved it, and how was it tested?', we have the answer in one place."

**Follow-up:**

- **"How does this support responsible AI?"**
  *"Nothing reaches production without passing evaluation and getting approval, and every change is recorded. That gives us an audit trail and clear ownership."*

#### Code example: Registering a model and moving it to production (MLflow)

```python
import mlflow
from mlflow import MlflowClient

client = MlflowClient()

# 1. Register a trained model as a new version
result = mlflow.register_model(
    model_uri="runs:/abc123/model",     # Where the trained model is saved
    name="demand-forecast",
)
print(f"Registered version: {result.version}")   # e.g., version 5

# 2. Add useful info for governance
client.set_model_version_tag("demand-forecast", result.version, "owner", "ml-team")
client.set_model_version_tag("demand-forecast", result.version, "approved_by", "jane.doe")

# 3. Point the "champion" (production) label to the new version
client.set_registered_model_alias("demand-forecast", "champion", result.version)
```

The old version (v4) is **not deleted**. The "champion" label just moves from v4 to v5.

#### Code example: Rollback

If v5 has a problem, move the label back. That's it.

```python
client.set_registered_model_alias("demand-forecast", "champion", 4)
```

#### Code example: What the production app loads

The app always asks for "whatever is champion," so it never needs to know the version number.

```python
model = mlflow.pyfunc.load_model("models:/demand-forecast@champion")
```

#### Example: What an agent registry entry looks like

```json
{
  "agent_name": "customer-help-agent",
  "version": "3",
  "owner": "ai-team",
  "llm_model": "gpt-4o",
  "prompt_version": "v7",
  "tools": ["search_products", "check_order_status"],
  "evaluation_score": 0.92,
  "approval_status": "approved",
  "approved_by": "jane.doe",
  "deployed_on": "2026-06-15"
}
```

---

### 8. "How have you used Terraform or Infrastructure as Code?"

> "I used Terraform to provision the Azure resources for our AI platform, such as resource groups, storage, Key Vault, networking, AI services, and Kubernetes clusters. Everything was in Git, so changes were reviewed through pull requests. We could create identical dev, staging, and production environments, and there was no manual clicking in the portal."

**Follow-ups:**

- **"How do you manage Terraform state?"**
  *"Remote state in an Azure Storage account with locking, so two people can't change the same infrastructure at the same time."*
- **"Terraform or Bicep?"**
  *"Bicep is Azure-only and simple for Azure-native teams. Terraform works across clouds and has a larger ecosystem. I'm comfortable with both and would follow the team standard."*
- **"How do you handle secrets?"**
  *"Never in code. Secrets go in Azure Key Vault, and services use managed identities so they don't need passwords at all."*

#### Code example: Simple Terraform file

```hcl
# Store Terraform "state" remotely in Azure, with locking
terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "tfstatestorage"
    container_name       = "tfstate"
    key                  = "ai-platform.tfstate"
  }
}

provider "azurerm" {
  features {}
}

# A resource group to hold the AI platform resources
resource "azurerm_resource_group" "ai" {
  name     = "ai-platform-${var.environment}"   # e.g., ai-platform-dev, ai-platform-prod
  location = "canadacentral"
}

# A storage account for model files and data
resource "azurerm_storage_account" "models" {
  name                     = "aimodels${var.environment}"
  resource_group_name      = azurerm_resource_group.ai.name
  location                 = azurerm_resource_group.ai.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

variable "environment" {
  type = string    # Pass "dev", "staging", or "prod"
}
```

**Key idea:** The same file creates dev, staging, and prod. Only the `environment` value changes, so all environments match.

Common commands:

```bash
terraform plan  -var="environment=dev"   # Preview what will change
terraform apply -var="environment=dev"   # Actually create/update resources
```

#### Code example: Reading a secret from Key Vault with managed identity (no password in code)

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# DefaultAzureCredential uses the app's managed identity automatically
credential = DefaultAzureCredential()

client = SecretClient(
    vault_url="https://my-ai-keyvault.vault.azure.net/",
    credential=credential,
)

db_password = client.get_secret("database-password").value
```

**Key idea:** The code never contains a password. Azure checks the app's identity and decides if it's allowed.

---

### 9. "Explain RAG in simple terms."

> "RAG means Retrieval-Augmented Generation. An LLM doesn't know your company's data. So before asking the LLM, we search your documents, find the most relevant pieces, and give them to the LLM along with the question. The LLM then answers using that information. It's like giving someone an open-book exam instead of asking from memory."

**Follow-up:**

- **"What if the RAG answers are poor?"**
  *"First check whether retrieval is the problem: are the right documents being found? If not, adjust chunk size, improve the embeddings, or add hybrid search. If retrieval is good but answers are bad, improve the prompt. I'd measure both parts separately with an evaluation set."*

#### Code example: RAG in its simplest form

```python
def search_documents(question):
    # In real life: search a vector database like Azure AI Search
    return [
        "Return policy: Items can be returned within 90 days with a receipt.",
        "Exchanges are free at any store location.",
    ]

def answer_with_rag(question):
    # Step 1: RETRIEVE the most relevant pieces of company data
    docs = search_documents(question)

    # Step 2: AUGMENT the prompt with that data
    prompt = f"""Answer the question using ONLY the information below.
If the answer is not there, say "I don't know."

Information:
{chr(10).join(docs)}

Question: {question}"""

    # Step 3: GENERATE the answer with the LLM
    return ask_llm(prompt)     # ask_llm() from Section 6

print(answer_with_rag("How long do I have to return something?"))
```

**Key idea:** Retrieval + Augmented prompt + Generation = RAG. The "use ONLY the information below" line helps reduce hallucinations.

---

### 10. "What are AI agents, and what's different about running them in production?"

> "An AI agent is an LLM that can plan steps and use tools, like calling an API or searching a database, to complete a task, not just answer a question. In production they're riskier because they take actions. So you need guardrails: give agents only the permissions they need, limit the number of steps, add human approval for important actions, and trace every step so you can see what the agent did and why."

**Follow-up:**

- **"How would you stop an agent from doing something harmful?"**
  *"Least-privilege access to tools, content safety filters, input checks against prompt injection, human-in-the-loop for high-impact actions, and full logging for audits."*

#### Code example: Simple agent guardrails

```python
ALLOWED_TOOLS = {"search_products", "check_order_status"}   # Least privilege
NEEDS_HUMAN_APPROVAL = {"issue_refund"}                    # High-impact actions
MAX_STEPS = 5                                               # Stop endless loops

def run_tool(tool_name, step):
    # Guardrail 1: limit the number of steps
    if step > MAX_STEPS:
        return "Stopped: too many steps."

    # Guardrail 2: human approval for risky actions
    if tool_name in NEEDS_HUMAN_APPROVAL:
        return "Waiting for human approval."

    # Guardrail 3: only allow approved tools
    if tool_name not in ALLOWED_TOOLS:
        return f"Blocked: '{tool_name}' is not allowed."

    # Guardrail 4: log every action for audits
    print(f"[AUDIT] step={step} tool={tool_name}")
    return f"Running {tool_name}..."

print(run_tool("check_order_status", step=1))   # Allowed
print(run_tool("issue_refund", step=2))         # Needs approval
print(run_tool("delete_database", step=3))      # Blocked
```

---

### 11. "What's your experience with Docker and Kubernetes?"

> "I containerized our model and agent services with Docker so they run the same everywhere. We deployed them on Kubernetes, which handles scaling, restarts failed containers, and allows rolling updates with no downtime."

**Follow-up:**

- **"How do you scale a model service?"**
  *"Horizontal Pod Autoscaling based on CPU, memory, or request count. For LLM apps calling Azure OpenAI, the bottleneck is often the API quota, not our pods, so we monitor that too."*

#### Code example: A simple Dockerfile

```dockerfile
# Start from a small Python image
FROM python:3.11-slim

WORKDIR /app

# Install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Start the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Code example: Kubernetes autoscaling (HPA)

"If average CPU goes above 70%, add more copies (pods), up to 10."

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-agent-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-agent          # The app to scale
  minReplicas: 2            # Always keep at least 2 running
  maxReplicas: 10           # Never more than 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

**Key idea:** `minReplicas: 2` means if one pod crashes, the other keeps serving users. That helps uptime.

---

### 12. "How do you handle security and compliance for AI platforms?"

> "I follow a few basics: role-based access control so people only have the access they need, managed identities instead of keys, secrets in Key Vault, private endpoints so AI services aren't open to the internet, and logging for audits. For GenAI, I add content safety filters and make sure sensitive data like customer information isn't sent to models or logs without proper controls."

**Follow-up:**

- **"How would you handle customer PII in prompts?"**
  *"Mask or remove PII before sending data to the model where possible, keep data inside our Azure environment, and avoid logging full prompts that contain personal data."*

#### Code example: Masking PII before sending text to an LLM

```python
import re

def mask_pii(text):
    text = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[EMAIL]", text)          # Emails
    text = re.sub(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b", "[PHONE]", text)  # Phone numbers
    return text

message = "Hi, I'm Sam. Email me at sam@gmail.com or call 416-555-1234."
print(mask_pii(message))
# Hi, I'm Sam. Email me at [EMAIL] or call [PHONE].
```

**Key idea:** This is a simple example. In production, teams often use a dedicated service (like Azure AI Language PII detection) because simple patterns can miss things.

---

### 13. "How would you reduce the cost of AI workloads?"

> "For LLMs: use smaller models for simple tasks and bigger models only when needed, cache repeated answers, and keep prompts short. For infrastructure: autoscale down when traffic is low, and set budgets and cost alerts. Most important is visibility: a dashboard showing cost per application so teams can see what they spend."

#### Code example: Two simple cost savers (model routing + caching)

```python
cache = {}   # In production, use something like Redis

def pick_model(question):
    # Short, simple questions -> cheaper, smaller model
    if len(question.split()) < 15:
        return "gpt-4o-mini"
    return "gpt-4o"          # Complex questions -> bigger model

def answer(question):
    # 1. Caching: if we've answered this before, don't pay again
    if question in cache:
        return cache[question]

    # 2. Routing: use the cheapest model that can do the job
    model = pick_model(question)
    result = f"(answer from {model})"   # In real life: call the LLM here

    cache[question] = result
    return result
```

---

### 14. "Tell me about explaining something technical to a non-technical person."

> "At Exeevo, a business stakeholder asked why a GenAI feature couldn't go live right away. Instead of talking about evaluation pipelines, I explained it like a car safety inspection: we test it before it goes on the road so it doesn't give customers wrong answers. They understood, and we agreed on a simple checklist that showed what 'ready' meant."

**Follow-up:**

- **"What if a data scientist doesn't want to follow your platform process?"**
  *"I'd listen to understand why. Usually the process feels slow. Then I'd show how the templates actually save them time, and ask for feedback to make it easier. Adoption comes from making the right way the easy way."*

---

### 15. "How do you stay current with AI?"

> "I follow the Microsoft Azure AI and MLflow updates, read engineering blogs, and try new tools in small personal projects. For example, my Agentic AI Platform Prototype project was where I experimented with agent registries and lifecycle management before using those ideas at work."

---

### 16. "What are your salary expectations?"

The posted range is **$80,000–$131,000**. With about one year of full-time experience plus a Master's, a reasonable answer is:

> "Based on the posted range and my experience, I'm looking for something around $95,000 to $110,000, but I'm flexible and would consider the full package, including benefits and learning opportunities."

---

## Part 3: Questions to Ask Them (pick 2)

1. "What does the AI platform look like today, and what's the biggest priority for the first 6 months?"
2. "How mature is the agentic AI platform right now: early experiments or already in production?"
3. "How do the platform team and the AI teams work together day to day?"
4. "What would success look like for this person after one year?"

> **Bonus:** You could also ask what the **AAAI platform** includes, since it's in the job description. This shows you read it closely.

---

## Quick Checklist for the Video Call

- [ ] Practice the core story out loud 3–4 times
- [ ] Know how you measured every number on your resume
- [ ] Research one recent Canadian Tire AI or tech announcement
- [ ] Test mic, camera, and internet 15 minutes early
- [ ] Keep your resume open beside the camera
- [ ] Use "I" (not "we") when describing your own work
- [ ] Keep answers short, then stop and let them follow up



# Interview Answers: Monitoring, Health Checks & Staging

---

## 1. How do you know there's a production incident?

> "Mostly through automated alerts. We set alerts on key signals like high error rates, slow response times (latency), failed health checks, or a sudden jump in token usage or cost. When a threshold is crossed, the on-call person gets notified by email, Teams, or a paging tool. Sometimes we also learn from users or support tickets, but the goal is to catch problems before users notice."

### Common tools (Azure setup, which matches this job)

- **Azure Monitor alert rules** watch metrics like error rate, latency, and CPU, and fire when a threshold is crossed.
- **Application Insights** collects requests, failures, and traces from your apps, and runs availability tests (health checks).
- **Log Analytics** lets you write queries (in a language called KQL) to create alerts from logs, like *"more than 20 errors in 5 minutes."*
- **Action Groups** decide who gets notified and how: email, SMS, Microsoft Teams, or a paging tool like **PagerDuty** or **Opsgenie**.

---

## 2. Which monitoring tool did you use for health checks on production endpoints?

> "We used Azure Monitor with Application Insights. Application Insights has a feature called availability tests, which pings our endpoints every few minutes from different locations. If an endpoint doesn't respond or returns an error, it triggers an alert. That same data is how we calculated our 99.5% uptime."

> **Note:** Only say Azure Monitor if that's what you used. If you used something else, like Datadog, Grafana, or Prometheus, name that instead. Interviewers often ask a follow-up about the tool.

---

## 3. What is "deploy to staging"?

> "Staging is a copy of the production environment that real users don't use. Before releasing a new model or agent to production, we deploy it to staging first to test it in realistic conditions: checking that it connects correctly to other services, responds quickly, and gives good answers. If everything works, we promote the same version to production. It's like a dress rehearsal before the real show."