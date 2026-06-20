---
url: "https://jellyfish.co/blog/story-points-efficiency/"
title: "Story Points Efficiency | Jellyfish Blog"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/story-points-efficiency/#content)

We’ll get it right out of the way up front — measuring efficiency is tricky. But one desired outcome of using story points is that a collaborative process of estimation will ensure that tasks are well defined, understood, and — if necessary — broken into smaller pieces where that can be accomplished. As a result, if this is true, we might expect to see teams using story points to have faster cycle times.

## A Caveat

When we compare companies that use story points to companies that don’t, the use of story points isn’t the only difference between them. Using story points is most likely correlated with other attributes of engineering culture, process, and practices — some of which could also affect cycle time. For example, it could be that many companies using story points are working on larger tasks that require more time to complete, which leads to both longer cycle times and a use of story points. In other words, differences seen here might not be due to the use of story points, or the use of story points alone.

## Are Companies that Use Story Points More Efficient?

Let’s start at the high level. Are companies that use story points more efficient? To look at this question, we looked at a sample of 300,000 issues from 36 companies in two groups — those using story points (defined as having 40% or more of their issues with story points), and those not using story points (with 10% or less of their issues having story points). For each company, we computed the median issue cycle time in days:

![median issue cycle time](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2022/03/median-issue-cycle-time.webp)

As you can see, there’s a huge range of cycle times across both groups of companies, ranging from just a few hours to multiple days in both companies that use story points, and in those that don’t. Contrary to what we might have expected, there are more companies that don’t use story points that have a very short median cycle time, and more companies that do use story points with a longer cycle time. As a result, the average cycle time over the non-story-point companies is actually shorter than for the story-point-using companies, but the difference is not statistically significant (p=0.09).

The situation is quite similar when we look at allocation:

![allocation](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2022/03/allocation.webp)

Again, counterintuitively, issues — on average — in the non-story-point companies accumulate less FTE effort than in the story-point-using companies. While the spread is also very wide here, the difference is statistically significant.

The data don’t appear to support the hypothesis that using story points leads to faster, more efficient delivery at the company level. If anything, companies using story points allocate more effort per issue. But as we discussed in part 1 above, each team is different, and no company culture is monolithic. Perhaps there are some more discernible patterns at the team level?

## Are Teams that Use Story Points More Efficient?

We took a sample of about 90,000 issues completed by over 400 engineering teams, roughly half from teams using story points, and half from teams not using story points. (We classified teams as “using story points” if at least half of their issues had story points — but the results did not change using a threshold of two thirds instead). Comparing their cycle times shows they are almost the same:

![story points](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2022/03/story-points.png)

It appears that the issues from teams using story points do actually have slightly shorter cycle times, but a t-Test shows that the small difference in means is not statistically significant (p=0.23).

Another measure we can use to compare teams is the allocation per issue. As introduced above, this is a measure of the cumulative effort in terms of FTE-days allocated to issues. Again, we might expect more efficient teams to complete tickets with less allocated effort, on average. Here’s what the numbers say:

![average issue allocation](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2022/03/average-issue-allocation.png)

Again, the numbers are very similar, and it indeed looks like teams using story points actually spend slightly less allocated time per issue than teams not using story points (by roughly an hour, based on an 8-hour work day). In this case, the difference is statistically significant according to a t-Test (p << 0.01) — but because the difference is so small, this hardly qualifies as convincing evidence that story points make a big difference here.

Taken together, these analyses do not seem to support the hypothesis that teams using story points are substantially faster or more efficient than those that don’t.

## Conclusion

Estimation is hard, and on the whole, story points are not a strong predictor of how long an issue will take to deliver, or how much effort it will require in terms of FTEs. That said, there’s a lot of variation across teams, and some teams are much better than others — maybe because of practice, or because they do work that is more predictable by nature. At the macro level, we don’t see evidence that companies using story points — or the engineering teams within those companies that do — deliver faster or more efficiently than those that don’t.

We’re using imperfect measures of efficiency, and we’re only looking at a narrow slice of what constitutes a well-performing engineering team here, so there is more work to be done to fully understand the impact of story points. But the window of data we’ve looked through here doesn’t provide a strong view that they work.

About the author

![Benjamin Kotrc](https://jellyfish.co/wp-content/uploads/2022/03/Benjamin-Kotrc.jpg)

Benjamin Kotrc is Research Director at Jellyfish.

Follow:

## Dive Deeper with Jellyfish Content

[![Jellyfish ADO Integration](https://jellyfish.co/wp-content/uploads/2025/10/blog-Jellyfish-and-azure-devops-1024x561.webp)](https://jellyfish.co/blog/ado/)[**Jellyfish Now Brings Developer Productivity and AI Insights to Azure DevOps Customers**](https://jellyfish.co/blog/ado/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/ado/)

[![What are DORA metrics? And Why Are They So Important](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-45-1024x536.jpg)](https://jellyfish.co/blog/dora-metrics-101/)[**What are DORA metrics? And Why Are They So Important?**](https://jellyfish.co/blog/dora-metrics-101/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-101/)

[![](https://jellyfish.co/wp-content/uploads/2025/03/blog-Product-Strategy_-The-Zeroth-Engineering-Unlock-1024x545.webp)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)[**Product Strategy: The Zeroth Engineering Unlock**](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified