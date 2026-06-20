---
url: "https://jellyfish.co/blog/improving-jira-workflows/"
title: "Improving Jira Workflows | Jellyfish Blog"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/improving-jira-workflows/#content)

![Best Practices for Jira Workflows](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header.-2-1.jpg)

![](https://jellyfish.co/wp-content/uploads/2021/11/Jellyfish_Blog-Author-Headshots_Evan-Klein.webp)

Evan Klein

September 14, 2021

## Best Practice: Balance consistency with autonomy when building workflows across teams

Building out a workflow that works effectively takes some time, but it’s worth the investment. Jira workflows are highly customizable, and this will likely be an iterative process, but don’t settle with a sub-optimal workflow. When you’ve developed a workflow that functions well, think about how much of that you want to standardize across different teams in your organization. A one-size-fits-all approach likely won’t work and could limit efficiency on some teams, but some amount of consistency around workflows can be helpful for driving communication and collaboration across teams, for comparisons and sharing of learnings, for cross-team mobility, and for reporting and analytics to improve processes.

While we’ll stop short of being prescriptive in exactly how to build and what to include in your workflows, here are 5 suggestions:

1. Different teams and projects will need to have different statuses, but it may be helpful to guide your team to think about how statuses align to the value stream of their software development process. Simplicity almost always trumps complex and convoluted workflows. Too many statuses and transitions will likely leave you unable to see the forest for the trees.
2. Consider who has permission to transition issues and in what circumstances, especially whether they can revert issues to a previous state.
3. Use the “Assignee” component as you move issues through the workflow. Too often teams will leave this step out, which results in issues sitting unworked for long periods of time, a lack of visibility both during and after the process (who do you turn to with questions about a particular piece of code or decision?), and a lack of accountability on teams.
4. Don’t make Jira workflows more complicated than they need to be by unassigning people when the work is done or passing all Jira tickets through a single person for approval.
5. Ensure that statuses in your workflow are tied to specific resolutions. Jira does not consider work on an issue to be finished until the “Resolution” field has a value. By linking the “Complete” or “Fixed” or “Won’t Fix” status to a corresponding resolution, you will ensure issues will not be accidentally left as active.

## Best Practice: Automate your workflows as much as possible

The benefits of automating development processes are well documented by now, and in fact many consider it to be a key to success for modern software engineering organizations. But when it comes to Jira workflows, a process that is so central to software development for many agile teams, most still manage in a relatively manual way. That does not need to be the case. By linking coding and development work done outside of Jira to associated projects, teams can remove a lot of manual, and error-prone process management and create projects that are simpler to manage, easier to collaborate, and cleaner to report from.

### Proper linking for Jira workflow automation

The most obvious, and most important linking should happen between Jira and Git, but linking should also be done for Incident Management (Pagerduty, Splunk On-Call \[formerly VictorOps\], etc.), Customer Support (Zendesk, Freshdesk, etc.), and other tools common in your development process. By linking coding, bug fix, support, and other work to its related Jira project, each engineer and their teammates will be able to see work done in relation to their projects, which means less context (and platform) switching, greater visibility for other teammates working on the same project, and better communication as issues move through the workflow. Proper linking can also enable automation of issue status changes and assignment to team members (we recommend teams standardize the practice of putting the Jira ticket number in the title of the commit or PR in Git (i.e. ABC-123)).

Linking also ensures that code work is limited to specific Jira issues, avoiding the submission of large blocks of code to tick off multiple issues. Proper hygiene in this sense creates a record of work that is easier to parse and cleaner to report. Automation has the added benefit of maintaining standardization. By removing manual tagging or labeling, automating issues movement through workflows, and assignment, it becomes clear to see how much of each type of work is taking place, and how that breakdown affects your engineering teams. This will help you track [Allocation](https://www.jellyfish.co/blog/what-is-allocation/), or the categories of work into which teams are investing time, which will be helpful for operational planning, team and hiring decisions, and more.

For many software development teams, Jira is essential for tracking issues and projects, which means it is central to engineering operations. Check out part 1 of this series to learn about ways that teams successfully [organize their projects in Jira,](https://www.jellyfish.co/blog/jira-best-practices-project-organization/) or part 2 to explore [how to use Jira structure to improve your engineering operations](https://www.jellyfish.co/blog/jira-structure/).

To learn more about how Jellyfish works with Jira to help drive alignment and improve engineering operations, head over to [jellyfish.co](https://www.jellyfish.co/).

## Dive Deeper with Jellyfish Content

[![Jellyfish ADO Integration](https://jellyfish.co/wp-content/uploads/2025/10/blog-Jellyfish-and-azure-devops-1024x561.webp)](https://jellyfish.co/blog/ado/)[**Jellyfish Now Brings Developer Productivity and AI Insights to Azure DevOps Customers**](https://jellyfish.co/blog/ado/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/ado/)

[![What are DORA metrics? And Why Are They So Important](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-45-1024x536.jpg)](https://jellyfish.co/blog/dora-metrics-101/)[**What are DORA metrics? And Why Are They So Important?**](https://jellyfish.co/blog/dora-metrics-101/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-101/)

[![](https://jellyfish.co/wp-content/uploads/2025/03/blog-Product-Strategy_-The-Zeroth-Engineering-Unlock-1024x545.webp)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)[**Product Strategy: The Zeroth Engineering Unlock**](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified