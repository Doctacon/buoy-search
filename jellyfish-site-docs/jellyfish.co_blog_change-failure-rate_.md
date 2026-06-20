---
url: "https://jellyfish.co/blog/change-failure-rate/"
title: "Change Failure Rate | Jellyfish Blog"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/change-failure-rate/#content)

![Why defining failure rate is the key to measuring change failure rate](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-21-1.jpg)

![](https://jellyfish.co/wp-content/uploads/2021/11/Jellyfish_Blog-Author-Headshots_Evan-Klein.webp)

Evan Klein

July 27, 2022

## What is change failure rate?

Change failure rate measures the percentage of deployments that result in a failure in production, which ultimately requires some type of remediation (to be fixed, patched, or rollback after they are deployed). It is a measure of the quality and stability of your teams’ releases. Change failure rate answers the question “what portion of the changes that we make to production result in an incident or outage?” A high change failure rate could indicate, for example, that your teams don’t have enough of a handle on testing or that they have an inefficient or error-prone deployment process.

### How do you measure change failure rate?

Change failure rate is easy enough to calculate assuming your team is measuring the right metrics. Simply divide the number of deployments that cause failures by the total number of deployments. If your team deployed five times today and two of them resulted in failures, your change failure rate is 40%.

## Change failure rate and the DORA metrics

As a software development organization, our goal is always rapid _and_ stable delivery of software to end users. That is the DevOps way after all. When the business pushes for faster delivery timelines, more new features, expanded roadmaps, etc., it can be tempting to optimize for speed at the expense of stability or quality. But we all know that approach will come back to harm us in the long run. How you respond to incidents and failures is equally if not more important than deploying more times in a day.

The DevOps Research and Assessment (DORA) group has shown us that elite performing teams will measure and optimize around [four key DORA metrics](https://www.jellyfish.co/blog/dora-metrics-101/):

- Lead time for changes
- [Deployment frequency](https://www.jellyfish.co/blog/breaking-down-deployment-frequency/)
- Time to recover
- Change failure rate

But more than just measuring change failure rate, the way your team defines failures is such a critical step in this process to make sure you are optimizing for the right things for your business.

## The importance of defining failures to work for your organization

While change failure rate has been broadly accepted as an important DORA metric to track, what’s not often acknowledged is that it can actually be complicated to define failure. There are several ways of determining what a failure means for your organization, and there’s not always agreement on which definitions to use, when, and why. The challenge arises when there is confusion around what constitutes a failure for your organization, hence the importance of defining failures across your entire organization up front. Here are a few common ways we see engineering teams defining failure:

- **Align to pre-defined incidents**: most teams will have a standard definition of an incident in order to trigger their incident management tool (e.g. Pagerduty) to fire a notification. This is a good way to determine that something relatively serious occurred, and for teams building software with SLAs or which really needs a high uptime for their customers, this can be a good way to track failures. However, it’s not always the case that the deployment that occured immediately before an incident actually caused that incident.
- **Align to rollbacks**: this is the easiest (and therefore relatively common) way to define failures, though not always the most comprehensive. In this case, teams simply track any deployments that required a rollback and mark those as failures.
- **Limit to outages**: some teams are less worried about every incident and only want to look at deployments that caused such major problems that their application was not accessible to customers.

There are other ways to define failure too, and the way your team defines it should ultimately map to your business priorities and customer expectations. This definition can have a significant impact on the change failure rate you calculate, so it’s important that the definition is not only relevant, but also accepted and used across the organization.

## What is a good change failure rate?

Ideally, your team’s change failure rate is as close to zero as you can get it. But failures will happen. Fortunately, DORA has given us some benchmarks from the thousands of teams they studied, which you can use as a guideline. According to [the 2021 Accelerate State of DevOps](https://services.google.com/fh/files/misc/state-of-devops-2021.pdf) report, elite-performing teams will have change failure rates less than 16%:

![](https://www.jellyfish.co/wp-content/uploads/2022/07/State-of-DevOps-Benchmarks.png)

## Getting started

Change failure rate is one of the most important metrics for measuring and improving the stability and quality of the software your teams deploy. But the devil, as they say, is in the details. Avoid confusion, measurement inconsistencies, or worse – misinformed decision-making – by defining failure for your organization up front. This is a necessary first step before you measure change failure rate. And tactically, make sure any tool your teams use to [measure change failure rate](https://www.jellyfish.co/platform/devops-metrics/) allows you that flexibility in how you define failure. Whatever definition you use, change failure rate can be a foundational metric to track and improve the efficacy and performance of your engineering teams.

## Dive Deeper with Jellyfish Content

[![Jellyfish ADO Integration](https://jellyfish.co/wp-content/uploads/2025/10/blog-Jellyfish-and-azure-devops-1024x561.webp)](https://jellyfish.co/blog/ado/)[**Jellyfish Now Brings Developer Productivity and AI Insights to Azure DevOps Customers**](https://jellyfish.co/blog/ado/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/ado/)

[![What are DORA metrics? And Why Are They So Important](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-45-1024x536.jpg)](https://jellyfish.co/blog/dora-metrics-101/)[**What are DORA metrics? And Why Are They So Important?**](https://jellyfish.co/blog/dora-metrics-101/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-101/)

[![](https://jellyfish.co/wp-content/uploads/2025/03/blog-Product-Strategy_-The-Zeroth-Engineering-Unlock-1024x545.webp)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)[**Product Strategy: The Zeroth Engineering Unlock**](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified