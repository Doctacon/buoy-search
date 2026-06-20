---
url: "https://jellyfish.co/blog/larger-pull-requests/"
title: "Do Larger Pull Requests Receive More Extensive Reviews | Jellyfish Blog"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/larger-pull-requests/#content)

![](https://jellyfish.co/wp-content/uploads/2023/07/Blog-Large-Pull-Req.jpg)

![](https://jellyfish.co/wp-content/uploads/2021/11/Jellyfish_Blog-Author-Headshots_Mobolaji-Williams.webp)

Mobolaji Williams

March 22, 2022

In Github’s “The State of the Octoverse” ( [https://octoverse.github.com/](https://octoverse.github.com/)) Sarah Drasner, VP of Developer Experience at Netlify, was quoted as saying:

> “Most of my work as an engineering manager has been teaching people how to scope work to smaller bits. So any time you have a big honking \[pull request\] it’s a nightmare to review—either too much discussion or none because no one can get their head around it.”

Let’s see if Drasner’s experience is reflected in the data. In particular let’s investigate the relationship between size of a pull request and the number of comments it receives.

## The Big Anticipator Theory of PR Reviews

[Pull requests (PRs)](https://www.jellyfish.co/library/pull-request/) are the currency of the realm for software engineers collaborating through Git tools. They allow for easy, distributed management of collaborative software projects and provide a structure for quickly proposing and approving changes in a code base. The typical process for introducing such changes begins with a developer modifying the code on a local branch of a repository, followed by the developer “requesting” that said local branch be “pulled” into the repository’s main one. The PR is then reviewed by another developer who provides comments and who requests additional changes before the original change is finally merged into the main branch.

A large part of the reviewer’s job is to catch potential bugs before they arise in production. For single-line PRs, since the change is small, one might expect that a reviewer would provide few or no comments assuming that the author was fully aware of the ramifications of their code changes.

But let’s say there is a base error rate of one bug per every few lines of code. Then, as the number of lines of code added increases, so too should the number of bugs or potential areas of improvement and, consequently, the number of reviewer comments should increase as well. Let’s call this the “Bug Anticipator Theory of PR Reviews.”

Now, does this actually happen?

## Examining the Data

We explored this question by collecting data on 2 million PRs across 102 companies. We wanted to determine how PR “size” (as defined by lines added or files changed) correlated with the number of PR comments.

As a first exploration, we took our collection of PRs and plotted the number of comments associated with the PR against the number of lines added or the number of files changed.

|     |     |
| --- | --- |
| ![](https://stgjellyfish.wpengine.com/wp-content/uploads/2022/12/scatter_comments_vs_files0-1-300x273-1.png) | ![](https://stgjellyfish.wpengine.com/wp-content/uploads/2022/12/scatter_comments_vs_files0-1-300x273-1.png) |

From a quick look at the plots, _it seems_ that there isn’t a linear relationship between the amount of commentary a PR receives and its size, for if there was such a relationship we would see both distributions of points rising upwards as we move to the right. The fact that we don’t see this might lead us to conclude that larger PRs do not necessarily receive more comments than smaller PRs. In fact the scatter plots suggest such large PRs receive fewer comments than their smaller counterparts. Let’s check this more quantitatively.

Computing the correlation for both plots we obtain statistically significant values of 0.22 for the first and 0.17 for the second which, depending on how stringent we are about the strength of correlations, either affirms or denies what we see in the plots. Namely, on the affirmation side, perhaps these values suggest that the PR size and comment number correlation is too weak to be significant or, on the denial side, maybe  the correlation is slight enough to be consistent with what we would expect from the “Bug Anticipator Theory of PR reviews.”

Moreover, the results suggest that the apparent negative correlation in the above scatter plots is illusory: There is at most a positive correlation and at least no correlation between PR size and number of comments.

We can refine these conclusions by pursuing the more granular task of determining if larger PRs indeed receive fewer comments than smaller PRs. We note that the plots above contain many overlapping points, and so we get a better view of the distributions by binning our data by size and computing the mean number of comments in each bin. For both definitions of PR size, i.e., “files changed” and “number of lines added”  we created four bins. For the “files changed” definition we grouped PRs into whether the PR changed between 1 and 5, 6 and 10, 11, and 30 or 30+ files. For the “lines added” definition we grouped PRs into whether the PR added between 1 and 50, 51 and 200, 201 and 500, and 500+ lines. The ranges were defined to be inclusive for both the lower limit and the upper limit of the range.

Here is the fractional breakdown for how the proportion of PRs fall into each category

|     |     |
| --- | --- |
| ![](https://stgjellyfish.wpengine.com/wp-content/uploads/2022/12/frac_prs_lines0-1.png) | ![](https://stgjellyfish.wpengine.com/wp-content/uploads/2022/12/frac_prs_files0-1.png) |

We see that large PRs, by either definition, are rare and most PRs involve fewer than five lines changed or 50 lines added.

We can create a similar graph for PR comments. Creating bins of 0 comments, between 1 and 5 comments, between 6 and 10 comments, and greater than 11 comments, we find:

![](https://stgjellyfish.wpengine.com/wp-content/uploads/2022/12/frac_pr_comments0-1-e1624375685571.png)

We see that about half of all PRs (48%) are “rubber stamped” in that they receive no comments at all, and a large majority (85%) receive fewer than six comments. The cases where a PR received more than five comments are quite rare.

Returning to our original question, how does the average number of comments for a PR vary across bins? To answer this question we created bar plots where the height was the mean number of comments for each bin with error bars defined by the associated standard deviation.

|     |     |
| --- | --- |
| ![](https://stgjellyfish.wpengine.com/wp-content/uploads/2022/12/comments_vs_files0-1-300x238-1.png) | ![](https://stgjellyfish.wpengine.com/wp-content/uploads/2022/12/comments_vs_lines0-2-e1624376324467.png) |

From the above figures we see that the mean number of comments actually increases as we increase the size of the PR for both of our definitions. However, the standard deviation also increases so that while on average larger PRs receive more comments they also have wider distributions of number of comments, meaning there is greater variability in their comment number.

## **Was Sarah Drasner Right?**

Let’s return to Drasner’s original assertion:

> “…any time you have a big honking PR it’s a nightmare to review—either too much discussion or none because no one can get their head around it.”

First, we know from the “Fraction of PRs in ‘PR Comment’ bins” plot that the case of no discussion (i.e., zero comments) occurs in about half of all PRs as an aggregate. So it is true that no discussion is generally always likely. However, if we disaggregate our PRs into various size bin, then the mean number of comments for each bins changes as does the distribution of comments. In the plot on the left below, we compare the distribution of comments for the smallest PRs (1-50 lines added) to that of the largest PRs (500+ lines added).

|     |     |
| --- | --- |
| ![](https://stgjellyfish.wpengine.com/wp-content/uploads/2022/12/prs_vs_lines0-1-e1624362307989.png) | ![](https://stgjellyfish.wpengine.com/wp-content/uploads/2022/12/bars_comments_vs_lines0-1.png) |

We see that the largest PRs have a wider tail in their distribution of comments which means they are more likely than smallest PRs to have a high number of comments. We see this result another way on the stacked bar chart on the right: As PRs increase in size, the proportion of them that have a lot of discussion (i.e., 11+ comments) increases as well.

Thus, it is not that larger PRs _either_ have too much or too little discussion, but rather that they have a larger variability in their amount of discussion than that seen in smaller PRs.

What does this mean for you and your team? First, large PRs tend to be rare, so the variability in their number of comments might not be a pressing issue. But if you want a more consistent (i.e., in time) development process from creating a branch, to starting a pull-request, to receiving comments, and then finally merging, it seems that it is better to keep your PRs less than 200 lines. In this range, a majority of PRs receive fewer than five comments and ostensibly spend less time in review. The exact relevance of “time in review” will have to wait for another blog post.

### **Questions to Ask your Team**

- What is the average size of your PRs amongst the teams you manage?

- Do your PRs receive too few comments? Do they receive too many which lead them to languish in review?

- Does your experience match Drasner’s? Namely, do your large PRs generally get too many or too few comments?
- Do you know why your large PRs receive fewer comments than anticipated?

## Dive Deeper with Jellyfish Content

[![Jellyfish ADO Integration](https://jellyfish.co/wp-content/uploads/2025/10/blog-Jellyfish-and-azure-devops-1024x561.webp)](https://jellyfish.co/blog/ado/)[**Jellyfish Now Brings Developer Productivity and AI Insights to Azure DevOps Customers**](https://jellyfish.co/blog/ado/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/ado/)

[![What are DORA metrics? And Why Are They So Important](https://jellyfish.co/wp-content/uploads/2023/07/Blog-image-header-45-1024x536.jpg)](https://jellyfish.co/blog/dora-metrics-101/)[**What are DORA metrics? And Why Are They So Important?**](https://jellyfish.co/blog/dora-metrics-101/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-101/)

[![](https://jellyfish.co/wp-content/uploads/2025/03/blog-Product-Strategy_-The-Zeroth-Engineering-Unlock-1024x545.webp)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)[**Product Strategy: The Zeroth Engineering Unlock**](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/product-strategy-the-zeroth-engineering-unlock/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified