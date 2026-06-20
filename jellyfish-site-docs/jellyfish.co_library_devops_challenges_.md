---
url: "https://jellyfish.co/library/devops/challenges/"
title: "6 Common DevOps Challenges & How to Solve Them"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/devops/challenges/#content)

In this article

If you read enterprise vendor blogs, DevOps sounds like a flawless assembly line where code flows perfectly from a developer’s laptop to production.

If you ask the engineers managing those pipelines, you get a very different story. The reality of modern software delivery is often a chaotic mix of undocumented infrastructure, tool fatigue, and cultural resistance. Moving to continuous delivery requires more than just purchasing a new deployment tool—it requires fundamentally changing how your organization handles accountability and architecture.

Here are six of the most critical DevOps challenges engineering teams face today, straight from practitioners on the ground, and how leadership can help solve them.

1\. Securing Cultural Buy-in and Overcoming Legacy Habits

## 1\. Securing Cultural Buy-in and Overcoming Legacy Habits

Many organizations assume that changing job titles will magically fix a broken delivery pipeline. In reality, leadership often views DevOps as a quick cost-cutting measure rather than a fundamental shift in shared ownership, leading to massive pushback from legacy development teams and deeply ingrained silos.

As one [DevOps engineer](https://www.reddit.com/r/devops/comments/18fj4sn/biggest_devops_challenge/) [explained](https://www.reddit.com/r/devops/comments/18fj4sn/biggest_devops_challenge/): _“Adoption and buy-in from a cultural perspective. True and comprehensive DevOps is radically different from most legacy structures, and as such, often requires significant process change to fully implement. This presents all kinds of challenges from development teams… The return of proper DevOps isn’t gained quickly. It’s a long-term return, often found in cost avoidance, so it becomes really hard to sell to suits that want a multiple return in the next 3 quarters.”_

**How to solve it:**

- **Tie deployment health to developer KPIs:** Ensure that feature delivery metrics are actively balanced with operational stability metrics during performance reviews to enforce shared ownership among all team members.
- **Embed operations directly into product pods:** Remove the physical and organizational barriers by placing reliability engineers into daily standups alongside core developers to build true cross-functional teams.
- **Translate engineering work into business outcomes:** Stop pitching the benefits of DevOps to your executive team and start presenting concrete reductions in downtime, faster time-to-market, and decreased developer onboarding costs

**Learn more →** One of the most frustrating parts of leadership is translating technical workflows into terms the rest of the business actually cares about. If you are struggling to secure executive buy-in, Jellyfish Co-Founder and CEO Andrew Lau shares his perspective from both sides of the table, offering actionable advice on how to navigate the hardest questions your board and CEO will throw at you. [**Get the free guide**](https://jellyfish.co/resources/ceo-translator-guide/).

2\. Managing Toolchain Sprawl and Cognitive Load

## 2\. Managing Toolchain Sprawl and Cognitive Load

The ecosystem of DevOps tools is massive and constantly shifting. Expecting one person or a small team to master every new iteration of Kubernetes, Docker, Terraform, Jenkins, and various cloud providers leads directly to burnout.

One [professional shared](https://www.reddit.com/r/devops/comments/80ftc6/what_are_some_of_the_biggest_challenges_you_face/) the exhausting reality of keeping up: _“The complete diversity of tools and releases every day is both a gift and a curse… the amount of time you need to spend staying relevant is a part-time job unto itself, and companies expecting specialized experts in technologies with less than a few years of mass adoption. I have to be up 2 hours earlier every morning before the actual job starts and stay an hour later just to do in-depth studying.”_

**How to solve it:**

- **Implement a strict one-in-one-out tool policy:** Force teams to formally deprecate an overlapping legacy system before approving procurement for new toolsets or frameworks.
- **Abstract complexity with an internal developer platform (IDP):** Build a [self-service platform](https://jellyfish.co/library/platform-engineering/internal-developer-platform/) that allows developers to provision infrastructure and ship code without needing to constantly learn new APIs or become Kubernetes
- **Allocate dedicated upskilling hours:** Instead of treating tool education as an extracurricular activity, officially block out engineering sprint time to foster a culture of continuous learning.

3\. Letting Infrastructure as Code (IaC) Rot Into Technical Debt

## 3\. Letting Infrastructure as Code (IaC) Rot Into Technical Debt

Treating infrastructure as code is a massive leap forward, but only if you maintain it with the same rigor as your application code. Too often, teams write complex deployment scripts once, abandon them, and leave zero documentation or even proper version control behind.

Another [engineer chimed in](https://www.reddit.com/r/devops/comments/1jqbexk/whats_the_most_frustrating_part_of_devops_that_no/) on the lack of maintenance: _“I’m currently working with a cloud platform team that does IaC without knowing why, so every repo is set and forget. No care and feeding of the code unless they need to make a change, and then it’s hours to unpick, sort new modules into place, etc., before they can change a simple IP.”_

**How to solve it:**

- **Automate** **infrastructure drift detection:** Run scheduled jobs that compare your actual cloud state to your Terraform state files, immediately flagging any manual console changes in your DevOps environment for review.
- **Enforce CI/CD pipelines for infrastructure changes:** Require all IaC updates to pass through automated linting, security scanning, and peer review before they can be merged into the main branch.
- **Mandate comprehensive README files:** Programmatically block pull requests for new infrastructure repositories that lack defined dependencies, architectural diagrams, and deployment instructions.

4\. Over-engineering Pipelines for Simple Use Cases

## 4\. Over-engineering Pipelines for Simple Use Cases

Not every internal application needs a scalable, globally distributed, multi-region microservices architecture. DevOps engineers often fall into the trap of building incredibly complex pipelines for tools that simply do not require them, slowing down the actual development process.

One user [summarized the frustration](https://www.reddit.com/r/devops/comments/1jqbexk/whats_the_most_frustrating_part_of_devops_that_no/) perfectly: _“Trying to put advanced DevOps on a project that doesn’t need it. How many times do we see in here a story about someone implementing microservices, or feature flags or something, for an app used by 100 people? Not everything needs continuous ringed deployment, sometimes simple CI/CD with testing and a backlog is enough.”_

**How to solve it:**

- **Require architectural decision records (ADRs):** Mandate written documentation for why a specific infrastructure pattern or orchestration method was chosen, forcing engineers to justify the operational cost of adding a new microservice.
- **Establish a strict complexity budget:** Define maximum thresholds for the number of routing layers and dependencies allowed for tier-three internal applications to keep DevOps practices
- **Enforce standard deployment templates:** Provide pre-configured, baseline CI/CD templates for low-risk applications so engineers don’t waste time reinventing custom DevOps pipelines from scratch.

5\. Being Treated as an Isolated Cost Center

## 5\. Being Treated as an Isolated Cost Center

When organizations fail to understand shared responsibility, they treat DevOps professionals as a glorified IT support desk. This strips away their ability to do strategic automation work and makes them an easy target during budget cuts.

One Reddit [user highlighted](https://www.reddit.com/r/devops/comments/1jqbexk/whats_the_most_frustrating_part_of_devops_that_no/) how this impacts the DevOps team’s perceived value: _“Not gonna say anything new but being seen as a cost centre instead of delivering value through efficiency, automation, reduced risks due to redundancy/HA, etc. Almost always resulting in being understaffed. Quite different \[from\] how actual developers are being seen with questionable ROI for new features.”_

**How to solve it:**

- **Quantify automation in engineering hours saved:** Transition your reporting from vanity metrics to concrete numbers, showing executives exactly how many manual provisioning hours were eliminated this quarter.
- **Establish strict engagement rules for developers:** Require product teams to provide specific logs, error messages, and proof of initial troubleshooting before they are allowed to escalate a ticket to the [platform team](https://jellyfish.co/library/platform-engineering/team-structure/).
- **Map engineering allocation to business initiatives:** Actively track where your specialized operational talent is spending their time to prove they are driving strategic growth rather than just fixing bugs.

**PRO TIP**: Jellyfish automatically tracks your [resource allocation](https://jellyfish.co/platform/resource-allocations/), giving you clear visibility into exactly how much time your DevOps team spends on strategic automation versus unplanned maintenance. Use this concrete data to shift the conversation from cost to value and definitively prove your team’s impact to executive leadership.

![Jellyfish Allocations](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/05/Jellyfish-Allocations-3.png)

6\. Ignoring Observability and Post-Deployment Metrics

## 6\. Ignoring Observability and Post-Deployment Metrics

Continuous delivery does not end when the code hits production. A major challenge is that organizations ship features quickly but never actually collect the data required to see if those features solved the user’s problem.

As one engineer [pointed out on Reddit](https://www.reddit.com/r/devops/comments/18fj4sn/biggest_devops_challenge/): _“It’s supposed to be a process where CI and CD are but two parts, however the part where we collect data is by far the least used one and instead I see product managers ‘forget’ AB testing (or similar) all the time in favour of how they ‘feel’ that a change is received by the customer/end users, or ignore feedback because it doesn’t fit their narrative.”_

**How to solve it:**

- **Establish mandatory observability SLAs:** Block deployments that do not include basic telemetry hooks for error rates, latency, and adoption metrics.
- **Configure automated rollback triggers:** Set your deployment pipelines to automatically roll back to the previous build if error rates exceed a specified threshold within the first 10 minutes of a release.
- **Broadcast DORA metrics company-wide:** Make [deployment frequency](https://jellyfish.co/blog/breaking-down-deployment-frequency/), [lead time for changes](https://jellyfish.co/library/change-lead-time/), and [change failure rates](https://jellyfish.co/blog/change-failure-rate/) highly visible to the entire product organization to force data-driven decision-making.

How Can Jellyfish Help

## How Can Jellyfish Help

![Jellyfish Dashboard](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/05/Jellyfish-Dashboard.png)

Solving cultural friction, technical debt, and pipeline bottlenecks is nearly impossible when you have to spend hours manually pulling data from fragmented tools just to justify your team’s existence.

To permanently shift your DevOps function from an isolated cost center into a strategic business driver, you need objective data. **Jellyfish** connects directly to your continuous integration, incident management, and issue-tracking tools to give you a complete view of your engineering operations.

With Jellyfish, you can:

- **Prove your business impact:** Translate technical engineering work into concrete business value by tracking [resource allocation](https://jellyfish.co/platform/resource-allocations/). Show executives exactly how much time your team invests in strategic infrastructure automation versus fixing bugs and fighting legacy fires.
- **Pinpoint the real bottlenecks in your pipeline:** Use [Life Cycle Explorer](https://jellyfish.co/platform/life-cycle-explorer/) to get a granular view of your software development life cycle. Highlight the exact stages where code sits idle, allowing you to adapt your workflows and streamline manual handoffs instead of over-engineering complex new tools.
- **Measure continuous improvement automatically:** Track [core DORA](https://jellyfish.co/platform/engineering-metrics/) [metrics](https://jellyfish.co/platform/engineering-metrics/)—including deployment frequency, mean time to resolution, and change failure rate—without maintaining [custom](https://jellyfish.co/platform/data-hub/) [dashboards](https://jellyfish.co/platform/data-hub/). This provides the hard data required to prove that your new operational practices are actually accelerating software delivery.
- **Reduce cognitive load and prevent burnout:** Gain deep visibility into [how work is distributed](https://jellyfish.co/solutions/engineering-product-operations/team-workflow-analysis/) across your platform team. Ensure your specialized engineers are properly balanced between handling daily operational tickets and executing the deep-work initiatives required to permanently eliminate technical debt.

![Jellyfish CHG Hleathcare](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/05/Jellyfish-CHG-Hleathcare.png)

Gain the objective visibility you need to optimize your workflows, prove ROI, and deliver high-quality software faster.

To learn more about Jellyfish, [**take a product tour**](https://jellyfish.co/tour/) or [**request a demo**](https://jellyfish.co/request-a-demo/) today.

FAQs

## FAQs

### How do you successfully implement DevOps across a legacy organization?

To successfully implement DevOps in deeply entrenched architectures, stop treating DevOps adoption as a purely cultural mandate and treat it as a structural engineering problem.

- **Abstract infrastructure with an internal developer platform (IDP)**: [Build golden paths](https://jellyfish.co/library/platform-engineering/golden-paths/) that allow developers to deploy to production environments without needing deep expertise in AWS or complex configuration management.
- **Decouple from dedicated operations teams**: Shift from a ticket-based request system to a self-service model, removing the manual friction that traditionally blocks rapid delivery.
- **Drive behavioral changes through tooling, not lectures:** You foster a true DevOps culture by providing systems that make the right way the easiest way, rather than forcing legacy developers to memorize new agile methodologies.

### How do you integrate DevSecOps without bottlenecking development?

True DevSecOps means moving security out of the final review phase and directly into the PR pipeline.

- **Shift security left with automated testing:** Embed scanners directly into pre-commit hooks to catch vulnerabilities before code is ever merged.
- **Provide developers with the right tools:** Give engineers localized, fast-feedback linting so they can verify security and core functionality without waiting on central QA.
- **Maintain rapid release cycles:** By enforcing end-to-end compliance programmatically at the individual contributor level, you prevent late-stage security audits from halting deployments.

### How do you measure and prove the ROI of your DevOps transformation?

A successful DevOps implementation cannot be justified to the business using only CI/CD build minutes or commit volume. To prove value:

- **Map engineering time to business outcomes:** Show your non-technical stakeholders exactly how many manual provisioning hours were eliminated and redirected into building revenue-generating features.
- **Track DORA metrics in real-time:** Use objective telemetry to prove that reducing your mean time to recovery (MTTR) directly preserves uptime and protects the bottom line.

About the author

![Lauren Hamberg](https://jellyfish.co/wp-content/uploads/2025/03/Lauren-Hamburg.jpg)

Lauren is Senior Product Marketing Director at Jellyfish where she works closely with the product team to bring software engineering intelligence solutions to market. Prior to Jellyfish, Lauren served as Director of Product Marketing at Pluralsight.

Follow: [LinkedIn](https://www.linkedin.com/in/laurenhamberg/)

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-Data-Hub-1024x610.png)](https://jellyfish.co/blog/dora-metrics-tools/)[**8 Top-Rated Tools for Measuring DORA Metrics**](https://jellyfish.co/blog/dora-metrics-tools/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-tools/)

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

Qualified