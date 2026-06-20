---
url: "https://jellyfish.co/blog/ai-assisted-pull-requests-are-18-larger/"
title: "Better Code, or Just Bigger? AI-Assisted Pull Requests Are 18% Larger - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/ai-assisted-pull-requests-are-18-larger/#content)

In this article

Last month we shared some exciting work we did in collaboration with folks at OpenAI [investigating the impact of AI coding tools](https://jellyfish.co/blog/jellyfish-openai-team-up-to-measure-impact-of-ai-coding-tools/) across millions of pull requests for more than 500 companies.

Among other things, we found that full adoption of AI coding tools correlated with a 113% increase in PR throughput. (Check out OpenAI’s take on the analysis [here](https://www.linkedin.com/posts/aaron-ronnie-chatterji_theres-a-lot-of-buzz-and-real-debate-about-activity-7362158640918630404-9i9g?utm_source=share&utm_medium=member_desktop&rcm=ACoAAArFJU8BN29tPoEA6-a1i6Ho1N45qxndAxg) and our full post [here](https://jellyfish.co/blog/jellyfish-openai-team-up-to-measure-impact-of-ai-coding-tools/).)

AI-assisted PRs are getting bigger

## AI-assisted PRs are getting bigger

As we continue to dig deeper into the data, one interesting discovery is that in addition to increasing PR throughput and improving cycle times, teams with high levels of AI adoption also are pushing _larger_ PRs.

As before, we defined a company-wide “AI Adoption Rate” which reflects how regularly engineers on a team are using AI tools (defined as the fraction of active coding days an engineer used AI, averaged across all engineers on the team). For the plot below, each data point is a snapshot of the average additions per PR and the level of AI adoption for a given company and week.

What we see is that going from 0% to 100% AI adoption corresponds to an increase from 74.8 additions per PR to 88.4 additions per PR – an 18.2% increase. In other words, as companies increase AI adoption, their product features and platform enhancements tend to involve more lines of code than before.

![companies with higher AI use push larger PRs](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/companies-with-higher-AI-use-push-larger-PRs.png)

Why are PRs getting bigger?

## Why are PRs getting bigger?

Many factors could be driving this change. To look a little deeper, let’s compare some metrics for the top quartile of companies in the plot above (75–100% AI adoption) versus the bottom quartile (0–25% AI adoption).

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
|  | **Metric** | **Bottom AI** <br>**Adoption Quartile** | **Top AI** <br>**Adoption Quartile** | **Absolute Difference** | **Percent** <br>**Difference (%)** |
|  | **Avg AI Adoption Rate (%)** | 12.3 | 71.5 | 59.2 | 480.6 |
| PR Size<br>Metrics | **Avg Additions per PR** | 64.8 | 72.1 | 7.2 | 11.2 |
| **Avg Deletions per PR** | 20.8 | 21.6 | 0.9 | 4.1 |
| **Avg Net Additions per PR** | 44.1 | 50.5 | 6.4 | 14.5 |
| **Avg Total Changes per PR** | 85.6 | 93.7 | 8.1 | 9.4 |
| **Avg Files per PR** | 3.8 | 3.9 | 0.1 | 2.1 |
| File Type<br>Metrics | **Percent TypeScript files** | 4.1 | 7.2 | 3.1 | 76.4 |
| **Percent Python files (%)** | 2.8 | 4.8 | 2.0 | 71.0 |
| **Percent Markdown files (%)** | 1.8 | 2.8 | 1.1 | 61.1 |
| **Percent YAML files (%)** | 6.8 | 9.7 | 2.9 | 41.7 |

Looking at these metrics, we can see that most of the change appears to be from net new code, not rewritten code. Companies in the top quartile are only pushing 4.1% more deletions on average, versus 14.5% more net additions. Interestingly, we don’t see a big increase in the number of files per PR, suggesting AI is generating more code within the same files, not necessarily finding more changes to make across files.

If we take a look across file types, we see that companies in the top quartile are using certain languages and file formats at a much higher rate (up to 76% more), particularly TypeScript, Python, YAML, and Markdown. This trend aligns with the fact that LLMs generally perform better when working with these highly structured, well-documented programming languages and supporting configuration and documentation formats. The AI-assisted code that high-adoption companies are writing in these formats tends to be more explicit, with more comments and other conditional code (e.g. exception handling) than might otherwise be written without it.

Is bigger code better?

## Is bigger code better?

Here at Jellyfish we’ve found that an increase in PR throughput is typically a good thing, corresponding to more value delivered to customers. But what about _bigger_ code? That depends. It could mean code that is more robust and well-commented, but it could also mean code that is overly complex and harder to debug, iterate on, and maintain. As AI technology continues to evolve, we’ll keep looking at how AI coding assistants and agents are impacting code generation – both quantity _and_ quality.

About the author

![Nicholas Arcolano](https://jellyfish.co/wp-content/uploads/2026/01/Nicholas-Arcolano-Edited.jpg)

Nicholas Arcolano, Ph.D. is Head of Research at Jellyfish where he leads Jellyfish Research, a multidisciplinary department that focuses on new product concepts, advanced ML and AI algorithms, and analytics and data science support across the company.

Follow: [LinkedIn](https://www.linkedin.com/in/arcolano/Nicholas%20Arcolano,%20Ph.D.)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified