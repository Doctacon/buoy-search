---
url: "https://jellyfish.co/library/ai-in-software-development/responsibility-of-developers-generative-ai/"
title: "What is the Responsibility of Developers Using Gen AI?"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/ai-in-software-development/responsibility-of-developers-generative-ai/#content)

In this article

Software engineers are becoming AI supervisors. They prompt models, validate outputs, and orchestrate systems that generate most of their codebase

Most organizations weren’t ready for this change. Engineering teams rush to adopt generative AI tools for competitive advantage, but they operate without clear processes for oversight or quality assurance.

No one knows who’s accountable when AI-generated code brings bugs, security vulnerabilities, or biased outcomes. Here’s how this Reddit developer [put it](https://www.reddit.com/r/ArtificialInteligence/comments/1lower3/comment/n0qsj8p/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

![AI ethical concerns](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/AI-ethical-concerns.png)

Without clear guidelines, teams often end up with messy codebases, legal headaches, and ethical issues that harm both the product and team morale.

This guide gives engineering teams the frameworks they need. It breaks down developer responsibilities in the AI era and helps leaders create environments where ethical AI use becomes standard practice.

What is the Responsibility of Developers Using Generative AI?

## What is the Responsibility of Developers Using Generative AI?

When AI writes the code, developers become the last line of defense. They validate outputs, catch problems, and own the results, whether good or bad.

Here’s what that means in practice and in different areas:

### Technical Responsibility

Technical responsibility starts with treating AI-generated code like any other contribution — it needs thorough review and [testing](https://jellyfish.co/blog/unit-testing-automation/).

#### **Bias avoidance**

**The problem** **:** Generative AI models copy biases from their training data and make them worse. The code they generate can discriminate against users, lock people out, and expose your company to lawsuits. The root cause goes deeper than most developers realize. Here’s how this Reddit user [explains it](https://www.reddit.com/r/compsci/comments/nh1vrq/comment/gyvgonu/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

![Bias in AI](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Bias-in-AI.png)

**What developers must do:**

- Test every AI output with diverse user personas and edge cases before deployment
- Review generated logic for nuanced assumptions about gender, race, age, or location
- Get validation that forms, error messages, and user flows work across different cultural contexts
- Check variable names and comments for exclusionary or inappropriate language
- Run accessibility tests on any UI components the artificial intelligence generates
- Document bias patterns you discover and share them with your team

**Example:** An AI-generated loan approval system could reject high-quality applications from certain zip codes and embed historical redlining practices into your code. If you test with synthetic data across different demographics, you’ll catch this before it becomes a fair lending violation that costs millions in fines.

#### **Data security**

**The problem:** AI pulls from millions of code examples, including old Stack Overflow posts full of security flaws. The generated code looks professional and runs fine, so developers ship it without catching the SQL injections, exposed API keys, or authentication bypasses hidden inside. This is becoming more and more common, [according to Reddit devs](https://www.reddit.com/r/ExperiencedDevs/comments/1nmnx5b/comment/ng9uyg8/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

![AI data security](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/AI-data-security.png)

**What developers must do:**

- Review every database query for SQL injection vulnerabilities, especially string concatenations
- Check all API endpoints for proper authentication and authorization controls
- Validate input sanitization on any user-facing forms or data entry points
- Test for [exposed sensitive data](https://jellyfish.co/library/developer-productivity/peer-code-review-best-practices/) in logs, error messages, or API responses
- Scan AI-generated dependencies for known security vulnerabilities
- Run security linters and penetration tests on all AI-generated code before deployment

**Example:** An AI might generate a user search feature that directly concatenates user input into SQL queries instead of using parameterized statements. This creates a SQL injection vulnerability that attackers could exploit to steal your entire customer database within minutes of deployment.

#### **Continuous monitoring**

**The problem:** AI-generated code behaves unpredictably in production, especially when it encounters scenarios outside its training data. Problems that slip past testing can escalate quickly and even cause outages, data corruption, or security breaches that damage your system before anyone notices.

**What developers must do:**

- Set up automated alerts for unusual error rates or performance drops in AI-generated components
- [Track metrics](https://jellyfish.co/library/software-engineering-analytics/) specific to AI code, like response times, memory usage, and failure patterns
- Monitor user complaints and support tickets for issues linked to recently deployed AI code
- Review logs daily for unexpected behaviors or edge cases the AI didn’t handle
- Create rollback plans for every AI-generated feature in case problems come up post-deployment

**Example:** An AI-generated caching system might work perfectly during testing but start corrupting data when traffic spikes hit production. Without monitoring, this corruption could spread through your database for days before users report strange behavior in their accounts.

**PRO TIP:** Jellyfish’s [DevOps Metrics](https://jellyfish.co/platform/devops-metrics/) automatically track DORA metrics like deployment frequency and mean time to recovery across your pipeline. You can compare how AI-generated code performs against human-written code in production. When AI code causes more incidents or slower recovery times, you’ll know to adjust your review process.

![](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Jellyfish-Deployment-Rate.png)

### Professional Responsibility

Professional standards don’t disappear because AI enters the workflow. You still need to maintain your [skills](https://jellyfish.co/library/engineering-management-skills/), collaborate effectively, and deliver quality code.

#### **Accountability**

**The problem:** Some developers treat AI-generated code as someone else’s responsibility, claiming “the AI wrote it” when bugs appear. This accountability gap creates sloppy codebases where no one owns problems, and quality standards collapse. One engineering lead [breaks it down](https://www.reddit.com/r/ExperiencedDevs/comments/1lkz5a9/comment/mzvt5rw/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

![AI accountability](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/AI-accountability.png)

**What developers must do:**

- Take full ownership of any code you commit, regardless of who or what wrote it
- Test AI-generated code as thoroughly as you would test your own work
- Never blame AI for bugs or issues during [code reviews](https://jellyfish.co/blog/impact-of-ai-code-review-agents/) or incident reports
- Document your prompts and modifications so others can understand your decision-making and use cases
- Fix problems in AI code immediately rather than waiting for someone else to handle it

**Example:** A developer ships an AI-generated authentication system that locks out users after a weekend deployment. Instead of saying “the AI got it wrong,” they take ownership, roll back the change, fix the logic, and document lessons learned for the team.

#### **Transparency**

**The problem** **:** When developers hide AI involvement, teams lose track of what code they understand. Debugging becomes a nightmare when no one knows if a human wrote the broken code or which [AI tool](https://jellyfish.co/blog/best-ai-coding-tools/) generated it.

**What developers must do:**

- Mark the AI-generated code with clear comments on which tool created it
- Document the prompts you used to generate the code for future reference
- Explain any changes you made to the AI’s original output
- Share AI tools and techniques that work well with your team
- Disclose when you don’t fully understand how AI-generated code works
- Keep a log of AI-assisted changes for debugging and audit purposes

**Example:** A developer uses AI to generate a complex sorting algorithm but doesn’t document this fact. Months later, when the algorithm fails with specific data sets, the team wastes days trying to understand logic that no human fully comprehends.

#### **User education**

**The problem:** Developers copy AI-generated code without understanding how it works, then deploy it to production. This creates a codebase full of messy functions that no one can debug or explain when customers ask questions. The standard should be clear. Here’s how this developer [put it](https://www.reddit.com/r/ExperiencedDevs/comments/1lkz5a9/comment/mzxw1jk/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

_“I have no problem if you generate code using ChatGPT or any other AI assistant. But do you understand it? If so, all good. If not, you’re in the same boat as if you’d just written gibberish before.”_

**What developers must do:**

- Never ship AI code you can’t explain line by line to a junior developer
- Test your understanding by modifying the AI code without breaking it
- Write documentation that explains what the code does, not just what you prompted
- Be able to debug AI-generated code without regenerating it from scratch
- Ask senior developers to review AI code if you don’t fully grasp how it works

**Example**: A developer uses AI to generate a complex recursive function for tree traversal, but doesn’t understand recursion basics. When the function causes stack overflow errors in production, they can’t fix it and must rewrite the entire feature from scratch under deadline pressure.

**PRO TIP:** Jellyfish [Allocations](https://jellyfish.co/platform/resource-allocations/) tracks where your engineering time actually goes — new features, technical debt, or unplanned work. After teams adopt AI, you’ll see if they build more features or waste time on AI-created problems.

![Jellyfish Resource Allocations](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Jellyfish-Resource-Allocations.png)

### Ethical Responsibility

When AI writes code that touches user data or makes decisions about people, ethics matter as much as functionality.

Developers need to make sure that their AI-generated code respects data privacy and treats all users fairly.

#### **Consider the societal impact**

**The problem:** AI-written code can discriminate at scale and affect thousands of users before anyone notices the pattern. These algorithmic decisions might shape who gets jobs, loans, healthcare access, and other life-changing opportunities. And some companies are [learning this lesson](https://www.reddit.com/r/recruitinghell/comments/1msmlcy/comment/n99dnyk/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) the hard way.

![AI societal impact](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/AI-societal-impact.png)

**What developers must do:**

- Test generative AI systems for discriminatory patterns across age, race, gender, and other protected categories
- Consider who might be excluded or harmed by the code’s decisions
- Build in human review processes for high-stakes automated decisions
- Document potential societal risks and discuss them with stakeholders
- Create feedback mechanisms so affected users can report unfair treatment

**Example:** An AI-generated healthcare scheduling system might prioritize younger patients for appointments based on “efficiency” [metrics](https://jellyfish.co/platform/engineering-metrics/) in its training data. This could delay care for elderly patients who need it most, and create a public health crisis and legal liability.

#### **Seek expert guidance**

**The problem:** Developers might work with AI in domains they don’t fully understand (e.g., healthcare, finance, law), where mistakes have serious consequences. You can’t spot errors in AI-generated code when you don’t know what correct looks like in that field.

**What developers must do:**

- Consult domain experts before you use AI code in specialized fields
- Ask legal teams to review AI systems that make decisions about people
- Partner with ethicists or bias researchers for higher-impact consumer features
- Document which experts reviewed the code and what concerns they raised

**Example:** An AI-generated tax calculation feature seems to work in testing but mishandles state tax rules for remote workers. A tax professional would have spotted this immediately, but the bug ships and affects thousands of users’ returns.

The Core Ethical Challenges in Practice

## The Core Ethical Challenges in Practice

Most teams run into similar ethical problems when they start using AI for code generation. And usually, these issues need team-wide or company-wide approaches to handle properly.

Here are some of the main ones you should pay attention to:

### The Intellectual Property Minefield

**The challenge:** Generative models train on copyrighted code and generate outputs that might violate intellectual property rights. No one knows who owns AI-generated code or who gets sued when it infringes on someone’s patent.

**Example:** Your AI generates a sorting algorithm that matches a patented implementation used by a financial services company. You don’t realize this until a competitor points it out during due diligence for an acquisition. It could potentially kill the deal or reduce your company’s valuation.

**Avoid this mistake ⚠️:** Don’t assume AI-generated code is automatically yours to use freely. Many developers ship AI code without checking for potential IP conflicts, thinking the AI “created” something original.

### The Black Box Problem

**The challenge:** AI generates [complex code](https://jellyfish.co/library/code-complexity/) that works, but no one understands how or why. When this code breaks, teams can’t debug it because they never understood the logic in the first place.

**Example:** An AI generates a machine learning pipeline with nested functions and obscure variable names. It processes real-world data correctly for months until it suddenly starts dropping random records, and no developer can figure out where the logic fails because no human was involved in designing the flow.

**Avoid this mistake ⚠️:** Don’t ship code you can’t explain or debug yourself. Too many developers just copy AI output that seems to work without understanding the logic. One developer [learned this the hard way](https://www.reddit.com/r/BlackboxAI_/comments/1luqqpm/comment/n20cay8/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> If you’re coding with tools like GPT, GitHub, and OpenAI, you have to have some knowledge of coding structure, flow, and logically what is doing what. If I just vibe coded and didn’t correct it, find the hallucinations and where its logic fails, my project would be dead right now, and I wouldn’t know why.

**PRO TIP:** Jellyfish provides [complete visibility](https://jellyfish.co/platform/engineering-metrics/) into who works on what code and how it flows through your pipeline. When mysterious AI-generated logic breaks, you can trace exactly which developer committed it, what prompts they used (if documented), and how long the team spent debugging it.

![Jellyfish AI Impact visibility](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Jellyfish-AI-Impact-visibility.png)

### The Risk of AI-Generated Security Flaws

**The challenge:** AI learns from millions of code examples, including outdated, vulnerable patterns from the past two decades. It confidently reproduces these security flaws in new code without warning developers about the [potential risks](https://jellyfish.co/blog/how-to-mitigate-delivery-risk-in-software-engineering/).

**Example:** An AI generates a file upload feature using code patterns from 2015 that don’t validate file types or sizes properly. Attackers exploit this to upload malicious scripts that compromise your entire server, which then leads to a data breach that affects thousands of customers.

**Avoid this mistake ⚠️:** Don’t trust AI to handle security-critical code without extensive review. AI can’t differentiate between secure and vulnerable code patterns, so it reproduces SQL injections, XSS vulnerabilities, and authentication bypasses that it learned from old tutorials.

A Framework for Engineering Leaders: How to Support Your Team

## A Framework for Engineering Leaders: How to Support Your Team

[Engineering leaders](https://jellyfish.co/solutions/people-management/) set the tone for how teams use AI responsibly. Without clear policies and support systems, developers make inconsistent decisions that create risk.

Here’s how to build an environment where your team can use AI tools effectively and ethically.

### 1\. Establish Clear Guidelines and Policies

Policies create order when teams start with AI tools. Without them, developers make their own rules, code quality varies wildly, and risks pop up everywhere.

Every AI policy needs these core elements:

- **AI tool approval process**: Define which tools developers can use and who approves new ones before [adoption](https://jellyfish.co/blog/ai-coding-tool-adoption-best-practices/).
- **Code ownership rules**: Clarify who owns AI-generated code and who takes responsibility if it fails.
- **Documentation requirements**: Specify what developers must document, including prompts, tools used, and modifications made.
- **Review standards**: Set extra review steps and [safeguards for AI code](https://jellyfish.co/blog/prepare-for-technical-due-diligence/), especially for security-critical components.
- **Training mandates**: Ask developers to complete AI literacy training before they start using large language models (LLMs) in production.

Policies work best when paired with practical review tools. This checklist helps reviewers verify that AI-generated code meets your standards.

|     |     |     |     |
| --- | --- | --- | --- |
| **Review item** | **Pass** | **Fail** | **N/A** |
| The developer can explain all the code logic | ☐ | ☐ | ☐ |
| Security scan completed | ☐ | ☐ | ☐ |
| AI source documented in comments | ☐ | ☐ | ☐ |
| Tested with edge cases | ☐ | ☐ | ☐ |
| Bias testing performed | ☐ | ☐ | ☐ |
| Performance benchmarked | ☐ | ☐ | ☐ |
| No sensitive data in prompts | ☐ | ☐ | ☐ |
| Legal review completed (if needed) | ☐ | ☐ | ☐ |

_**Note:** This checklist is a starting point. Customize it based on your industry requirements and risk tolerance._

Start with basic policies and expand them as your team learns. Roll out changes gradually, get feedback from developers, and adjust based on what you see works in practice.

### 2\. Mandatory Human Oversight

AI code requires human review, no exceptions. Skip this step or assign it to junior developers, and you’ll find bugs only after your users do. Proper oversight prevents these disasters and keeps humans in control of the [software development process](https://jellyfish.co/blog/sdlc-best-practices/).

Different types of code require different levels of human oversight. You can use this framework to decide who reviews what:

- **High-risk code** (authentication, payments, personal data): Requires senior developer review plus security specialist approval.
- **Medium-risk code** (business logic, APIs, data processing): Needs thorough peer review with [automated security scanning](https://jellyfish.co/library/developer-productivity/automation-in-software-development/).
- **Low-risk code** (UI components, formatting, documentation): Standard review process with basic testing.
- **Experimental code** (prototypes, proofs of concept): Developer discretion, but must document AI involvement.

Simple scripts might work fine with basic review, but production systems need experienced developers to validate every architectural decision. As one developer [warns](https://www.reddit.com/r/softwaredevelopment/comments/1n3jic4/comment/nbe1y6p/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) from experience:

> _For any non-helloworld software, AI is not to be used without tight human oversight, and might be unhelpful enough that just not using it is more productive. If you use it, don’t let it dictate the code structure._

Integrate oversight into your current workflow instead of bolting it on later. Set up reviewer assignments upfront so everyone knows their role. The best oversight happens when developers barely notice it’s there.

### 3\. Invest in Training and AI Literacy

Traditional coding bootcamps don’t teach AI literacy, and vendors focus on features rather than responsible use.

That’s why teams that invest in proper training see fewer bugs, security issues, and ethical problems while developers become more productive with AI tools.

Here are some core training modules every team needs:

- **AI fundamentals**: How models work, their limitations, and why they hallucinate.
- **Prompt engineering**: Writing clear prompts, [iterating effectively](https://jellyfish.co/library/engineering-efficiency/), and getting consistent results.
- **Security awareness**: Common vulnerabilities in AI code and how to spot them.
- **Ethical considerations**: Detecting bias, protecting privacy, and maintaining accountability.
- **Tool proficiency**: Advanced features of your approved AI tools and when to use them.
- **Code review skills**: Evaluating AI-generated code for quality, security, and maintainability.

Companies that get AI adoption right create internal champions who guide their teams through the continuous learning curve.

One AI steering committee member [shares their approach](https://www.reddit.com/r/instructionaldesign/comments/1izulmk/comment/mf61kcm/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

![AI training and literacy](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/AI-training-and-literacy.png)

You should track your team’s advancements by monitoring [code quality](https://jellyfish.co/library/quality-metrics/) and security incidents before and after training.

Well-trained teams should spot more bugs during review, ship fewer vulnerabilities, and spend less time debugging AI-generated code.

### 4\. Adapt Your Quality and Review Processes

Standard code reviews don’t work for AI-generated code. Your reviewers look for human mistakes while AI creates entirely different problems — phantom functions, ancient coding patterns, and security holes that look legitimate.

Here’s what to change in your review process:

- **Extended review time**: AI code needs deeper inspection since no human wrote the logic initially.
- **Specialized reviewers**: Assign people who understand both the business domain and AI behavior patterns.
- **Performance benchmarking**: Compare AI code efficiency against [human-written baselines](https://jellyfish.co/blog/how-ai-coding-tools-can-help-engineers-level-up/).
- **Documentation requirements**: Record prompts used, modifications made, and why you trust the output.

Different types of problems need different reviewers and different amounts of time. That’s why it’s best to break your AI code reviews into stages.

This approach brings thorough coverage without overwhelming any single reviewer:

|     |     |     |     |
| --- | --- | --- | --- |
| **Stage** | **Focus** | **Who reviews** | **Time needed** |
| Initial scan | Syntax, obvious errors, formatting | Automated tools | ≈5 minutes |
| Security review | Vulnerabilities, data handling, and authentication | Security team | ≈30 minutes |
| Logic verification | Business rules, accuracy, edge cases | Domain expert | ≈45 minutes |
| Performance check | Speed, memory usage, scalability | Senior developer | ≈20 minutes |
| Final approval | Overall quality and maintainability | Tech lead | ≈15 minutes |

Don’t let perfect reviews kill your velocity. Automate the basic checks and save human reviewers for complex problems.

Ensuring Responsible AI with Jellyfish

## Ensuring Responsible AI with Jellyfish

You’ve set policies for responsible AI use, but how do you know if teams follow them?

Most organizations can’t see who uses AI tools, whether they help or hurt [productivity](https://jellyfish.co/blog/how-to-measure-developer-productivity/), or which teams need support. And without data, you can’t manage AI risks or even prove its value.

That’s where **Jellyfish** comes in. Our [engineering management platform](https://jellyfish.co/platform/engineering-management-platform/) connects to your development tools to understand how teams use AI, quantify its impact on delivery metrics, and surface the insights you need to manage AI adoption the right way.

Here’s how Jellyfish supports responsible development with AI and helps you build trust:

- **Track AI tool adoption across teams:** Monitor which teams adopt Copilot, Cursor, Gemini, or Sourcegraph and [spot gaps in usage](https://jellyfish.co/platform/jellyfish-ai-impact/) or training needs.
- **Compare tool performance objectively:** See which AI tools deliver results for specific teams, tasks, and programming languages.
- **Measure the productivity impact:** Track whether AI truly [speeds up delivery](https://jellyfish.co/library/software-delivery-management/), optimizes quality, or just adds complexity to your workflow.
- **Monitor AI-generated code in your workflow:** Track where AI-generated code creates delays or quality problems in your development process.
- **Prevent team burnout from AI integration**: Balance AI adoption speed with [team capacity](https://jellyfish.co/solutions/capacity-planner/) to avoid overwhelming developers with new tools.
- **Align AI investments with business priorities:** Connect AI tool usage to business outcomes and verify that tools support key objectives.

With clear insights into usage, impact, and team health, you can build an engineering culture that uses AI responsibly and effectively.

[**Schedule an AI Impact demo**](https://jellyfish.co/get-an-ai-impact-demo/) and see how you can get started.

FAQs on the Responsible Use of Generative AI

## FAQs on the Responsible Use of Generative AI

### Who is ultimately responsible for a bug in AI-driven code?

The developer who commits the code owns the bug, period. AI is a tool like any other — if you use it to generate code and push it to production, you take responsibility for any problems.

### What is the single biggest mistake teams make when adopting generative AI technologies?

Teams rush to adopt AI tools without setting up any guidelines or oversight. Every developer does their own thing, which creates a mess of inconsistent code quality and security risks.

By the time problems surface in production, the damage is done, and clean-up takes months.

### How can developers prevent generative AI from creating harmful content or misinformation?

Developers need to review and validate every AI output before it reaches users, especially for sensitive topics or protected groups.

Make sure to test AI-generated content with diverse personas and edge cases to quickly spot bias or harmful patterns. And never deploy AI systems that make decisions about people without human review and the ability for users to appeal or report problems.

### What are the industry’s ethical standards for generative AI development?

The industry hasn’t agreed on universal ethical practices yet, though most companies follow principles around transparency, fairness, and accountability.

Major tech firms publish their own AI ethics guidelines, but these vary widely and lack enforcement mechanisms

### What should a basic AI usage policy for an engineering team include?

A basic AI policy sets clear rules about which tools developers can use and how they must handle AI-generated code. At a minimum, your policy should cover these AI applications:

- **Approved tools list**: Which AI tools developers can use and who approves new ones.
- **Code ownership**: Who takes responsibility when AI code fails.
- **Documentation rules**: How to mark and track AI-generated code.
- **Review requirements**: Extra checks needed for AI code before deployment.
- **Security restrictions**: What AI can’t touch (passwords, payment systems, personal data).
- **Training requirements**: What developers must learn before using AI tools.

Learn More About AI in Software Development

## Learn More About AI in Software Development

- [What is the Impact of AI on Software Development?](https://jellyfish.co/library/ai-in-software-development/)
- [Benefits of AI in Software Development](https://jellyfish.co/library/ai-in-software-development/benefits/)
- [The Risks of Using AI in Software Development](https://jellyfish.co/library/ai-in-software-development/risks-of-using-generative-ai/)
- [How to Measure the ROI of AI Code Assistants in Software Development](https://jellyfish.co/library/ai-in-software-development/measuring-roi-of-code-assistants/)
- [How to Use AI in Software Development: 7 Best Practices & Examples for Engineering Teams](https://jellyfish.co/library/ai-in-software-development/use-cases-and-best-practices/)
- [AI in Software Testing and Quality Assurance](https://jellyfish.co/library/ai-in-software-development/software-testing-qa/)
- [Will AI Replace Software Engineers? No and Here’s Why](https://jellyfish.co/library/ai-in-software-development/will-ai-replace-software-engineers/)
- [What’s The Future of Software Engineering with AI?](https://jellyfish.co/library/ai-in-software-development/future-trends/)

About the author

![Lauren Hamberg](https://jellyfish.co/wp-content/uploads/2025/03/Lauren-Hamburg.jpg)

Lauren is Senior Product Marketing Director at Jellyfish where she works closely with the product team to bring software engineering intelligence solutions to market. Prior to Jellyfish, Lauren served as Director of Product Marketing at Pluralsight.

Follow: [LinkedIn](https://www.linkedin.com/in/laurenhamberg/)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

Qualified

AI, AI Agent

Jellyfish AI Assistant

Speak now

Hi, I'm your Jellyfish AI Assistant! Curious whether your AI token spend is actually moving developer productivity?

Conversation

Hi, I'm your Jellyfish AI Assistant! Curious whether your AI token spend is actually moving developer productivity?

Message input

Book a Demo

Customer Support

By messaging, you agree this chat may be monitored, recorded, and used as described in our [Privacy Policy](https://jellyfish.co/library/privacy-policy/).

![Messenger](https://messenger-assets.qualified.com/uploads/7uox2MSGiNK5FJ86L2PK2TJoeEQYQuuRo3NCY/60e5ccc0f79a2a42b920769d889689a23f1bd502b4d96a5073c5c362547269c7.png)
Ask us