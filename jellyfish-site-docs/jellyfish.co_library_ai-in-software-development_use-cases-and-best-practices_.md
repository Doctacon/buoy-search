---
url: "https://jellyfish.co/library/ai-in-software-development/use-cases-and-best-practices/"
title: "Using AI in Software Development: 7 Best Practices & Examples"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/ai-in-software-development/use-cases-and-best-practices/#content)

In this article

Spend five minutes on LinkedIn or tech Twitter, and you’ll feel like you’re the last developer on earth still writing code manually.

Feeds are flooded with developers bragging about their AI workflows. They claim they haven’t written a loop in months. The bots handle _everything_ now.

However, the truth is a bit more complicated. Developers online fall into two camps. Some engineers are thoroughly unimpressed, like this Reddit user who shared their experience:

![Engineer unimpressed with AI](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Engineer-unimpressed-with-AI.png)

(Source: [Reddit](https://www.reddit.com/r/ExperiencedDevs/comments/1hm8gxj/comment/m3sovyi/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button))

Meanwhile, other developers rely on AI for a massive range of tasks. Writing tests, building regexes, cleaning up components, extracting functions, generating boilerplate, formatting code, and much more.

They claim that artificial intelligence handles most of their repetitive work:

![AI handles repetitive engineering work](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/AI-handles-repetitive-engineering-work.png)

(Source: [Reddit](https://www.reddit.com/r/ArtificialInteligence/comments/1gr20ax/comment/lx3z79u/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button))

Below, we’ll provide an honest breakdown of where AI can deliver value, where it falls short of expectations, and how you can find the sweet spot for your team’s [AI adoption](https://jellyfish.co/blog/ai-coding-tool-adoption-best-practices/).

Part 1: Laying the Foundation (Planning & Design)

## Part 1: Laying the Foundation (Planning & Design)

The planning phase is where AI can save you from expensive mistakes down the road.

Instead of starting from scratch or missing critical considerations, you can use AI to explore approaches, validate ideas, and structure your project properly from day one.

### 1\. Use AI to De-Risk Your Project Planning

You know the drill. [Leadership](https://jellyfish.co/solutions/people-management/) announces a “simple integration with Salesforce.” Your team starts building.

Two weeks in, you discover it needs bi-directional sync, custom field mapping, and conflict resolution. The basic API integration your engineers built won’t scale, and now you’re back to square one.

The problem is that humans assume too much and ask too little. AI systematically probes every aspect of a vague requirement and exposes the gotchas that typically emerge mid-sprint.

|     |     |
| --- | --- |
| **The Old Way** | **The AI Way** |
| **Day 1:** Simple Salesforce integration | **Day 1:** Simple Salesforce integration + AI exploration |
| **Day 5:** Start coding basics | **Day 2:** AI reveals all hidden requirements up front |
| **Day 14:** Wait, it needs bi-directional sync? | **Day 5:** Start coding with full picture |
| **Day 40:** Still rebuilding… | **Day 26:** Moving to next feature |

The beauty of AI is that you also don’t need perfectly formed instructions to start. You can give it your raw, unfiltered project notes, and it shapes them into clear action items and milestones. This Reddit developer [explained it perfectly](https://www.reddit.com/r/Futurology/comments/1jc6r40/comment/mi21u4a/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> Don’t get me started about writing up task lists and project planning. I can just throw a stream-of-consciousness stream of text at it, and the AI will organize everything into neat, professional-sounding tasks and milestones. **_I love this_**.

Take that Salesforce integration example. You tell AI something like: “Need to sync our user data with Salesforce, probably real-time, sales team wants to see everything.”

The [AI assistant](https://jellyfish.co/blog/best-ai-coding-tools/) immediately asks about API rate limits, data volume, conflict resolution strategies, field mapping complexity, and whether you need audit trails.

It flags that Salesforce’s bulk API might be necessary and recommends checking your current webhook infrastructure. The expensive mistakes never make it into code.

**PRO TIP 💡:** Jellyfish’s [Resource Allocations](https://jellyfish.co/platform/resource-allocations/) feature shows if AI-assisted planning leads to less time spent on unplanned work and fewer mid-sprint surprises. You’ll know if AI helps you catch problems early or if you’re still getting blindsided by hidden complexity.

![Jellyfish Resource Allocations](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Jellyfish-Resource-Allocations.png)

### 2\. Leverage AI as an Architectural Sounding Board

Architecture decisions happen in an echo chamber. Your team agrees to adopt Kubernetes because everyone’s doing it. Nobody questions whether you need that [complexity](https://jellyfish.co/library/code-complexity/) for your 50,000 daily users.

Six months later, you’re drowning in YAML files and your deployment velocity has tanked. Nobody played devil’s advocate when it mattered.

Stack Overflow’s May 2024 study found that [76.6% of developers](https://stackoverflow.co/labs/2024-developer-survey-insights-for-ai-ml/) are using or planning to use generative AI tools, and architecture decisions are a perfect use case. They want something to challenge their assumptions without the politics or ego.

The value comes from AI asking the questions your team might not. Every architecture choice has tradeoffs that are easy to overlook:

|     |     |
| --- | --- |
| **What teams propose** | **What AI points out** |
| “Let’s move to microservices.” | “With your 5-person team, who’s managing service discovery, distributed tracing, and inter-service communication?” |
| “NoSQL will solve our scaling issues.” | “How will you handle your complex reporting requirements without joins?” |
| “We should go serverless.” | “Your P95 latency requirement is 200ms — have you modeled cold start impact?” |
| “Event sourcing is perfect for this.” | “What’s your plan for GDPR compliance and event deletion?” |
| “GraphQL will simplify our APIs.” | “How will you prevent N+1 queries with your current team’s experience level?” |
| “Let’s containerize everything.” | “You’re doing 2 deployments per month—is the orchestration overhead worth it?” |
| “We need a data lake.” | “Who’s going to maintain software quality and governance across unstructured data?” |
| “Kubernetes will standardize our deployments.” | “Do you have the 2-3 dedicated people needed to manage a high-quality Kubernetes cluster?” |

It’s about having someone (better yet, something) that asks the right questions. One Reddit developer [put it](https://www.reddit.com/r/programming/comments/1joeiaj/comment/mktfsqs/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) like this:

> It’s great as a talking rubber duck. Especially for planning architecture overhauls. ‘I think we can move X process to Y technology.’ ‘Have you considered the following limitations?’

For example, let’s say that a team is planning to split their monolith into 12 microservices. AI asks about their [deployment frequency](https://jellyfish.co/blog/breaking-down-deployment-frequency/), team size, and on-call rotation. When it learns they deploy weekly with eight developers and two people on call, it points out the mismatch.

They’d need to coordinate 12 services every release with minimal support. The team scales back to three services instead and delivers the same improvements without the operational nightmare.

Part 2: The Building Phase (Coding & Documentation)

## Part 2: The Building Phase (Coding & Documentation)

Now comes the part where AI saves your team hours every sprint.

From generating boilerplate to writing tests to creating documentation, AI handles the repetitive development work that nobody enjoys but everyone needs to do.

### 3\. Treat AI as a Pair Programmer for Code Generation

According to Stack Overflow, [82% of developers](https://survey.stackoverflow.co/2024/ai#2-ai-in-the-development-workflow) use AI primarily for code generation. Makes perfect sense. It’s the most tangible benefit with the fastest payoff.

The trick is knowing what to delegate and what to keep. One Reddit developer [shared their strategy](https://www.reddit.com/r/ExperiencedDevs/comments/1hm8gxj/comment/m3sb9b4/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> In terms of writing code, yes, the code gen capabilities are not perfect and require manual review, but the time it takes me to manually review and fix small implementation details is significantly less than the time it would take me to write it myself.
>
> **I treat Cursor as a Junior dev that occasionally makes mistakes, but also has a complete understanding of the entire codebase and can type code at the speed of light**. Honestly, recent models like Claude Sonnet 3.5 are already quite damn good with certain languages and frameworks (like React), and it’s only getting better with time.

Thinking of AI this way makes the [boundaries](https://jellyfish.co/blog/how-to-talk-to-your-software-team-about-ai/) clear. A junior developer shouldn’t architect your database, but they can absolutely write API endpoints and data migrations. The same applies to AI.

Here’s how that breaks down in practice:

|     |     |
| --- | --- |
| **Use AI For** | **Avoid AI For** |
| Boilerplate and CRUD operations | Complex business logic with nuanced rules |
| Test scaffolding and iterative test cases | Security-critical implementations |
| API endpoint creation | Payment processing or authentication flows |
| Data transformation functions | Performance-critical algorithms |
| React/Vue component structure | Cryptographic implementations |
| Database migrations | Regulatory compliance code |
| Error handling patterns | Multi-threaded or concurrent code |
| Documentation comments | Machine learning model architecture |

The takeaway is simple. AI has seen millions of login forms, but has never seen your specific authentication flow. It knows REST patterns but not your API conventions.

But speed can become a liability when you don’t understand what you’re shipping. Another developer shared an [important warning](https://www.reddit.com/r/cscareerquestions/comments/1lxn1hq/comment/n2nh967/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> If you do not understand the code that it’s generating, then better not to use it. It’s just a tool, so you have to know how to use it effectively. Consider that a hammer is many things, but a hammer can ruin your product if used improperly during the building process. It’s the same idea with AI.

Here’s a simple checklist that prevents most AI-related problems:

- Do I understand what this code does?
- Have I checked for edge cases?
- Is the error handling appropriate?
- Will my team be able to maintain this?
- Does it follow our regular coding standards?
- Have I tested it with real data?

This might even seem like overhead, but it’s faster than debugging mysterious failures in production. The best teams make this review process so [automatic](https://jellyfish.co/library/developer-productivity/automation-in-software-development/) that it barely slows them down.

**PRO TIP 💡:** Track how AI affects your code review process with our [Life Cycle Explorer](https://jellyfish.co/platform/life-cycle-explorer/). Many teams find that AI-driven code flies through initial creation but gets stuck in review longer because developers need extra time to understand what the AI built. If your review times spike after adopting AI, you need better commenting standards for AI-powered code.

![Jellyfish Lifecycle Explorer](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Jellyfish-Lifecycle-Explorer.png)

### 4\. Automate the Chore of Documentation

Documentation is the vegetable on your development plate. You know you need it, your future self will thank you for it, but you’ll still push it aside to work on literally anything else. Then the sprint review arrives, and you [scramble to write something](https://jellyfish.co/blog/how-to-mitigate-delivery-risk-in-software-engineering/), anything.

Gartner reports that [42% of organizations](https://www.gartner.com/peer-community/oneminuteinsights/omi-generative-ai-software-engineering-teams-adoption-training-ko8) with GenAI use it for document generation. The work is formulaic enough for AI to handle, but painful enough that everyone wants it automated.

AI agents handle these documentation tasks particularly well:

- API documentation from code
- README files
- Code comments and docstrings
- Database schema documentation
- Troubleshooting guides
- Release notes
- Architecture decision records
- Onboarding documentation

The process becomes so much simpler when AI provides the first draft. One developer [explained](https://www.reddit.com/r/ExperiencedDevs/comments/1hm8gxj/comment/mgdjxwv/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) how this works:

> Imagine you need to write documentation (or any other boring, busy work). Instead of writing the whole thing from scratch, you get the AI to fill in the bulk, and then you just adapt or fill in / correct missing/incorrect info. So basically, you go from being a writer of documentation to a reviewer of documentation.

For example, let’s say a team needs to document their authentication system. Twenty endpoints, OAuth flows, role-based permissions — easily a week of documentation work.

They feed the code to AI, which writes detailed API docs in about 20 minutes. The team spends four hours reviewing, correcting technical details, and adding examples. They finish before lunch what usually takes a full sprint.

Part 3: Ensuring Code Quality and Maintenance

## Part 3: Ensuring Code Quality and Maintenance

Maintenance work piles up in every codebase, but developers rarely prioritize it. AI gives teams a way to tackle technical debt and [quality issues](https://jellyfish.co/library/quality-metrics/) without pulling developers off feature work.

Here’s how teams use AI to keep their code healthy while still [shipping on schedule](https://jellyfish.co/solutions/software-delivery-management/).

### 5\. Use AI for Automated Testing and QA Processes

Testing always loses the priority battle. The feature has to ship, the deadline won’t move, and writing tests feels like a luxury you can’t afford. So you ship without them and hope nothing breaks (it usually does).

According to [Tricentis](https://www.tricentis.com/news/survey-testing-the-most-valuable-ai-investment), teams now apply AI across all testing phases — 47.5% for planning what to test, 44% for test case generation, and 32% for analyzing results.

They handle tests during the sprint, so they don’t have to worry about technical debt later on.

Here’s what that looks like in practice:

|     |     |     |
| --- | --- | --- |
| **Testing phase** | **How AI helps** | **Typical time saved** |
| **Planning** | Analyzes code changes and identifies risky areas that need test coverage | 2-3 hours per sprint |
| **Generation** | Creates unit tests, edge cases, and test data from your functions | 60-80% faster than manual |
| **Execution Analysis** | Identifies patterns in test failures and suggests root causes | 1-2 hours per release |
| **Maintenance** | Updates existing tests when code changes break them | 70% of update time |

You can also use AI to catch bugs that human reviewers often miss. Here’s one user experience from [Reddit](https://www.reddit.com/r/ExperiencedDevs/comments/1d09y0a/comment/l5lrxns/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) that puts it in perspective:

> **Unit tests are what I use it for as well.** Plus, I’ve successfully gotten it to find an issue in a piece of code that I had looked at for a literal hour without finding it.
>
> I had overlooked a simple stream disposal causing a weird race condition, and I found it after I pasted the code and a summary of the issue.

For example, say your team needs tests for an inventory module with 50 functions full of complex business logic. Writing [comprehensive tests](https://jellyfish.co/blog/unit-testing-automation/) manually would take a developer a full week.

Instead, you give the functions to AI and get complete test suites in less than two hours. Your team spends another day reviewing the tests, polishing domain-specific edge cases, and removing redundant checks. You get better coverage in two days than you typically achieve in five.

### 6\. Streamline Version Control and Collaboration

Your senior engineers have eight PRs in their queue while trying to finish their own features. Junior developers lose momentum waiting for feedback, often for days. By the time reviews come back, they’ve already context-switched to something else.

[AI speeds up reviews](https://jellyfish.co/blog/impact-of-ai-code-review-agents/) at every stage. It runs the routine checks, explains complex changes, and provides the context reviewers need. Code that sat for days now merges in hours.

Here’s a clearer breakdown of AI’s role in the PR process:

|     |     |     |
| --- | --- | --- |
| **Stage** | **How AI Helps** | **Time Saved** |
| **Before Commit** | Runs pre-commit checks, catches style issues, and identifies potential bugs | 30 min per PR |
| **PR Creation** | Generates detailed descriptions from diffs, suggests appropriate reviewers based on code ownership | 15 min per PR |
| **During Review** | Explains complex changes in plain English, highlights risk areas, and suggests test cases | 45 min per review |
| **After Merge** | Updates related documentation, creates follow-up tickets, and notifies affected teams | 20 min per merge |

_**Note:** Time savings vary by team size and codebase complexity_

For example, say your team’s reviews typically take three days. With AI pre-checks, you outline formatting issues, missing tests, and [security problems](https://jellyfish.co/blog/prepare-for-technical-due-diligence/) before review.

AI writes clear PR descriptions and explains complex changes. Your reviewers understand the code faster, and reviews drop to one day.

You can also use AI for cross-team coordination. When you change a shared API, AI knows which teams to notify and writes the message. It flags breaking changes and recommends migration guides. No more Slack threads or meetings to coordinate.

**PRO TIP 💡:** Monitor how AI affects your PR review blockers with Jellyfish’s [engineering metrics](https://jellyfish.co/platform/engineering-metrics/). If AI helps developers create code faster but reviewers can’t keep up, you’ll see queue times increase even though individual reviews go quicker. The data tells you whether you need more reviewers or better AI-assisted review tools to balance the workflow.

![Jellyfish AI engineering metrics](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Jellyfish-AI-engineering-metrics.png)

### 7\. Make Continuous Learning a Team Habit

Every developer hits the same wall when tackling unfamiliar territory. You need to implement something outside your expertise, but you don’t even know what to Google.

You waste hours reading documentation that assumes knowledge you don’t have, or Stack Overflow answers that solve slightly different problems.

GitHub’s research confirms this learning value. [57% of developers](https://github.blog/news-insights/research/survey-reveals-ais-impact-on-the-developer-experience) say AI coding tools help them improve their coding language skills, making it the top-reported benefit.

Here’s how AI guides developers through the learning process:

- You describe a vague need (“handle real-time updates”) → AI explains your options (WebSockets, SSE, polling)
- You ask about unfamiliar concepts (“What’s a monad?”) → AI provides examples in your language
- You need help choosing patterns (“Observer or Pub/Sub?”) → AI compares trade-offs for your use case
- You want [implementation help](https://jellyfish.co/blog/ai-coding-tool-adoption-best-practices/) (“How in Python?”) → AI gives you working code with explanations

This is especially powerful for problems where you lack the vocabulary to even search effectively. One developer [explained this](https://www.reddit.com/r/webdev/comments/1ffw9lh/comment/mgcbop4/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) perfectly:

> I am using AI not to code. But I ask questions when I venture into territory where I lack knowledge and the how-to to go about things.
>
> For example, I have a problem and don’t know which programming patterns would fit best and how to combine them to achieve my goal. Then the AI listens to my problem in human language and then gives me multiple ways to go about stuff.
>
> The best part is that I learn new concepts and words that I had no clue about before. So in this way, AI fills a gap that was hard to close with Google alone. Google is best when you know what you are looking for. AI is great when you don’t even know the right question to ask. That’s how I use it.

**Remember ⚠️**: AI explanations can be incorrect or outdated. Check official docs for anything critical and make sure you understand solutions before you use them. AI accelerates deep learning but doesn’t replace it.

From Best Practices to Real-World Impact with Jellyfish

## From Best Practices to Real-World Impact with Jellyfish

You can follow every AI best practice in the book, but without hard data on who uses these development tools, how they use them, and what impact they have, you won’t know if any of it works.

Teams need to understand which developers get the most value from AI, where friction still exists, and whether their spending makes sense.

**Jellyfish** gives you these answers.

Jellyfish is an [engineering management platform](https://jellyfish.co/platform/engineering-management-platform/) that integrates with your existing stack — Jira, GitHub, GitLab, and AI tools like Copilot and Cursor.

It tracks how your teams build software, where they focus their effort, and whether AI tools make them faster or just change how they work.

Here’s exactly what you can do with Jellyfish by your side:

- **Track AI adoption and impact across your entire organization:** Jellyfish shows you exactly who uses AI tools, how often they use them, and which programming languages and [development workflows](https://jellyfish.co/blog/sdlc-best-practices/) benefit most.
- **Compare different AI-powered tools head-to-head:** If you’re testing Copilot, Cursor, and Gemini across different teams, Jellyfish shows you [which tool performs best](https://jellyfish.co/platform/jellyfish-ai-impact/) for specific use cases.
- **See where your developers spend their time:** Resource Allocations shows whether AI helps your teams focus on roadmap features instead of maintenance work. You’ll know if AI-assisted developers tackle harder problems or just finish simple and repetitive tasks faster.
- **Find the bottlenecks in your dev process:** [Life Cycle Explorer](https://jellyfish.co/platform/life-cycle-explorer/) shows you exactly where tasks get stuck in your pipeline. You’ll learn if AI speeds up coding but creates longer review queues, or if it helps throughout the entire process.
- **Prove AI makes developers faster.** Jellyfish tracks whether your pull requests merge quickly, whether developers close more tickets per sprint, and whether code reaches production sooner.
- **Connect your entire AI development stack in minutes:** The platform [integrates](https://jellyfish.co/platform/integrations/) with Jira, GitHub Copilot, GitLab, and AI models like Cursor through simple API connections. Your developers keep working normally while Jellyfish pulls the data it needs to measure performance and AI impact.

[**Schedule an AI impact demo**](https://jellyfish.co/get-an-ai-impact-demo/) to get hard data on how AI changes your team’s performance.

FAQs

## FAQs

### **How can I ensure AI-generated code meets our quality standards?**

Make code review non-negotiable for all AI output, just like you would for a junior developer’s work.

Run your standard test suites, linting rules, and security scans on everything AI generates before it reaches production. Train your team to review AI code for subtle bugs, edge cases, and patterns that don’t match your codebase conventions.

### **What’s the difference between an LLM chatbot like ChatGPT and a dedicated coding assistant?**

OpenAI’s ChatGPT works like a knowledgeable colleague you can ask questions, but it doesn’t see your codebase or integrate with your editor. It’s a natural language processing model at its core.

Specialized coding assistants like Copilot or Cursor operate inside your IDE, understand your project context, and recommend code as you type based on what you’re working on. They’re much more advanced than large language models, and you can use them for more complex problem-solving.

### **What are the best types of coding tasks to start with when using AI?**

Begin with unit tests — AI writes comprehensive test cases faster than most developers and outlines edge cases you might miss.

Then use it for standard features like form validation, frontend refactoring, error handling, or API integrations that follow common patterns.

Save complex business logic and system architecture for human brains, at least until you understand exactly how AI handles your specific codebase.

### **How can I use AI software to improve communication with non-technical stakeholders?**

Ask AI to rewrite your technical updates for executive audiences — it strips out the implementation details and focuses on business outcomes and timelines.

You can also use it to create FAQ documents that answer the questions stakeholders ask, like “when will this be ready?” rather than “how does it work?” AI can also generate presentation slides that tell a story about progress and impact instead of listing technical achievements.

### **Besides helping to write code, what other complex problems can AI help solve?**

AI helps with the complex problems that slow down every engineering team.

- Debug production issues by correlating errors across logs, [metrics](https://jellyfish.co/library/metrics-in-software-engineering/), and system components
- Plans complex migrations with granular steps, risk assessments, and rollback strategies
- Outlines security vulnerabilities and explains why specific code patterns create risk
- Optimizes performance by analyzing code paths and recommending targeted improvements
- Compares technical options and presents trade-offs for architectural decision-making
- Finds patterns in incident data to prevent future failures

Think of AI as your analysis assistant that processes massive amounts of information to point out insights you’d probably miss.

Learn More About AI in Software Development

## Learn More About AI in Software Development

- [What is the Impact of AI on Software Development?](https://jellyfish.co/library/ai-in-software-development/)
- [Benefits of AI in Software Development](https://jellyfish.co/library/ai-in-software-development/benefits/)
- [The Risks of Using AI in Software Development](https://jellyfish.co/library/ai-in-software-development/risks-of-using-generative-ai/)
- [How to Measure the ROI of AI Code Assistants in Software Development](https://jellyfish.co/library/ai-in-software-development/measuring-roi-of-code-assistants/)
- [AI in Software Testing and Quality Assurance](https://jellyfish.co/library/ai-in-software-development/software-testing-qa/)
- [Will AI Replace Software Engineers? No and Here’s Why](https://jellyfish.co/library/ai-in-software-development/will-ai-replace-software-engineers/)
- [What’s The Future of Software Engineering with AI?](https://jellyfish.co/library/ai-in-software-development/future-trends/)
- [What is the Responsibility of Developers Using Generative AI? Key Ethical Considerations & Best Practices](https://jellyfish.co/library/ai-in-software-development/responsibility-of-developers-generative-ai/)

About the author

![Lauren Hamberg](https://jellyfish.co/wp-content/uploads/2025/03/Lauren-Hamburg.jpg)

Lauren is Senior Product Marketing Director at Jellyfish where she works closely with the product team to bring software engineering intelligence solutions to market. Prior to Jellyfish, Lauren served as Director of Product Marketing at Pluralsight.

Follow: [LinkedIn](https://www.linkedin.com/in/laurenhamberg/)

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-Data-Hub-1024x610.png)](https://jellyfish.co/blog/dora-metrics-tools/)[**8 Top-Rated Tools for Measuring DORA Metrics**](https://jellyfish.co/blog/dora-metrics-tools/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-tools/)

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

Qualified