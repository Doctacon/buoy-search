---
url: "https://jellyfish.co/library/developer-experience/challenges/"
title: "4 Developer Experience Challenges (& How to Solve Them)"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/developer-experience/challenges/#content)

In this article

Shipping a single feature now involves more tools, services, apps, and dependencies than entire products did a decade ago. But the deadlines haven’t gotten more forgiving.

Engineering leaders are caught in the middle, which is why so many have started treating [developer experience](https://jellyfish.co/library/developer-experience/) as a strategic priority.

It’s an easy case to make. Developers who aren’t battling their own tools do better work and stay longer. The problem is execution. Studies say that roughly [75% of engineering leaders](https://blogs.vmware.com/tanzu/forrester-report-elevating-developer-experience/) say their DevEx strategy isn’t where it needs to be (mature enough).

This piece goes over four challenges you’re likely dealing with and practical ways to handle each one.

1\. Tool Sprawl and Legacy Infrastructure

## 1\. Tool Sprawl and Legacy Infrastructure

**The problem:** Most engineering teams don’t have just one or two tools to manage. They have dozens, often stitched together over the years without a coherent ecosystem plan.

Port’s 2024 survey found that the average enterprise developer switches between [7.4 different tools](https://www.port.io/blog/the-2024-state-of-internal-developer-portal-report) every day. And nearly all teams surveyed (94%) said they’re unhappy with how their tooling fits together.

**Why it matters:** Every tool switch is a small interruption. Multiply that across a full team and a full week, and you’re losing significant time to [context switching](https://jellyfish.co/blog/less-is-more-an-action-plan-for-reducing-context-switching/) alone. Legacy systems make it worse. They’re often poorly documented, hard to maintain, and slow to work with, but too embedded to easily replace.

**How to fix it:**

- **Audit your current stack** and see which tools are actively used, which overlap, and which create the most friction
- **Consolidate where you can** **by retiring redundant tools** and standardizing on fewer platforms that cover more ground
- **Create a deprecation plan for legacy systems** rather than letting them linger indefinitely without ownership
- **Assign clear ownership** for each major tool or platform so someone is accountable for its maintenance and improvement
- **Build a single entry point** like an internal developer portal so engineers aren’t jumping between a dozen tabs

2\. Complexity of Modern Stacks & Workflows

## 2\. Complexity of Modern Stacks & Workflows

**The problem:** Tech stacks have gotten more complicated over the years. You’ve got microservices, Kubernetes, CI/CD pipelines, cloud infrastructure, multiple programming languages, and plenty more, depending on the team. Most engineers understand the parts they work with, but not the whole thing.

**Why it matters**: Complex systems slow everything down. Debugging is slower, onboarding takes longer, and people hesitate before making changes. Many engineering teams say they spend over [20% of their time](https://www.themoderndatacompany.com/resources/the-modern-data-report-2024---2025-how-organizations-manage-and-scale-data) on architecture maintenance alone.

**How to fix it:**

- **Keep architecture docs visual** **and up to date** so engineers can see how things connect without reverse-engineering the system
- **Standardize the common tasks** like deploys and rollbacks so engineers aren’t figuring it out from scratch every time
- **Build onboarding around the full stack,** not just the codebase, so new hires understand how the environment works
- **Remove abstraction layers that don’t earn their keep** instead of letting them stick around because they’ve always been there
- **Schedule** [**regular architecture check-ins**](https://jellyfish.co/blog/ai-coding-tools-not-paying-off-your-code-architecture-might-be-to-blame/) to prevent accidental complexity from piling up over time

**PRO TIP:** Jellyfish’s [resource allocation insights](https://jellyfish.co/platform/resource-allocations/) show the true cost of complexity. You can track how much time goes to unplanned work and maintenance versus roadmap priorities, and use that data to justify investments in reducing technical overhead.

![Jellyfish Allocations](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/12/Jellyfish-Allocations-5.png)

3\. Friction from Security and Compliance Hurdles

## 3\. Friction from Security and Compliance Hurdles

**The problem:** Nobody argues against security and compliance, but the processes around them often get in the way of actual work. Developers wait on access requests, navigate unclear policies, and deal with approval chains that slow everything down.

A 2025 industry survey found that [51% of developers](https://www.revealbi.io/reveal-survey-report-top-software-development-challenges-for-2025) ranked security as their top software development challenge, with data privacy also ranking high.

![Biggest Software Development Challenges](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/12/Biggest-Software-Development-Challenges.png)

(Source: [Reveal](https://www.revealbi.io/reveal-survey-report-top-software-development-challenges-for-2025))

**Why it matters:** When security processes are slow or unclear, developers either wait around or find workarounds. Neither outcome is good. Waiting kills momentum and [delays releases](https://jellyfish.co/blog/sdlc-best-practices/). Workarounds create risk and defeat the purpose of having controls in the first place. The goal should be security that works with developers, not against them.

**How to fix it:**

- **Automate access requests and streamline approvals** so developers aren’t stuck waiting days for permissions they need to do their jobs
- **Create self-service options for common requests** like work environment access or credential rotation, so developers can move without filing tickets
- **Write clear, accessible documentation for compliance requirements** so engineers understand what’s expected without chasing down answers
- **Include security teams from the start of a project**, not just at the end, when it’s too late to change things the easy way
- **Revisit security workflows on a regular basis** to remove bottlenecks that slow teams down without improving protection

4\. Unclear Requirements and Workflow Interruptions

## 4\. Unclear Requirements and Workflow Interruptions

**The problem**: Developers often start work without a clear picture of what they’re supposed to build. Requirements are vague, acceptance criteria are missing, and questions don’t get answered until the work is already underway.

In a Stack Overflow survey, [33% of developers](https://survey.stackoverflow.co/2016) said that unclear requirements were their biggest challenge.

![Engineering challenges at work](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/12/Engineering-challenges-at-work.png)

(Source: [Stack Overflow](https://survey.stackoverflow.co/2016))

**Why it matters:** Without clear requirements, developers fill in the blanks themselves. Sometimes they get it right, often they don’t. The result is extra rounds of revisions and time lost to work that has to be redone.

**How to fix it:**

- **Write clear acceptance criteria** before the development process starts, so engineers know what they’re building toward
- **Make it easy to reach product and design** when developers need a quick answer to keep moving
- [**Use structured templates**](https://jellyfish.co/blog/how-jellyfish-plans-to-streamline-engineering-workflows-and-maximize-productivity-in-2024/) **for new feature specs** to make sure the basics are covered before a ticket moves to development
- **Batch questions and feedback into scheduled check-ins** instead of scattering them across the day as interruptions
- **Document decisions as they happen** so context doesn’t get lost, and the same questions don’t come up again later

Strategic Investments to Enhance DevEx

## Strategic Investments to Enhance DevEx

Solving [individual problems](https://jellyfish.co/library/developer-productivity/pain-points/) helps, but improving developer experience in a lasting way often means stepping back and investing in some foundational changes.

Here’s what you should pay attention to:

### Invest in Automation and Standardization

Without some level of standardization, things spiral. Every team ends up with its own stack, pipeline, and way of doing things. That might feel like flexibility at first, but over time, it becomes a burden. Here’s how this Reddit engineer [explained it](https://www.reddit.com/r/ExperiencedDevs/comments/1k9xlmb/comment/mphtark/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

![Invest in Automation and Standardization](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/12/Invest-in-Automation-and-Standardization.png)

Standardization makes everything easier to manage and maintain. It also sets the stage for automation. When processes are consistent, you can automate them once and apply that work everywhere.

This is especially relevant now that AI-assisted development tools are becoming mainstream. [McKinsey research](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/unleashing-developer-productivity-with-generative-ai) found that developers using generative AI tools can complete coding tasks up to twice as fast.

But keep in mind that kind of **acceleration depends on having well-defined, repeatable developer workflows in place**. The more standardized your environment, the more value you get from automation of any kind.

The point isn’t to lock everything down. It’s to create sensible defaults that reduce overhead, and then let automation take care of the repetitive work.

Here are a few areas where this tends to have the most [business impact](https://jellyfish.co/blog/communicating-the-business-impact-of-engineering/):

- **Standardized CI/CD pipelines** and DevOps practices that work the same way across the org and make automation easier to maintain
- **Service templates and starter scaffolding** that give teams a consistent foundation for new projects
- **Automated quality gates** for testing, linting, and security that don’t need any manual steps
- [**Artificial intelligence (AI) coding assistants**](https://jellyfish.co/blog/best-ai-coding-tools/) integrated into common workflows for faster code generation and code review
- **Clear rules, methodologies, and frameworks for when it’s okay to deviate,** so exceptions are deliberate rather than accidental

The two go hand in hand. Standardization creates the foundation, and automation keeps things running smoothly without constant manual effort.

### Build a Centralized Developer Portal

Without a single place to go for information, developers end up jumping between tools constantly. They check the wiki for docs, a different system for service ownership, another for deployment status, and another for on-call schedules.

Each switch takes time, and the cost adds up. Research by Dr. Gloria Mark found that it takes over [23 minutes](https://ics.uci.edu/~gmark/chi08-mark.pdf) on average to fully regain focus after an interruption. And even small context switches chip away at [productivity](https://jellyfish.co/blog/how-to-measure-developer-productivity/) throughout the day.

A developer portal brings all of this into one place. Instead of bouncing between tools, engineers have a single starting point. As one engineer [pointed out](https://www.reddit.com/r/devops/comments/1ei9z8d/comment/lg7zqc9/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button), it also changes how new team members get up to speed:

![Benefits of Centralized Developer Portal](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/12/Benefits-of-Centralized-Developer-Portal.png)

If we look at the day-to-day, a well-built portal becomes the first place engineers go when they need answers. Here’s how another engineer on Reddit [broke down](https://www.reddit.com/r/devops/comments/17u6tmv/comment/k9i6sf6/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) the practical benefits:

![Practical benefits of Centralized Developer Portal](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/12/Practical-benefits-of-Centralized-Developer-Portal.png)

What goes into a portal depends on the org, but there are a few things that tend to show up in most good implementations:

|     |     |
| --- | --- |
| **Component** | **Purpose** |
| Service catalog | Shows what services exist, who owns them, and how they relate |
| Pipeline and infra links | Lets developers check deployments and infrastructure in one place |
| Documentation | Keeps docs searchable and tied to the services they cover, including API references |
| Starter templates | Gives teams a consistent foundation for new services |
| Ownership and on-call | Makes it obvious who to reach when something goes wrong |

A good portal earns its place by being genuinely useful. Once developers trust that they can find what they need there, it becomes the default starting point for everything.

**PRO TIP:** Pair your portal rollout with Jellyfish [DevEx surveys](https://jellyfish.co/platform/devex/) to get direct feedback on what’s working and what’s not. Combine that with adoption and delivery metrics to see the full picture of how the portal is affecting your teams.

![Jellyfish DevEx Surveys](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/12/Jellyfish-DevEx-Surveys-1.png)

### Foster a Culture of Internal Collaboration and Continuous Learning

Many teams are set up like an assembly line. Product figures out what to build, design mocks up, and engineering builds it. It’s a tidy way to organize people, but it’s not how high-performing teams actually operate. One engineer [put it this way](https://www.reddit.com/r/ExperiencedDevs/comments/1oh99ee/comment/nlmy8bs/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

![Foster a Culture of Internal Collaboration and Continuous Learning](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/12/Foster-a-Culture-of-Internal-Collaboration-and-Continuous-Learning.png)

In practice, **the best teams don’t follow a strict handoff model**. Engineers contribute to product thinking, while designers factor in technical constraints. But none of that happens automatically. It has to be supported at the org level.

The same goes for learning. When developers have room to grow, share knowledge, and adopt new technologies, they do better work and stick around longer.

A [Forrester-commissioned study](https://humanitec.com/blog/key-findings-from-forrester-opportunity-snapshot) found that organizations with strong DevEx see 74% improved productivity and 81% better ability to attract and retain talent.

A few ways to make this part of how your team works:

- Bring engineers into product conversations early instead of handing them a finished spec to implement
- Set up regular knowledge-sharing moments like tech talks, demos, or informal architecture walkthroughs
- Senior developers can mentor newer team members through tech talks, demos, or informal architecture walkthroughs
- Give developers dedicated time to learn through courses, conferences, or just time to explore [new tools](https://jellyfish.co/library/developer-productivity/tools/)
- Make cross-team communication easy with open Slack channels, office hours, or internal Q&A forums
- Recognize teammates who help others, so collaboration is valued as much as shipping functionalities

It’s not flashy, but it works. And it costs less than replacing developers who got frustrated and left.

Why Investing in DevEx is an Investment in the Business

## Why Investing in DevEx is an Investment in the Business

[Developer experience](https://jellyfish.co/blog/developer-experience-best-practices/) can feel like an internal concern, something that matters to engineers but doesn’t show up on a balance sheet. But there’s more data on this than most people realize.

The link between developer experience and business outcomes is well documented at this point:

- **Individual performance:** A [Microsoft study](https://azure.microsoft.com/en-us/blog/quantifying-the-impact-of-developer-experience/) found that improved DevEx leads to better job performance, creativity, and learning at the individual level. Engineers who aren’t fighting their development environment have more capacity to do their best work and maintain their well-being.
- **Retention:** According to Atlassian’s 2024 State of Developer Experience report, [63% of developers](https://www.atlassian.com/software/compass/resources/state-of-developer-2024) say DevEx is essential when deciding whether to stay at their current job. That makes it one of the biggest levers for keeping your best people and [preventing burnout](https://jellyfish.co/blog/engineering-burnout/).
- **Code quality**: Teams with strong DevEx [produce high-quality code](https://azure.microsoft.com/en-us/blog/quantifying-the-impact-of-developer-experience/) and accumulate less technical debt. That means fewer bugs, less rework, faster time-to-market, and a healthier codebase over time.
- **Speed and output:** Teams with top-quartile developer experience scores [perform 4-5x better](https://getdx.com/research/the-one-number-you-need-to-increase-roi-per-engineer/) on development speed and quality than those in the bottom quartile.
- **Cost of turnover**: Losing a developer [costs 1.5-2.5x their annual salary](https://dora.dev/research/2024/dora-report/) once you account for hiring, training, and ramping up. Good DevEx helps you avoid paying that tax repeatedly.

Good DevEx isn’t “charity” for engineers. It’s how you get more out of the team you already have while delivering better results for end users.

Gain Visibility into DevEx with Jellyfish

## Gain Visibility into DevEx with Jellyfish

Improving developer experience sounds straightforward until you try to figure out where to start. Most orgs don’t have good answers on what’s slowing development teams down, where time truly goes, or how developers feel about the way things work.

**Jellyfish** helps engineering leaders and stakeholders close that gap. It’s a [software engineering management platform](https://jellyfish.co/platform/engineering-management-platform/) that connects quantitative data from your existing tools with qualitative feedback from developers.

The result is a clear view of how your teams operate, where friction shows up, and what’s worth prioritizing.

Here are just some of the key capabilities:

- [**Developer experience surveys**](https://jellyfish.co/platform/devex/): Run surveys that get to the root of developer sentiment on tooling, processes, and day-to-day work. Built-in segmentation shows you how different teams and roles experience things differently.
- **DORA metrics and delivery tracking**: Pull deployment frequency, lead time, change failure rate, and MTTR directly from your CI/CD and incident tools. No manual tracking needed.
- [**Life Cycle Explorer**](https://jellyfish.co/platform/life-cycle-explorer/): Outline where delays happen in the engineering life cycle. Understand the root causes and take action to improve flow across teams.
- **Resource allocation insights**: Understand how your team’s effort maps to business priorities. Jellyfish shows the breakdown between strategic work, tech debt, and reactive tasks in real time.
- [**AI impact measurement**](https://jellyfish.co/platform/jellyfish-ai-impact/): Track how AI coding tools like GitHub Copilot affect productivity across your org. Teams can measure adoption and see whether the investment is paying off.

Better developer experience starts with understanding what’s happening across your teams. Jellyfish makes that possible.

[**Book a demo**](https://jellyfish.co/request-a-demo/) and see how it can help your organization.

FAQs

## FAQs

### How does improving DevEx directly impact developer productivity?

DevEx enhancements target the things that slow developers down:

- Less time waiting on builds and deployments
- Fewer context switches between tools
- Clearer ownership and faster answers
- Simpler onboarding for new team members

Remove enough friction and productivity follows.

### With limited resources, how should a CTO prioritize DevEx improvements?

You should prioritize based on impact and effort. Look for high-pain, low-cost fixes first. Things like better documentation, streamlined access requests, or standardized workflows.

Then use developer feedback to guide where to invest, and revisit priorities as you learn more. This way, you can iterate based on real-time development cycle data.

### What role does automation play in solving DevEx challenges?

Automation takes repetitive developer work off your team’s plates. Things like builds, tests, deployments, and access requests. The less manual work in the process, the smoother things run, and the more time goes toward actual building.

Learn More About Developer Experience

## Learn More About Developer Experience

- [Developer Experience (DevEx): The Modern Guide for 2026](https://jellyfish.co/library/developer-experience/)
- [How AI is Enhancing Developer Experience and Boosting Productivity](https://jellyfish.co/library/developer-experience/ai-devex/)
- [How to Improve Developer Experience for Remote Engineering Teams](https://jellyfish.co/library/developer-experience/remote-teams/)
- [14 Best Developer Experience (DevEx) Tools Heading Into 2026](https://jellyfish.co/blog/best-developer-experience-tools/)
- [15 Developer Experience Best Practices for High-Performing Engineering Teams](https://jellyfish.co/library/developer-experience/best-practices/)
- [How to Improve Developer Experience: 16 Proven Strategies and Methods](https://jellyfish.co/library/developer-experience/how-to-improve-devex/)
- [How To Create an Effective Developer Experience Survey](https://jellyfish.co/library/developer-experience/surveys/)
- [15 DevEx Metrics for Engineering Leaders to Consider: Because 14 Wasn’t Enough](https://jellyfish.co/library/developer-experience/metrics/)

About the author

![Lauren Hamberg](https://jellyfish.co/wp-content/uploads/2025/03/Lauren-Hamburg.jpg)

Lauren is Senior Product Marketing Director at Jellyfish where she works closely with the product team to bring software engineering intelligence solutions to market. Prior to Jellyfish, Lauren served as Director of Product Marketing at Pluralsight.

Follow: [LinkedIn](https://www.linkedin.com/in/laurenhamberg/)

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-Data-Hub-1024x610.png)](https://jellyfish.co/blog/dora-metrics-tools/)[**8 Top-Rated Tools for Measuring DORA Metrics**](https://jellyfish.co/blog/dora-metrics-tools/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-tools/)

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

Qualified