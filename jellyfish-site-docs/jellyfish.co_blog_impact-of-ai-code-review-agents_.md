---
url: "https://jellyfish.co/blog/impact-of-ai-code-review-agents/"
title: "The Real Impact of AI Code Review Agents: What We Learned from 1,000 Reviews - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/impact-of-ai-code-review-agents/#content)

In this article

Last month, we offered a first look at [AI agent adoption data](https://jellyfish.co/blog/rise-of-agentic-ai-in-engineering/) to understand the emerging AI-DLC. That analysis, covering more than 400 companies from December 2024 to May 2025, showed the growing popularity of AI agents – tools that don’t just assist but act – among engineering teams.

Now we’re taking a deeper dive specifically into the use of code review agents, evaluating developer sentiment and, crucially, their impact in the form of real changes made to code in order to better understand their actual utility. To do so, we analyzed comments and commit messages from 1,000 code reviews across 400 companies from May to July 2025.

Agent Adoption

## Agent Adoption

In terms of usage, we found most teams are still in the trial and experimentation phase. Of the 400 companies in our dataset, **75% have tried none or one of these review tools in the past three months, and 93% have tried two or fewer.** The vast majority are steadily continuing to use the few tools they have tried, and only 16% seem to be consistently trying out more. Of all the companies using these tools, **only 8% seemed to have moved past experimentation into a more settled state,** meaning they tried out multiple tools and are now using only one or two.

![Jellyfish AI code review agent adoption](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Jellyfish-AI-code-review-agent-adoption.png)

Among the companies that do use agents, agents only appeared on 22% of the average company’s code reviews over the past three months. Only a handful of companies used them on more than 50% of their code reviews, with the leaders (in terms of usage) reaching 92%.

We then sought to determine how often an agent’s feedback is being accepted. To do so, we used LLMs to analyze the sequence of comments and commit messages made by both humans and agents. **We were surprised to find that humans only responded to 56% of the agent reviews, and only 18% seemed to result in an actual change being made.** While small, even 18% means time savings for developers, and fewer bugs slipping through the cracks.

From the data, our main takeaway is that while code review agents are indeed being used, we’re still far from widespread and consistent adoption.

Developer Sentiment

## Developer Sentiment

Among developers actually using these agents, how do they feel about their utility? To analyze the quality and effectiveness of human-agent interactions, we identified code reviews featuring meaningful exchanges between humans and review bots, then employed sentiment analysis to assess these interactions. **We found that most people tend to be neutral (56%) or positive (36%) in their interactions with agents, with only 8% of interactions as negative.**

We’ve already established how impactful these review tools can be, and the comments from developers absolutely back that up. In our dataset we saw shouts of “Go offff!” and “nice catch; good bot,” with developers praising the AI’s ability to spot issues: “Great catch \[agent name\]!” and “Good robot!” Many comments expressed relief and gratitude, exclaiming “great idea, love it! will do” and admitting, “that would have driven us crazy ’til we found it.”

Of course, we know that none of these tools are perfect. Sometimes there’s a palpable frustration, with comments like “A human would have figured this out 🤷‍♂️” and blunt criticisms such as “You’re fragile \[agent name\].” The exasperation can turn colorful: “Oh, FFS. Of course we do 🤦” or a stark, “??? This is straight up wrong.” Others challenge the AI directly: “I disagree mr. bot – I’m fairly certain that’s the serializer.” And then there are the truly exasperated, who might tell the bot, “You’re drunk, @\[agent name\], go to sleep” and follow it up with “And no sense of humor either.”

On the whole though, we saw more positive or neutral comments than negative ones, illustrating developers’ openness to trying code review agents.

While we’re nowhere near full agent adoption, the AI-DLC is undoubtedly here. Now is the time to begin experimenting with AI agents to see how your engineering team can benefit. As our data shows, the impact on code quality and efficiency is real, and the potential for improvement is enormous.

![](https://jellyfish.co/wp-content/uploads/2025/09/blog-code-review-data.webp)

#### What's the real impact of code review agents?

Take a closer look with Jellyfish AI Impact.

[Get a Demo](https://jellyfish.co/get-an-ai-impact-demo/)

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