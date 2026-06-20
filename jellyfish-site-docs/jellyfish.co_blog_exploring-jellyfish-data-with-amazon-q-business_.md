---
url: "https://jellyfish.co/blog/exploring-jellyfish-data-with-amazon-q-business/"
title: "Exploring Jellyfish Data with Amazon Q Business: How we Leveraged Amazon’s GenAI Assistant and Jellyfish’s API to Gain In-depth Insights - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/exploring-jellyfish-data-with-amazon-q-business/#content)

![Jellyfish API](https://jellyfish.co/wp-content/uploads/2024/11/blog-Exploring-Jellyfish-Data-with-Amazon-Q-Business-scaled.webp)

![](https://jellyfish.co/wp-content/uploads/2023/08/Jellyfish_Blog-Author-Headshots_Jellyfish.webp)

Liz Coolman and Luke Stevens

November 26, 2024

At Jellyfish, we empower engineering leaders to drive better business outcomes by giving them more robust and accurate ways to measure and communicate the impact of their teams’ work.

While Jellyfish provides a deep view of engineering effort and business alignment, we know there are times you may need Jellyfish data in a different system to work most effectively. That’s why today we’re excited to share our brand new API.

The Jellyfish API is a series of endpoints that give users the ability to connect operational metrics, software deliverables, and engineering investment data from Jellyfish to third-party tools. The API enables customers to seamlessly integrate Jellyfish data across critical business processes outside of the platform. A key benefit of APIs is maximum flexibility in the end state of the data. For instance, you can now integrate Jellyfish with various third-party platforms so teams can easily centralize information-sharing and reduce context switching between multiple tools.

Given the slew of possibilities made available by these new API endpoints, and the unrelenting desire to experiment, we decided to test new destinations for Jellyfish data ourselves. We hope that by sharing what we’ve learned, we can inspire creative ways for our customers to leverage the Jellyfish API to gain and learn from key insights – everywhere.

## Getting Started

Given the prevalence of LLMs (Large Language Models) and AI-driven analytics, we were eager to explore tools that could be paired with the Jellyfish API to make data querying more intuitive, productive, and accessible. [Amazon Q Business](https://aws.amazon.com/q/business/) caught our attention as a GenAI Assistant we could explore to synthesize information from API outputs and documentation to speed up API utilization, and provide on-demand insights that could be requested in various workflows outside the Jellyfish platform.

## How We Experimented with Amazon Q Business

In testing Amazon Q Business’ capabilities against Jellyfish resources, we wanted to learn two things:

1. Can Amazon Q Business read Jellyfish API documentation and provide guidance on how to use it?
2. Can Amazon Q Business index outputs from the Jellyfish API so we can ask meaningful questions about our teams’ deliverables, metrics, investments, and performance?

The following steps outline our process and outputs from Amazon Q Business:

- **Setting Up the Data Source:** We configured Amazon Q Business to crawl and index Jellyfish’s public website, API documents, and the YAML from our API Swagger doc. We utilized a [S3 Data Connector](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-connector.html) to allow Amazon Q Business to access data from these Jellyfish artifacts to create a foundation for informed responses that incorporated our terminology.

- **Guidance on API Queries:** Amazon Q Business helped us understand which Jellyfish API calls to use for different data outputs. For example, it suggested methods to retrieve specific insights – such as performance metrics or project timelines – meaning less time sifting through documentation to find the most relevant endpoints for our needs.

- **Coding & CSV Exports**: With guidance from Amazon Q Business, we generated code to query our data and exported those outputs to CSVs.

- **Requesting Jellyfish Findings:** After running these queries and getting our data outputs, we added the CSVs to the S3 bucket and re-synced the data source. We then asked Amazon Q Business a variety of questions about our teams pulled from Jellyfish, such as:

- “What sort of performance-related work is currently in progress?”
- “What deliverables are past due?”
- “Tell me about Team X’s metrics”

![Amazon Q Business_Jellyfish](https://www.jellyfish.co/wp-content/uploads/2024/11/Amazon-Q-Business_Jellyfish.png)

The results were impressive. Amazon Q Business was able to quickly identify the relevant data points for the appropriate use cases, and on the occasions where it didn’t, a simple follow-up was usually enough to generate a useful response. We’re confident that with a bit of tweaking Amazon Q Business could consistently generate accurate and actionable responses.

## Looking Ahead

We wanted to keep this initial exercise exploratory and lightweight, but with expanded scope, we’d explore the following:

- **Automate API Query Updates:** Set up automatic daily queries to ensure data remains fresh.
- **Expand Data Connectivity:** Research Amazon Q Business’s data connector features and identify opportunities to ingest data in different formats or from additional sources like Jira or Confluence, which would open up even more querying possibilities.
- **Refine Data Structuring for Enhanced Responses:** By shaping API responses to focus on specific details, such as project progress or team member contributions, we could optimize Amazon Q Business’s responses for our needs.
- **Integrate with Slack**: Connect Amazon Q Business to a Slack interface for greater accessibility and the ability to ask ad-hoc questions about our efforts from an app we already spend a lot of time in. Amazon provides a guide to deploying a Slack gateway [here](https://aws.amazon.com/blogs/machine-learning/deploy-a-slack-gateway-for-amazon-q-your-business-expert/).

## Key Takeaways

Working with Amazon Q Business highlighted its ability to synthesize complex information, including API documentation and support materials. It was able to guide us through various API endpoints, as well as outline available options. Additionally, Amazon Q Business was able to retrieve summaries about relevant topics from the Jellyfish API when questioned. We found the initial setup and training of the tool straightforward, which allowed us to get results quickly.

**Considering using Amazon Q Business or exploring other AI tools for data insights? Would you build something like this for your org? We’d love to hear from you!** **Reach out to** [**api@jellyfish.co**](mailto:api@jellyfish.co) **to get in touch.**

**Happy building!**

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish Kiro Integration](https://jellyfish.co/wp-content/uploads/2026/06/blog-Jellyfish-Kiro-1024x561.webp)](https://jellyfish.co/blog/jellyfish-partners-with-kiro-to-measure-ai-engineering-impact/)[**Jellyfish Partners with Kiro to Measure AI Engineering Impact**](https://jellyfish.co/blog/jellyfish-partners-with-kiro-to-measure-ai-engineering-impact/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-partners-with-kiro-to-measure-ai-engineering-impact/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified