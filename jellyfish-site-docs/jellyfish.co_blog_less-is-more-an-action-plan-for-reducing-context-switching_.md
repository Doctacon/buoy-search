---
url: "https://jellyfish.co/blog/less-is-more-an-action-plan-for-reducing-context-switching/"
title: "An Action Plan for Reducing Context Switching | Jellyfish Blog"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/less-is-more-an-action-plan-for-reducing-context-switching/#content)

![Less is More: An Action Plan for Reducing Context Switching (Part 1)](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-5-1.jpg)

![](https://jellyfish.co/wp-content/uploads/2022/03/Jim-Krygowski.jpg)

Jim Krygowski

April 11, 2023

In a previous blog I wrote about an experiment we ran to [reduce thrashing by managing unplanned work](https://www.jellyfish.co/blog/jellyfish-reduced-thrashing/). That blog focused on the positive benefits we (at Jellyfish) experienced in roadmap allocations and cycle time after we optimized how our engineering organization supported the production environment. Here, we continue to explore this theme together with Jellyfish Research.

Since we started researching and writing this blog there’s been a sea change in the software industry. We’ve transitioned from a growth at all costs mindset to one of focus and efficiency and doing more with less. It’s very likely that as you read this you’re being asked to meet commitments with fewer resources and grappling with how to meet those expectations. It’s our hope that our findings will help you meet these challenges by inspiring you to think differently about your work streams.

Our investigation was inspired by the book [The Phoenix Project](https://itrevolution.com/the-phoenix-project/) (which itself was inspired by [The Goal](https://www.tocinstitute.org/the-goal-summary.html)). The main character in The Phoenix Project grapples with Work in Progress (WIP) or stuff that is started but not yet done. What the main character learns is that as WIP grows the output of his team decreases. The lesson is that our approach to work is tremendously impactful to our productivity.

## The Impact of Context Switching on Software Engineers

Why is WIP so impactful? The problem is focus: if a worker is switching between multiple tasks they’re more likely to make mistakes which results in rework. But why are these mistakes being made? It all boils down to context switching.

Context switching is an unavoidable drawback of having too much WIP. There is a cost to multitasking that, in the worst case, causes you to make mistakes when you forget something vital about the tasks you’re switching between. In the best case it causes you to lose time as you reset your mental frame. Cal Newport writes in [A World Without Email](https://www.calnewport.com/books/a-world-without-email/) about years of research showing how juggling between tasks is antithetical to how the human brain works and results in lower performance. This idea is also discussed in other publications. [A paper](https://dl.acm.org/doi/10.1145/3084100.3084116) presented at the 2017 ICSSP found that:

_“\[D\]evelopers who work on 2 or 3 projects spend on average 17% of their effort on context switching between tasks from different projects.”_

From personal experience, through the teams I’ve led or been a member of, when controlling WIP was a challenge it invariably resulted in a struggle to deliver.

But here’s the question: What proof do we have that limiting WIP for software engineers results in higher throughput? Our hypothesis is that engineers who focus on one thing at a time get more things done over time. How can we be sure? Data science to the rescue.

## Less is more; reduce the amount of work in progress

Using data from the Jellyfish platform we constructed a novel analysis of WIP’s impact on delivery throughput. From this analysis we found that engineers who were able to limit their WIP to one issue at a time were _significantly_ more productive than their peers who juggled 2 or more tasks concurrently. We used cycle time as our proxy for productivity and controlled for the size of work by taking the total effort put towards an issue into account.

For the data analytically minded we’ll dive into the method in a post authored by Jellyfish Research next week  In the meantime, the tl;dr here is that a task that would have taken a day of effort if done uninterrupted takes two days when an engineer is juggling two other tasks at the same time. If an engineer has four tasks in progress the effort goes from one to _fourteen_ days for the single task. The clear call to action here is to **limit your work in progress in order to deliver more**. Maybe you already knew this but we’re excited that we can see this in our data and can therefore quantify this notion.

## A 3 Part Action Plan

We’ll close out this post with a call to action for engineering managers and team leads: The engineers on our teams are not looking to stretch themselves thin. They often end up juggling multiple tasks more as a result of circumstance than of planning. So I’d like to encourage you think about taking these 3 steps:

#### Step 1: Make Work Visible

To call back to The Phoenix Project, the problem with WIP was only fully realized after the team worked to “make work visible”. So, spend time to make work visible (either through engineering management platforms or building custom Jira dashboards) and use this to understand what your team takes on each day.

#### Step 2: Align Work to Business Priorities

Working on the wrong thing (particularly when you’re stretching) is a terrible thing for team morale. When you’ve made your work visible, invest time talking to stakeholders and understanding their priorities. Frame up your work backlog to make prioritization clear and discuss with your team and your stakeholders.

#### Step 3: Protect Focus

A prioritized roadmap is only useful if you work it in order of priority which boils down to jealously protecting focus of each development iteration your team runs. The reality is that your team _will_ be interrupted with unplanned work but as a team you need to anticipate that and employ tactics such as choosing an engineer to provide the team cover from inbound work. Based on our research we believe that by not doing _all of the things at once_ you’ll do _more of the things over time_.

Stay tuned next week for our post that details the fun stuff: the metrics and methodology behind our analysis

## Dive Deeper with Jellyfish Content

[![Jellyfish ADO Integration](https://jellyfish.co/wp-content/uploads/2025/10/blog-Jellyfish-and-azure-devops-1024x561.webp)](https://jellyfish.co/blog/ado/)[**Jellyfish Now Brings Developer Productivity and AI Insights to Azure DevOps Customers**](https://jellyfish.co/blog/ado/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/ado/)

[![What are DORA metrics? And Why Are They So Important](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-45-1024x536.jpg)](https://jellyfish.co/blog/dora-metrics-101/)[**What are DORA metrics? And Why Are They So Important?**](https://jellyfish.co/blog/dora-metrics-101/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-101/)

[![](https://jellyfish.co/wp-content/uploads/2025/03/blog-Product-Strategy_-The-Zeroth-Engineering-Unlock-1024x545.webp)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)[**Product Strategy: The Zeroth Engineering Unlock**](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified