---
url: "https://jellyfish.co/blog/ai-code-review-doubled-pr-throughput/"
title: "At Jellyfish, Turning On AI Code Review Doubled Our PR Throughput - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/ai-code-review-doubled-pr-throughput/#content)

In this article

We turned on AI code review using [Cursor Bugbot](https://cursor.com/bugbot) for 18 engineers. Their PR throughput more than doubled.

Not because they worked more.

Not because they wrote more code.

Because they started shipping it differently.

That result is easy to misinterpret. More PRs does not automatically mean more productivity.

So instead of guessing, we designed an experiment to understand what actually changed.

The Experiment: Measuring Impact (and Controlling for Bias)

## The Experiment: Measuring Impact (and Controlling for Bias)

One of the biggest challenges in evaluating developer tools is selection bias. It’s easy to imagine that the developers who rapidly adopt AI tools are already more productive.

To control for this, we compared the same 18 developers in two back-to-back periods of equal length, before and after Bugbot was enabled.

- **Before:** April 8 – June 5, 2025 (43 business days)
- **After:** June 6 – August 7, 2025 (43 business days)

We chose adjacent time windows to minimize confounding variables like team changes, roadmap shifts, or improvements to the AI tooling. This isn’t a randomized controlled experiment. However, there were no major process or team changes during this window, making it a reasonable approximation for isolating Bugbot’s impact.

**The Results**

|     |     |     |     |
| --- | --- | --- | --- |
| **Metric** | **Before** | **After** | **Change** |
| PRs per developer | 11.4 | 23.9 | +110% |
| Changes requested rate\* | 4.9% | 3.0% | -39% |
| Bugs per developer\*\* | 2.7 | 2.2 | -20% |

_\\* % of PRs where reviewers requested changes_

_\\*\\* Based on issues filed and tagged as defects in our tracking system_

The same developers more than doubled their PR output immediately after Bugbot was enabled. At the same time, our quality signals improved: fewer PRs required changes, and fewer bugs were reported per developer.

What Does “More PRs” Actually Mean?

## What Does “More PRs” Actually Mean?

At first glance, “more PRs” might sound like busy work. But the underlying shift is structural:

**PR size dropped by 82%**, from 1,481 lines to 268 lines on average.

This suggests that developers aren’t doing more work. They’re breaking work into smaller, more reviewable units, which increases throughput and reduces friction in the review process.

In this context, productivity isn’t just output volume. It’s the rate at which meaningful, reviewable work moves through the system.

Why Bugbot Changes Developer Behavior

## Why Bugbot Changes Developer Behavior

The data points to a few reinforcing effects:

1. **Faster feedback loops.** Bugbot reviews PRs in minutes (0.2 hours median), not hours. Developers can iterate quickly and move on to the next task instead of waiting for review.
2. **Confidence to ship early.** Bugbot catches issues before human review, so developers open PRs sooner rather than polishing locally. There is less fear of “wasting” a reviewer’s time.
3. **Reduced context-switching.** Without Bugbot, you open a PR, wait hours for review, then context-switch back. With instant Bugbot feedback, you can address issues immediately while still in flow, then move to the next PR.
4. **Small PRs move faster**. When PRs are small, human reviewers can approve them quickly while keeping the whole pipeline moving.

Comment Quality: Do Developers Actually Find It Useful?

## Comment Quality: Do Developers Actually Find It Useful?

Productivity gains only matter if developers trust the tool. We analyzed reactions (thumbs up / thumbs down) on Bugbot’s 1,371 comments across 374 PRs.

|     |     |
| --- | --- |
| **Metric** | **Value** |
| Comments with reactions | 27.7% |
| Thumbs up | 282 |
| Thumbs down | 70 |
| Positive sentiment | 80.1% |

**The takeaway:** When developers choose to engage with Bugbot feedback, 4 out of 5 reactions are positive 👍 That’s a strong signal that the AI is providing useful, actionable feedback rather than noise.

Bugbot isn’t perfect. It occasionally flags low-signal issues, but developers appear to find the tradeoff worthwhile.

Nine Months Later: Do the Gains Persist?

## Nine Months Later: Do the Gains Persist?

The before/after comparison showed immediate gains. But do they last?

We looked at a more recent 53-day window (January to March 2026), comparing our 18 Bugbot users to 54 non-users.

|     |     |     |     |
| --- | --- | --- | --- |
| **Metric** | **Bugbot Users (18)** | **Non-Users (54)** | **Difference** |
| PRs per developer | 38.2 | 18.4 | +108% |
| Avg PR size (lines) | 268 | 1,481 | -82% |
| Changes requested rate | 3.1% | 3.4% | -11% |
| Time to first review (incl. bots) | 0.2h | 0.6h | -74% |

Unlike the initial analysis, this is a cross-sectional comparison, so selection bias may play a role. However, the magnitude and persistence of the differences suggest the effect is not purely due to developer self-selection.

Nine months after adoption, Bugbot users are still shipping roughly twice as many PRs while maintaining smaller, faster-reviewed changes.

Tradeoffs

## Tradeoffs

One tradeoff worth noting: Bugbot users have longer median cycle times (17.8h vs. 5.5h).

We believe this is a volume effect. With twice as many PRs in flight, there’s more competition for human reviewer attention. While cycle time increases, overall throughput still increases.

We’re continuing to monitor this, but don’t currently see it as a quality issue.

Key Takeaways

## Key Takeaways

So how is Bugbot impacting the team at Jellyfish?

1. **Productivity gains are real:** The same developers more than doubled their output after adoption
2. **Code quality improved:** 39% fewer changes requested, 20% fewer bugs per developer
3. **Developers find it useful:** 80% positive sentiment on AI feedback
4. **Smaller, more reviewable PRs:** 82% smaller than non-users
5. **Benefits persist**: Still seeing ~2x productivity nine months later

AI code review isn’t about replacing human reviewers. It’s about tightening feedback loops, so developers can ship smaller, better changes more frequently. That shift, more than the tool itself, is what drives the impact.

**_If you’re curious about how AI tooling is actually impacting your team’s workflow, that’s exactly what we measure at_** [**_Jellyfish_**](https://jellyfish.co/) **_. You can learn more or_** [**_request a demo_**](https://jellyfish.co/request-a-demo/) **_._**

About the author

![Irene Ng](https://jellyfish.co/wp-content/uploads/2026/03/Irene-Ng.jpg)

Irene is a Senior Software Engineer at Jellyfish.﻿

Follow: [LinkedIn](https://www.linkedin.com/in/ireneng09/)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified