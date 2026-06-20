---
url: "https://jellyfish.co/blog/unit-testing-automation/"
title: "How Generative AI Improves Developer Quality of Life through Unit Testing Automation - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/unit-testing-automation/#content)

![Unit testing automation](https://jellyfish.co/wp-content/uploads/2024/09/blog-genai-unit-testing.webp)

![](https://jellyfish.co/wp-content/uploads/2024/09/Ray-Gilbert.png)

Ray Gilbert

September 26, 2024

_The following is a contributed article from_ [_Ray Gilbert_](https://www.linkedin.com/in/raymondgilbert/) _. Ray is VP of Engineering at_ [_Ostro_](https://www.ostrohealth.com/) _, an AI-powered technology platform for better health care provider and consumer engagement. If you are interested in contributing to the Jellyfish blog, reach out to [gail.axelrod@jellyfish.co](mailto:gail.axelrod@jellyfish.co)._

Retrofitting unit tests onto established systems often feels exhausting, repetitive, and non-value-adding. In this post, I’ll explain how [generative AI](https://www.jellyfish.co/solutions/jellyfish-copilot/) can improve this process and significantly enhance developers’ quality of life, leading to greater productivity and higher-impact work for your team.

## The Challenge: Toil of Retrofitting Unit Tests

Toil in [software development](https://www.jellyfish.co/blog/can-you-measure-software-development/) is any repetitive, manual task that doesn’t significantly advance business goals or move a project forward. Retrofitting unit tests into legacy code falls into this category. While unit tests are critical to maintaining code quality and reliability, asking your most talented engineers to write tests for extant code can be an inefficient use of their expertise and creativity, given that there are alternate approaches. They should focus on new features, innovation, and solving higher-level problems. However, omitting unit tests is not an option because it would significantly weaken the overall stability of your software.

This is where [AI comes into play](https://www.jellyfish.co/blog/4-engineering-leaders-on-the-pros-and-cons-of-chatgpt-and-github-copilot/).

## AI as a Solution: Automating First Passes of Unit Tests

AI is well suited to address the toil of retrofitting unit tests as the complexity of the task is relatively low, and there is a large corpus of examples LLMs incorporate in their training. By automating the initial, tedious step of creating these tests, developers can focus on more meaningful tasks – such as reviewing, refining, and ensuring test accuracy – rather than starting from scratch. This reduction in toil improves efficiency and [elevates job satisfaction](https://www.jellyfish.co/blog/why-team-health-should-be-your-engineering-organizations-new-north-star/) for your developers, as they focus more on meaningful work and less on repetitive tasks.

One can start by using LLMs’ chat interfaces directly to build the initial framework for test generation. The process can be scaled by building pipelines that run the codebase through LLMs and automating unit test generation.

### Addressing Concerns: The Role of Human Oversight

While AI can significantly streamline the process of creating unit tests, it’s natural for there to be concerns about the reliability and effectiveness of AI generated tests. Here are some key points to consider:

1. **AI as a Starting Point:** AI-generated tests should be viewed as a first draft or starting point, not a final product. They provide a foundation that can save significant time, but they are meant to supplement human expertise.
2. **Quality Assurance:** Human developers are crucial in reviewing, refining, and validating AI-generated tests. They bring domain knowledge and understanding of edge cases that AI might miss.
3. **Customization for Project Needs:** AI models may not fully grasp project specific requirements or coding standards from the outset. Developers must adjust the generated tests to align with their team’s needs and practices.
4. **Continuous Improvement:** As developers review and refine AI-generated tests, they can provide feedback to improve the AI’s output over time, creating a virtuous cycle of improvement.
5. **Complementary Skills:** AI generates boilerplate code and covers obvious test cases, while humans excel at understanding complex business logic and identifying subtle edge cases. Combining AI efficiency and human insight leads to more robust test suites.
6. **Code Coverage isn’t Everything:** While AI can quickly generate tests that achieve high code coverage, it’s important to remember that coverage alone doesn’t guarantee quality. Human oversight ensures that tests are meaningful and validate the code’s behavior.

### Reducing Developer Toil, Elevating Impact

By removing the repetitive task of retrofitting unit tests, AI allows developers to focus on more impactful work. Instead of getting bogged down with writing tests for already written code, they can be free to push boundaries, innovate, and move your projects forward.

Integrating AI for unit testing is not just a technical improvement – it’s an investment in your developers’ quality of life and the future of your business. By alleviating toil, you empower your team to spend more time solving problems that matter, driving both satisfaction and business outcomes.

## Getting Started with AI-Powered Unit Testing

To effectively implement AI-driven unit testing, I recommend the following foundational tenets (unless you know better ones – in which case please share them with me!):

### Experimentation is a First Principle of Successful Organizations

Encourage your teams to test different AI models and prompt configurations to find the best match for your codebase. Building a culture of experimentation and openness to new tools is vital for success in any engineering org.

### Think Before You Hand Over Data to an AI hand

Consider Privacy and Terms of Use. Ensure that the AI you choose won’t use your code for training purposes if that is important to your organization. Avoid sharing sensitive information and secrets (e.g., API keys) with any AI system, and prioritize solutions that respect your intellectual property and that are approved for use by your organization.

### Leaders Must Be Champions of Experimentation

Make resources, including budget for tool licenses and training, readily available to encourage your teams to try new tools. This will foster a mindset of continuous improvement and innovation and show the organization’s top-level commitment.

## The 30-Day Challenge – AI Unit Testing Pilot

Are you ready to try this in your organization? Here is a simple 30-day pilot program to get you started.

**Week 1**

Research and select an AI tool for unit test generation. Select two to three evaluation KPIs. Start with a pool of four to six and aim to run your pilot with the two to three best / preferred choices. You want to get data on multiple solutions for optimum evaluation.

**Week 2**

Conduct a pilot project on a small module of your codebase. Again, to get a good data sampling, pick two to three projects and use each tool from Step 1 to build out your test suite.

**Week 3**

Analyze the results and gather team feedback. Incorporate both quantitative and qualitative inputs. Your KPIs from Week 1 cover the quantitative inputs. For the qualitative, survey your developers and dive deep into their experiences during this challenge. Which tools were best at which use cases? What deficiencies in the tooling did you find? How would you improve the experience?

**Week 4**

Present findings to stakeholders and plan for broader implementation. Lean into the benefits and shortfalls, along with your plans to optimize and address them. Present the big picture of benefits and the investment needed to increase the rates of return of those benefits.

## Appendix – Implementing AI-Assisted Unit Testing: A Comprehensive Guide

**1\. Pilot Program**

- Select a small, low-risk project or module for initial implementation.
- Choose two to three developers to spearhead the pilot.
- Set clear goals and metrics for the pilot (e.g., time saved, test coverage increases).

**2\. Tool Selection**

- Research available AI tools.
- Consider factors like privacy, integration with existing tools, and cost.
- Test two to three options on sample code before making a final decision.

**3\. Team Training**

- Conduct a coworking event to introduce the new tool(s) and get hands on.
- Task the Pilot Team to create best practices and guidelines for AI assisted test writing.

**4\. Integration into Workflow**

- Update your development process to include AI-assisted test generation.
- Integrate the AI tool with your IDE and CICD system.
- Establish a review process for AI-generated tests.

**5\. Scaling Up**

- After the pilot, gradually expand to more teams and projects.
- Collect and address feedback from early adopters.
- Adjust processes and guidelines based on lessons learned.

**6\. Continuous Improvement**

- Regularly assess the effectiveness of AI-generated tests.
- Stay updated on advancements in AI tools.
- Encourage knowledge sharing among teams about effective prompts and techniques.

**7\. Cultural Shift**

- Address any concerns about AI replacing jobs; emphasize that AI is a tool to enhance productivity and reduce toil.
- Celebrate successes and share case studies within your organization.
- Encourage a culture of experimentation and openness to new technologies.

**8\. Measuring Success**

- Track critical metrics: time saved, increase in test coverage, reduction in bugs.
- Gather qualitative feedback on developer satisfaction and productivity.
- Regularly report on ROI to stakeholders.

### _Already using AI in your engineering org? Start measuring the impact with_ [_Copilot Dashboard from Jellyfish._](https://www.jellyfish.co/solutions/jellyfish-copilot/)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified