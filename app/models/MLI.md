
## Table of Contents

- [Introduce](#introduce)
- [Aspire Ontario Exp (AI-Assisted Software Engineer)(Sept 2025 – Apr 2026)](#aspire-ontario-exp-ai-assisted-software-engineersept-2025--apr-2026)
- [Meallens Exp (Full-Stack Developer) (June 2023 – Sept 2025)](#meallens-exp-full-stack-developer-june-2023--sept-2025)
- [Project 1: Multi-Agent Code Review Pipeline](#project-1-multi-agent-code-review-pipeline)
- [Project 2: Legacy to Modern Migration Framework](#project-2-legacy-to-modern-migration-framework)
- [Zapier](#zapier)
- [About this company?](#about-this-company)
- [Why are you interested in this position?](#why-are-you-interested-in-this-position)
- [Why should we hire you?](#why-should-we-hire-you)
- [How do you use AI?](#how-do-you-use-ai)
- [Non-Technical People.](#non-technical-people)
- [Multiple Task/Project?](#multiple-taskproject)
- [Strong Programming Language?](#strong-programming-language)
- [Comfortable Learning New Tech?](#comfortable-learning-new-tech)
- [What's your biggest weakness?](#whats-your-biggest-weakness)
- [Describe a difficult bug you solved.](#describe-a-difficult-bug-you-solved)
- [Questions](#questions)
- [Bonus Questions](#bonus-questions)




# Introduction

I recently finished my Master's in Applied Computing with a focus on AI at the University of Windsor. Alongside my studies, I worked as a Co-op AI Application Developer at Aspire Ontario, where I built an AI-powered IT support tool. Before that, I was a Full Stack Developer Intern at Meallens. Across both roles, I've built backend systems using Python, and frontend interfaces using React, and worked with AI tools like Azure OpenAI to automate real business processes.

 I enjoy solving problems using modern tools and technologies. I am always eager to learn and continuously improve my skills to stay updated with latest technologies and contribute effectively to build impactful solutions.


# Aspire Ontario Exp (AI Application Developer Co-op)(Jan 2025 – Jan 2026)
So during my co-op at Aspire Ontario, I worked as an AI Application Developer, and my main project was building an AI-powered IT support tool for the team.

On the backend, I used Python and a framework called FastAPI to build the core system, and on the frontend, I built the user interface using React. I worked on both sides of the app.

The biggest part of the project was integrating Azure OpenAI's LLM API, so the tool could automatically summarize IT incidents without write that up manually. This feature saved lots of hours every week.

I also used Docker to package the app, so it would run the same way whether it was on my machine or in production and that made deployments a lot smoother. And I worked in an Agile team, doing sprint planning and delivering new features regularly.

I also wrote automated tests to catch bugs early, which helped cut down production issues. And I got real experience supporting the app after it was live.

Overall, it was a really hands-on role and I got to work across the full stack, build real AI features.



# Meallens Exp (Software Developer Intern) (Jan 2023 – Dec 2024)

During my internship at Meallens, I worked as a Full Stack Software Developer, I worked on both the backend and the frontend of their internal dashboard.

On the backend, I built REST APIs using Python and Flask which are used as the connection points for fetch and send data. 

On the frontend, I built React components for the dashboard, which are the reusable pieces that user sees and interacts with.

I also worked on performance, I noticed some of our database queries were slow, so I dug into the SQL and optimized them, which made our API response time faster.

Overall, it was a great first real-world experience and I learned how to work with distributed team.


# Project 1: GenAI Incident Analyzer (Azure OpenAI + RAG)

So the goal of GenAI Incident Analyzer to help solve a common problem in IT support when the same type of incident keeps happening, but nobody has an easy way to look back and see how it was solved last time. So analysts end up spending hours re-investigating problems that were already solved before.

**Challenge:**

The challenge was how to get an AI to give accurate, trustworthy answers about our specific IT tickets, instead of just generic guesses. A regular AI model doesn't know anything about our company's past incidents on its own.

So the best option was using RAG.  Instead of asking the AI to just guess an answer, the system first looks up similar past incidents from our ServiceNow ticket data, and then feeds that real information to the AI model, which was Azure OpenAI. So the AI's answer is grounded in actual past cases, not just a guess.

When a new incident came in, the system searched through historical tickets to find similar past issues. Then it passed that context to the LLM, which suggested a likely root cause based on what actually worked before. I also wrote and refined the prompts to make the answers more accurate and consistent, and I documented that so the team could reuse it later.

**Result:**
The average time to resolve them dropped from about 4 hours down to 45 minutes. So instead of analysts starting from scratch every time, they had the AI pointing them straight to the likely cause, backed by real historical data."


# Project 2: React + FastAPI Observability Dashboard
The goal of This project was about building a real-time dashboard that showed the health of our systems — things like whether servers were running fine, or if something was starting to go wrong — all in one place instead of people having to check multiple tools separately.

The challenge was that the data was coming from different observability tools — basically monitoring systems that track things like performance and errors — and it needed to be pulled together and shown in a way that was easy to understand at a glance, and updated in real time, not just refreshed every so often.

For the backend, I used FastAPI to build the service that collected and processed the system health data. For the frontend, I used React to build the actual dashboard — the visual part where you could see metrics and system status update live.

I also set up a CI/CD pipeline using GitHub Actions, which basically means every time code changes were made, it would automatically get tested and deployed, instead of someone doing that manually every time. That made the whole development process faster and safer.

The result was a dashboard that ran reliably in production — we tracked 99% uptime over two months, which means the system stayed healthy and available almost the entire time, and the team had one clear place to check system health instead of jumping between tools."

# Zapier
Zapier is a no-code automation tool that connects different apps together, so they can talk to each other and complete tasks automatically. 

I used Zapier to build an Automated Lead Capture and Follow-Up System. The goal was to cut down manual work and make sure every new lead gets a fast response, without anyone on the team having to act on it right away.

Here's how it works: when a customer fills out a Google Form, that automatically triggers the Zapier workflow. First, the lead's information gets saved into a Google Sheet, so we have a clean record of every lead. 

Next, Zapier sends a notification to a Slack channel, so the team knows right away that a new lead has come in. Then, it automatically sends a personalized welcome email to the customer through Gmail — so they hear back from us immediately, even before a human follows up. And if a lead matches certain criteria, like a high-value customer, Zapier automatically flags it as high-priority so the team can follow up faster.

The end result was a system that removed a lot of manual, repetitive work..



## Table of Contents

- [Introduce](#introduce)
- [Aspire Ontario Exp (AI-Assisted Software Engineer)(Sept 2025 – Apr 2026)](#aspire-ontario-exp-ai-assisted-software-engineersept-2025--apr-2026)
- [Meallens Exp (Full-Stack Developer) (June 2023 – Sept 2025)](#meallens-exp-full-stack-developer-june-2023--sept-2025)
- [Project 1: Multi-Agent Code Review Pipeline](#project-1-multi-agent-code-review-pipeline)
- [Project 2: Legacy to Modern Migration Framework](#project-2-legacy-to-modern-migration-framework)
- [Zapier](#zapier)
- [About this company?](#about-this-company)
- [Why are you interested in this position?](#why-are-you-interested-in-this-position)
- [Why should we hire you?](#why-should-we-hire-you)
- [How do you use AI?](#how-do-you-use-ai)
- [Non-Technical People.](#non-technical-people)
- [Multiple Task/Project?](#multiple-taskproject)
- [Strong Programming Language?](#strong-programming-language)
- [Comfortable Learning New Tech?](#comfortable-learning-new-tech)
- [What's your biggest weakness?](#whats-your-biggest-weakness)
- [Describe a difficult bug you solved.](#describe-a-difficult-bug-you-solved)
- [Questions](#questions)
- [Bonus Questions](#bonus-questions)



# About this company?
Manulife is a large financial services company based in Toronto. It provides insurance, investment, and financial services to millions of customers around the world, and in the U.S. it operates under the John Hancock brand.

# Why are you interested?
I am interested in this role because it is a great fit for my experience. 

During my previous role, I have worked with Python, React, and Azure OpenAI, which is very similar to the kind of work described in this role. 

I'm excited about the opportunity to build AI solutions at a much larger scale, and learn from an experienced team.




# What you will learn from this Job?
- I would learn to work on a big company
- I would learn about making things more reliable and secure at that scale.
- I would learn in depth about tools like ServiceNow
- I would get the experience of working with engineers across differrent regions



# Non-Technical People.
I worked with users who weren't technical. When explaining something to a non-technical user, I avoid technical jargon and focus on the business impact rather than the technology behind it. I try to use simple language, relatable examples, and break the explanation into small steps.



# Multiple Task/Project?

I first understand which tasks have the highest business impact.

Then I break larger work into smaller milestones and communicate progress regularly.


# RAG Hallucination

Hallucination is when the AI confidently gives an answer that sounds right but isn't actually true or grounded in real data. 
A few ways I addressed this in my project:

- Grounding with RAG — instead of letting the model answer from memory alone, I made sure it only answered based on retrieved, real ticket data. This alone removes a lot of hallucination risk.

- Prompt engineering — I wrote prompts that explicitly instructed the model to say 'not enough information' rather than guess, if it couldn't find a good match.

- Testing and iteration — I tested outputs against known cases to check accuracy before rolling it out, and documented what worked so the prompt patterns were reusable and reliable going forward.

Basically, the goal isn't to fully eliminate hallucination — it's to reduce the risk and make sure a human is still in the loop for anything important."


# Comfortable Learning New Tech?

I am very comfortable. I expect continuous learning to be part of the job because technology evolves quickly, especially in the AI sector.

When I find something new, I usually build a small proof of concept first, read the documentation, and then apply it to a real project.

# What's your biggest weakness?

Earlier in my career, I sometimes spent too much time trying to find the perfect solution before moving forward.

I've learned that delivering a solid first version, gathering feedback, and iterating usually leads to better outcomes."

# Describe a difficult bug you solved.

I once had an issue where an API worked locally but failed in production due to environment variable configuration.

I reproduced the issue, checked the deployment logs, compared the environments, identified the missing configuration, and added validation to prevent similar issues in the future.



# Questions
- What would success look like in the first 3-6 months?
  >>> That's great to hear. Thank you for sharing that.
- What kinds of applications would I be building?
  >>> That's helpful. Could you also tell me a bit about...
- Are developers encouraged to experiment with new AI tools and workflows?
  >>> That sounds like an environment I'd really enjoy working in. Thanks for sharing.
- What are the next steps of the hiring process?



## Table of Contents

- [Introduce](#introduce)
- [Aspire Ontario Exp (AI-Assisted Software Engineer)(Sept 2025 – Apr 2026)](#aspire-ontario-exp-ai-assisted-software-engineersept-2025--apr-2026)
- [Meallens Exp (Full-Stack Developer) (June 2023 – Sept 2025)](#meallens-exp-full-stack-developer-june-2023--sept-2025)
- [Project 1: Multi-Agent Code Review Pipeline](#project-1-multi-agent-code-review-pipeline)
- [Project 2: Legacy to Modern Migration Framework](#project-2-legacy-to-modern-migration-framework)
- [Zapier](#zapier)
- [About this company?](#about-this-company)
- [Why are you interested in this position?](#why-are-you-interested-in-this-position)
- [Why should we hire you?](#why-should-we-hire-you)
- [How do you use AI?](#how-do-you-use-ai)
- [Non-Technical People.](#non-technical-people)
- [Multiple Task/Project?](#multiple-taskproject)
- [Strong Programming Language?](#strong-programming-language)
- [Comfortable Learning New Tech?](#comfortable-learning-new-tech)
- [What's your biggest weakness?](#whats-your-biggest-weakness)
- [Describe a difficult bug you solved.](#describe-a-difficult-bug-you-solved)
- [Questions](#questions)
- [Bonus Questions](#bonus-questions)


# Bonus Questions




How do you approach prompt engineering?

"I start with a clear system prompt that defines the role and tone, then structure the user input cleanly. I iterate by testing edge cases and adjusting the prompt until the output is consistent and accurate."

What are the limitations of LLMs in an enterprise setting?

"LLMs can hallucinate, have a knowledge cutoff, and can be expensive at scale. In enterprise settings, you also need to be careful about sending sensitive data to external APIs, which is why private deployments like Azure OpenAI matter."


Frontend & Integration
What's your experience with React?

"I've built a few small React apps — mostly dashboards that fetch data from a backend API and display it dynamically. I'm comfortable with components, hooks, and state management."

Have you integrated a frontend with a backend API?

"Yes, I used fetch and Axios to call REST endpoints from a React frontend. I handled loading states, error messages, and used environment variables to manage API URLs across environments."


Collaboration & Process
Describe your experience in an Agile environment.

"During my internship, we worked in two-week sprints with daily standups. I picked up tickets from the backlog, gave status updates, and participated in retrospectives to improve our process."

Tell me about working with a cross-functional team.

"I worked with a design team and a data analyst on a dashboard project. I handled the API and they handled the visuals and data requirements. Regular syncs helped us stay aligned."

How do you handle feedback on your code?

"I welcome it. I treat code reviews as a learning opportunity. If I disagree with a suggestion, I ask questions to understand the reasoning rather than pushing back defensively."


Behavioural
Tell me about a time you learned a new technology quickly.

"I had to use Docker for the first time midway through a project. I spent a weekend going through the docs and a tutorial, containerized the app, and had it running in our pipeline within two days."

Describe a project that didn't go as planned.

"An API I built kept timing out under load. I hadn't accounted for response time from the LLM. I added async handling and a loading indicator on the frontend, and that fixed the user experience while I worked on optimizing the backend."

How do you prioritize multiple tasks in a sprint?

"I focus on blockers first, then high-impact tasks. I communicate early if something is taking longer than expected so the team can adjust. I also break big tasks into smaller pieces to make progress visible."


## Table of Contents

- [Introduce](#introduce)
- [Aspire Ontario Exp (AI-Assisted Software Engineer)(Sept 2025 – Apr 2026)](#aspire-ontario-exp-ai-assisted-software-engineersept-2025--apr-2026)
- [Meallens Exp (Full-Stack Developer) (June 2023 – Sept 2025)](#meallens-exp-full-stack-developer-june-2023--sept-2025)
- [Project 1: Multi-Agent Code Review Pipeline](#project-1-multi-agent-code-review-pipeline)
- [Project 2: Legacy to Modern Migration Framework](#project-2-legacy-to-modern-migration-framework)
- [Zapier](#zapier)
- [About this company?](#about-this-company)
- [Why are you interested in this position?](#why-are-you-interested-in-this-position)
- [Why should we hire you?](#why-should-we-hire-you)
- [How do you use AI?](#how-do-you-use-ai)
- [Non-Technical People.](#non-technical-people)
- [Multiple Task/Project?](#multiple-taskproject)
- [Strong Programming Language?](#strong-programming-language)
- [Comfortable Learning New Tech?](#comfortable-learning-new-tech)
- [What's your biggest weakness?](#whats-your-biggest-weakness)
- [Describe a difficult bug you solved.](#describe-a-difficult-bug-you-solved)
- [Questions](#questions)
- [Bonus Questions](#bonus-questions)