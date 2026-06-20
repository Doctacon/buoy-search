---
url: "https://jellyfish.co/blog/jellyfish-openai-team-up-to-measure-impact-of-ai-coding-tools/"
title: "Jellyfish and OpenAI Team Up to Measure the Impact of AI Coding Tools - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/jellyfish-openai-team-up-to-measure-impact-of-ai-coding-tools/#content)

In this article

When it comes to determining the [impact of AI coding tools](https://jellyfish.co/platform/jellyfish-ai-impact/), reliable data has been few and far between, and published results can tell conflicting stories. For instance, a recent study from [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) found that in some cases and under some conditions, AI tools can actually slow developers down, while an earlier study from [Microsoft](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566) showed significant gains.

At Jellyfish, we’ve been collecting a robust set of AI impact data across more than 500 companies, representing the coding activities of tens of thousands of engineers, comprising millions of pull requests and billions of lines of code. Real-world data at this scale can help us understand what’s really going on out in the field as companies engage in the journey of AI transformation.

We recently teamed up with the folks at OpenAI to take a closer look at how AI tools are affecting coding productivity and quality. Here’s what we found:

Increasing AI adoption means shipping more code, and faster

## Increasing AI adoption means shipping more code, and faster

We defined a company-wide “AI Adoption Rate” which reflects how regularly engineers on a team are using AI tools. It is defined as the fraction of active coding days an engineer used AI, averaged across all engineers on the team. In the following plots, each data point is a snapshot of a given performance metric and a company’s level of AI adoption for a single week, allowing us to see trends as companies achieve higher levels of AI adoption.

What we see is that in terms of PR throughput, going from 0% AI adoption to 100% adoption corresponds to an increase from 1.36 PRs per engineer on average to 2.90 PRs – a 113% increase.

![PRs_Jellyfish_OpenAI](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/08/PRs_Jellyfish_OpenAI.png)

Increasing AI adoption also correlates with pushing code to production faster. In going from 0% to 100% AI adoption, an average company can expect their median cycle time to drop four hours from 16.7 to 12.7  – a 24% reduction.

![Faster Cycle Times_Jellyfish_OpenAI](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/08/Faster-Cycle-Times_Jellyfish_OpenAI.png)

But what about code quality?

## But what about code quality?

One of the things we looked at was the fraction of total PRs that are linked to bug tickets. We see that the highest levels of AI adoption correspond to an increase of 26.8% in the proportion of tickets (9.5% versus a baseline of 7.5%). In other words, companies with high AI adoption are pushing more code, _and_ a higher fraction of those PRs are bug fixes.

It may be the case that higher AI use is _causing_ more bugs, or it may be helping teams _fix_ more bugs – or it may be a combination of both. One interesting observation is that we aren’t seeing a comparable increase in revert PRs (pull requests whose primary purpose is to undo previous changes, typically due to a critical failure), suggesting that AI doesn’t seem to be causing major quality issues across the board.

![Bug Fixes_Jellyfish_OpenAI](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/08/Bug-Fixes_Jellyfish_OpenAI.png)

AI tools still need human judgment to deliver quality at speed

## AI tools still need human judgment to deliver quality at speed

While errors are few and far between, they still diminish the time savings and productivity gains from AI and show just how vital human skill and oversight remain in the AI era. As AI models improve and training and usage increase, we expect quality and speed to further improve.

![](https://jellyfish.co/wp-content/uploads/2025/07/ai-impact-dashboard-update-scaled.png)

#### Get Started with AI Impact

Get a better understanding of AI’s impact on your engineering team. Learn more about Jellyfish AI Impact and get a demo.

[Learn More](https://jellyfish.co/demo-request-ai-impact/)

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