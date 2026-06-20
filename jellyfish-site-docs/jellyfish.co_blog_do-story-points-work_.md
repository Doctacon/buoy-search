---
url: "https://jellyfish.co/blog/do-story-points-work/"
title: "Do Story Points Work To Predict Effort? | Jellyfish Blog"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/do-story-points-work/#content)

![Do Story Points Work to Predict Effort?](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-30-1.jpg)

![](https://jellyfish.co/wp-content/uploads/2022/03/Benjamin-Kotrc.jpg)

Benjamin Kotrc

March 22, 2022

Engineers love to hate story points. But do they actually work?

Estimation is notoriously difficult, and story points are often used as a tool in software engineering to capture an overall estimate of the effort involved in a particular piece of work on a product backlog — factoring in the amount of work, its complexity, and uncertainty. The hope is that this will lead to better prioritization decisions, and more reliable predictions of what a team can complete in a given time period: ultimately, a more effective and efficient engineering team.

At Jellyfish, our customers run a wide gamut of software engineering cultures and practices. Some teams use story points, and some don’t — but with the diversity of data Jellyfish brings together, we’re in a unique position to look into the use of story points, and how it affects the dynamics of software development across many different companies, and software engineering teams in them.

## Story Points and Cycle Time

One of the key motivations for using story points is the promise of more reliable delivery commitments. For example: knowing with confidence how much work a team will be able to complete in the upcoming sprint by knowing that team’s velocity. Although story points are explicitly not time estimates (since one engineer’s hour is not the same as another’s), the desired predictability does imply a correlation with time — in aggregate. Does that relationship hold up in the data?

Here’s an example from one customer, over a year’s worth of Jira issues (but the pattern looks similar for other companies):

![](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2022/03/Story-Points-1.png)

You can see that there is some relationship between story points and issue cycle time. The median cycle time (larger, green circles) is about 4 days for 1-point issues, about 6 days for 2-point issues, and about 8 days for 3-point issues. But the correlation is very weak (note how far up and down the cycle time scale issues with the same number of story points go!). 1-point issues commonly span cycle times from less than a day to three weeks or more, and the same is true for 5-point issues, for example.

There are tens of thousands of points plotted on this graph, so it can be hard to see how densely those points (each representing a Jira issue) are plotted over the top of one another. A histogram shows that density — here are the histograms for 1-point stories and 5-point stories compared:

![](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2022/03/Story-Points-2.png)

You can see that 1-point stories are, in fact, more likely to do be done in two days or less (about 40% of 1-point stories versus about 10% of 5-point stories are done that quickly). But notice how much overlap there is between these two distributions — both sorts of stories are equally likely to take about a week to complete, and both can take three or four or more weeks (issues taking longer than 50 days aren’t plotted in this histogram).

In short, at the company level, story points do have a coarse relationship with cycle time, but don’t say very much about how long it’ll take an issue to be completed.

## Story Points and Allocation

Cycle time is only one measure of the effort involved in completing a task. Consider that an engineer could have several issues in flight at the same time: for example, five equal-sized issues in progress over five days, in parallel, might really only represent one day of effort each, though each will show a five-day cycle time. Thanks to the Jellyfish work model, which parses and combines data from multiple sources — including task management systems, code source control, and calendars — we can look more clearly at the actual effort expended in terms of FTE person-months, using what we call [_allocation_](http://www.jellyfish.co/blog/what-is-allocation/).

![](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2022/03/Story-Points-3.png)

But even from the point of view of allocation, as you can see in this plot, the correspondence between effort and story points is weak. Not surprising, you might say, because these results combine the story point estimates of many different teams, each of which have their own story point scales, which may have very different meaning. How does the situation look on a per-team basis?

## Story Points and Allocation At the Team Level

Here’s what the relationship between story points and allocation looks like for just one of the teams at the same company:

![](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2022/03/Story-Points-4.png)

As you can see, the situation is similar: the median allocation for issues with few story points is lower than for those with many story points, but the spread is huge — meaning there is a lot of overlap between story points. Imagine you had an issue that you knew took 0.1 person-months of allocated effort to complete: how many story points did this team likely assign to it? From the plot, it’d be very hard to tell whether it had 1 story point or 5 story points!

One way to measure the strength of this correspondence is using a correlation coefficient. This number is one when two quantities are perfectly linearly correlated (story points perfectly predict allocation along a straight line), and zero when there is no correlation at all (story points are not related to allocation). Instead of looking at countless plots like the one above, we can look summarize the strength of the correlation between story points and allocations over many teams using this number:

![](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2022/03/Story-Points-5.png)

Here you can see the correlation between story points and allocation for over 400 software engineering teams that use story points (showing only those that meet a statistical significance threshold, which is much less than half of them). As you can see, for most of them, the correlation is quite weak, as in the example above. But for a small proportion of the teams, the correlation is stronger. This tells us that teams vary widely in their ability to predict how much effort tasks take. On average, teams aren’t very good at it, but some teams do much better than others. This could be for any number of reasons — some teams may simply have more practice at estimation than others, but different teams also work on different things, and the nature of the work some teams do may also be less uncertain and more predictable.

In conclusion, our data bears out what those engineers who have tried to accurately predict how much effort a task is going to take to complete already suspect: it’s difficult. On average, the relationship between story points and cycle time, or between story points and allocation, is quite weak. But not all teams are the same: there is a wide variability in how strongly story points correlate with effort (as measured by allocation). For a small proportion of teams, there’s a tighter correlation between story points and allocation — which may be because these teams are more skilled at estimation, or because their work is more predictable by its nature.

## Dive Deeper with Jellyfish Content

[![Jellyfish ADO Integration](https://jellyfish.co/wp-content/uploads/2025/10/blog-Jellyfish-and-azure-devops-1024x561.webp)](https://jellyfish.co/blog/ado/)[**Jellyfish Now Brings Developer Productivity and AI Insights to Azure DevOps Customers**](https://jellyfish.co/blog/ado/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/ado/)

[![What are DORA metrics? And Why Are They So Important](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-45-1024x536.jpg)](https://jellyfish.co/blog/dora-metrics-101/)[**What are DORA metrics? And Why Are They So Important?**](https://jellyfish.co/blog/dora-metrics-101/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-101/)

[![](https://jellyfish.co/wp-content/uploads/2025/03/blog-Product-Strategy_-The-Zeroth-Engineering-Unlock-1024x545.webp)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)[**Product Strategy: The Zeroth Engineering Unlock**](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified