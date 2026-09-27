# Interview Prep: AI ModelOps Engineer, Canadian Tire Corporation

> **Format:** 30-minute video interview (likely first round). Expect ~5 min intro, 15–20 min questions, 5 min for your questions. Keep each answer to 1–2 minutes.
>
> **Tip:** Swap in your real details (tool names, numbers, incidents). Real details sound more confident than memorized ones.

---

## Part 1: Your Core Story (use it again and again)

Build one strong story from your Exeevo work. You can reuse parts of it for *"tell me about a project,"* *"tell me about a challenge,"* and *"what are you proud of."*

### Situation
> "At Exeevo, our data science and AI teams were building ML models and GenAI agents, but deployments were mostly manual. Nobody had one place to see which model or agent version was in production, who owned it, or whether it was healthy. Releases were slow, and we often learned about problems from users."

### Task
> "My job was to make AI deployment faster, safer, and easier to monitor."

### Action
> "I did three main things.
>
> **First**, I built CI/CD pipelines. Every model or agent went through the same steps: build a Docker container, run tests and evaluations, register the version, deploy to staging, then deploy to production after approval.
>
> **Second**, I set up a model and agent registry. We used MLflow for models, and for agents we tracked the owner, version, prompt version, LLM used, tools, evaluation scores, and approval status.
>
> **Third**, I built the observability stack: logs, metrics, and alerts for latency, error rates, token usage, and cost. I provisioned all the infrastructure with Terraform, so every environment was the same and could be recreated."

### Result
> "Release time dropped by about 30%, incident response time dropped by about 40%, and we kept 99.5% platform uptime. More than 5 AI solutions were managed through the registry, which made governance and audits much easier."

### Be ready to explain your numbers

| Metric | How to explain it |
|---|---|
| **30% faster releases** | "We compared average time from code merge to production before and after the pipeline. It went from about X days to Y days." |
| **40% faster incident response** | "We measured the time from when a problem started to when someone started working on it. Alerts meant we found issues ourselves instead of waiting for user reports." |
| **99.5% uptime** | "We tracked availability of our production endpoints through health checks in our monitoring tool, measured monthly." |

---

## Part 2: Likely Questions, Answers, and Follow-ups

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

---

### 6. "Tell me about a production incident and how you fixed it."

*Use a real one if you have it. Here's an example structure:*

> "One of our GenAI services suddenly became very slow, and some requests failed. Our alerts caught the rise in latency and errors. Looking at the logs, I saw many '429 Too Many Requests' errors from the Azure OpenAI endpoint, meaning we'd hit our rate limit because usage had grown. Short term, I added retry with backoff so requests didn't fail right away. Long term, we increased the quota, spread traffic across deployments, and added an alert for rate-limit errors so we'd see it earlier next time. I also wrote a short post-incident review so the team could learn from it."

**Follow-up:**

- **"How do you do root cause analysis?"**
  *"Start with what changed: a deployment, traffic, or config. Check the dashboards to find when it started, then use logs and traces to narrow it down. Fix the immediate issue first, then find the real cause so it doesn't happen again."*

---

### 7. "You established model and agent registries. What's in them and why do they matter?"

> "A registry is one source of truth for everything in production. For models, MLflow stored the version, training data reference, metrics, and stage, like staging or production. For agents, we tracked the owner, which LLM it used, prompt version, tools it could access, evaluation results, and approval status. It matters for governance. If an auditor or manager asks 'what's running, who approved it, and how was it tested?', we have the answer in one place."

**Follow-up:**

- **"How does this support responsible AI?"**
  *"Nothing reaches production without passing evaluation and getting approval, and every change is recorded. That gives us an audit trail and clear ownership."*

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

---

### 9. "Explain RAG in simple terms."

> "RAG means Retrieval-Augmented Generation. An LLM doesn't know your company's data. So before asking the LLM, we search your documents, find the most relevant pieces, and give them to the LLM along with the question. The LLM then answers using that information. It's like giving someone an open-book exam instead of asking from memory."

**Follow-up:**

- **"What if the RAG answers are poor?"**
  *"First check whether retrieval is the problem: are the right documents being found? If not, adjust chunk size, improve the embeddings, or add hybrid search. If retrieval is good but answers are bad, improve the prompt. I'd measure both parts separately with an evaluation set."*

---

### 10. "What are AI agents, and what's different about running them in production?"

> "An AI agent is an LLM that can plan steps and use tools, like calling an API or searching a database, to complete a task, not just answer a question. In production they're riskier because they take actions. So you need guardrails: give agents only the permissions they need, limit the number of steps, add human approval for important actions, and trace every step so you can see what the agent did and why."

**Follow-up:**

- **"How would you stop an agent from doing something harmful?"**
  *"Least-privilege access to tools, content safety filters, input checks against prompt injection, human-in-the-loop for high-impact actions, and full logging for audits."*

---

### 11. "What's your experience with Docker and Kubernetes?"

> "I containerized our model and agent services with Docker so they run the same everywhere. We deployed them on Kubernetes, which handles scaling, restarts failed containers, and allows rolling updates with no downtime."

**Follow-up:**

- **"How do you scale a model service?"**
  *"Horizontal Pod Autoscaling based on CPU, memory, or request count. For LLM apps calling Azure OpenAI, the bottleneck is often the API quota, not our pods, so we monitor that too."*

---

### 12. "How do you handle security and compliance for AI platforms?"

> "I follow a few basics: role-based access control so people only have the access they need, managed identities instead of keys, secrets in Key Vault, private endpoints so AI services aren't open to the internet, and logging for audits. For GenAI, I add content safety filters and make sure sensitive data like customer information isn't sent to models or logs without proper controls."

**Follow-up:**

- **"How would you handle customer PII in prompts?"**
  *"Mask or remove PII before sending data to the model where possible, keep data inside our Azure environment, and avoid logging full prompts that contain personal data."*

---

### 13. "How would you reduce the cost of AI workloads?"

> "For LLMs: use smaller models for simple tasks and bigger models only when needed, cache repeated answers, and keep prompts short. For infrastructure: autoscale down when traffic is low, and set budgets and cost alerts. Most important is visibility: a dashboard showing cost per application so teams can see what they spend."

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