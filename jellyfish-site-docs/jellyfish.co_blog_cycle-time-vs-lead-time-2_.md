---
url: "https://jellyfish.co/blog/cycle-time-vs-lead-time-2/"
title: "Cycle Time vs. Lead Time | Jellyfish Blog"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/cycle-time-vs-lead-time-2/#content)

![Cycle Time vs. Lead Time: Know the Difference!](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-33-1.jpg)

![](https://jellyfish.co/wp-content/uploads/2021/11/Jellyfish_Blog-Author-Headshots_Aston-Whiteling.webp)

Aston Whiteling

November 16, 2021

Time. It’s what DevOps really boils down to, isn’t it?

Streamlining your development and operations so that their interactions are perpetually and efficiently intertwined, minimizing the time spent executing engineering processes.

That’s the idea, anyway. In practice, things can get a lot messier than my expository line above might let on.

DORA (Google’s DevOps Research and Assessment group) make it look easy; they exploded onto the scene with their ‘State of DevOps’ reports leading up to their seminal handbook [_Accelerate_](https://itrevolution.com/book/accelerate/) _,_ which outlines a simple set of metrics to support DevOps success. In doing so, they inspire engineering organizations the world over to adopt a metrics based approach to DevOps.

Some businesses were so eager to adopt the ideology that they ended up _‘building the plane while flying it’_ so to speak. DevOps implementations began without a firm understanding of how to measure successful adoption of the practice.

Since _Accelerate_’s publishing, the four key [DORA metrics](https://www.jellyfish.co/blog/dora-metrics-101/) have been refracted to include a dazzling array of variants, causing a great deal of confusion around knowing when and where a specific measurement will be effective.

Nowhere is this more apparent than with [_Lead Time_](https://www.jellyfish.co/blog/lead-time-in-devops/) and it’s compatriot [_Cycle Time_](https://www.jellyfish.co/blog/issue-cycle-time-the-staple-engineering-operations-metric/). On the surface, they seem rather similar. They both measure a period of time reflecting the execution of a work process and both are valuable in the scope of DevOps. The key here is that they’re valuable in different contexts. These can be challenging to decipher; [Engineering Management Platform (EMP)](https://www.jellyfish.co/blog/what-is-an-engineering-management-platform/) vendors and engineering teams alike can sometimes cross wires and believe these two metrics are equitable.

In this article I’m going to draw attention to the distinction between _Lead Time_ and _Cycle Time_, as well as highlight the correct context in which each metric is at its most valuable.

## **Operational (Cycle Time) Vs. Strategic (Lead Time)**

On the one hand, DevOps’ is a highly strategic methodology. It’s a practical blending of IT and Engineering functions, to be sure, but the outcome has an expansive impact on the go-to-market strategy which software businesses can adopt. On the other side of the spectrum, DevOps can be used purely as a benefit to operations. It’s inherently IT and Engineering functions that are being streamlined. This means that its outcome can be strictly operational if that’s the desired scope.

But it’s this contrast that’s caused so much confusion when it comes to DevOps metrics. Their value is entirely dependent on your chosen definition of success, be it operational or strategic. Understanding which context delivers your desired success criteria is thus key when implementing a metrics based DevOps strategy.

This is where we find _Cycle Time_ butting heads with _Lead Time._

### Cycle Time

You see, _Cycle Time_ is an operational metric. It’s the measure of how long it takes to execute a process where one _‘unit of work’_ is the outcome. This can be, for example, the time it takes between an engineer opening a pull request and when that same PR is merged. Or it might be the time from an issue in Jira to move from ‘In Progress’ to ‘Done’. _Cycle Time_ can help estimate the delivery date of a given project, streamline processes to meet project targets, and improve overall efficiency for a given task. It’s a powerful metric, no doubt; an ideal evaluation tool – from an operational perspective, that is.

Cycle time is also easy to measure. All you need is a binary set of dates and times from your source contral’s metadata or your issue tracking tool and you’re good to go. It can be tempting to extrapolate the wisdom you get from this metric around process efficiency, and apply that to infer wider business value. But _Cycle Time_ has too narrow a focus. It does not consider ideation or value delivery, and so using this metric in place of _Lead Time_ can cause inaccurate reporting at best. At worst, when the metric fails to predict business impact, it can underpin a loss of trust within Engineering.

### Lead Time

If you’re after a more strategic view, one that can deliver value to those outside of technical roles, then you’re looking to measure _Lead Time_: the time from when a change request is initiated to when that change is running in production.

_Lead Time_ has an expanded scope in comparison to _Cycle Time._ Where _Cycle Time_ focuses on a siloed process, the goal in measuring _Lead Time_ is understanding how long it takes to deliver value to your customers from the time when the necessary change was conceived. Ideally, it involves encompassing processes and ideation prior to your initial source control action, and therefore is a better measure for the time between the inception of the idea and when that idea begins to bring market advantage.

Accurate calculation of lead time requires incorporating multiple sources (e.g. Jira + GitHub + CircleCI), which makes it that much more difficult to calculate. But in doing so, other organizations within the business, such as Product and Sales, gain more value from this measurement and become invested in Engineering success.

### **Why Using Both Cycle Time AND Lead Time Is Best**

Two metrics, two distinct value scenarios.

_Cycle Time_ is easier to calculate (usually from just one system) but has a more narrow focus on process efficiency. It is extremely valuable when it comes to operational streamlining.

_Lead Time_ is more challenging to calculate but offers a broader business perspective. By keeping the ideation or change initiation as well as value delivery process within scope, _Lead Time_ makes business alignment easier to achieve.

Context is key, and depending on your desired outcomes for DevOps success, each metric can bring value to your organization. Evaluate which metric is better suited for what you want to achieve.

Just be weary of vendors who confuse the two; make sure the metric they’re advertising is the one you’re getting!

Ideally, you’d calculate both and leverage the appropriate value from each metric within their respective functional areas. That’s why at Jellyfish we provide both _Cycle Time_ and _Lead Time_ with the [Jellyfish Engineering Management Platform](https://www.jellyfish.co/platform/). If you’d like to learn more about a solution to support your organization, check out our [feature announcement blog](https://www.jellyfish.co/blog/devops-metrics-jellyfish-announcement) or watch our two-minute [DevOps overview video](https://www.youtube.com/watch?v=kyqlpT9fz5g) to see how Jellyfish is helping elite engineering teams optimize their DevOps processes.

## Dive Deeper with Jellyfish Content

[![Jellyfish ADO Integration](https://jellyfish.co/wp-content/uploads/2025/10/blog-Jellyfish-and-azure-devops-1024x561.webp)](https://jellyfish.co/blog/ado/)[**Jellyfish Now Brings Developer Productivity and AI Insights to Azure DevOps Customers**](https://jellyfish.co/blog/ado/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/ado/)

[![What are DORA metrics? And Why Are They So Important](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-45-1024x536.jpg)](https://jellyfish.co/blog/dora-metrics-101/)[**What are DORA metrics? And Why Are They So Important?**](https://jellyfish.co/blog/dora-metrics-101/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-101/)

[![](https://jellyfish.co/wp-content/uploads/2025/03/blog-Product-Strategy_-The-Zeroth-Engineering-Unlock-1024x545.webp)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)[**Product Strategy: The Zeroth Engineering Unlock**](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified