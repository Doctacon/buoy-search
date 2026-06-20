---
url: "https://jellyfish.co/blog/how-prevalent-is-autonomous-agent-use-heres-what-the-data-says/"
title: "How Prevalent is Autonomous Agent Use? Here’s What the Data Says. - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/how-prevalent-is-autonomous-agent-use-heres-what-the-data-says/#content)

In this article

Over the past year, engineering teams have more readily allowed autonomous coding agents to take concrete actions in their development workflows. These agents don’t just assist developers in their IDEs, they open pull requests, make commits, create their own issues, and sometimes even merge code on their own.

**Here at Jellyfish we have a rich dataset of nearly five million merged PRs from more than six hundred different companies over the last three months,** and we’ve been using it to [track the rise of AI coding tools](https://jellyfish.co/research/ai-coding/). Now we’re taking a closer look at a small subset of these tools, sometimes referred to as “autonomous” or “workflow” agents, which are defined by their ability to fully interpret and execute tasks without the direct supervision of a human.

Autonomous agents (like Devin or Codex) operate very differently from the more widespread coding assistant tools, like [Cursor](https://jellyfish.co/blog/measure-ai-impact-copilot-cursor-gemini-sourcegraph/) or [Windsurf](https://jellyfish.co/blog/ai-impact-windsurf/), so we wanted to see if we could isolate their usage in order to better understand their adoption across the industry. By flagging PRs that show signs of autonomous agent behavior – for example being opened or merged by an agent or including commits that were authored by one – we get a better picture of how real software teams are experimenting with these autonomous agents in production.

The picture we’re seeing so far? It’s early days. _Really early._

PRs Influenced by Agents

## PRs Influenced by Agents

Out of **millions of PRs** across hundreds of customer companies, only **about 8,000** in the last three months show signs of autonomous agent involvement. That’s a _tiny_ fraction of all engineering activity (less than 0.2%) and it’s limited to only 44% of companies in our dataset. This means that **about half of our customers aren’t using autonomous agents at all.**

Even among companies who are early adopters, these tools show up in only **a small portion of their total PRs** (1.47%), and in an even smaller portion that actually get merged (0.44%). While we _are_ seeing consistent usage in _some_ organizations, and we’ll take a closer look at those later, autonomous agents are still largely **confined to the edges of the dev process**.

For this analysis, we used a strict, action-based definition of agent activity:

- A PR was **opened** by an AI agent, or
- **Merged** by an AI agent, or
- Includes at least one **commit authored** by an AI agent

Looking at the data this way helps us focus on actual autonomous behavior, not just tools that make suggestions or generate code synchronously while a user is coding or actively supervising. It also means that we are intentionally not counting some activity from tools like Claude and Copilot, because they’re _just_ barely behind the scenes enough that they’re not actually taking these actions themselves (e.g., the agent writes a block of code, but the developer is taking the action of committing that code). Most of the time, a user still reviews/edits and commits the code themselves when using these tools.

Tools Used and For What

## Tools Used and For What

Among the agent PRs in our dataset, several tools show up frequently and consistently. The most represented tools in this month’s data include more task-specific tools like Sourcegraph and Snyk, as well as the full-spectrum ones like Devin, Cursor Agent, and GitHub Copilot Agent. Also in the mix are Codegen and Claude Code.

While the majority of all PRs continue to touch multiple file types, we noticed some really interesting patterns in the difference between agent and non-agent PRs. One thing is very clear: **infra work is where autonomous agents are gaining the most traction.**

|     |     |     |
| --- | --- | --- |
| **Work Type** | **% of All PRs** | **% of Agent PRs** |
| **Infra** | 7.2% | 31.2% |
| **Full-stack** | 81.5% | 49.6% |
| **Backend** | 6.4% | 11.5% |
| **Frontend** | 4.8% | 7.7% |

This makes sense. Work like config updates and dependency management are often well-scoped, straightforward tasks. They also happen to be some of the least fun kinds of work to do, all of which makes them a perfect and natural starting point to pass off to agents.

But **specific, targeted usage is happening across the stack**. Backend and frontend work each make up roughly **twice the share** among agent PRs compared to all PRs, indicating that agents are being used for focused changes in a variety of technical domains.

User Retention

## User Retention

Trying something once is easy. But are developers actually taking the time to integrate autonomous agents into their workflows? Is the time-to-value shorter than the time-to-frustration-and-giving-up?

We looked at the **retention curve** to see how many developers continue using these agents after their first agent PR, and the drop-off is steep:

- **Week 0:** 100% (everyone starts here)
- **Week 1:** ~23% (already a _significant_ drop)
- **Week 4:** ~15%
- **Week 10+:** <10%

Our data suggests that **developers are experimenting**, but often don’t continue using autonomous agents. Drop off could be due to friction, lack of confidence, unclear value, or difficulty finding the right tool for the right use case. The issue isn’t with the capabilities of these agents – they do have many consistent and loyal users – but rather about learning how to use them most _effectively_.

This all goes to show that just making a tool available isn’t enough – **there’s an art to change management**. Providing teams with necessary training, allowing them the breathing room to overcome the startup costs and challenges, and identifying power users within your org in order to understand what works and what doesn’t, are all critical parts of the adoption journey.

The Big Picture

## The Big Picture

Despite the hype, we are still early in real-world adoption of autonomous agents. Truly autonomous agent tools are _far_ less pervasive than coding assistants – for now. Many teams are just beginning to experiment, and most PRs – even from agent-heavy companies – are still authored, reviewed, and merged entirely by humans. Progress into the “ [year of the agent](https://www.linkedin.com/posts/bcg-on-digital-and-technology_tech-trends-2025-the-year-of-the-agents-activity-7292279984075747329-8yhH/)” has been more measured than early 2025 predictions suggested. But it doesn’t mean we won’t get there.

Autonomous agents are starting to claim small, specific pieces of the SDLC and while . adoption is limited right now, it is real – with the most significant gains being made in infra work and other specific, targeted tasks. For most teams, agents are not yet part of the day-to-day workflow, but experimentation is happening and the foundations are being laid.

We don’t believe that autonomy is the future of all engineering work. But we do believe it’s an extremely powerful and important part of that future.

About the author

![Sofia Thompson](https://jellyfish.co/wp-content/uploads/2025/09/Sofia-Thompson.jpg)

Sofia is a Data Scientist at Jellyfish.

Follow: [LinkedIn](https://www.linkedin.com/in/sofithompson/)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified