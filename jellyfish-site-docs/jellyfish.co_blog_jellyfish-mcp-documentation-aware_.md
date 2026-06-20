---
url: "https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/"
title: "Product Update: The Jellyfish MCP Is Now Documentation-Aware - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/#content)

_**Editor’s Note:** This article first appeared on the Jellyfish Research Substack. [You can read it and subscribe here.](https://jellyfishresearch.substack.com/p/product-update-the-jellyfish-mcp)_

Grounded answers, plus real docs for your agentic coding loops

The Jellyfish MCP just got a little smarter about Jellyfish itself. With our latest update, your AI assistant can now reach into the Jellyfish help center — searching our documentation and reading full articles on demand — so the answers it gives are grounded in how the product actually works.

If you’ve used the Jellyfish MCP to ask about your team’s effort allocation, delivery metrics, or AI impact, you already know how much faster it is to get insights in a single conversation. But until now, questions about how Jellyfish works — how to configure a feature, where a metric comes from, how to set something up — were answered from the model’s general knowledge alone. That left room for vague or out-of-date guidance.

## What’s New

We added two new tools, backed by two new endpoints, that connect the MCP to the Jellyfish help center. When you ask a “how do I…” or “how does this work” question, the assistant first searches our documentation to find the most relevant articles, then pulls in their full content as context before answering.

## What This Means for You

- Fewer generic answers. Guidance reflects the current product, not a best guess.
- The source is right there. Responses are backed by the actual help articles, so you can dig deeper when you want to.
- One conversation, end to end. Ask about your data and how to act on it without leaving the assistant or hunting through docs in another tab.

## How to Use It

You don’t need to do anything special — just ask your questions naturally, and the assistant decides when to consult the help center on its own. Two patterns where this is especially powerful:

- **Ask questions:** in plain language via you agent. “How do I set up SSO in Jellyfish?” or “How does AI Impact measure adoption?” The assistant searches the documentation, pulls the most relevant article, and answers with steps grounded in how the product actually works — no tab-switching, no guesswork
- **Build context for agentic coding loops:** If you’re using an AI agent to write code against the Jellyfish API, the MCP can now feed it the right documentation as it works. Instead of the agent guessing at endpoints or parameters, it can search the help center, read the relevant articles, and ground its implementation in real, current docs. The result is more accurate code, fewer wrong turns, and a tighter loop — the agent pulls its own context exactly when it needs it rather than relying on what it happened to know.

![Jellyfish MCP documentation aware](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2026/06/8c02cc1b-df22-4334-8610-3d163968fbdc_1986x2144.webp)

_A documentation example showing how the MCP returns reliable information about our API._

## Setup

Nothing changes about how you use the MCP. If you already have the Claude Desktop extension installed, you will need to update the MCP config with the latest release 1.1.1

- **For MCP Extension Users:** Update your MCP config with new release. Install the extension by downloading the .mcpb file from the [Jellyfish MCP GitHub repository](https://github.com/Jellyfish-AI/jellyfish-mcp/releases), double-clicking to install, and providing your Jellyfish API token when prompted.
- **For NPM users:** Update will be pushed automatically, so no setup is required for existing users. New users can follow instructions from the [Jellyfish MCP GitHub repository](https://github.com/Jellyfish-AI/jellyfish-mcp/releases)

Grounding AI in a trustworthy, current context is one of the hardest parts of making it genuinely useful — and connecting the MCP to our own documentation is a meaningful step in that direction.

It’s one more way we’re working to make sure that when you ask Jellyfish a question, you get an answer you can rely on and trust

About the author

![Tomas Pardiñas](https://jellyfish.co/wp-content/uploads/2026/06/Tomas-Pardinas-Headshot.jpg)

Tomas Pardiñas is a Senior Product Research at Jellyfish.

Follow: [LinkedIn](https://www.linkedin.com/in/tomas-pardinas/)

About the author

![Sophie Goldstein](https://jellyfish.co/wp-content/uploads/2025/09/Sophie-Goldstein.jpg)

Sophie is a research intern at Jellyfish.

Follow: [LinkedIn](https://www.linkedin.com/in/sophiejgoldstein/)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish Kiro Integration](https://jellyfish.co/wp-content/uploads/2026/06/blog-Jellyfish-Kiro-1024x561.webp)](https://jellyfish.co/blog/jellyfish-partners-with-kiro-to-measure-ai-engineering-impact/)[**Jellyfish Partners with Kiro to Measure AI Engineering Impact**](https://jellyfish.co/blog/jellyfish-partners-with-kiro-to-measure-ai-engineering-impact/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-partners-with-kiro-to-measure-ai-engineering-impact/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified