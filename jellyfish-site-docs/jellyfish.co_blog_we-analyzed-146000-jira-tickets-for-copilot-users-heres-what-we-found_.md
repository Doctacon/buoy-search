---
url: "https://jellyfish.co/blog/we-analyzed-146000-jira-tickets-for-copilot-users-heres-what-we-found/"
title: "We Analyzed 146,000 Jira tickets for Copilot Users. Here's What We Found. - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/we-analyzed-146000-jira-tickets-for-copilot-users-heres-what-we-found/#content)

![We Analyzed 146,000 Jira tickets here's what we found](https://jellyfish.co/wp-content/uploads/2024/12/blog-We-Analyzed-146000-Jira-tickets.webp)

![](https://jellyfish.co/wp-content/uploads/2023/04/Lena-Chretien.webp)

Lena Chretien – Jellyfish Research

January 14, 2025

Generative [AI coding tools](https://jellyfish.co/blog/best-ai-coding-tools/) are transforming the way software engineers work, reshaping traditional workflows with a mix of new opportunities and challenges. Among these innovations, GitHub Copilot stands out as a leader. Copilot leverages the capabilities of advanced language models to deliver real-time code suggestions, enabling developers to translate natural language inputs into functioning code seamlessly.

Initial studies on the impact of GitHub Copilot paint a mixed picture. While some research highlights increased developer productivity and satisfaction – qualitative surveys suggest satisfaction improvements of up to 50% and controlled coding studies have shown 55% reduction in task completion time – real-world gains are often much smaller, only around 8%.

Clearly, the impact of GitHub Copilot on key workflows – like code review cycles, collaboration, and task allocation – warrants a deeper look.

To do that, we conducted an extended study across 145 companies and more than 6,500 engineers using platform data from [Jellyfish’s Copilot Dashboard](https://jellyfish.co/platform/jellyfish-copilot/). Here we explore how Copilot influences productivity, throughput, and code quality at scale, as well as who benefits the most.

## The Data

We analyzed two groups:

- 6,500 engineers with active GitHub Copilot licenses
- 11,400 engineers without Copilot licenses (the baseline group)

The study compared engineers’ coding behavior before Copilot adoption to their behavior after the adoption for work items where Copilot was actively used. In total, the dataset comprised:

- 146,000 Jira tickets for Copilot users
- 428,000 Jira tickets for non-Copilot users

Our metrics included:

- **Coding Time vs. PR Review Time:** Work cycles were divided into active coding time and PR review time.
- **PR Pickup Time:** Time between opening a PR and its first review.
- **Throughput:** Number of pull requests (PRs) submitted per week.
- **Code Quality:** Measured using bug-related Jira tickets.

## What We Learned

### 1\. Adoption Rates

Despite Copilot’s growing visibility, company-level adoption remains low, averaging just 22.6%. Individual usage is, on average, 50%, meaning that engineers usually use Copilot one out of two days. However this varies on an individual basis from engineers barely using it to engineers using it every day.

This disparity highlights the mixed reception of Copilot and points to the need for organizational strategies and formalized change management to encourage effective adoption and broader, more consistent use across teams.

### 2\. Coding and PR Metrics

Copilot significantly enhances coding efficiency, with users experiencing:

- A 20% reduction in coding time
- A 26% reduction in PR review time
- A 24% decrease in overall work time (coding + review)

To put this in perspective, this means Copilot users save approximately 3 full workdays on average _per_ ticket, 1 day per ticket from reduced coding times, and 2 days per ticket from faster PR Review times. A typical ticket takes anywhere from 3.5 to 25 days to resolve, translating to a time savings of 12% to 85% when using Copilot.

![Coding and PR metrics changes with Copilot](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/01/Coding-and-PR-metrics-changes-with-Copilot.png)

Interestingly, the reduction in work time varied between different roles and coding tasks:

- Test and automation engineers saw the largest reduction in coding time (4 days), likely due to Copilot’s ability to generate tests efficiently
- Back-end engineers showed larger reductions than front-end and full stack engineers  (1.8 days vs. 0.4 days)
- Roles like security and analytics reported mixed results.

### 3\. Seniority-Based Differences

Senior and Principal engineers benefited the most:

- Senior engineers reduced coding time by 22%, compared to just 4% for Junior developers.
- Work time decreased by 14% for experienced engineers but only 11% for Juniors.

This suggests that Copilot’s full potential is unlocked by engineers with strong foundational skills. Junior developers, while benefiting from syntax suggestions, may struggle to critically assess Copilot’s output, potentially hindering deeper learning. As one CTO we spoke with put it, “senior developers can write better prompts.”

### 4\. Throughput

Our study revealed that Copilot users merged 10% more PRs per week compared to non-users. However, they resolved fewer Jira tickets overall, indicating:

- An emphasis on fewer, more complex tasks.
- Improved output depth rather than sheer task volume.

### 5\. Code Quality

Using bug-related Jira tickets as a proxy for code quality, we observed a reduction in bug excess (the difference between created and resolved bugs). This indicates that while more bugs are created, they are also resolved more quickly with the help of Copilot.

## Key Takeaways and a Look at What Comes Next

Our findings offer a nuanced view of GitHub Copilot’s impact on engineering workflows:

- **Efficiency Gains:** Copilot significantly reduces coding and PR review times, saving engineers valuable hours. The most experienced engineers benefit the most, using Copilot to streamline workflows effectively.
- **Skill Development:** Junior developers see smaller improvements, suggesting a need for balanced AI usage. Organizations must ensure that AI tools complement learning rather than replace foundational coding skills.
- **Throughput vs. Complexity:** Copilot appears to enable engineers to focus on larger, more complex tasks, as reflected in the 10% increase in merged PRs.
- **Improved Code Quality:** Faster resolutions point to potential improvements in code quality.

However, challenges remain. It’s important to remember that adoption rates are still low, averaging just 22.6% at the company level. And variability in individual usage highlights the importance of targeted training and change management to encourage adoption.

GitHub Copilot has the potential to transform software engineering yet its success depends on thoughtful integration strategies. Organizations must invest in training to ensure engineers at all levels – especially more junior developers – can effectively use Copilot without sacrificing skill development.

By addressing these challenges, companies can unlock the full potential of AI tools like Copilot, empowering engineering teams to achieve higher productivity, better collaboration, and improved code quality.

**_Gain a better understanding of Copilot’s impact on your team. Learn more about [Jellyfish’s Copilot Dashboard here](https://jellyfish.co/platform/jellyfish-copilot/)._**

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified