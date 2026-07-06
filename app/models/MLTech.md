# Table of Content
- [Introduction](#introduction)
- [Project/Exp Aspire](#projectexp-in-aspire-ontario-genai-incident-analyzer)
- [Deployment](#deployment)
- [What is RAG](#what-is-rag)
- [Cosine Similarity](#cosine-similarity)
- [Semantic Search](#semantic-search)
- [Hallucinations](#hallucinations)
- [Temperatue](#temperature-in-llms)
- [Measuring Success](#measuring-success)
- [Docker](#docker)
- [CI/CD](#cicd)
- [Prompt Engineerring](#prompt-engineering)
- [React](#react)


# Introduction

I recently finished my Master's in Applied Computing with a focus on AI at the University of Windsor. Alongside my studies, I worked as a Co-op AI Application Developer at Aspire Ontario, where I built an AI-powered IT support tool. Before that, I was a Full Stack Developer Intern at Meallens. Across both roles, I've built backend systems using Python, and frontend interfaces using React, and worked with AI tools like Azure OpenAI to automate real business processes.

I enjoy solving problems using modern tools and technologies. I am always eager to learn and continuously improve my skills to stay updated with latest technologies and contribute effectively to build impactful solutions.


# Project/Exp in Aspire Ontario: GenAI Incident Analyzer

Overview of the Project:

The goal was to build a system that could understand the meaning of an incident, retrieve the most relevant historical resolutions, and use an LLM to generate a grounded recommendation instead of relying on general knowledge.

# Phase 1: Building the Knowledge Base (Steps in Detail)

## Typical Project Structure

A simple project layout might look like:

```text
project/
│
├── ingest.py          # Load ServiceNow tickets
├── preprocess.py      # Clean and chunk text
├── embed.py           # Generate embeddings
├── pinecone_db.py     # Create index and upsert vectors
├── retrieve.py        # Query Pinecone
├── chatbot.py         # Prompt the LLM
└── app.py             # User interface
```

## Step 1 — Decide What Data You Need and From Where

In ServiceNow, incident data lives mainly in the `incident` table, but the useful "solution" text is spread across a few places.

Not every ticket is useful—many closed tickets have empty or useless close notes (e.g., "fixed" or "resolved via reboot" with no detail). Part of the project is filtering for tickets that actually contain a usable resolution.

---

## Step 2 — Extract the Data

You'll pull data out of ServiceNow using the Table API (REST), which returns JSON.

A typical extraction call looks like:

```http
GET /api/now/table/incident?sysparm_query=active=false^close_notesISNOTEMPTY&sysparm_fields=number,short_description,description,close_notes,category,subcategory,cmdb_ci,priority,resolution_code,resolved_at&sysparm_limit=500
```

Each record comes back as JSON:

```json
{
  "number": "INC0012345",
  "short_description": "VPN client fails to connect after Windows update",
  "description": "User reports Cisco AnyConnect fails with error 442 after latest patch...",
  "close_notes": "Reinstalled AnyConnect client v4.10, cleared cached profile, reconnected successfully.",
  "category": "Network",
  "subcategory": "VPN",
  "cmdb_ci": "Cisco AnyConnect",
  "priority": "3",
  "resolution_code": "Solved (Permanently)",
  "resolved_at": "2025-11-02 14:32:10"
}
```
```json
{
  "number": "INC0012389",
  "short_description": "Printer offline in Finance department",
  "description": "User reports HP LaserJet M501 on 3rd floor showing offline status, unable to print invoices.",
  "close_notes": "Print spooler service was hung. Restarted spooler service and re-added printer queue. Confirmed test print successful.",
  "category": "Hardware",
  "subcategory": "Printer",
  "cmdb_ci": "HP LaserJet M501",
  "priority": "4",
  "resolution_code": "Solved (Permanently)",
  "resolved_at": "2025-09-14 09:15:22"
}
```
```json
{
  "number": "INC0012410",
  "short_description": "Outlook crashes on startup after latest update",
  "description": "Multiple users in Sales team reporting Outlook 365 crashes immediately after opening, error code 0x80070005.",
  "close_notes": "Identified conflict with a third-party add-in (Salesforce Outlook plugin). Disabled add-in via Outlook safe mode, then updated to latest plugin version 4.2.1. Issue resolved after reboot.",
  "category": "Software",
  "subcategory": "Email",
  "cmdb_ci": "Microsoft Outlook 365",
  "priority": "2",
  "resolution_code": "Solved (Permanently)",
  "resolved_at": "2025-08-03 11:42:07"
}
```
```json
{
  "number": "INC0012455",
  "short_description": "User unable to access shared drive",
  "description": "User reports 'Access Denied' error when trying to open \\\\fileserver01\\finance share, worked fine yesterday.",
  "close_notes": "User's AD group membership had been removed during a recent security group cleanup. Re-added user to Finance_ReadWrite AD group, confirmed access restored after group policy refresh.",
  "category": "Access Management",
  "subcategory": "File Share",
  "cmdb_ci": "fileserver01",
  "priority": "3",
  "resolution_code": "Solved (Permanently)",
  "resolved_at": "2025-10-21 16:03:55"
}
```

For a first load, you'd export the last **1–3 years** of closed incidents (however far back the data is still relevant—old tickets referencing decommissioned systems should be excluded).

Options include:

- Scheduled ServiceNow Scripted REST API export
- An integration user with API access pulling on a schedule
- ServiceNow's built-in Export to JSON/CSV for a one-time historical load

---

## Step 3 — Clean and Preprocess

Raw ticket text is messy. This step matters more than people expect.

Tasks include:

- Strip HTML tags (ServiceNow rich-text fields often contain `<p>`, `<span style=...>`, etc.)
- Remove boilerplate/signatures ("Sent from my iPhone," auto-reply footers, email headers pasted into descriptions)
- Redact PII—usernames, employee IDs, IP addresses, phone numbers—especially important if data may flow into a third-party LLM API
- Deduplicate—many incidents are near-identical restatements of the same root cause; you don't need 200 copies of "printer offline, restarted print spooler"
- Filter out low-signal tickets—empty close notes or notes that just say "see KB0001234" without content
- Normalize fields—consistent category/priority labels and resolved timestamps parsed as real dates

---

## Step 4 — Chunk the Data

This is a key design decision, and incident tickets are simpler than most RAG use cases because they're naturally short and self-contained.

### Option 1: One Chunk per Ticket (Recommended)

Combine:

- `short_description`
- `description`
- `close_notes`

into a single text block, and attach metadata (category, CI, priority, date) as filterable fields alongside the vector.

Most tickets are only a few hundred words, so this fits comfortably in one chunk.

### Option 2: Split Long Tickets

If a ticket has extensive work notes (long troubleshooting threads), split it into:

- Problem chunk
- Resolution chunk

linked by ticket ID so retrieval can surface either.

Each chunk should look like:

```text
Title: VPN client fails to connect after Windows update
Category: Network / VPN
Affected CI: Cisco AnyConnect

Problem:
User reports Cisco AnyConnect fails with error 442 after latest patch...

Resolution:
Reinstalled AnyConnect client v4.10, cleared cached profile, reconnected successfully.
```

---

## Step 5 — Generate Embeddings

Each chunk gets converted into a vector (a list of numbers representing its meaning) using an embedding model.

Possible embedding models include:

- OpenAI `text-embedding-3`

This step is batched—you run it once over your historical data, then incrementally for new tickets.

---

## Step 6 — Store in a Vector Database

The vectors plus their metadata get stored in a vector database that supports similarity search.

Popular options include:

- Pinecone

Each entry stores:

- The embedding vector
- The original text chunk
- Structured metadata:
  - Ticket number
  - Category
  - Configuration Item (CI)
  - Resolution code
  - Resolution date

This metadata allows filtered searches such as:

> Only search Network tickets from the last year.

## Why Pinecone

- Fully managed and serverless—no infrastructure to deploy or maintain.
- Very quick to get started, requiring only a few lines of code.
- Automatically handles scaling, sharding, and backups.
- **Downside:** Proprietary and cloud-only (SaaS), meaning your data is stored on Pinecone's infrastructure and costs increase with usage.
- **Best suited for:** Teams that want to move quickly without managing their own infrastructure.

---

# Phase 2: Answering a New Incident

## Step 1 — Analyst Asks a Question

Instead of manually searching, the analyst enters a query such as:

> User reports VPN error 442 after latest Windows patch.

---

## Step 2 — Embed the Query

The **same embedding model** used during ingestion converts the analyst's query into a vector.

This consistency is important—you cannot mix embedding models between indexing and querying.

---

## Step 3 — Vector Search

The vector database compares the query vector against all stored ticket vectors and returns the **top-k** most similar tickets (typically **3–5**), ranked by similarity.

You can also apply metadata filters, for example:

- Only Network category
- Only tickets resolved in the last 12 months

---

## Step 4 — Construct the LLM Prompt and Generate an Answer

The retrieved ticket texts are inserted into a prompt template together with the new incident description.

Example:

```text
You are an IT support assistant. A new incident has been reported.

New incident:
{analyst's description}

Here are similar past resolved incidents:

[INC0012345]
Problem: ...
Resolution: ...

[INC0009876]
Problem: ...
Resolution: ...

[INC0008321]
Problem: ...
Resolution: ...

Based on these past resolutions, suggest a likely fix for the new incident.

Cite which ticket number(s) your suggestion is based on.

If none of the past tickets seem relevant, say so clearly.
```

This is the **generation** step.

The LLM (via an API or an in-house model) writes a natural-language answer grounded in the retrieved tickets rather than guessing from general knowledge.

---

## Step 5 — Analyst Reviews and Resolves

The analyst receives:

- A suggested fix
- Source ticket citations

They apply or adapt the recommendation and close the ticket in ServiceNow as normal.

---

## Step 6 — Feedback Loop

The newly closed ticket becomes future training data.

During the next ingestion run it is:

1. Extracted
2. Embedded
3. Added to the vector database

The knowledge base therefore grows continuously.

A lightweight feedback mechanism (e.g., 👍 / 👎 on suggestions) should also be implemented to measure answer quality and help:

- Tune retrieval parameters
- Identify poor-quality source tickets
- Improve future recommendations


---
---
---

# Deployment

**Overview:**

FastAPI backend in a container on Azure App Service, managed vector DB (Pinecone), and a scheduled Azure Function for ingestion.

## **Deployment Details:**
## Architecture Recap

| Component | Technology |
|-----------|------------|
| **Compute** | Azure Container Apps or Azure App Service (hosting the FastAPI backend) |
| **LLM + Embeddings** | Azure OpenAI Service |
| **Vector Database** | Pinecone (external SaaS, accessed via API) |
| **Secrets Management** | Azure Key Vault |
| **Scheduled Ingestion** | Azure Functions (Timer Trigger) |
| **Identity** | Microsoft Entra ID (Azure Active Directory) |
| **Monitoring** | Azure Application Insights |
| **CI/CD** | GitHub Actions or Azure DevOps Pipelines |

---

## Step 1 — Provision Azure OpenAI

Request access and deploy your models in Azure OpenAI Studio:

- Deploy a **chat model** (e.g., GPT-4o)
- Deploy an **embedding model** (e.g., `text-embedding-3-large`)

Record the following information:

- Azure OpenAI endpoint URL
- Chat deployment name
- Embedding deployment name
- API key or Managed Identity configuration

> Both deployments are required:
>
> - **Embeddings** are used during ingestion and retrieval.
> - **Chat model** is used to generate responses.

---

## Step 2 — Set Up Pinecone

Create a Pinecone project and index.

Configure:

- Index dimensions matching your embedding model
  - Example: **3072 dimensions** for `text-embedding-3-large`
- Similarity metric:
  - **Cosine similarity**

Pinecone is fully managed, so no infrastructure needs provisioning.

Record:

- Pinecone API key
- Environment/Host URL

---

## Step 3 — Store Secrets in Azure Key Vault

Store every credential in Key Vault rather than embedding them in code or CI/CD.

Recommended secrets:

- Azure OpenAI endpoint
- Azure OpenAI API key (or use Managed Identity)
- Pinecone API key
- ServiceNow credentials
- OAuth client secrets

---

## Step 4 — Containerize the FastAPI Backend

### `requirements.txt`

```text
fastapi
uvicorn
openai
pinecone-client
azure-identity
azure-keyvault-secrets
```

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Step 5 — Push the Image to Azure Container Registry

---

## Step 6 — Deploy the Backend to Azure Container Apps

Azure Container Apps is generally preferable to Azure App Service because it:

- Scales to zero when idle
- Is cost-efficient for internal tools
- Supports streaming HTTP responses for chat applications

Create the Container Apps environment:

---

## Step 7 — Enable Managed Identity

Instead of storing Azure OpenAI credentials as environment variables:

1. Assign a Managed Identity to the Container App.
2. Grant it access to:
   - Azure Key Vault
   - Azure OpenAI

Benefits:

- No Azure secrets stored in GitHub.
- Credentials never appear in deployment files.
- Runtime authentication is automatic.

---

## Step 8 — Deploy the Ingestion Pipeline

Deploy a Timer-triggered Azure Function.

Responsibilities:

- Retrieve newly closed ServiceNow incidents
- Clean and preprocess text
- Generate embeddings
- Upsert vectors into Pinecone

Create the Function App:


Configure:

- Managed Identity
- Key Vault access
- Azure OpenAI access
- Timer trigger

Example timer schedule:

```text
0 0 2 * * *
```

(Runs daily at **2:00 AM**.)

---

## Step 9 — Configure CI/CD

Deploy automatically on every push to `main`.


Only one GitHub secret is required:


All other credentials remain inside Azure Key Vault.

---

## Step 10 (Future Development) — Secure Analyst Access

If the chatbot is a standalone web application:

1. Register it in Microsoft Entra ID.
2. Enable Easy Auth on the Container App **or** implement OIDC in FastAPI.

Analysts authenticate using their existing corporate credentials.

Example:

---

## Step 11 — Configure Monitoring

Create an Application Insights instance.

Connect both:

- Container App
- Azure Function

Capture telemetry including:

- Request latency
- Errors and exceptions
- Token usage
- Retrieved Pinecone documents
- Prompt version
- User feedback (thumbs up/down)

---

## Step 12 (Future Developments) — Create a Staging Environment

Provision a duplicate environment with a `-staging` suffix.

Use:

- Separate Azure Container App
- Separate Azure OpenAI deployment
- Separate Pinecone index
- Separate resource group (recommended)

Validate:

- Prompt updates
- Retrieval improvements
- Model changes

before promoting to production.

Azure Container Apps also supports **traffic-splitting between revisions** for gradual rollouts.

---
---
---

# What is RAG

RAG stands for Retrieval-Augmented Generation. It's a technique where an AI model first retrieves relevant information from an external knowledge source—such as documents, a database, or a vector store—and then uses that information to generate a more accurate and context-aware response. This helps reduce hallucinations and allows the model to answer questions using up-to-date or domain-specific data without retraining the model.

# Cosine Similarity

Cosine similarity measures how similar two vectors are by looking at the angle between them, not their length. Every piece of text (a query or a ticket) becomes a vector — a long list of numbers positioned somewhere in this high-dimensional "meaning space." Cosine similarity gives you a score between -1 and 1 (in practice usually 0 to 1 for text embeddings): 1 means the vectors point in exactly the same direction (essentially identical meaning), 0 means they're unrelated, and negative means opposite meaning.


# Semantic Search

Semantic search is the process built on top of vector embeddings. Instead of matching exact keywords like a traditional database query (e.g., `WHERE description LIKE '%VPN%'`), it compares the **meaning** of a user's query with the meaning of every stored document.

For example, a query such as:

> "Can't connect to remote network"

can successfully retrieve a ticket titled:

> "VPN client failing to authenticate"

Even though the two texts share few or no exact keywords, they express nearly the same idea. Their embedding vectors therefore point in similar directions in vector space, resulting in a high **cosine similarity** score.


# Hallucinations

explicitly instruct the model to only use the provided context and to say "no matching precedent found" when retrieval confidence is low; always display the source ticket numbers so the analyst can verify against the original before acting; and consider a similarity score threshold — if the best match is still weakly similar, don't even attempt to generate an answer, just show "no strong match found" instead of forcing a shaky one.

- **Grounding (RAG):** Retrieve relevant documents, databases, or web results and generate answers based on that evidence.
- **Prompt engineering:** Instruct the model to answer only from provided context and say "I don't know" when evidence is insufficient.
- **Use system instructions:** Set clear behavioral rules, such as avoiding speculation and requiring evidence-backed responses.
- **Citations and source attribution:** Ask the model to provide references or quote the source used for each claim.
- **Confidence thresholds:** Require the model to abstain or flag uncertainty when confidence is low.


- **Human-in-the-loop review:** Route high-risk or low-confidence responses to a human reviewer.
- **Knowledge-base updates:** Keep retrieval indexes and external data sources current so the model uses fresh information.


# Temperature in LLMs

Temperature in an LLM controls how random or creative the model’s output is.

## Simple idea

- **Low temperature** → more strict, predictable, factual  
- **High temperature** → more creative, diverse, unpredictable

- **Smaller context windows with relevant retrieval:** Provide only the most relevant information to reduce distractions from irrelevant context.
- **Fact-checking pipelines:** Run the generated response through a secondary model or rule-based fact checker before presenting it.
- **Model selection:** Use models that are optimized for factual accuracy and tool use for knowledge-intensive tasks.


# Measuring Success

1. Retrieval quality (does it find the right past tickets?)
2. Answer quality (is the generated suggestion actually helpful?)
3. Adoption and usage
4. Feedback signal (A simple thumbs up/down on each suggested answer gives you a running satisfaction rate, and — importantly — lets you flag which source tickets are consistently linked to bad suggestions)
5. Business outcome metrics — the ones that matter most to leadership


# Docker

> Docker let us package the application and its dependencies so it behaved consistently across development, testing, and production environments.


# CI/CD
```text
Code Push
     ↓
Tests Run
     ↓
Docker Image Builds
     ↓
Deploy
```

# Prompt Engineering
- Step 1 — Start with a baseline prompt
- Step 2 — Build a test set of real incidents
- Step 3 — Run the test set and manually review outputs
- Step 4 — Iterate on specific, isolated changes
- Step 5 — Version and log your prompts
- Step 6 — Monitor in production, not just in testing
- Step 7 — Separate "retrieval problems" from "prompt problems" when debugging



# React

React steps:

When the user submits a prompt in the React frontend, React sends an HTTP request (usually a POST request) to the backend API. The backend processes the request, calls the LLM or other services if needed, gets the response, and sends it back to React. React then updates the UI and displays the response to the user.

**React Advantages:**

- **Reusable components:** Write a component once (for example, a Button or ProductCard) and use it throughout your app.
- **Automatic UI updates:** When data changes, React updates the affected parts of the page automatically.
- **Easier maintenance:** Splitting the UI into components makes the codebase easier to understand and modify.
- **Good performance:** React efficiently updates only the parts of the page that changed, rather than rebuilding the entire page.
- **Large ecosystem:** There are many libraries and tools that integrate well with React.





---




---
---
---


# AI Product Analyst Interview Preparation Guide

## What the AI Manager Is Likely Trying to Evaluate

In a 30-minute interview, they'll likely be trying to answer these questions:

- Can this person build software?
- Do they understand modern GenAI applications beyond just calling ChatGPT?
- Can they explain technical concepts clearly?
- Are they curious and coachable?

Since it's a new graduate role, they're **not** expecting someone who has deployed enterprise AI systems. They're looking for someone with strong fundamentals and the ability to learn quickly.

---

# Priority 1: Be Able to Talk Deeply About Your Projects

This will probably make up **50% of the interview**.

### Expect questions like:

- Tell me about yourself.
- Which AI project are you most proud of?
- Walk me through one project from start to finish.
- What was your contribution?
- What challenges did you face?
- If you had another month, what would you improve?

## For Every Project on Your Resume, Prepare This Structure

### Problem

What problem were you solving?

### Architecture

```text
Frontend
    ↓
Backend
    ↓
AI Model
    ↓
Database
```

Draw it on paper if needed.

### Tech Stack

Be prepared to explain why you chose:

- Python
- FastAPI
- React
- Azure/OpenAI
- Vector database

### Challenges

Examples include:

- Hallucinations
- Latency
- Prompt engineering
- Authentication
- Deployment
- Scaling

### Impact

Numbers always help.

Examples:

- Reduced processing time by **30%**
- Classified **10,000 documents**
- Supported **100 users**

---

# Priority 2: Python + FastAPI

The job description specifically mentions **FastAPI**.

You don't need to memorize syntax.

Know:

- Why FastAPI?
- Difference between Flask and FastAPI
- REST APIs
- GET vs POST
- JSON
- Request/Response
- Async programming

### Example Question

> If React sends a prompt to your backend, what happens?

### Good Answer

```text
React UI
    ↓
POST Request
    ↓
FastAPI Endpoint
    ↓
OpenAI API
    ↓
Receive Response
    ↓
Return JSON
    ↓
Display in UI
```

---
---
---
---

# Priority 6: AI Product Thinking

This is important because the title is **AI Product Analyst**, not just AI Developer.

### Possible Question

> How would you improve IT operations using GenAI?

### Ideas

- ServiceNow ticket summarization
- Incident classification
- Root cause analysis
- Chatbot for internal employees
- Documentation search
- Runbook generation

---

# Priority 7: Behavioral Questions

Prepare STAR stories.

### Examples

- Tell me about a difficult project.
- Tell me about a conflict.
- Tell me about learning something quickly.
- Tell me about failure.
- Tell me about working with teammates.

---

# Questions They May Ask

## Backend

- How would you expose your model using an API?

## Product

- Suppose customer responses become slow.
- How would you debug it?


---
---
---
---
---
---
---
---
---
---
# AI Product Analyst Interview Preparation (Resume-Based)

Thanks for sharing your resume. Based on this, I think the interview is likely to be **resume-driven rather than algorithm-heavy**.

One thing I want to point out before we get into preparation:

> **Make sure every bullet on your resume is something you can explain in detail.**

For example, if you wrote:

> "Reduced ticket resolution by 30%."

Be prepared to answer:

- How was that measured?
- What was the baseline?
- How much of the improvement came from your work versus the team's?
- What exactly did your application do?

The AI manager will often dig one or two levels deeper. If your resume accurately reflects your experience and you can explain it clearly, that's a strong position to be in.

---

# What I Think the Interview Flow Will Look Like

---
---
---

# They Will Almost Certainly Ask About Your AI Application Developer Role

Expect to spend **10–15 minutes** discussing this experience.
### Possible Questions

- What problem was the application solving?
- Walk me through the architecture.

### Architecture

```text
React Frontend
        ↓
FastAPI Backend
        ↓
Azure OpenAI API
        ↓
Response
        ↓
Frontend Displays Summary
```

Then expect follow-up questions:

- Why FastAPI?
- Why React?
- How did Azure OpenAI fit in?
- What prompts did you use?
- How did you test it?
- What challenges did you face?
- How did users interact with it?
- How was it deployed?

---
---

# FastAPI Questions

Since FastAPI is explicitly mentioned in the job description, expect questions like:

- Why FastAPI over Flask?
- What is a REST API?
- Explain a POST request.
- What does JSON look like?
- How does the frontend communicate with the backend?
- How do you handle errors?
- How would you secure an API?

---

# Azure OpenAI

Potential questions:

- How did you integrate Azure OpenAI?
- What's the difference between Azure OpenAI and OpenAI?

### Good High-Level Answer

> The models are similar, but Azure OpenAI integrates with Azure services, provides enterprise security and governance features, and helps organizations meet compliance requirements.

---

# Docker

Don't just say:

> "I used Docker."

Instead, explain **why**:

> Docker let us package the application and its dependencies so it behaved consistently across development, testing, and production environments.

---

# CI/CD

You mention GitHub Actions.

Be ready to explain the deployment pipeline:

```text
Code Push
     ↓
Tests Run
     ↓
Docker Image Builds
     ↓
Deploy
```

---


---

# Product Thinking

Since the title is **AI Product Analyst**, don't focus only on implementation.

Be prepared for questions like:

> How would you know if your AI solution is successful?

Talk about measurable outcomes such as:

- Reduced resolution time
- Improved user satisfaction
- Fewer repeated tickets
- Lower manual effort
- Better response quality

Showing that you think about **business outcomes—not just code—will help distinguish you.**

---

# Behavioral Questions

Prepare STAR examples for:

- A technical challenge
- Working with teammates
- Learning a new technology quickly
- Receiving feedback
- Handling multiple priorities

---

# Questions to Ask the AI Manager

I would ask one or two thoughtful questions, such as:

- "What kinds of GenAI use cases is the team most excited about right now?"
- "How do you balance experimenting with new AI capabilities while maintaining reliability in production?"
- "What would you hope someone in this role accomplishes during their first six months?"

These questions show interest in both the technology and the business context.

---

# One Final Suggestion

One thing stands out to me:

Your resume reads as an almost perfect match to the job description—so much so that the AI manager may naturally probe to understand the depth of your experience.

That's not a bad thing, but it means you should be ready to go beyond the bullet points.

If you can clearly explain:

- The architecture
- Technical trade-offs
- Challenges
- Design decisions
- Your individual contributions
- The business impact

...you'll likely make a much stronger impression than someone who simply lists the technologies they used.

# API Basics:

## Why FastAPI?

FastAPI is a modern Python framework for building APIs that is fast, easy to use, and supports automatic validation and documentation out of the box.

---

## Difference between Flask and FastAPI

Flask is simpler and synchronous by default, while FastAPI is faster, supports async programming, and automatically generates API docs and data validation.

---

## REST APIs

REST APIs are a way for applications to communicate over HTTP using standard methods like GET, POST, PUT, and DELETE to manage resources.

---

## GET vs POST

- **GET** is used to retrieve data from a server  
- **POST** is used to send data to a server (often to create or process something)

---

## JSON

JSON is a lightweight data format used to store and exchange data between a client and a server in a readable key-value structure.

---

## Request / Response

- A **request** is what a client sends to a server (asking for data or action)  
- A **response** is what the server sends back after processing it

---

## Async Programming

Async programming allows a program to handle multiple tasks at the same time without waiting for each one to finish, improving efficiency especially for I/O operations.


# React Basics:

## Components

Components are reusable building blocks of a React app that define part of the UI, like a button, navbar, or product card.

---

## State

State is data inside a component that can change over time and automatically updates the UI when it changes.

---

## Props

Props are inputs passed from a parent component to a child component to make components reusable and dynamic.

---

## Fetch API

Fetch API is a built-in JavaScript method used in React to make HTTP requests to get or send data from/to a server.

---

## Calling Backend APIs

Calling backend APIs in React means sending requests (like GET or POST) to a server to fetch or update data and then using that data to update the UI.

# Azure Basics

## Azure Functions

Azure Functions is a serverless compute service that runs small pieces of code in response to events (like HTTP requests) without managing servers.

---

## Azure App Service

Azure App Service is a platform for hosting web apps and APIs, where Microsoft handles infrastructure, scaling, and deployment.

---

## Azure Storage

Azure Storage is a service for saving data in the cloud, such as files, blobs, tables, and queues, in a scalable and durable way.

---

## Azure Key Vault

Azure Key Vault is a secure service used to store and manage sensitive information like API keys, passwords, and certificates.


# Questions
- What would success look like in the first 3-6 months?
  >>> That's great to hear. Thank you for sharing that.
- What kinds of applications would I be building?
  >>> That's helpful. Could you also tell me a bit about...
- Are developers encouraged to experiment with new AI tools and workflows?
  >>> That sounds like an environment I'd really enjoy working in. Thanks for sharing.
- What are the next steps of the hiring process?
- What are the biggest technical challenges the team is working on right now?
- How do junior team members typically receive mentorship and feedback?