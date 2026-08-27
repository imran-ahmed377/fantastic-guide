

“How would you design a scalable API?”

“Why are you interested in this position?”

“Why do you want to work for our company?”

“Tell me about your relevant experience.”

“Tell me about a challenging situation you faced and how you handled it.”

“Why should we hire you?”

RAG Pipeline Design Considerations:
  - Document ingestion
  - Chunking
  - Embeddings
  - Vector search
  - Prompt construction
  - LLM selection
  - Citations/source grounding
  - Authentication
  - Access control
  - Hallucination prevention
  - Logging
  - Latency
  - Cost
  - Evaluation


# Table of Contents
- [Greetings](#greetings)
- [Intro](#intro)
- [EXP1: AI Developer (Exeevo sept 2025 - Apr 2026)](#exp1-ai-developer-exeevo-sept-2025---apr-2026)
- [EXP2: Python Backend Developer (Vista Print june 2023 - Aug 2024)](#exp2-python-backend-developer-vista-print-june-2023---aug-2024)
- [Project: LLM-Powered RAG Chatbot API](#project-llm-powered-rag-chatbot-api)
---
- [What is Marsh](#what-is-marsh)
- [Why Marsh](#why-marsh)
- [Questions]

---
- [Technical QnA](#technical-qna)
  - [1. Python Backend — FastAPI & Flask](#1-python-backend--fastapi--flask)
  - [2. End-to-End RAG Pipeline for Enterprise](#2-end-to-end-rag-pipeline-for-enterprise)

# Greetings
I am so happy to be here!

# Intro
Thank you for giving me the opportunity, I am Imran Ahmed, I am an AI Developer with experience in AI Agent Development, LLM, RAG, and FastAPI. In my recent role at Exeevo I have developed and deployed end to end RAG based Agentic AI solution. My proudest results are improving retrieval accuracy by 25% through better embeddings and vector search, reducing query latency by 20% by optimizing PostgreSQL and SQL Server integrations.

I am a very organized person, I like to work in teams, and I pick up new technologies quickly.

I am applying to this job because of the use of AI for risk assessment and use of AI for something actually useful for the society. Also lot of skills perfecty allign with my experience.

Outside of work, I spend my time learning new AI technologies, and contributing to open-source projects. Currently I am working on a open-source project that ranks city's based on multiple factors like safety, cost of living, and quality of life. I also enjoy traveling, and swiming. 



# EXP1: AI Developer (Exeevo sept 2025 - Apr 2026)
In my most recent role as an AI Developer at Exeevo, I worked on AI solutions that helped employees quickly find information and automate repetitive tasks. 

For example, I built an AI-powered chatbot using Python, FastAPI, and RAG, where company information was stored in PostgreSQL with pgvector. The system could understand a user's question, find the most relevant information from internal documents, and generate an answer using an LLM such as GPT. I also built AI agents using MCP and tool calling that could interact with internal APIs and databases to automate multi-step tasks. I focused on testing and improving the quality of AI responses, which helped improve retrieval accuracy by 25% and reduce AI-related errors by 35%. So, my main responsibility was taking AI capabilities like GPT and turning them into reliable applications that could be used in real business processes.


# EXP2: Python Backend Developer (Vista Print june 2023 - Aug 2024)
I worked as a Python Backend Developer at Vistaprint. My main responsibility was building and maintaining backend services that supported the company’s business applications and handled more than 10,000 transactions per day. I mainly used Python, Flask, and PostgreSQL. For example, I designed and optimized database queries and schemas to make applications respond faster, which improved performance by about 40%. I also used Docker to package the applications and CI/CD pipelines to automate testing and deployment, reducing release time by 25%. I worked with distributed teams to deliver secure and reliable software while meeting tight deadlines.


# Project: LLM-Powered RAG Chatbot API
The goal of this project was to build a chatbot that could answer questions based on company-specific documents instead of relying only on general AI knowledge.

For example, if an employee asked, ‘What is our vacation policy?’, the chatbot could search the company’s internal documents and provide an answer based on that information.

My role was to build the backend using Python and FastAPI. I used RAG (Retrieval-Augmented Generation) to first find relevant information from documents using embeddings and pgvector in PostgreSQL, and then provided that information to a GPT model to generate the answer. I also added prompt versioning, authentication, and content-filtering guardrails to make the system more reliable and secure. I tested different prompts and models to balance answer quality, speed, and cost.

As a result, the chatbot provided more accurate, context-specific answers, and the guardrails improved output safety by about 30%. The project demonstrated how we could turn an LLM into a practical business application rather than just a general-purpose chatbot.

---

# What is Marsh
Marsh is a global risk and insurance advisory company that helps businesses understand their risks, protect themselves from major financial losses, and make better decisions about the future.


# Why Marsh
- I worked on a very similar Project at Exeevo, where I built a RAG-based chatbot that could answer questions using company-specific documents.  

I want to work at Marsh because I really connect with its purpose of building the confidence to thrive through the power of perspective. I like the idea of using technology and AI to turn complex information into useful insights, and I believe my experience building AI and RAG solutions can help Marsh deliver practical solutions for its clients.


# Questions
- What would success look like in this position during the first six months?
>I appreciate you explaining that
- What are the biggest challenges someone in this role would be expected to tackle?
>That’s really helpful
- How would you describe the team I would be working with?
>That’s really helpful
- What will be the next round of interviews like? Will there be any technical assessments or coding challenges?
>That’s really helpful

>I believe that covers everything I wanted to ask.


# Table of Contents
- [Greetings](#greetings)
- [Intro](#intro)
- [EXP1: AI Developer (Exeevo sept 2025 - Apr 2026)](#exp1-ai-developer-exeevo-sept-2025---apr-2026)
- [EXP2: Python Backend Developer (Vista Print june 2023 - Aug 2024)](#exp2-python-backend-developer-vista-print-june-2023---aug-2024)
- [Project: LLM-Powered RAG Chatbot API](#project-llm-powered-rag-chatbot-api)
---
- [What is Marsh](#what-is-marsh)
- [Why Marsh](#why-marsh)
---
- [Technical QnA](#technical-qna)
  - [1. Python Backend — FastAPI & Flask](#1-python-backend--fastapi--flask)
  - [2. End-to-End RAG Pipeline for Enterprise](#2-end-to-end-rag-pipeline-for-enterprise)

---

# Technical QnA:
### 1. Python Backend — FastAPI & Flask

**Simple definition:**
A Python backend is the **part of an application that runs behind the scenes**. It receives requests, processes information, talks to databases or AI models, and sends a response back to the user.

**FastAPI and Flask** are Python frameworks that help us build these backend services and APIs.

**Simple example:**
Imagine an employee asks a chatbot:

> “How many vacation days do I have?”

The backend receives the question → checks the employee's information in the database → processes the request → sends the answer back to the chatbot.

**Common use cases:**

- Building REST APIs
- Connecting applications to databases
- Building AI/LLM APIs
- User authentication
- Processing business requests
- Real-time responses using WebSockets

**Easy interview explanation:**

> “I use Python with FastAPI or Flask to build the backend services that connect the user interface with databases, AI models, and other business systems.”

---

# 2. End-to-End RAG Pipeline for Enterprise

### Simple definition

**RAG (Retrieval-Augmented Generation)** is a way to make an AI model answer questions using **an organization's own information**.

Instead of asking GPT to answer from its general knowledge, we first **search the company's trusted documents**, find the relevant information, and give that information to the AI to generate the answer.

### Simple example

Imagine a company has thousands of documents containing:

- HR policies
- Employee benefits
- Product information
- Customer support documents
- Company procedures

An employee asks:

> **“What is the company's work-from-home policy?”**

The RAG system does this:

**1. Documents →** Collect company documents  
↓  
**2. Chunking →** Break documents into smaller pieces  
↓  
**3. Embeddings →** Convert those pieces into numerical representations  
↓  
**4. Vector Database →** Store them in **PostgreSQL + pgvector**  
↓  
**5. User Question →** Employee asks a question  
↓  
**6. Retrieval →** Find the most relevant document sections  
↓  
**7. LLM →** Send the question + relevant information to **GPT**  
↓  
**8. Answer →** Generate a response based on the company's information

### What does "end-to-end" mean?

It means you build and manage the **whole process**, from getting the company's documents into the system to delivering the final answer to the user.

### Enterprise RAG use cases

- **HR:** “What is our parental leave policy?”
- **Customer support:** “How do I troubleshoot this product?”
- **Legal:** “What does this contract say about termination?”
- **Finance:** “What is our expense reimbursement policy?”
- **IT:** “How do I request access to this system?”
- **Sales:** “What features are included in our enterprise plan?”

### Easy interview explanation

> “RAG allows an AI application to answer questions using a company's own information. In my project, I used **Python and FastAPI** for the backend, **PostgreSQL with pgvector** for storing and searching document embeddings, and **GPT** to generate the final answer. The pipeline takes company documents, converts them into searchable information, retrieves the relevant content when a user asks a question, and then gives that context to the LLM to generate a more accurate answer.”

# Table of Contents
- [Greetings](#greetings)
- [Intro](#intro)
- [EXP1: AI Developer (Exeevo sept 2025 - Apr 2026)](#exp1-ai-developer-exeevo-sept-2025---apr-2026)
- [EXP2: Python Backend Developer (Vista Print june 2023 - Aug 2024)](#exp2-python-backend-developer-vista-print-june-2023---aug-2024)
- [Project: LLM-Powered RAG Chatbot API](#project-llm-powered-rag-chatbot-api)
---
- [What is Marsh](#what-is-marsh)
- [Why Marsh](#why-marsh)
---
- [Technical QnA](#technical-qna)
  - [1. Python Backend — FastAPI & Flask](#1-python-backend--fastapi--flask)
  - [2. End-to-End RAG Pipeline for Enterprise](#2-end-to-end-rag-pipeline-for-enterprise)


# Notes
- The legacy system maybe using Flask (Why do they want flask?) so they maybe want new system to communicate with the older system

- How the system will calculate this years data with last years data? 

- How embeddings works? How to retrieve the most relevant information from the database?

- How hallucinations can be prevented? How to make sure the answer is accurate and relevant?

- How to design the vector database schema for storing embeddings? How to optimize retrieval speed and accuracy?

- how asynchronous and synchronous processing can be used in the RAG pipeline to improve performance and scalability?

- caching strategies for frequently asked questions to reduce retrieval time and improve response speed.

- Can User A accidentally retrieve User B's client information?

- system prompt design



# End to end system design
                         ┌──────────────────────┐
                         │   Marsh Employee     │
                         │   / Client / App     │
                         └──────────┬───────────┘
                                    │
                                    │ REST (sync) / WebSocket (async)
                                    ▼
                         ┌──────────────────────┐
                         │ Backend API Layer    │
                         │ • Flask  (sync)      │
                         │ • FastAPI (async)    │
                         │ • Auth, rate limit   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Agent Orchestrator  │
                         │ • Prompt design      │
                         │ • Tool/function call │
                         │ • MCP                │
                         └──────────┬───────────┘
                                    │
                     ┌──────────────┼──────────────┐
                     ▼                             ▼
        ┌─────────────────────┐        ┌─────────────────────┐
        │   RAG Pipeline       │        │   Other Tools        │
        │ • Embeddings         │        │ • SQL (SQLAlchemy)   │
        │ • Vector search      │        │ • scikit-learn       │
        │ • pgvector           │        │ • Files / messaging  │
        └──────────┬───────────┘        └──────────┬───────────┘
                    │                               │
                    └───────────────┬───────────────┘
                                     ▼
                         ┌──────────────────────┐
                         │      LLM Layer       │
                         │ • GPT / open-source  │
                         │ • Guardrails         │
                         │ • Content filtering  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Response to Client  │
                         │ • REST (full JSON)   │
                         │ • WebSocket (stream) │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Observability     │
                         │ • Eval / monitoring  │
                         │ • Perf profiling     │
                         └──────────────────────┘

        ┌─────────────────────────────────────────────────┐
        │  Data Layer: PostgreSQL + pgvector, SQL Server,  │
        │  SQLAlchemy, indexing, transactions              │
        └─────────────────────────────────────────────────┘

        ┌─────────────────────────────────────────────────┐
        │  DevOps: Docker → Kubernetes → GitHub Actions    │
        │  → CI/CD                                         │
        └─────────────────────────────────────────────────┘