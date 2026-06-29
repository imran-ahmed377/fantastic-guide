
## Table of Contents

- [Introduce](#introduce)
- [Aspire Ontario Exp (Application Support Analyst)](#aspire-ontario-exp-application-support-analyst)
- [Meallens Exp (Data Analyst)](#meallens-exp-data-analyst)
- [Project 1: ERP Data Issue Resolution System](#project-1-erp-data-issue-resolution-system)
- [Project 2: Power BI Operations Support Dashboard](#project-2-power-bi-operations-support-dashboard)
- [Zapier](#zapier)
- [About this company?](#about-this-company)
- [Why This Company?](#why-this-company)
- [What you will learn from this job?](#what-you-will-learn-from-this-job)
- [Handle a production incident](#handle-a-production-incident)
- [Production Issue / Challenge you faced in a project](#challenge-you-faced-in-a-project)
- [Biggest mistake](#biggest-mistake)
- [Project didn’t work as expected](#project-didnt-work-as-expected)
- [Took initiative](#took-initiative)
- [Requirement unclear / ambiguous](#requirement-unclear--ambiguous)
- [Power BI dashboard created](#power-bi-dashboard-created)
- [Order Missing from ERP](#order-missing-from-erp)
- [Troubleshoot / Root Cause Analysis](#root-cause-analysis)
- [SQL functions use regularly](#sql-functions-use-regularly)
- [Power BI performance](#power-bi-performance)
- [NON Technical](#non-technical-user-explain)
- [DAX](#dax)
- [Questions](#questions)

# Introduce
I'm a software developer with experience building full-stack applications using Python, JavaScript/TypeScript, SQL, and modern web frameworks. In my recent projects, I've worked on building production-ready applications, REST APIs, and database-driven systems.

I've also integrated AI tools like GitHub Copilot, OpenAI and Claude into my workflow for generating code, debugging, writing tests, and accelerating development. 

What excites me about this role is that AI is a core part of software engineering rather than just a productivity tool. I enjoy solving problems using modern tools and technologies. I am always eager to learn and continuously improve my skills to stay updated with latest technologies and contribute effectively to build impactful solutions.


# Aspire Ontario Exp (AI-Assisted Software Engineer)(Sept 2025 – Apr 2026)
At Aspire Ontario, I worked on building internal software platforms called Exeevo. I worked on developing a full-stack CRM application.

I designed data pipelines, and I collaborated closely with business stakeholders to understand their requirements.

The legacy application was developed using Django, so I used next.js and FastAPI to modernize the internal platform.

I designed workflows using multiple AI agents for code generation, code reviews, testing, and documentation. And it automated around 70% of our repetitive engineering tasks and reduced overall development time.

I worked directly with product managers. And during discovery sessions, I gather business requirements and translate them into clear technical specifications.

I built a Python and Airflow-based data pipeline for processing each day data analytics and reporting.



# Meallens Exp (Full-Stack Developer) (June 2023 – Sept 2025)

In my last role at Meallens, I worked as a Full-Stack Developer, and I worked on modernizing the company's inventory management system. I migrated a legacy application to modern tech stack using TypeScript, React, and Node.js.

I worked on both the frontend and backend, I built features like inventory item management, stock update forms, search and filtering functionality, and user management screens, and developed APIs, fixed bugs, and improved the overall performance and maintainability of the application. 

I also used AI tools like Cursor and Claude to speed up repetitive tasks, like generating CRUD APIs.

I also wrote technical documentation, implementation guides and release notes.


# Project 1: Multi-Agent Code Review Pipeline

The goal was to automate parts of the pull request review process because manual reviews takes a long time to check code style, and basic security issues.

I designed the workflow using CrewAI, where I created three specialized agents. One agent for code quality, another for common security issues, and the third agent reviewed coding style and best practices. 

When a pull request was submitted, each agent analyzed the code independently, and their results were combined into a single review.

To make the feedback more useful, I integrated the Claude API to generate clear, human-readable review comments instead of just returning raw warnings or error messages. That made the suggestions much easier to understand.

Challenge: 

One **challenge** was making sure the agents didn't produce duplicate or conflicting feedback. I addressed that by defining clear responsibilities for each agent and structuring the workflow.

Result:

The pipeline ended up processing over 200 pull requests per month and saved more than 10 hours each week.


# Project 2: Legacy to Modern Migration Framework
I worked on creating a framework to migrate legacy PHP applications to Python much more efficiently using AI.

The goal was combining AI tools with a structured workflow to reduce manual migration process.

I designed an agentic workflow using Claude Code along with a set of custom prompts. I broke the migration into smaller steps and avoided converting the entire application at once. such as, I had separate prompts for analyzing the existing PHP code, translating business logic into Python, refactoring the generated code, and validating the output.

To make sure the migrated code was reliable, I used Codex to generate unit tests and then reviewed and refined those tests. By the end of the project, I achieved around 95% test coverage, which gave me confidence that the migrated application behaved the same as the original.

**Challenge:**

The biggest challenge was making sure the AI-generated code preserved the original business logic and didn't introduce subtle bugs. I validated each module individually, ran the generated tests, and reviwed the output before moving on to the next step.

**Result:**

The project reduced the migration timeline from an estimated six weeks to about two weeks. After I documented the workflow and the prompting strategy, I presented the framework to the private equity team, and they adopted it as a standard approach for migration projects across three portfolio companies.

# Zapier
I have worked on an Automated Lead Capture and Follow-Up System project using Zapier. The goal was to reduce manual work and make sure every new lead gets a quick response.

When a customer fills out a form on the Google Forms, Zapier automatically starts the workflow. First, the lead information is saved in Google Sheets.

Then, a notification is sent to the Slack channel so the team know a new lead has arrived. After that, the system automatically sends a personalized welcome email to the customer through Gmail. If a lead meets certain criteria, Zapier automatically assigns that lead to the high-priority for faster follow-up.









# About this company?
FirePower Capital is a Toronto based company that helps medium-sized businesses grow. They act like a matchmaker to help owners sell or buy other companies. They also act like a flexible bank, directly lending money or investing cash into these businesses when traditional banks won't.

# Why are you interested in this position?
Three things stood out to me.
- the opportunity to build software that directly impacts businesses instead of working on isolated features.

- the importance on AI-assisted development. I already use AI daily, and I'd like to work in a team where it's part of the engineering culture.

- the variety of projects. Working across different portfolio companies sounds like a great opportunity to learn quickly.

# Why should we hire you?

I think my strengths align well with what you're looking for.

I enjoy building software that solves real business problems, I'm comfortable using AI to improve development speed, and I communicate well with both technical and non-technical stakeholders.

I'm also someone who learns quickly and enjoys taking ownership of projects from idea to deployment.


# How do you use AI?
I use AI throughout the software development lifecycle.

During planning, I use it to brainstorm architecture and identify edge cases.

During implementation, I use it to generate boilerplate code, APIs, database queries, and unit tests.

During debugging, I ask it to explain errors or suggest alternative approaches.

I treat AI as a collaborator rather than an authority. I always review, test, and validate the generated code before using it.



# Non-Technical People.
I worked with users who weren't technical. Rather than discussing implementation details, I focused on understanding their workflow and pain points.

I translated their needs into technical requirements, built a prototype,gathered feedback, and refined the application based on their input.


# Multiple Task/Project?

I first understand which tasks have the highest business impact.

Then I break larger work into smaller milestones and communicate progress regularly.


# Strong Programming Language?

Python is probably my strongest language, followed by JavaScript and TypeScript.

I'm comfortable working with SQL databases and building REST APIs. More importantly, I'm confident learning new technologies quickly when a project requires them.


# Comfortable Learning New Tech?

Very comfortable. Technology evolves quickly, especially with AI tools, so I expect continuous learning to be part of the job.

When I encounter something new, I usually build a small proof of concept first, read the documentation, and then apply it to a real project.

# Why should we hire you?

I think my strengths align well with what you're looking for.

I enjoy building software that solves real business problems, I'm comfortable using AI to improve development speed, and I communicate well with both technical and non-technical stakeholders.

I'm also someone who learns quickly and enjoys taking ownership of projects from idea to deployment.

# What's your biggest weakness?

Earlier in my career, I sometimes spent too much time trying to find the perfect solution before moving forward.

I've learned that delivering a solid first version, gathering feedback, and iterating usually leads to better outcomes."

# Describe a difficult bug you solved.

I once had an issue where an API worked locally but failed in production due to environment variable configuration.

I reproduced the issue, checked the deployment logs, compared the environments, identified the missing configuration, and added validation to prevent similar issues in the future.














# Non Technical User Explain
When explaining something to a non-technical user, I avoid technical jargon and focus on the business impact rather than the technology behind it. I try to use simple language, relatable examples, and break the explanation into small steps.






# Questions
- What would success look like in the first 90 days?
  >>> That's great to hear. Thank you for sharing that.
- What kinds of applications would I be building?
  >>> That's helpful. Could you also tell me a bit about...
- Are developers encouraged to experiment with new AI tools and workflows?
  >>> That sounds like an environment I'd really enjoy working in. Thanks for sharing.
- What are the next steps of the hiring process?

# Bonus Questions
- "Walk me through your favorite project."
- "How would you refactor a large legacy application?"
- "How do you decide whether AI-generated code is safe to use?"
- "Describe your Git workflow."
- "How do you write maintainable code?"
- "Tell me about a time you disagreed with a teammate."
- "How would you design an internal dashboard for a business?"
- "What's your experience with SQL and databases?"
- "How do you measure whether the software you built actually improved the business?"

