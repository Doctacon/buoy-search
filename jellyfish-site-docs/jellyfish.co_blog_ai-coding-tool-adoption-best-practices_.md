---
url: "https://jellyfish.co/blog/ai-coding-tool-adoption-best-practices/"
title: "Guiding AI Coding Tool Adoption with Intention: Best Practices for Engineering Teams - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/ai-coding-tool-adoption-best-practices/#content)

In this article

We’ve all seen the landscape of Software Engineering undergo a transformative shift due to the rapid adoption of AI and Large Language Models (LLMs). While these innovations have revolutionized workflows for many already, not all engineering teams have experienced their full potential – yet.

As an engineer at Jellyfish, I’ve witnessed firsthand how thoughtfully introducing [AI coding tools](https://jellyfish.co/blog/best-ai-coding-tools/) can significantly elevate team productivity and alignment. Drawing from our own journey, I want to share concrete strategies and lessons learned, enabling you to thoughtfully plan and execute your team’s AI adoption strategy.

## How Jellyfish Approached AI Adoption

Our curiosity about tools like GitHub Copilot started with two basic questions: what could they do for our internal engineering processes, and could we see their impact directly inside of Jellyfish? A handful of engineers (myself included) wanted to answer these questions as quickly as possible, and so we began to explore the landscape of AI-native developer tools.

Recognizing the immediate need for security and compliance, leadership collaborated closely with our security team to ensure safe and approved adoption. This early partnership enabled us to rapidly integrate and deploy AI coding tools to a few developers at first, with the intent to scale up as needed. Because we were building the dashboards that would show the impact of AI on productivity metrics and issue lifecycle, we got a front‑row seat to watch those numbers change in real time, and that gave us the confidence to keep scaling.

We started by pairing a handful of engineers with our security team to run small demos of Copilot and other AI assistants. From those demos, we spun up a living playbook, housed in our internal Confluence space. This guide walked every engineer through installing the IDE or plugins required, authenticating their license, and getting to work with AI-native tools. We invited newly onboarded members to keep the document up-to-date to ensure the instructions remained accurate and relevant. Alongside the playbook, we held a few focused round-table discussions where engineers from frontend, backend, QA, and DevOps shared how they were using AI in their day-to-day work. We also wove AI assistance into our code review process, trying out Copilot reviews and pointing out instances where AI-generated code was clever (or fell short).

![How to request Copilot access](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/05/Confluence.png)_One of our Confluence Documents for newly onboarded users, detailing how to request a Copilot license._

Furthermore, understanding that engineers interact with AI in varied ways, we worked with security to adopt cloud-hosted language model APIs and acquire Gemini for our Google Workspace, providing a wide range of compliant tools. We also created digital communal spaces, like dedicated Slack channels, for conversations around AI adoption and related news, effectively creating a champion network. At Jellyfish, our approach has been deliberate but agile, always keeping security and quality top of mind as we scaled adoption across the team.

A Practical Formula for Adoption

## A Practical Formula for Adoption

While initial enthusiasm for AI is a valuable starting point, embedding these tools deeply within an engineering team is typically a more gradual process. Drawing from our own journey at Jellyfish, we’ve developed a structured approach that your organization can adapt to thoughtfully navigate AI adoption and cultivate lasting success.

Here’s how we did it:

### 1\. Rally Executive Support

Getting your leadership team curious is the most important first step. Begin with a concrete story that illustrates real impact. For executives, think of AI as a strategic lever for faster delivery, cost efficiency, and happier engineers. Frame a small pilot with clear success metrics, perhaps a decrease in issue cycle time or happier qualitative [developer experience](https://jellyfish.co/library/developer-experience/) reports, and back it with a sandbox license budget. Host a lean AI Guild of a few folks who meet at a regular cadence to share prompts, surface quick wins, and feed insights back to you. Your visible sponsorship signals that this experiment matters and creates momentum for broader adoption.

### 2\. Start Small and Empower Advocates

For the pilot, begin with a small, enthusiastic group of “power users” who can become your internal champions. It’s best to choose engineers from different parts of the stack (backend, frontend, infra, etc.) who will offer good insights into diverse use cases. These early adopters can then help create accessible, practical guides. Given that early adoption experiences can differ significantly from one engineer to another, this internal documentation is essential.

![How to set up AI coding account](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/05/How-to-set-up-AI-coding-account.png)

_Detailed instructions on how to set up AI coding tools in a secure way helped boost confidence in our adoption process._

It should be thoughtfully developed to ensure AI is utilized in ways that align with your specific business needs, clearly outlining security protocols, compliance requirements, and effective, approved usage patterns. To further support this initial phase, ensure the overall onboarding process for AI-forward IDEs and tools is as straightforward and well-supported as possible, minimizing friction and encouraging exploration within established guidelines.

### 3\. Baseline Sentiment and Continuous Feedback

Before widespread rollout, it’s essential to establish a baseline for your team’s sentiment toward [AI coding tools](https://jellyfish.co/blog/best-ai-coding-tools/). This baseline allows you to qualitatively measure the effectiveness of your adoption strategy. A Developer Experience survey tool – such as [Jellyfish DevEx](https://jellyfish.co/platform/devex/) – makes it straightforward to gauge engineers’ initial feelings about these new technologies.

![AI DevEx survey](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/05/AI-DevEx-survey.png)

_Measuring the sentiment around AI tooling can help you determine the success of your adoption org-wide._

By starting with a clear understanding of real concerns rather than assumptions, you can proactively address actual barriers to adoption. Sending the same survey periodically after rollout enables you to track evolving attitudes, demonstrating progress and highlighting areas for improvement. Complement this practice with regular pulse surveys, perhaps asking, “Did this tool save you time this week?” to continuously refine your approach, ensuring ongoing alignment and measurable success.

### 4\. Clear Policies and Curated Resources

It’s important to define clear, accessible policies for how AI tools should be used, especially when it comes to security, licensing, and data privacy. Giving your team a simple, one-page policy on AI usage can remove a lot of guesswork. Outline what data is safe to include in prompts (public schemas, mock data) and what should stay out (customer PII, proprietary algorithms), note any licensing or attribution requirements, and remind everyone that all AI-generated code still needs a human review. Pin this policy in your docs site or central wiki so it’s always one click away.

![AI coding resource index](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/05/AI-coding-resource-index.png)

_Maintain a Resource Index in your knowledge base for highly visible AI policies and best use practices._

Alongside the policy you can offer quick-start resources that make experimenting smoother. A “Cheat Sheet” with approved prompt patterns, a short FAQ on common security concerns, and a dedicated Slack channel or office-hours drop-in with your security partner are all low-effort ways to give engineers on-demand guidance.

> When people know exactly where to look for answers, they feel safer trying new tools, and your security team stays in the loop without slowing anyone down.

### 5\. Integrate AI into Daily Workflows

Make it easy for engineers to try these tools in the natural flow of their work. This can start with your AI guild or early advocates creating clear “Getting Started” guides tailored to each environment your developers use, whether that’s VSCode, JetBrains, or Cursor, to help new users ramp up quickly. Focus your rollout on the workflows where AI tools will have the biggest impact, such as code generation and code review, as these are moments where well-integrated AI support can drive immediate, meaningful change. Even small nudges, like targeted reminders to groups of non-adopters, can go a long way in encouraging initial exploration.

### 6\. Wide Variety of Access Points

Provide a wide variety of access points for interacting with these tools. Recognize that not all engineers want to talk to LLMs through an IDE; sometimes there are questions that belong outside of code context, or a desire to run personal workflows on data from various sources. Work with your security team to adopt cloud-hosted language model APIs and other AI-powered workspace tools to give your team a range of options, all within a security-compliant environment. The more tools you provide your colleagues, the more room they have to experiment.

### 7\. The Champion Network

Once there are many high-touch individuals all using AI tools in your engineering department, it makes sense to have a few digital communal spaces where they can collaborate and share things related to the field. At Jellyfish, we have several Slack channels dedicated to conversations around AI adoption, AI-related news (like model releases and research studies), and more. The stronger this network is, the more you’ll drive conversations around how your organization can innovate and adopt new technologies related to AI. Moreover, these channels  serve as a critical, real-time feedback loop to leadership and any dedicated AI strategy teams, highlighting successes, surfacing grassroots innovations, and pinpointing areas where the broader adoption process could be refined or better supported.

Navigating the Side Effects of AI Adoption

## Navigating the Side Effects of AI Adoption

As with any major shift in tooling or process, AI adoption introduces new patterns; some anticipated, others less so. While the benefits are often immediately visible, it’s just as important to proactively manage the subtler, longer-term side effects that can emerge once these tools become part of everyday development work.

### Reviewing AI-Generated Code

You’ll likely see more AI-assisted code popping up in pull requests, and that’s a good thing! It’s a chance to subtly adapt your review dynamics while holding onto your core engineering values. The key thing to remember is that the engineer who commits the code is always accountable for its quality, security, and functionality, whether an AI lent a hand or not. Instead of implementing  mandatory ‘AI-generated’ labels for your PRs, simply foster an awareness among reviewers that AI tools are now a common part of a developer’s toolkit.

What’s crucial is that your code review process stays rigorous. Every piece of submitted code, no matter how it started, needs a thorough check for correctness, maintainability, and how well it aligns with your standards. If a particular section of code prompts questions, the review is the perfect time for a conversation with the author to understand their approach. This kind of collaborative scrutiny helps ensure all code is well-understood and seamlessly integrated, neatly avoiding informational blindspots without needing any extra flags.

### Creating Opportunities for Mentorship

As the gap between idea and implementation narrows with AI, there’s a real need to design systems that preserve foundational learning. Mentorship becomes more important, not less. It’s worth creating intentional opportunities through pair programming, design reviews, or structured onboarding for junior engineers to explore the “why” behind the work, not just the “what.” The goal is to ensure that AI is an accelerant instead of a shortcut. While AI tools are typically great at solving hyper-local problems, they can inadvertently erode system-level coherence, tending to optimize for the file or function rather than the broader architecture.

Senior engineers play a critical role here, both through mentorship and regular architectural reviews. During code reviews of AI-assisted work from junior team members, more senior engineers should foster a dialogue, asking questions about why a particular AI-suggested solution was chosen, what alternatives were considered, and the potential trade-offs involved. You might also institute workshops or shared learning sessions focused on effective prompting techniques for deep understanding and exploration. The overarching goal is to ensure that AI serves as an accelerant for skill development and comprehension, rather than a shortcut that bypasses foundational knowledge.

Considering these side effects early allows teams to guide adoption with intention. AI tools will influence how engineers write code, collaborate, and make decisions. By planning for that influence, teams can maintain the integrity of their engineering culture and ensure that their use of AI supports long-term technical and organizational goals.

Moving Forward

## Moving Forward

Adopting AI within an engineering team is not a single decision. Instead, it’s a series of choices that shape how your organization works and grows. Give your teams practical resources, and keep listening to find out what’s working and what’s not. As the tools improve, so will your understanding of where they fit and how they help. Engineering teams that approach AI adoption with focus and care will build stronger habits and better outcomes over time.

About the author

![Davis Keene](https://jellyfish.co/wp-content/uploads/2025/05/Davis-Keene.jpg)

Davis Keene is a Senior Software Engineer at Jellyfish. He has a love for learning and tackles complex systems and learns about the world through trial, error, and code.

Follow: [LinkedIn](https://www.linkedin.com/in/daviskeene/)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified