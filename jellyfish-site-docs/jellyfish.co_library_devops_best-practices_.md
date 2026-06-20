---
url: "https://jellyfish.co/library/devops/best-practices/"
title: "12 DevOps Best Practices [Based on Real Experiences]"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/devops/best-practices/#content)

In this article

If you search for “DevOps best practices,” you will find endless theoretical lists that assume you work at a FAANG company with infinite resources, massive scale, and perfect automated testing.

But out in the real world, engineering leaders are fighting a different battle. You are balancing legacy monoliths, manual approval gates, alert fatigue, and the constant pressure to ship faster without breaking production. Pragmatic DevOps isn’t about blindly copying Netflix; it is about applying the right level of automation and cultural shifts to solve your specific business bottlenecks.

We scoured industry guidelines and tapped into unfiltered discussions from the DevOps teams actually doing the work to compile this list. Here are 12 DevOps best practices grounded in reality, complete with the hard truths you won’t find in a vendor’s sales pitch.

1\. Align Architecture with Actual Business Needs

## 1\. Align Architecture with Actual Business Needs

The tech industry loves cargo-culting the latest architectural trends. Teams will often spend months migrating to microservices or Kubernetes simply because it is considered a best practice, severely over-engineering a product that barely has 1,000 active users.

As one practitioner [bluntly stated](https://www.reddit.com/r/devops/comments/17m63nj/dont_forget_that_much_of_what_defines_devops_best/): _“Don’t forget that much of what defines ‘DevOps Best Practice’ is methods and strategies that are really only for huge web SaaS platforms at global scale… Monoliths are almost always better than microservices… Unless you know why you need microservices, don’t do it… A lot of so-called engineers live and die by following blog posts like a cooking recipe.”_

**How to implement this best practice properly:**

- **Require an Architectural Decision Record (ADR):** Before adopting a complex new orchestrator, force the team to formally document the specific business bottleneck (like horizontal scaling limits) that the new technology solves.
- **Embrace the modular monolith:** If you are a small team, build a well-structured monolith first. It is infinitely easier to extract a single microservice later than it is to manage 15 poorly defined distributed services on day one.
- **Match infrastructure to revenue:** Do not build multi-region, active-active failovers for internal tools or MVPs. Scale your architectural complexity at the exact same pace you scale your revenue.

2\. Transition to True Continuous Delivery (CD)

## 2\. Transition to True Continuous Delivery (CD)

Continuous Integration (CI) is widely adopted, but true Continuous Delivery—where code automatically deploys to production without a human clicking a button—remains the white whale of enterprise engineering.

One engineer [highlighted this massive industry gap](https://www.reddit.com/r/devops/comments/1mlke5t/whats_one_standard_devops_practice_thats_actually/): _“Continuous Delivery (CD) by far \[is the rarest standard practice\]. I’ve never once witnessed a dev team release code to production without some kind of gate in place… The business still wanted that last step to be manual every time.”_

However, when CD is embraced, the cultural shift is massive. Another [engineer argued](https://www.reddit.com/r/devops/comments/17m63nj/dont_forget_that_much_of_what_defines_devops_best/): _“The whole point is getting releases away from being these big events or fire drills. Fixing a bug shouldn’t be a huge problem, in CD it’s just your normal day… Releases were constrained by technology and resources in the past and now they’re not, so the whole paradigm can shift.”_

**How to implement this best practice properly:**

- **Automate the final gate for low-risk services:** Start your CD journey by entirely automating the deployment of your lowest-risk, tier-three internal applications to build trust with business stakeholders.
- **Decouple deployments from releases:** Use feature flags to merge and deploy code changes to production constantly. The code sits dormant until the product manager flips the switch to actually _release_ the new feature to the user.
- **Implement automated rollback triggers:** Set your pipelines to automatically roll back to the previous build if the error rate spikes above 5% within the first 10 minutes of a deployment.

**PRO TIP:** You cannot improve your continuous delivery pipeline if you do not know your baseline. Jellyfish automatically tracks the most important [engineering](https://jellyfish.co/platform/engineering-metrics/) [metrics](https://jellyfish.co/platform/engineering-metrics/), such as [deployment frequency](https://jellyfish.co/blog/breaking-down-deployment-frequency/) and [change failure rate](https://jellyfish.co/blog/change-failure-rate/), giving you instant, out-of-the-box visibility into whether your CD efforts are actually speeding up your software release cycles.

![Jellyfish_Issue Change Lead Time](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/05/Jellyfish_Issue-Change-Lead-Time.png)

3\. Make Git the Absolute Source of Truth

## 3\. Make Git the Absolute Source of Truth

If a developer can log into an AWS console and manually tweak a security group to fix an issue, your environment is fragile. GitOps enforces the practice that your Git repository is the sole source of truth for both your application and your infrastructure.

An [engineer shared](https://www.reddit.com/r/devops/comments/17m63nj/dont_forget_that_much_of_what_defines_devops_best/) the transformative power of this approach: _“I’ve been loving switching people to GitOps… forcing them to all make the main branch of GitHub their source of truth was life changing. Try making a change to prod, and ArgoCD will change it right back. Follow the process, get the right approvals, and record every change, and magically prod isn’t crashing anymore.”_

**How to implement this best practice properly:**

- **Revoke manual write access to production:** Restrict cloud console access to read-only for developers. If they need to change a configuration, they must push a [pull request](https://jellyfish.co/library/pull-request/) to the infrastructure repository.
- **Use reconciliation loops:** Deploy tools like ArgoCD or Flux that continuously monitor your live environment and automatically overwrite any manual configuration drift to match the Git
- **Version control** **your databases:** Treat database schema changes exactly like code. Use migration tools (like Flyway or Liquibase) triggered entirely through your [CI/CD pipeline](https://jellyfish.co/library/ci-cd/).

4\. Stop Over-Engineering Infrastructure as Code (Beware of DRY)

## 4\. Stop Over-Engineering Infrastructure as Code (Beware of DRY)

In software engineering, [Don’t Repeat Yourself (DRY)](https://dev.to/codeofaccuracy/the-dry-dont-repeat-yourself-2ld2) is a golden rule. But when applied too strictly to Infrastructure as Code (IaC) like Terraform, it creates a tangled, unreadable web of variable inheritance that makes debugging a nightmare.

A frustrated engineer offered this [unusual tip](https://www.reddit.com/r/devops/comments/1oi1daa/whats_a_best_practice_you_actually_disagree_with/): _“DRY dogma kills so much Infrastructure as Code. So many Terraform bugs are obfuscated by unnecessary layers of variable inheritance created by bad usage of tools… Please, by all means, repeat yourself instead of implementing an unmaintainable chain of inheritance.”_

**How to implement this best practice properly:**

- **Optimize** **for readability, not deduplication:** It is perfectly acceptable to have 15 identical lines of Terraform in two different environment files if it means an engineer can understand the configuration at a glance during an outage.
- **Ban deeply nested modules:** Restrict your IaC modules to a maximum of one level deep. If a module calls another module that calls another module, you have created a black box.
- **Fail fast by avoiding defaults:** Do not set default values in your Helm charts or Terraform variables just to save lines of code. Force the engineer to explicitly declare the value for each environment so there are no production surprises.

5\. Enforce Strict Environment Parity

## 5\. Enforce Strict Environment Parity

If your application works flawlessly in staging but crashes the moment it hits production, you have a parity problem. CI/CD pipelines should compile an artifact exactly once, and that exact same immutable artifact should be promoted through every environment.

One engineer [pointed out](https://www.reddit.com/r/devops/comments/1mlke5t/whats_one_standard_devops_practice_thats_actually/) how often teams sabotage themselves here: _“Build once, deploy many. I can’t tell you how often I’ve seen bespoke builds per environment… Usually, along with long-lived branches, cherry picks, and a ton of flaky behavior as a result. I mean, seriously, I’ve seen this all over. Why do we do this to ourselves?!”_

**How to implement this best practice properly:**

- **Promote images, not code:** Configure your pipeline to build a Docker image, tag it, and push it to a registry in the very first CI stage. Your staging and production pipelines must simply pull and run that exact image hash.
- **Externalize your configurations:** The only thing that should change between environments is the configuration data (API keys, database URLs). Inject these via environment variables or secret managers at runtime.
- **Standardize local development processes:** Use dev containers or remote cloud development environments so developers are writing code on the exact same OS and library versions that run in production.

6\. Treat Operations as Software Engineering

## 6\. Treat Operations as Software Engineering

DevOps is not about writing bash scripts to automate server reboots. It is about applying the rigorous disciplines of software engineering—testing, version control, and modularity—to operational infrastructure.

An experienced practitioner [offered this advice](https://www.reddit.com/r/devops/comments/1gdriey/advice_on_integrating_devops_practices_in_a/) for modernizing Ops:

_“You are now a software developer doing Ops. I will repeat, you are a software developer doing Ops. Beat that into your subconscious. ClickOps doesn’t exist anymore… Your recipe to success is Git, Automated Testing, and Continuous Delivery. Having proper tests for your stuff is such an underrated aspect of being a DevOps Engineer.”_

**How to implement this best practice properly:**

- **Test your infrastructure code**: Use tools like tflint or terratest to automatically validate your infrastructure changes in a sandbox before they are allowed to merge.
- **Build self-service APIs:** Wrap your common operational tasks (like provisioning a new database or granting access) in an API or Slack integration so developers can self-serve.
- **Actively track and eliminate toil:** Define _toil_ (repetitive, manual operational work) and track the hours spent on it. Dedicate at least 20% of every sprint specifically to automating that toil away.

**Recommended read →** [The DevOps Transformation Roadmap for](https://jellyfish.co/library/devops-transformation/) [Operations Teams](https://jellyfish.co/library/devops-transformation/)

7\. Rethink Code Reviews and Embrace Pair Programming

## 7\. Rethink Code Reviews and Embrace Pair Programming

Strict pull request (PR) processes are a standard best practice, but they frequently become massive bottlenecks that slow down software delivery and frustrate team members.

One engineer [pointed out](https://www.reddit.com/r/devops/comments/1mlke5t/whats_one_standard_devops_practice_thats_actually/) the hidden value of [pair programming](https://jellyfish.co/blog/pair-programming-measurement-with-jellyfish-supporting-contemporary-software-development/): _“Pair work is necessary to mitigate tech debt. But managers see two people working on one thing as a waste of resources. They don’t see the avoided cost of problems that did not occur.”_

Another engineer voiced the [frustration of PR gridlock](https://www.reddit.com/r/devops/comments/1oi1daa/whats_a_best_practice_you_actually_disagree_with/) on Reddit: _“Somehow people are so adamant that code review is a must and pull request is a must because ‘it shares knowledge and ensures quality’… It has also always been a massive bottleneck in every single org I’ve been at… I prefer the option of making pull requests optional, and try working in pairs so you have a second opinion while you work.”_

**How to implement this best practice properly:**

- **Log pair programming as a strategic investment:** Educate product managers that pairing is an active form of real-time [code review](https://jellyfish.co/library/developer-productivity/peer-code-review-best-practices/) that eliminates the async wait times of traditional PRs.
- **Implement strict PR size limits:** Reject pull requests that exceed 400 lines of code. Massive PRs cannot be reviewed effectively and encourage reviewers to blindly approve them just to clear their queue.
- **Experiment with trunk-based development:** For high-trust, senior development teams, allow direct commits to the main branch protected by an incredibly robust, automated test suite that catches regressions instantly.

**PRO TIP:** If you suspect pull requests are stalling your delivery, use Jellyfish’s [Life Cycle Explorer](https://jellyfish.co/platform/life-cycle-explorer/). It pinpoints exactly where code sits idle—whether it is waiting for a review, stuck in QA, or pending deployment—so you can fix the exact workflow causing the delay.

![Jellyfish Life Cycle Explorer](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/05/Jellyfish-Life-Cycle-Explorer.png)

8\. Stop Overpaying for Theoretical Redundancy

## 8\. Stop Overpaying for Theoretical Redundancy

Every business wants the [five-nines of uptime](https://fivenines.io/blog/server-performance-monitoring-key-metrics-and-achieving-five-nines-uptime/) (99.999%), but few actually need it, and even fewer understand the exponential cost of maintaining it. Keeping idle resources running just in case of a failure is an outdated practice.

One practitioner [challenged the dogma of Availability Zones](https://www.reddit.com/r/devops/comments/1oi1daa/whats_a_best_practice_you_actually_disagree_with/): _“I was crucified in /sre for suggesting using AZs is a default everybody does and ‘good practice’ but there’s little indication that AZs go down significantly more often than a whole region… yet everybody uses like 3 AZs for redundancy, at 4x the cost or whatever (instances plus traffic plus time invested in the complexity of fail over).”_

Another engineer offered a [grounded perspective on uptime](https://www.reddit.com/r/devops/comments/17m63nj/dont_forget_that_much_of_what_defines_devops_best/): _“Yes, every business wants >99.99% uptime when they need it, but if Chick-fil-A is closed every Sunday, you can bring everything down for an hour then if you need to. Maybe that simplifies your deployment process or infrastructure.”_

**How to implement this best practice properly:**

- **Define actual Service Level Objectives (SLOs):** Force the business to define exactly how much downtime is acceptable and tie architectural costs to that number. Do not build an active-active failover for a B2B app that only sees traffic during office hours.
- **Rely on dynamic auto-scaling:** Stop pre-provisioning massive buffers of idle compute. Trust your auto-scaling groups and container orchestrators to spin up resources strictly when demand spikes.
- **Measure the cost of complexity:** Before adding a message queue or a caching layer for resiliency, calculate the engineering hours required to maintain, patch, and monitor that new component over three years.

**Recommended read →** [Cognitive Complexity in Software Engineering](https://jellyfish.co/library/cognitive-complexity/)

9\. Tune Your Observability

## 9\. Tune Your Observability

Setting up monitoring is easy, but making those alerts actually useful is incredibly hard. If your team ignores a PagerDuty alert because “it always does that on Tuesdays,” your monitoring is actively harming your reliability.

An [engineer called out](https://www.reddit.com/r/devops/comments/1mlke5t/whats_one_standard_devops_practice_thats_actually/) this common failure: _“Proper monitoring and alerting. Everyone sets it up, almost nobody actually tunes it.”_

Another engineer expressed the [pain of bad logging](https://www.reddit.com/r/devops/comments/1oi1daa/whats_a_best_practice_you_actually_disagree_with/): _“Using AWS CloudWatch logs and SNS for email alerts is kinda bad. The emails don’t show what the actual exception message was, only metric information… And it’s impossible to know if I broke something or these exceptions have been happening for 10 years.”_

**How to implement this best practice properly:**

- **Audit and delete noisy alerts:** Conduct a monthly review of all triggered alerts. If an alert triggered five times and required zero human intervention, delete it immediately.
- **Implement the RED method:** Base your high-priority alerting on Rate, Errors, and Duration. If the user experience is not currently degraded by one of these three metrics, it should not page an engineer at 2 AM.
- **Ensure logs are immediately actionable:** Mandate that all application exceptions include the stack trace, the affected microservice, and a direct link to the runbook for resolution.

10\. Prove Your Disaster Recovery (Don't Just Take Snapshots)

## 10\. Prove Your Disaster Recovery (Don’t Just Take Snapshots)

Everyone backs up their databases. Very few teams actually practice restoring those databases into a clean environment under the pressure of a simulated outage.

An [engineer highlighted](https://www.reddit.com/r/devops/comments/1mlke5t/whats_one_standard_devops_practice_thats_actually/) this critical flaw on Reddit: _“Proven disaster recovery. You might have the snapshots, but can you actually restore from 0? Or even better… Let’s say you only run in West Europe and your DR region is North Europe. Suddenly, the West Europe region is completely unavailable for 6 hours. You’re \[screwed\] – you’re going to try and spin up in North Europe, but so is everyone else, so good luck getting any resources there.”_

**How to implement this best practice properly:**

- **Schedule quarterly “Game Days”:** Intentionally sever access to a staging database and force the engineering team to restore it from backups while timing the recovery.
- **Automate the restoration process:** A backup is useless if it requires reading a 40-page outdated wiki document to restore. Script the exact database recovery process using your IaC
- **Test cross-region resource limits:** Ensure your cloud provider actually has the quotas and capacity reserved in your failover region to accommodate your entire infrastructure stack during a widespread outage.

11\. Automate Secret Rotation

## 11\. Automate Secret Rotation

Hardcoding passwords or leaving long-lived database credentials untouched for years is a massive security vulnerability. Yet, fully automated secret rotation remains incredibly rare in enterprise environments.

One practitioner exposed the [reality of this gap](https://www.reddit.com/r/devops/comments/1mlke5t/whats_one_standard_devops_practice_thats_actually/): _“Unless I’m being naive on my 20+ years of experience, I’m yet to see a company that rotates secrets automatically. Especially on those SQL servers… and all the ‘micro services’ that will also need automation to rotate the deployment after secret renewal that will never happen because of last-minute priority shifts.”_

**How to implement this best practice properly:**

- **Implement dynamic, short-lived secrets:** Use tools like HashiCorp Vault or AWS Secrets Manager to generate temporary database credentials that automatically expire after 15 minutes, rendering leaked keys useless.
- **Bind secrets to the pipeline, not the human:** Developers should never know the actual production deployment keys. The CI/CD system should retrieve them at runtime and flush them from memory immediately after use.
- **Use pre-commit hooks to block leaks:** Enforce automated scanning (like GitLeaks) on developer machines to prevent them from ever pushing hardcoded API keys to a remote repository.

12\. Ditch Arbitrary Estimates and Measure Actual Cycle Time

## 12\. Ditch Arbitrary Estimates and Measure Actual Cycle Time

A lot of engineering teams get bogged down in rigid Agile methodologies, spending hours arguing over story points and sprint commitments instead of actually writing code. When DevOps is implemented properly, continuous flow replaces rigid sprint boundaries.

As one engineer [controversially shared](https://www.reddit.com/r/devops/comments/1oi1daa/whats_a_best_practice_you_actually_disagree_with/): _“One of my most ‘controversial’ beliefs at work is that I fundamentally think that estimates are worthless and all effort put into setting ‘planned start’ and ‘planned end’ is completely wasted time. The job will be done when it’s done either way… No amount of pointing at the dates will ever make the product ready.”_

**How to implement this best practice properly:**

- **Track cycle time instead of velocity:** Focus on how long it takes a piece of work to go from the first commit to running in production, rather than how many imaginary points the team burned down during a sprint.
- **Standardize issue sizes:** Instead of guessing the effort required for every ticket, train the team to break every task down into chunks that can realistically be completed in two days or less.
- **Forecast using historical data:** Use your actual past delivery metrics to project timelines for stakeholders, relying on empirical data rather than developers’ optimistic guesses.

**Learn more →** [Issue Cycle Time: The Staple Engineering Operations](https://jellyfish.co/blog/issue-cycle-time-the-staple-engineering-operations-metric/) [Metric](https://jellyfish.co/blog/issue-cycle-time-the-staple-engineering-operations-metric/)

Speak the Language of the Boardroom with Jellyfish

## Speak the Language of the Boardroom with Jellyfish

Engineering leaders often struggle to defend their budgets and headcount because they cannot translate technical achievements into business value. Your CEO and CFO do not care about Kubernetes clusters or Terraform modules; they care about revenue, margins, and strategic growth.

Jellyfish is an [**Engineering Management Platform**](https://jellyfish.co/platform/engineering-management-platform/) that bridges the gap between your engineering department and the executive suite by tying engineering work directly to business outcomes.

Use Jellyfish to:

- [**Align engineering with business strategy**](https://jellyfish.co/solutions/business-alignment/) **:** Prove exactly how much engineering effort is dedicated to the company’s top strategic initiatives, ensuring your department is driving growth rather than just keeping the lights on.

![Jellyfish Engineering Investment](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/05/Jellyfish-Engineering-Investment.png)

- [**Streamline**](https://jellyfish.co/solutions/software-capitalization/) [**software capitalization**](https://jellyfish.co/solutions/software-capitalization/) **:** Automate the tedious, manual process of calculating capitalizable software development Jellyfish provides precise, audit-ready data for your finance team, saving engineering managers hours of work every month.

![Jellyfish Initiatives](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/05/Jellyfish-Initiatives.png)

- [**Benchmark against industry peers**](https://jellyfish.co/platform/benchmarks/) **:** Understand what good actually looks like. Compare your team’s performance, allocation, and delivery speed against thousands of other engineering organizations to identify areas for competitive advantage.

![Jellyfish Benchmarking](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/05/Jellyfish-Benchmarking.png)

Stop defending your engineering team with anecdotal evidence. Equip yourself with the financial and operational data you need to secure your budget, align with the C-suite, and lead your organization with confidence.

To learn more about Jellyfish, [**take a product tour**](https://jellyfish.co/tour/) or [**request a demo**](https://jellyfish.co/request-a-demo/) today.

FAQs

## FAQs

### What is the most effective way to implement these best practices without disrupting current delivery?

When implementing DevOps best practices, do not attempt a massive, end-to-end overhaul of your entire software development lifecycle overnight; instead, focus on incremental adoption.

- **Target the biggest bottleneck first:** Identify the specific stage in your DevOps pipeline that is causing the longest lead time (such as manual QA or cumbersome configuration management) and apply targeted automation there before changing anything else.
- **Start with low-risk workloads:** Apply continuous deployment and strict containerization standards to tier-three internal tools first to build trust, then roll them out further.
- **Take an iterative approach:** A successful DevOps transformation requires continuous improvement. Adopt one or two practices per quarter so the team can adjust to the new DevOps process without burning out.

### How do you drive cultural alignment between development and operations teams?

True DevOps culture isn’t built through rigid project management frameworks; it requires dismantling organizational silos at the structural level.

You must align incentives by making developers responsible for the code quality running in production environments, while operations focuses on providing self-service deployment platforms. This shared accountability ensures everyone is focused on delivering quality software rather than shifting blame when things break.

### How should leaders evaluate new infrastructure platforms to prevent tool sprawl?

The goal of adopting new DevOps tools should always be to reduce cognitive load, not increase it. Leaders must equip their teams with the right tools that natively abstract away complex cloud configurations, which directly limits human error during provisioning.

Prioritize platforms that support deep DevSecOps integration and long-term scalability, ensuring your architecture remains maintainable as your engineering headcount grows.

About the author

![Lauren Hamberg](https://jellyfish.co/wp-content/uploads/2025/03/Lauren-Hamburg.jpg)

Lauren is Senior Product Marketing Director at Jellyfish where she works closely with the product team to bring software engineering intelligence solutions to market. Prior to Jellyfish, Lauren served as Director of Product Marketing at Pluralsight.

Follow: [LinkedIn](https://www.linkedin.com/in/laurenhamberg/)

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-Data-Hub-1024x610.png)](https://jellyfish.co/blog/dora-metrics-tools/)[**8 Top-Rated Tools for Measuring DORA Metrics**](https://jellyfish.co/blog/dora-metrics-tools/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-tools/)

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

Qualified