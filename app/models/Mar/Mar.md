

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




# End to end Agentic AI system design
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



# End to End Embedding Steps

## Step 1: Document Extraction

- **What you do:** You use a code library (like PyPDF, pdfplumber, or LangChain) to open your 1000 PDF pages.
- **The goal:** Strip out the raw text from the pages, separating it from the design and layout.

## Step 2: Chunking (Slicing the Cake)

- **What you do:** You cannot turn an entire 1000-page document into a single vector—it is too much data for the AI to handle. You must cut the text into small, bite-sized pieces called **chunks**.
- **The Golden Rule:** A standard chunk size is about **500 to 1000 words per chunk** (roughly 1 or 2 paragraphs). You also overlap them slightly (e.g., 50 words) so a sentence doesn't get cut in half at the border of a chunk.
- *Result:* Your 1000 PDF pages will turn into roughly **3,000 separate text chunks**.

### How to Decide Chunk Size (Paragraph Length)

A chunk is measured in **tokens** (which roughly equal 3/4 of a word).

- **The Default Choice (512 tokens / ~400 words):** This is a good starting point for many apps. It is long enough to hold a complete thought or paragraph, but short enough to keep retrieval focused.
- **When to Go Smaller (128–256 tokens):** Use smaller chunks if your PDFs are full of short, distinct facts, such as a dictionary, product catalog, FAQ, or a list of employee rules.
- **When to Go Larger (1000+ tokens):** Use larger chunks if your PDFs contain long, academic arguments or legal contract clauses where separating individual sentences would cause important context to be lost.

### How to Decide Overlap Size (The Safety Net)

Overlap means copying a small portion from the end of Chunk 1 and placing it at the beginning of Chunk 2. This helps prevent sentences or ideas from being split across chunk boundaries.

- **The General Rule:** Start with an overlap of around **10% to 20% of your chunk size**.
- If your chunk size is **500 words**, your overlap could be around **50 to 100 words**.
- If you have highly technical content, such as complex formulas or code blocks, you may need more overlap so that important context is not separated.

#### Simple Starting Point

For a typical business PDF, you could start with:

```text
Chunk Size: 512 tokens (~400 words)
Overlap:    10–20% (~40–80 words)
```

## Step 3: Embedding (Translating into Numbers)

- **What you do:** You send all 3,000 text chunks to an **Embedding Model** (like OpenAI's `text-embedding-3-small`).
- **The goal:** The model reads each paragraph and converts it into a long string of numbers (a vector) that mathematically represents its exact meaning.

### How to Choose: `text-embedding-3-small` vs. `text-embedding-3-large`

OpenAI offers two primary embedding options. Think of them as a **Standard Map** vs. a **High-Definition Satellite Map**.

| Feature | `text-embedding-3-small` | `text-embedding-3-large` |
| --- | ---: | ---: |
| **Vector Dimensions** | 1,536 numbers | 3,072 numbers |
| **Accuracy** | Good / Great for standard text | Best / Better at capturing subtle meaning |
| **Cost** | **Lower cost** | **Higher cost** |
| **Database Size** | Uses less storage | Uses roughly 2× the vector storage at full dimensions |

#### Choose `text-embedding-3-small` if:

- You are building a general business chatbot, such as an HR assistant or customer-support FAQ system.
- Your documents are mostly standard business text.
- You want to keep embedding and vector-storage costs low.
- You plan to use a reranker, which can improve the quality of the final retrieved results.

#### Choose `text-embedding-3-large` if:

- Your documents contain complex technical terminology, such as legal contracts, medical research, or advanced engineering manuals.
- You need higher retrieval quality and are willing to pay more for it.
- You need strong multilingual retrieval across languages such as English, Japanese, French, and others.

## Step 4: Upserting (Saving to the Vector Database)

- **What you do:** You upload (or "upsert") these 3,000 vectors into your vector database (like Pinecone).
- **What gets stored:** For each chunk, Pinecone saves three things:
  1. An **ID** (e.g., `chunk_142`).
  2. The **Vector** (the string of numbers for searching).
  3. The **Metadata** (the actual raw text of that paragraph and the page number, so you can read it later).

---

# After Embadding: Searching for Answers

1. **The Question:** A user asks: *"What is the warranty policy on page 450?"*

2. **The Fast Search:** The system converts the question into a vector (a list of numbers). It sends that vector to Pinecone or Azure AI Search, which searches the 3,000 stored chunks and retrieves the **top 50 closest matches**.

3. **The Rerank:** The reranker examines those 50 chunks against the original question. It assigns each chunk a relevance score. For example:

   - Chunk from page 450 → **0.98**
   - Chunk from page 449 → **0.91**
   - Chunk from page 120 → **0.42**
   - Unrelated chunk → **0.08**

   The reranker then sorts the chunks from **most relevant to least relevant**.

4. **The Cutoff:** The system applies its selection rule to the reranked results. For example, if the top score is `0.98`, the system might keep only chunks that are within a certain relative relevance range of that top score.

   This could reduce the 50 retrieved chunks down to **1–5 highly relevant chunks**, depending on the query and the scores.

5. **The Generation:** The system takes those final relevant chunks and places their text into the prompt sent to the **LLM** (such as ChatGPT or Claude).

   For example:

   > *"Answer the user's question using only the following retrieved information: [relevant chunks]."*

6. **The Result:** The LLM reads the retrieved information and generates the final answer.

   For example:

   *"According to page 450, the warranty lasts for 2 years."*

---

# End to End RAG Steps

## Step 1: The User Asks a Question

- **What happens:** A user types a question into your app (e.g., *"What is our company's refund policy for broken items?"*).
- **Explanation:** The system immediately sends this question to an **Embedding Model** (like OpenAI or Cohere) to turn the words into a string of numbers called a vector.

## Step 2: The Fast Search (Retrieval)

- **What happens:** The system takes those numbers and searches your **Vector Database** (where all your company documents are stored as numbers).
- **Explanation:** It does a super-fast math scan across millions of pages. It looks for pages that have a similar mathematical pattern to the user's question.

## Step 3: Grabbing the Rough Draft (Top-K)

- **What happens:** The database quickly grabs a fixed "rough draft" pile of pages—usually the **top 25 to 50 matches**.
- **Explanation:** This step is built for speed, not perfection. The system collects a wide safety net of pages to guarantee the correct answer is hidden somewhere inside the pile.

## Step 4: The Deep Clean (Reranking)

- **What happens:** The system sends those 25 to 50 rough pages, along with the original question, to the **Reranking API** (like Cohere or Jina AI).
- **Explanation:** The reranker reads the text of each page very carefully against the question. It gives every single page a precise relevance score between `0.0` and `1.0`.

## Step 5: Applying the 15% Cutoff Rule (Dynamic-K)

- **What happens:** The system looks at the highest-scoring page (the #1 match) and calculates a cutoff line that is 10% to 15% lower than that score.
- **Explanation:** Instead of keeping all 50 pages, it drops any page that falls below this cutoff line. If the question is simple, it might keep only 1 or 2 pages. If the question is complex, it might keep 5 or 6 pages.

## Step 6: Feeding the Final AI (The Prompt)

- **What happens:** The system takes the final, trimmed down, perfectly ordered pages and pastes them into a prompt for the **Large Language Model (LLM)** (like ChatGPT or Claude).
- **Explanation:** The prompt looks something like: *"Using only these 3 specific pages of text, please answer this question for the user."*

## Step 7: The Final Answer is Delivered

- **What happens:** The LLM reads the perfect, junk-free information and writes a clear response.
- **Explanation:** Because the reranker filtered out all the confusing, unrelated data, the LLM generates a highly accurate answer quickly and without hallucinating (making things up).

---

## 3. The End-to-End Workflow with Azure AI Search

If you build your app inside Microsoft Azure, the workflow becomes **much simpler** because Azure can handle almost every step automatically using its built-in features.

Here is what the **Azure AI Search Workflow** looks like:

### Phase 1: The One-Time Setup (Ingestion)

Instead of writing complex code to chop up your PDFs and turn them into numbers, Azure does it for you:

1. **Upload:** You drop your 1000 PDF pages into an **Azure Blob Storage** folder.
2. **Crack & Chunk:** You turn on Azure's **Document Cracking** feature. It automatically reads the PDFs and chops them into chunks using your chosen chunk/overlap sizes.
3. **Embed:** Azure has a native connection to Azure OpenAI. It automatically passes the chunks to `text-embedding-3-small` and saves the numbers directly into your **Azure AI Search Index**.

### Phase 2: The Live User Query (The RAG Loop)

When a user asks a question, Azure runs its combined search in a single API call:

```text
[User Question]
       ↓
1. Hybrid Search
   (Finds text keywords + vector numbers at the same time)
       ↓
2. Retrieve Top-K
   (Grabs the top 50 matches)
       ↓
3. Semantic Ranker
   (Azure's built-in AI reranks the 50 chunks)
       ↓
4. Top 3–5 Chunks
       ↓
Azure OpenAI GPT-4o
       ↓
Answer Generated
```