---
url: "https://jellyfish.co/blog/prepare-for-technical-due-diligence/"
title: "What is Technical Due Diligence? | Jellyfish Blog"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/prepare-for-technical-due-diligence/#content)

![](https://jellyfish.co/wp-content/uploads/2023/07/agence-olloweb-d9ILr-dbEdg-unsplash-1.jpg)

![](https://jellyfish.co/wp-content/uploads/2021/11/Jellyfish_Blog-Author-Headshots_Evan-Klein.webp)

Evan Klein

October 05, 2020

As the leader of a product or engineering organization, you’ve got a lot on your plate to think about: aligning with your CEO and go-to-market leaders, ensuring the success of your product, growing and leading an engineering team. Preparing for a future exit or future round of financing is likely low on your list of priorities. But with M&A activity [gaining steam again](https://www.pehub.com/ma-is-poised-for-a-steady-recovery-with-tech-and-healthcare-taking-the-lead/) and venture funds and PE firms continuing to aggressively [seek investments](https://news.crunchbase.com/news/why-mega-venture-funds-arent-slowing-down-in-2020/) in 2020, you never know what could happen, even when you don’t expect it. As the saying goes, “chance favors the prepared.”

There’s a lot to be done to prepare your product and your technical team when these opportunities do present themselves. In this article, we’ll outline a checklist of the most common and important things you’ll need to think about as a technical leader.

## What is Technical Due Diligence?

Any acquisition of, or investment into a software company will involve relatively extensive due diligence, and because the product that you and your team have built is so central to the success of your business, technical due diligence will be central to that process. The conversations will generally be held between technical leaders, or hired technical analysts, from the acquirers/investors and the technical leader or leaders of the company being acquired. The process will focus on answering several key questions, so make sure to take steps to be able to answer these questions favorably. Sometimes that will take gathering data from your team about systems currently in place. Sometimes it will require technology shifts or specific fixes. Technical due diligence will generally look most closely at the following:

## 7 Key Elements of Technical Due Diligence

### 1\. Your People:

This is often the most critical question raised. The acquiring company or investor wants to know that they can have confidence in the people involved in building the product. They’ll ask for things like organizational charts with all full time employees and their roles, any contracted resources, descriptions of the different departments in your organizations and why they exist, and an understanding of how these departments interact. They’ll also want to know salary and tenure information and backgrounds of people in key roles. This can all seem pretty invasive. It is! But look at it through the investor’s eyes. They are buying a substantial chunk of your company, and they want to know exactly what it is they’re buying. The company wants to know your staff like you do, so be prepared to speak about your team with confidence. You should have on hand:

- A list of every org you oversee
- A list of all employees in each department along with titles and salaries
- A hiring plan for what the team will look like as it scales

The “succession plan:” who are the key team players, who makes the machine run, and who’s next in charge (e.g. the lieutenants) for important initiatives. It’s a little morbid to think about, but acquirers may need to find “synergies” and highlighting who / what is critical is important.

### 2\. Your Code and Architecture:

Your product is likely core to why you’ve received an acquisition offer to begin with. But the acquiring company wants to make sure that the product is technically sound and can scale to their vision of growth, and they’ll certainly want to ensure the product is secure. They’ll look into the scalability of your architecture, how the code is written to make sure new developers can quickly contribute, old or legacy components that might require wholesale replacement or expensive refactoring, and open source or other third party components that might be problematic legally. Expect your codebase to be scanned for quality and security and for open source components, and be prepared that the results might demand some heavy lifting. The specifics to prepare for:

- A qualitative audit of architecture including architectural diagrams and explanations
- A detailed audit of your code for quality and security. Acquirers will run scans for code quality, application security tests like [Veracode](https://www.veracode.com/) or [Snyk](https://snyk.io/), even penetration tests and/or other similar type tools on your code. We’d suggest running such scans regularly, but you already have code quality scans built into CI, right? 😉
- An audit of your IP, including any open source licenses associated with components in your code. They’ll likely run a [Black Duck](https://www.synopsys.com/software-integrity/security-testing/software-composition-analysis.html) or similar scan.

### 3\. Your Infrastructure:

Acquiring companies and investors want to know the ins and outs of your product and make sure data (especially customer data) is secure and compliant. Be prepared with infrastructure diagrams or descriptions that outline how and why you’ve made the choices you have. They’ll ask questions like, “what are your business continuity and disaster recovery plans?” “Is the cost of infrastructure reasonable given the number of customers you have?” If you can answer these questions, you’ll be in good shape. Consider keeping a detailed outline of:

- Cloud (AWS, Azure, Google Cloud) costs broken down by product and architecture.
- An understanding for how you would trim costs here if you had to. Remember that COGS (costs of goods sold), of which these costs are a part, is the first and likely largest place where acquirers will look to “trim fat.”
- An audit of your compliance certifications (SOC, ISO, PCI, HIPAA, FedRAMP, etc.) along with any documentation around that

### 4\. Workflows and Processes:

Acquiring companies will want to understand the processes, tools, and delivery mechanisms you have in place to assess potential for growth. They’ll likely ask for a description of your deployment processes, including anything that is automated to prevent human error. They’ll want to know the tools you use for build, automation, testing, and monitoring your software. And they’ll look for the processes in place to enable engineers to grow the product and any read on productivity or demonstrated success of your engineering team. Ultimately they’re looking for any expensive process, tooling, or skill gaps that they will need to fill down the road. Be diligent about documenting:

- Your SDLC
- Your development tool stack ( [JIRA](https://jira.atlassian.com/), [GitHub](https://github.com/), etc.)
- The KPIs or [metrics you should already be tracking](https://www.jellyfish.co/blog/control-your-engineering-metrics/) in order to ensure your team’s success

### 5: Product Quality & User Value:

Like it or not, acquiring companies will probably not simply take your word for it that your product a) does what you say it does, delivering the right value to customers, and b) does that in a reliable way. They’ll speak with your Product and Sales teams to try to assess any quality or performance issues, and they may even try to speak with your customers. These are not necessarily deal breakers, but they can be expensive to address, and that factors into the decision-making. It’s best to be forthcoming about any known bugs, performance or other quality issues, and any plans you have to fix or mitigate those issues. Be prepared to show usage data split by:

- Product line
- Feature
- Customer cohort
- Probably a fair number of other slices so get creative

### 6: Budgets and Costs

Your brilliant product roadmap is great, but what’s it going to cost? Documenting the capital expenditures both past and future of executing on your plan will be of utmost importance in the diligence process. You may need to start planning and thinking more strategically about how you [capitalize your development costs](https://www.jellyfish.co/blog/what-why-rd-cost-capitalization/) over time against the revenues your software brings in.

### 7\. Technical Debt

Those performing diligence will want to know what your [technical debt](https://www.jellyfish.co/blog/technical-debt-definition/) looks like. They will be trying to figure out what costs they didn’t know about before they officially commit. That means things like aging code, old architecture ports, old and irrelevant documentation, etc. Get ahead of it by keeping and providing a list so that the acquirer or investor doesn’t have to find out on its own. Include costs associated with these issues. Understand how necessary they will be to fix and rank them. Of course, make sure this list is reasonable. Acquirers and investors don’t want to see a list with infinite work (that will scare them), nor do they want to see a list with almost no work to be done (they will assume you are lying).

### “Chance favors the prepared”

Technical due diligence requires a fair amount of work, so it makes sense to start preparing before you might think you’ll need to. Make sure your house is in order and build a story of diligence and competence. If you’re confident in your product and team, you should make those performing diligence confident as well. Make their lives easy and they (and your own executive team) will thank you for it.

Aligning engineering with business priorities should start well before any technical due diligence happens. This alignment is critical in the success of your company. Find out more, and get started with a [live demo](https://www.jellyfish.co/request-demo/)!

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2024/10/RD-staffing-model-1024x561.webp)](https://jellyfish.co/blog/rd-headcount-planning-model/)[**How to Use Real Data to Build Your 2026 R&D Headcount Planning Model**](https://jellyfish.co/blog/rd-headcount-planning-model/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/rd-headcount-planning-model/)

[![Budget planning season](https://jellyfish.co/wp-content/uploads/2024/08/blog-Why-Successful-RD-Budget-Planning-for-2025-Means-Closer-Alignment-Between-Finance-and-Engineering-1024x561.webp)](https://jellyfish.co/blog/successful-rd-budget-planning/)[**Why Successful R&D Budget Planning for 2026 Means Closer Alignment Between Finance & Engineering**](https://jellyfish.co/blog/successful-rd-budget-planning/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/successful-rd-budget-planning/)

[![What is DevFinOps?](https://jellyfish.co/wp-content/uploads/2024/07/blog-embrace-devfinops-1024x561.webp)](https://jellyfish.co/blog/what-is-devfinops/)[**What is DevFinOps?**](https://jellyfish.co/blog/what-is-devfinops/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/what-is-devfinops/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified