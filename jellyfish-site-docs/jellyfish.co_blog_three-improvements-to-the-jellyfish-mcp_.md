---
url: "https://jellyfish.co/blog/three-improvements-to-the-jellyfish-mcp/"
title: "Three Improvements to the Jellyfish MCP - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/three-improvements-to-the-jellyfish-mcp/#content)

_[This article](https://jellyfishresearch.substack.com/p/three-improvements-to-the-jellyfish) first appeared on the Jellyfish Research Substack. You can read and subscribe [here](https://jellyfishresearch.substack.com/)._

We’re continuously improving the [Jellyfish MCP](https://github.com/Jellyfish-AI/jellyfish-mcp) to give you a better experience with AI-powered engineering insights. Here’s what’s updated in the newest version:

1. **Data now outputs in TOON format instead of JSON.** How you send data to AI models matters more than you might think—send too much or in the wrong format, and you’re wasting tokens. We ran [an analysis](https://open.substack.com/pub/jellyfishresearch/p/the-token-tax-why-we-switched-to?utm_campaign=post-expanded-share&utm_medium=web) on Jellyfish data comparing formats and found that [TOON](https://github.com/toon-format/toon), a YAML-like format, is more token-efficient than JSON in most cases. The MCP now automatically translates data into TOON before sending it to your AI host application.
2. **Rebuilt from Python to Node.js.** The MCP server and Claude Desktop extension now share the same codebase in Node.js, which means faster updates and more consistent behavior across platforms. The Python version is no longer being updated, but the source code for the previous version is still available [here](https://github.com/Jellyfish-AI/jellyfish-mcp/tree/529714a472646460130c5edf2ff20f2e3c8d0d56).
3. **Docker support.** We published a [Docker image on Docker Hub](https://hub.docker.com/r/jellyfishco/jellyfish-mcp) so you can run the MCP server in a container. Once configured, Docker handles everything—no manual installs, and updates pull automatically so you’re always on the latest version.

_What this means for you:_ Nothing changes about how you use the MCP. Just make sure you’re on the latest version. If you want to try the new Docker setup, follow the directions in the [README](https://github.com/Jellyfish-AI/jellyfish-mcp), and once configured, it will automatically stay up to date.

The hardest part of building an MCP isn’t the engineering — it’s managing context. Every tool response sends data to an LLM, and figuring out how much context to include is an ongoing challenge when the model is essentially a black box. There’s no formula for getting it right, at least not yet. So we’re iterating: testing different approaches, exploring new ideas, and learning as we go. The switch to TOON came directly out of this process — and it won’t be the last change we make. If you’re building an MCP too, our experience has been that this kind of iteration is where the real progress happens.

About the author

![Sophie Goldstein](https://jellyfish.co/wp-content/uploads/2025/09/Sophie-Goldstein.jpg)

Sophie is a research intern at Jellyfish.

Follow: [LinkedIn](https://www.linkedin.com/in/sophiejgoldstein/)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified