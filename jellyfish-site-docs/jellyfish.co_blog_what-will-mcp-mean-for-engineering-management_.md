---
url: "https://jellyfish.co/blog/what-will-mcp-mean-for-engineering-management/"
title: "What will MCP mean for Engineering Management? - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/what-will-mcp-mean-for-engineering-management/#content)

In this article

If you follow software engineering – even peripherally – you know that AI is not just dominating the conversation, but is actually beginning to automate a decent chunk of engineering work. At Jellyfish we’re closely tracking these developments and have seen how employing AI in the software development process – not just for editing code, but for a wide variety of tasks from writing specs and creating documentation to reviewing code and more – is now expected practice.

As the leading Software Engineering Intelligence platform, we view providing quantitative insights into the role AI plays in software engineering as absolutely core to our mission and vision.

But AI isn’t only transforming the work of _building_ software. It’s being applied across roles including engineering management and other leadership functions – the core of Jellyfish’s userbase. So we’re not just looking at how AI impacts software development, but also how it’s used to help those in leadership positions.

Enter Model Context Protocol (MCP)

## Enter Model Context Protocol (MCP)

One of the challenges of LLMs is harnessing them to operate on proprietary information not available on the public web. Since LLMs are trained on practically the entire corpus of the web, they are amazing at any general knowledge task (including tasks such as writing code, composing text, etc.).

Many approaches exist for augmenting LLM knowledge and capabilities with local data, such as fine tuning or RAG architectures. But recently, a powerful new standard has emerged to enable use cases that not only rely on external data, but also allow LLMs to interact with APIs in a general manner: [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP).

MCP was introduced by Anthropic back in November 2024, is publicly supported by OpenAI and Google, and is rapidly becoming standard for how LLMs interact with other software tools. MCP exposes services to an LLM such that it can call upon those APIs to accomplish tasks related to the current task. For example, if you’re working on code, the MCP integration with GitHub can help your prompt pull the latest changes, or commit your work to a branch as you work. Or if you’re working on an analysis task, MCP integrations with databases like Postgres or Snowflake allow the LLM to pull in schema information or perform context-appropriate queries. There are dozens of MCP implementations to connect LLMs to a fast growing set of services.

Engineering Metrics in your LLM

## Engineering Metrics in your LLM

The exciting potential of MCP services to extend LLMs into systems and domains where humans typically operate got us thinking: how much more could LLMs help Engineering leaders if they had access to Engineering metrics?

To explore this idea, we’re building an MCP server to allow LLMs to access Jellyfish data via our API. If you’re a Jellyfish customer, you can now seamlessly integrate any data accessible via the Jellyfish API into your AI-powered workflows, chatbots and agents.

![Jellyfish MCP Demo](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/04/Jellyfish-MCP-Demo-2.gif)

What might this mean in the future? The possibilities are limitless, and we’re hoping to collaborate with users who are interested in trying out ideas in this space. But some examples that this could unlock include:

- **Leverage an LLM for alerting:** What if you had an analyst watching all of your key metrics on a regular basis, flagging anything that looks concerning or interesting, and digging in to suggest avenues for investigation? Now you can create prompts to do exactly that, looking at these regularly via the Jellyfish MCP.
- **Build a “Weekly Briefing” for each Engineering Manager:** Make a prompt to summarize the key metrics on each team, as well as flagging any deliverables that are either nearing completion, or aren’t tracking as expected. Summarize this information in a brief and consumable “weekly digest” for each engineering manager.
- **Business Value Correlation:** As an Engineering leader, put the LLM to work for you as a data analyst to consider leading indicators of ROI on your various key initiatives. Use the Jellyfish MCP to pull in cost data by initiative, and then use additional MCP integrations (e.g., the Pendo MCP server) to consider the relationship between your deliverables, their cost and the business value outcome they drive.

Give it A Try

## Give it A Try

There are practically endless variations to try, and so many interesting possibilities to explore. To get started, visit the [Jellyfish MCP Github repo](https://github.com/Jellyfish-AI/jellyfish-mcp). Reach out to us at [ai@jellyfish.co](mailto:ai@jellyfish.co) if you need any support, or just to tell us what exciting AI applications you’re building! This technology is evolving quickly, so we’ll be continuing to iterate on Jellyfish MCP – stay tuned for future improvements, and let us know what additional capabilities you’d like to see.

About the author

![Nicholas Arcolano](https://jellyfish.co/wp-content/uploads/2026/01/Nicholas-Arcolano-Edited.jpg)

Nicholas Arcolano, Ph.D. is Head of Research at Jellyfish where he leads Jellyfish Research, a multidisciplinary department that focuses on new product concepts, advanced ML and AI algorithms, and analytics and data science support across the company.

Follow: [LinkedIn](https://www.linkedin.com/in/arcolano/Nicholas%20Arcolano,%20Ph.D.)

About the author

![Adam Ferrari](https://jellyfish.co/wp-content/uploads/2025/03/Engineering-Together.jpg)

Adam Ferrari is an Advisor to Jellyfish. He is the former SVP Engineering at Starburst and EVP Engineering at Salsify. Subscribe to his newsletter, Engineering Together, [here](https://adamferrari.substack.com/account?original_app=&free_signup_confirmation=true).

Follow: [LinkedIn](https://www.linkedin.com/in/adamferrari/)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified