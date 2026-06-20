---
url: "https://jellyfish.co/blog/ai-tool-adoption-agent-usage-engineering-productivity/"
title: "From Hype to Impact: A Conversation on AI Tool Adoption, Agent Usage, and Engineering Productivity - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/ai-tool-adoption-agent-usage-engineering-productivity/#content)

In this article

We all know AI is transforming how we build software. But the benefits aren’t evenly distributed: while some organizations are doubling productivity, others have yet to see meaningful gains despite high adoption.

To find out why AI impacts organizations differently, we analyzed Jellyfish data from AI coding tools and autonomous agents, as well as signals from source control and task management. Pulling in data from 20 million pull requests across 1,000 companies and 200,000 developers, it’s one of the largest real-world studies of AI usage in software engineering.

In a recent webinar, Jellyfish Head of Research Nicholas Arcolano broke down the data to explain what we’re seeing at scale in terms of AI adoption, productivity, and expectations. Jellyfish Product Researcher Nickolas Albarran and Crafted’s Head of AI and Engineering Kyle Brill joined the discussion, drawing on their work with companies across the industry to show how the findings are playing out in the real world.

Here are some of the highlights from the conversation. You can also watch the full Deep Dive webinar [here](https://jellyfish.co/events-and-webinars/ai-benchmarks-what-jellyfish-research-learned-from-analyzing-20-million-pull-requests/).

What Does Good AI Adoption Look Like?

## What Does Good AI Adoption Look Like?

Lines of code is the most talked-about metric when it comes to measuring AI coding tool adoption. As adoption rises, so does the percentage of code written with the assistance of AI.

Our data shows that the proportion of companies creating at least half of all code with AI has increased significantly since June 2024. “As of late last year, we’re in a world where AI was involved in more than 50% of PRs at about 50% of companies,” explained Arcolano.

![AI Code Percentage Over Time](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/02/AI-Code-Percentage-Over-Time.png)

That increase in adoption matches what Brill is seeing at the companies he works with. “One of our clients has gone from basically 0% in around June of 2025, to probably being in that greater than 50% band, at least for certain engineers.”

But even at companies with the highest AI code percentage, adoption isn’t always evenly spread. While some engineers have made it into the >50% band, others haven’t yet figured out how to get there. “It’s about trusting the tools more and more,” said Brill. “You can jump between bands relatively quickly depending on your company and adoption curve; that’s one of the reasons why growth is so rapid.”

Albarran agreed, adding that adoption [drives adoption](https://jellyfish.co/platform/jellyfish-ai-impact/drive-adoption/): “Those ‘aha’ moments lead to really quick unlocks. Once you’ve got some real-world examples of using these tools in your code base, that jumps from one developer to a team, to teams of teams.” And while it may take longer to reach 50% AI code at enterprise companies than at AI-native startups, adoption is growing across the board.

Jellyfish data also shows steady growth in the fraction of total coding time spent using AI. By October 2025, most companies had reached over 90% adoption when viewed through this lens.

![Company Level AI Adoption Over Time](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/02/Company-Level-AI-Adoption-Over-Time.png)

Adoption can mean different things at different stages of your organization’s AI journey. One common starting point is the percentage of engineers with an AI coding tool license and how many are actually using it. As your strategy matures, you might start tracking how often developers are picking up the tools and how many are active daily versus weekly users. Understanding the percentage of your code base that AI touches is the next logical step.

“There’s no magic number when we’re talking about adoption; it’s really relative to where you are on your journey,” said Albarran. “What you care about is going to evolve as you evolve in your transformation.”

### Where are we with autonomous coding agents?

Expectations around autonomous coding agents were high going into 2025, with some predicting that AI would write all code without supervision by the end of the year. Jellyfish data shows we’re not there yet. Less than half of companies used a fully autonomous agent in the last three months of 2025, and they were involved in less than 0.2% of PRs.

“You might hear CEOs at AI companies claim all these things are going to be automated, but the folks that are in the real world and running engineering teams aren’t seeing that,” said Albarran. “Growth is going to continue, and it’ll be exciting to see, but it’s still early days.”

Brill agreed that autonomous AI agents are in the trial and experimentation phase. Engineers are still responsible for their own code, and most would be uncomfortable with a fully autonomous agent taking on a mainline merge slated for production. “I still review after the agentic review because, ultimately, my name’s on that code,” added Brill. “Human accountability still belongs in the conversation.

What Productivity Gains Should I Expect?

## What Productivity Gains Should I Expect?

The first productivity metric we analyzed was PR throughput – the average number of PRs merged per engineer per week.

Every point on the chart below is a snapshot of a particular company in a particular week. The X axis shows how often engineers are using AI when they code, and the Y axis shows the number of PRs per engineer. The resulting trend line indicates that when organizations go from zero to 100% adoption, they can expect a 2X increase in PR throughput.

![Companies with Higher AI Use Merge More PRs per Engineer](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/02/Companies-with-Higher-AI-Use-Merge-More-PRs-per-Engineer.png)

Data around [cycle times](https://jellyfish.co/blog/issue-cycle-time-the-staple-engineering-operations-metric/) also suggests real productivity gains. Median cycle time decreased with higher AI adoption rates, both for issues that landed same-day fixes and those that took more than a day to merge.

![AI faster cycle times](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/02/AI-faster-cycle-times.png)

### What does this actually mean for my organization?

Doubling the amount of code only makes sense if it translates to business value. Engineering leaders need to think about what productivity gains mean for their organization: Have teams been able to deliver more initiatives or [allocate more time to roadmap](https://jellyfish.co/platform/resource-allocations/) work instead of maintenance? Jellyfish insights help leaders understand how AI impacts individuals, teams, and repos, and answer complex questions with precision.

An increase in productivity also creates new challenges. “We’re coding faster, and we’re getting work done faster,” explained Albarran. “But this then becomes a change management problem – how do we actually reap the benefits of that as an organization? It’s not as simple as 2X code equals 2X more of everything.”

What If Expectations Don't Equal Reality?

## What If Expectations Don’t Equal Reality?

[Code architecture](https://jellyfish.co/blog/ai-coding-tools-not-paying-off-your-code-architecture-might-be-to-blame/) – how products and services are organized across repos – makes a big difference to the AI experience.

The chart below categorizes companies based on the number of repos engineers need to work with in order to do their jobs. Centralized, monolithic architectures are on the left and highly distributed architectures on the right, with balanced and distributed architectures in between.

![Repos and code architecture](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/02/Repos-and-code-architecture.png)

Returning to the scatter plot of PRs per engineer versus adoption rate, we get significantly different trend lines when we segment companies by their code architecture. Companies with a centralized code architecture achieve 4X productivity gains, while those with a highly distributed architecture can expect a slight negative impact.

“Code architecture isn’t the only thing that differentiates who’s having a good time and who’s having a bad time with AI, but it is an example of a decision that companies might have made a decade ago that has meaningful effects on their AI transformation,” said Arcolano.

![AI gains by code architecture](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/02/AI-gains-by-code-architecture.png)

Brill explained why centralizing documentation and markdown files into a single repo leads to better results with AI. “Your agents do best when they have context. And if that context is centralized, and it’s in a variety of different formats and traversable in the same co-located file structure, you’re going to have a better time than if you hope the agent can reason about specs and integrations across boundaries.”

What's Next?

## What’s Next?

For the software engineering industry, expectations around AI are shifting. New tools and capabilities set the bar higher, and it can be hard to know what to aim for.

AI coding tools are already making engineering organizations more productive, and autonomous agents promise to multiply those gains. “In my opinion, we’re on an exponential curve with the progression of these agents,” said Brill. “We’re going to see some very interesting things this year.” But Brill also warned against the consequences of not proceeding with caution: “Somebody will crash and burn horribly by not putting their agent on guardrails.”

Albarran also believes AI agents will become more widespread this year. “I think 100% of companies will have an autonomous agent that is automated in at least one part of the workflow,” said Albarran. “It might just be an agent that builds requirements, but you have to start somewhere, and starting small leads to a snowball effect.”

**_For more insights, check out the_** [**_full webinar recording here_**](https://jellyfish.co/events-and-webinars/ai-benchmarks-what-jellyfish-research-learned-from-analyzing-20-million-pull-requests/) **_. To find out how AI adoption is affecting delivery and quality at your organization, try_** [**_Jellyfish AI Impact_**](https://jellyfish.co/platform/jellyfish-ai-impact/) **_today._**

About the author

![Jellyfish](https://jellyfish.co/wp-content/uploads/2021/11/Jellyfish_Icon-Mark_White-e1780342228711.png)

Jellyfish is the leading Software Engineering Intelligence Platform, helping more than 700 companies including DraftKings, Keller Williams and Blue Yonder, leverage AI to transform how they build software. By turning fragmented data into context-rich guidance, Jellyfish enables better decision-making across AI adoption, planning, developer experience and delivery so R&D teams can deliver stronger business outcomes.

Follow: [LinkedIn](https://www.linkedin.com/company/jellyfish-co/)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified