# Table of Contents
- [Greetings](#greetings)
- [Intro](#intro)
- [Why do you want to leave your current role?](#why-do-you-want-to-leave-your-current-role)
- [EXP1: AI Solutions Analyst (Exeevo sept 2025 - Present)](#exp1-ai-solutions-analyst-exeevo-sept-2025---present)
- [EXP2: Data Analyst (Vista Print june 2023 - Aug 2024)](#exp2-data-analyst-vista-print-june-2023---aug-2024)
- [Project: Enterprise AI Governance Framework](#project-enterprise-ai-governance-framework)

---

- [Why BMO](#why-bmo)
- [Questions](#questions)

---

- [Technical QnA](#technical-qna)
  - [1. LLMs](#1-llms)
  - [2. AI Agents](#2-ai-agents)
  - [3. MCP](#3-mcp)
  - [4. Tool Calling](#4-tool-calling)
  - [5. Securing RAG Pipelines](#5-securing-rag-pipelines)

---

# Greetings

I am so happy to be here!

# Intro
I’m a Data Scientist with over two years of experience working on AI and analytics solutions. In my current role, I’ve been focused heavily on GenAI—building AI agents with Copilot Studio, evaluating vendor solutions, and supporting testing, monitoring, and AI governance. I also have a strong foundation in machine learning and Python. What attracted me to this BMO role is that it brings together the things I enjoy most: building practical AI solutions, working with business stakeholders, and making sure AI is deployed responsibly in a regulated environment.

# Why do you want to leave your current role?
I’m looking for a new opportunity where I can take on more responsibility and have a bigger impact.

# EXP1: AI Solutions Analyst (Exeevo sept 2025 - Present)

In my current role as an AI Solutions Analyst, I focus on implementing practical AI solutions for business teams. For example, I built AI agents using Microsoft Copilot Studio to automate employee questions and repetitive workflows. For one HR use case, I connected the agent to the company’s internal knowledge base using a RAG approach, so it could retrieve approved information before generating an answer. This achieved about 90% response accuracy and reduced query resolution time by 35%.

My role doesn’t stop at building the solution. I follow a full process: first, I understand the business problem, then prototype the AI solution, test its accuracy and reliability, monitor its performance, and prepare the governance documentation needed for approval. I also evaluate third-party AI tools and work with business and risk teams to make sure the solutions are practical, reliable, and compliant.

# EXP2: Data Analyst (Vista Print june 2023 - Aug 2024)
I worked as a Data Analyst at VistaPrint, where I used data to identify operational issues and help teams make better decisions. I mainly worked with Python and SQL to clean and analyze data, and built predictive models using techniques such as regression and classification to identify patterns and forecast outcomes.

For example, I developed predictive models to identify factors affecting process efficiency, which improved the team’s ability to identify improvement opportunities by about 15%. I also monitored the performance of our analytics solutions and helped with model validation and documentation to make sure they followed internal risk policies. Finally, I presented the results through Power BI and Tableau dashboards so that non-technical teams could easily understand the findings and take action.


# Project: Enterprise AI Governance Framework

The goal of this project was to create a consistent process for reviewing and approving AI solutions before they were used in the business.

For the action, I created governance templates in Confluence and SharePoint to document things like the AI use case, risks, validation results, and approval requirements. I also built a testing framework in Python to evaluate AI agents for accuracy, reliability, bias, and consistency. For example, if an HR agent was answering employee questions, we would test whether it gave accurate answers, whether it responded consistently to similar questions, and whether it showed any unintended bias. I used these test results to create standardized validation and approval documentation.

The result was a more consistent AI review process and reduced governance review turnaround time by about 20%. It also made it easier for business, risk, and compliance teams to understand and approve AI solutions.

---

# Why BMO
I like the mission of BMO and its focus on making a positive impact for customers, employees, and communities. I’m also excited about BMO’s focus on using AI to improve the employee and customer experience. This role is a great fit for me because it combines the areas I’ve been working in—AI solutions, GenAI, data science, and AI governance

---

# Questions 

- What would success look like in this role?
- What are the key challenges in this role?
- How do you measure the impact of your work?

# Table of Contents
- [Greetings](#greetings)
- [Intro](#intro)
- [Why do you want to leave your current role?](#why-do-you-want-to-leave-your-current-role)
- [EXP1: AI Solutions Analyst (Exeevo sept 2025 - Present)](#exp1-ai-solutions-analyst-exeevo-sept-2025---present)
- [EXP2: Data Analyst (Vista Print june 2023 - Aug 2024)](#exp2-data-analyst-vista-print-june-2023---aug-2024)
- [Project: Enterprise AI Governance Framework](#project-enterprise-ai-governance-framework)

---

- [Why BMO](#why-bmo)
- [Questions](#questions)

---

- [Technical QnA](#technical-qna)
  - [1. LLMs](#1-llms)
  - [2. AI Agents](#2-ai-agents)
  - [3. MCP](#3-mcp)
  - [4. Tool Calling](#4-tool-calling)
  - [5. Securing RAG Pipelines](#5-securing-rag-pipelines)

---

# Technical QnA:

## 1. LLMs

**Simple definition:**
An **LLM (Large Language Model)** is an AI model that understands and generates human-like text.

**Simple example:**
Think of ChatGPT. You ask, *“Write an email to a customer explaining a delayed order,”* and the LLM generates the response.

**Business use cases:**

- Summarizing documents or customer feedback
- Writing emails and reports
- Answering employee questions
- Extracting information from documents
- Generating business content

**Interview answer:**

> “An LLM is the underlying AI model that understands and generates text. For example, an employee could ask a question in natural language, and the LLM can understand the question and generate a useful response.”

---

# 2. AI Agents

**Simple definition:**
An **AI agent** is an AI system that can **understand a goal, decide what steps to take, and use tools or information to complete the task**.

The easiest way to remember it:

**LLM = thinks and generates**  
**AI Agent = thinks + takes action**

**Simple example:**

An employee asks:

> “I’m joining the company next Monday. What do I need to complete?”

An AI agent could:

1. Understand the request.
2. Look up the onboarding policy.
3. Check the employee's information.
4. Create a checklist.
5. Send the relevant information to the employee.

**Business use cases:**

- HR onboarding agents
- Customer service agents
- IT support agents
- Scheduling agents
- Employee policy assistants
- Automated workflow agents

**Interview answer:**

> “An AI agent goes beyond simply answering a question. It can understand a goal, access information or tools, and take actions to complete a task. For example, an HR agent could look up onboarding policies and provide an employee with the specific steps they need to complete.”

---

# 3. MCP

**Simple definition:**
**MCP (Model Context Protocol)** is a standard way for AI applications to **connect to external tools, data, and systems**.

Think of MCP as a **universal connector between an AI agent and business systems**.

**Simple example:**

Imagine an AI agent needs to answer:

> “What is the status of my vacation request?”

The information may be stored in an HR system.

Instead of building a completely different connection for every AI application, MCP provides a standardized way for the AI application to access that system.

**Business use cases:**

- AI accessing HR systems
- AI accessing CRM data
- AI working with databases
- AI accessing company documents
- AI interacting with business applications

**Interview answer:**

> “MCP is a standard that makes it easier for AI applications to connect with external tools and data. For example, an HR AI agent could use an MCP connection to access an approved HR system and retrieve an employee's vacation information.”

### Easy distinction

**RAG:** AI **reads information**  
**MCP:** AI **connects to systems/tools**  
**Tool calling:** AI **asks a specific tool to perform an action**

---

# 4. Tool Calling

**Simple definition:**
**Tool calling** allows an AI model or agent to decide when it needs an external tool and send that tool a structured request.

**Simple example:**

User asks:

> “What is the current USD to CAD exchange rate?”

The LLM doesn't need to guess. It can call an **exchange-rate tool**, get the current rate, and then give the user the answer.

Another business example:

> “Create a support ticket for my laptop issue.”

The AI agent can call the company's **ticketing system** and create the ticket.

**Business use cases:**

- Creating support tickets
- Sending emails
- Checking inventory
- Retrieving customer information
- Booking appointments
- Querying databases
- Updating CRM records

**Interview answer:**

> “Tool calling allows an AI agent to use external tools when it needs to perform a task. For example, if an employee asks an IT agent to create a support ticket, the agent can call the company's ticketing system and create the ticket instead of just telling the employee how to do it.”

---

# 5. Securing RAG Pipelines

This one is **particularly important for your BMO interview**.

### First: What is RAG?

**RAG = Retrieval-Augmented Generation.**

**Simple definition:**
RAG allows an AI system to **search approved company information before generating an answer**.

Instead of relying only on what the LLM learned during training:

**Question → Search company information → Find relevant information → LLM generates answer**

### Simple example

An employee asks:

> “What is BMO's parental leave policy?”

The AI searches the approved HR documents, retrieves the relevant policy, and uses that information to answer.

---

## What does "securing RAG" mean?

It means making sure the AI **only retrieves information that the user is allowed to see** and doesn't expose sensitive or incorrect information.

### Simple example

Imagine the company has:

- Public HR policies
- Employee salary information
- Manager-only documents
- Confidential legal documents

An employee asks:

> “Show me the salary information for my department.”

A secure RAG system should **check the employee's permissions before retrieving the information**.

The AI should not simply search everything in the database.

### Important security techniques

You can remember these five:

**1. Access control**  
Only retrieve documents the user is authorized to access.

**2. Data filtering**  
Filter sensitive information before it reaches the AI.

**3. Secure document storage**  
Protect the documents and vector database where information is stored.

**4. Prompt-injection protection**  
Prevent malicious instructions inside documents or user prompts from manipulating the AI.

**5. Logging and monitoring**  
Track what information was retrieved and monitor unusual behavior.

### Interview answer

> **“Securing a RAG pipeline means making sure the AI only retrieves and provides information that the user is authorized to access. For example, in an HR assistant, an employee might be allowed to see company policies but not confidential salary information. So I would use access controls and document-level permissions before retrieval, apply data filtering, protect against prompt injection, and monitor the system through logging and testing.”**


# Table of Contents
- [Greetings](#greetings)
- [Intro](#intro)
- [Why do you want to leave your current role?](#why-do-you-want-to-leave-your-current-role)
- [EXP1: AI Solutions Analyst (Exeevo sept 2025 - Present)](#exp1-ai-solutions-analyst-exeevo-sept-2025---present)
- [EXP2: Data Analyst (Vista Print june 2023 - Aug 2024)](#exp2-data-analyst-vista-print-june-2023---aug-2024)
- [Project: Enterprise AI Governance Framework](#project-enterprise-ai-governance-framework)

---

- [Why BMO](#why-bmo)
- [Questions](#questions)

---

- [Technical QnA](#technical-qna)
  - [1. LLMs](#1-llms)
  - [2. AI Agents](#2-ai-agents)
  - [3. MCP](#3-mcp)
  - [4. Tool Calling](#4-tool-calling)
  - [5. Securing RAG Pipelines](#5-securing-rag-pipelines)

---