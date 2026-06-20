---
url: "https://jellyfish.co/blog/vanity-metrics/"
title: "Vanity Metrics in Engineering | Jellyfish Blog"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/vanity-metrics/#content)

![Vanity Metrics in Engineering](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-8-1.jpg)

![](https://jellyfish.co/wp-content/uploads/2023/07/author_kevin-dallaire.png)

Kevin Dallaire

February 28, 2023

Our teams at Jellyfish work with engineering leaders across all industries to better understand what metrics matter the most within engineering teams. We look to guidance from the DORA team, follow the principles of the DevOps movement, and embrace a nuanced and balanced approach to engineering metrics.

Much of today’s discussion about engineering metrics is focused on what you _should_ measure, but we rarely discuss as a community what NOT to measure. Every team has a different situation or development process, but we have found that most teams that struggle to extract valuable insights from their engineering metrics choose to track the same metrics and regularly misinterpret their meaning. These must-avoid metrics regularly mislead even the most careful leaders, and negatively impact engineering teams.

We call these metrics **_vanity metrics,_** and in this post, we will discuss why you should avoid them at all costs.

## What are vanity metrics within engineering?

Vanity metrics are a term for KPIs that appear to make work look good to others but do not help you understand your own performance in a way that informs future strategies. There’s a temptation to use some of these metrics that we will detail below, especially when under pressure to deliver value back to the business. You might even use some of these metrics today. If you measure these metrics consider some of the alternatives that we recommend within our most recently released eBook, the [10 KPIs Every Engineering Leader Should Track](https://www.jellyfish.co/resources/10-kpis-engineering-leaders-should-track/).

And for a more detailed example of vanity metrics outside the context of engineering, John Cutler, a highly respected and well-known product leader, discussed the concept of [vanity within Product teams](https://amplitude.com/blog/vanity-metrics) and other departments. Much of this post was inspired by John’s take on this concept.

The four engineering vanity metrics that we will discuss within this post are:

- Lines of code
- Coding churn
- Code Impact
- Agile Velocity

## Lines of code

Lines of code is a textbook example of a vanity metric; its a volume-based metric of work that purposefully omits the required context surrounding the actual work and its business impact. Without any additional context, management cannot speak to the quality, impact, or longevity of the lines of code added with any sort of certainty. An organization that goals itself on lines of code will soon find itself buried in a mountain of technical debt.

Instead, we highly recommend completion or burndown rate to represent how your team is progressing through current work. With this type of metric managers can spot trends, identify potential bottlenecks, and work to optimize their engineering operations in a long-term sustainable way. It’s a way to report on engineering output without reducing complex development work to a single number.

## Coding churn

Code churn is the measure of how much code is re-written or deleted during a given period (usually during [the work stage](https://www.jellyfish.co/blog/jellyfish-life-cycle-explorer-announcement/) of the software development lifecycle.). Reworking code is a normal, if not an essential part of the development process, especially early on when solutions to a problem are not clear. Therefore the volume of code churn tells little about whether an individual or team is “high-performing.” A great deal of additional context is needed to interpret this metric, such as the type of code being worked on, why the code is going through several iterations, and how this churn impacts the delivery cycle.

## Code Impact

Code Impact attempts to quantify the change to a code base in a more holistic way than counting lines of code. It factors in certain parameters about the changes such as the volume of changed code (code added and subtracted), the code age, the number of files changed, and the number of total location edits, among other factors. The final output is a single score of the significance of the changes. But it is a vanity metric for several reasons.

First, “code impact” is a misnomer as it measures the wrong things to determine impact. This metric attempts to parse out the impact to the codebase, but it does not give insight into the impact to the functionality of the product, the value to customers, or the impact on the business.

Additionally, because there are so many factors behind the scoring of this metric, it suffers from overcomplication and a lack of actionability. There is no common criteria among work that scores high, therefore, you need to ask further questions to parse out the TRUE impact of such changes.

## Agile Velocity

Velocity has been adopted by those that follow Agile or Scrum methodologies as it attempts to assess the speed of your software development. It’s reached such a level of popularity that it’s possible [your CEO might ask you about it](https://www.jellyfish.co/blog/7-questions-ceos-ask-engineering-leaders/).

But popularity does not always translate to clarity, effectiveness, or accuracy. Agile velocity can fail because it relies on story points being a consistent and accurate way of assessing the total amount of work that went into engineering work. Story points have their place in Agile, but – as [discovered by Jellyfish Research](https://www.jellyfish.co/blog/do-story-points-work/) – they do not accurately predict the volume or speed of work required to accomplish a task. Teams within the same organization measure story points differently, and the type of work a team is charted with influences how precisely teams can regularly predict task difficulty, length, and risk.

As discussed previously, [issue cycle time](https://www.jellyfish.co/blog/issue-cycle-time-the-staple-engineering-operations-metric/) and [lead time](https://www.jellyfish.co/blog/lead-time-in-devops/) are much better indicators of the actual _velocity_ or tempo of a given software development group.

## Our Engineering Metrics Approach

At Jellyfish, we recommend a balanced approach to your engineering metrics strategy. There is no one silver bullet engineering metric, but you should not measure everything either (or else suffer from analysis paralysis). What you measure should always stem from your strategic business objectives and how engineering aligns with those objectives. And if you need some more specific recommendations be sure to consult the [SPACE Framework](https://www.jellyfish.co/blog/what-is-the-space-framework/), [DORA metrics](https://www.jellyfish.co/blog/dora-metrics-101/), as well as the [10 KPIs Every Engineering Leader Should Track](https://www.jellyfish.co/resources/10-kpis-engineering-leaders-should-track/), for guidance on what will work within your organization.

## Dive Deeper with Jellyfish Content

[![Jellyfish Data Hub](https://jellyfish.co/wp-content/uploads/2026/04/blog-data-hub-featureV2-1024x561.webp)](https://jellyfish.co/blog/introducing-jellyfish-data-hub-flexible-curated-engineering-insights/)[**Introducing Jellyfish Data Hub: Flexible, Curated Engineering Insights**](https://jellyfish.co/blog/introducing-jellyfish-data-hub-flexible-curated-engineering-insights/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/introducing-jellyfish-data-hub-flexible-curated-engineering-insights/)

[![Jellyfish Integrations](https://jellyfish.co/wp-content/uploads/2025/12/blog-new-integreationsv2-1024x561.webp)](https://jellyfish.co/blog/new-data-integrations/)[**Jellyfish Offers Richer Engineering Insights With 25+ New Data Integrations Across Major Dev Tools**](https://jellyfish.co/blog/new-data-integrations/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/new-data-integrations/)

[![blog-g2-winter26-featured](https://jellyfish.co/wp-content/uploads/2025/12/blog-g2-winter26-featured-1024x582.webp)](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-winter-2026/)[**Jellyfish Tops G2’s Software Development Analytics Tools Grid 14 Quarters and Counting**](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-winter-2026/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-winter-2026/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified