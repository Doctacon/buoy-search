---
url: "https://jellyfish.co/blog/is-tokenmaxxing-cost-effective-new-data-from-jellyfish-explains/"
title: "Is “tokenmaxxing” cost effective? New data from Jellyfish explains. - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/is-tokenmaxxing-cost-effective-new-data-from-jellyfish-explains/#content)

[“Tokenmaxxing”](https://www.wsj.com/cio-journal/why-some-companies-say-ai-tokenmaxxing-is-key-to-survival-e699a128) – the idea that success with AI coding comes down to using as many tokens as possible – is having a moment.

It’s an appealing metric. Tokens are the fundamental unit that AI coding tools use to read, write, and reason. So on its face, more tokens should mean more output, more productivity, more impact.

But is that actually true?

To answer that question and to understand the real ROI of token usage we turned to the data. We analyzed 12,000 developers across 200 companies in Q1 of this year. **What we found is that while more tokens do correlate with more output, they come at a dramatically higher price point per unit.**

Is “tokenmaxxing” cost effective?

## Is “tokenmaxxing” cost effective?

At a high level, token usage varies wildly across developers.

The typical user (50th percentile) consumes about 51 million tokens per month on AI coding. Meanwhile, the 90th percentile user consumes more than seven times that amount, at roughly 380 million tokens per month. A relatively small group of power users is driving a disproportionate share of total token consumption.

To understand what that means in practice, it helps to look at how tokens are actually measured and priced.

AI coding tools rely on three main types of tokens:

- Input tokens sent to the model,
- output tokens returned by the model, and
- cache tokens (both reads and writes) that allow the model to retain context without reprocessing everything from scratch.

Each of these token types is priced differently, and their usage varies significantly depending on workflows and tools.

Using published Claude API pricing, we estimated the monthly cost of this usage. **A typical median user spends about $52.38 per month on tokens. At the 75th percentile, that increases to $226.58, and at the 90th percentile, power users are spending approximately $691.14 per month.**

What do you get for all those tokens?

## What do you get for all those tokens?

To evaluate whether that spend is worth it, we joined token usage data with actual developer output, measured in merged pull requests.

Over the course of Q1 2026, developers in the bottom 20% of token spend used only about three dollars’ worth of tokens for the entire quarter and shipped an average of 11 merged PRs. By comparison, developers in the top 20% spent $1,822 over the same period and shipped 23 merged PRs on average.

In other words, significantly higher token usage does lead to more output, but not proportionally. **The cost per merged PR increases from just $0.28 in the lowest usage tier to $89.32 in the highest.**

More tokens means more output, but at a much higher price per unit.

Should you “tokenmax”?

## Should you “tokenmax”?

“Tokenmaxxing” treats token consumption itself as the goal – as if maximizing usage is the same thing as maximizing impact.

And like many simple metrics, it’s directionally useful but ultimately incomplete. It’s a bit like checking someone’s pulse: it tells you something is happening, but not whether it’s healthy or efficient.

The data makes this tradeoff clear. Looking at a subset of ~7,500 developers for whom we can join token usage to PR activity, we see that PR throughput increases steadily as token usage rises, climbing from about 0.77 PRs per week at the lowest levels of usage to 2.15 at the highest. But at the same time, the number of tokens required per PR increases dramatically. The median developer uses about 7 million tokens per PR, while developers in the top decile use roughly 69 million.

![Jellyfish AI Token Usage](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/04/token_decile_blog-scaled.png)

That’s nearly ten times more tokens for about two times the throughput. Tokens, in this sense, behave less like a linear input and more like rocket fuel. Going faster is possible, but it requires exponentially more resources to do so.

Finding the sweet spot

## Finding the sweet spot

The practical implication is that there is a clear efficiency curve when it comes to token usage.

The highest return doesn’t come from pushing a small group of developers to extreme levels of usage. Instead, it comes from getting more of the organization into the middle of the adoption curve, where usage is consistent, effective, and relatively efficient.

Broad, moderate adoption delivers far more value than narrow, extreme usage.

This also helps explain why many teams have yet to fully realize the promise of autonomous AI agents. While those systems can drive massive productivity gains, they require significant investments in infrastructure, including sandboxed environments, orchestration, and context engineering. Until those challenges are addressed, most organizations remain constrained by an “agentic barrier” – a limit that can’t simply be overcome by increasing token consumption.

Is “tokenmaxxing” worth it?

## So, is “tokenmaxxing” worth it?

The answer is: not on its own. Tokenmaxxing can increase output, but it is not cost effective at the extremes. The real opportunity for engineering leaders is not to maximize tokens, but to optimize how they are used.

Because in the end, the goal isn’t to spend more tokens. It’s to get more value out of each one.

_For more AI engineering trend data, check out_ [_Jellyfish’s original research here_](https://jellyfish.co/ai-engineering-trends/) _._

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