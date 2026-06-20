---
url: "https://jellyfish.co/blog/does-ai-assistance-mean-engineers-are-doing-less-coding-work-maybe-not/"
title: "Does AI Assistance Mean Engineers Are Doing Less Coding Work? Maybe Not. - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/does-ai-assistance-mean-engineers-are-doing-less-coding-work-maybe-not/#content)

_Fiona Chen and James Stratton are Ph.D. Candidates in economics at Harvard University. They research the impacts of AI on the labor market._

How do AI coding tools affect the types of tasks that software developers complete? A significant amount of public discourse has examined this question. On the one hand, champions of the tools have argued they will [free](https://www.businessinsider.com/github-ceo-ai-lets-engineers-be-more-creative-2025-5) [up](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/unleashing-developer-productivity-with-generative-ai?utm_source=chatgpt.com) [engineers’](https://arxiv.org/abs/2406.17910?utm_source=chatgpt.com) [time](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/?utm_source=chatgpt.com) on more routine coding tasks, and allow them to focus their energy on more creative and complex tasks. On the other, critics have argued that AI coding tools have only led firms to increase demands for code output – leading to a transformation of software engineering into [“warehouse work.”](https://www.nytimes.com/2025/05/25/business/amazon-ai-coders.html)

In this post, part of our ongoing work with Jellyfish, we leverage the richness of data collected through the [Jellyfish platform](https://jellyfish.co/platform/jellyfish-ai-impact/) to study the effects on AI adoption on the types of work that software engineers do. Specifically, we use the text descriptions of roughly **17 million Jira issues from 500 client firms** that have opted into research. The Jellyfish data offer a unique window into the granular assignment of work within firms, allowing us to gain new insight into how AI tools have affected the structure of work.

Using machine learning tools, we extract a set of features from the text descriptions of these Jira issues:

1. **Task categories:** We categorize tasks into different forms of software engineering work, such as user interface change versus code refactoring.
2. **Skill demands:** We label each task according to three forms of skill demands – technical skill, executive decision-making skill, or collaborative skill.

Our machine learning method relies on two steps:

1. We begin by labeling a sample of tasks using a large language model (LLM). [\[1\]](https://jellyfish.co/blog/does-ai-assistance-mean-engineers-are-doing-less-coding-work-maybe-not/#_ftn1)
2. Then, we scale these labels to the entire dataset using a supervised learning approach. [\[2\]](https://jellyfish.co/blog/does-ai-assistance-mean-engineers-are-doing-less-coding-work-maybe-not/#_ftn2)

Using these labels, we begin by examining differences in AI’s productivity effects across tasks that are exposed to AI versus ones that are not. Here, we measure productivity as the percent of a worker’s monthly tasks completed within 10 days. We’ve grouped task categories into AI-exposed and non-exposed. We group these categories based on our interviews with software engineers and managers: we consider a task category to be AI exposed if it relies on coding, and minimally relies on knowledge of company-specific context (e.g., code refactoring or user interface changes); in contrast, we consider a task to be non-exposed if it does not require coding (e.g., an administrative task) or it requires more knowledge of company-specific context (security).

We plot the effect of firm-level AI adoption on this productivity measure for each task category. [\[3\]](https://jellyfish.co/blog/does-ai-assistance-mean-engineers-are-doing-less-coding-work-maybe-not/#_ftn3) **We observe that the productivity effects are larger for the AI-exposed tasks.**

![ai exposed tasks vs non ai exposed tasks](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/ai-exposed-tasks-vs-non-ai-exposed-tasks.png)

As AI accelerates the completion of coding tasks, an engineer’s day-to-day work could shift in different ways. On one hand, these tools might free up time for non-coding responsibilities, such as scoping projects, collaborating with teammates, or planning long-term strategy. On the other hand, faster coding could simply mean that engineers are assigned even more coding tasks, keeping their workload focused on writing software rather than broadening their role.

To disentangle these hypotheses, we test the effect of AI adoption on the percent of a worker’s tasks that are AI-exposed, with results displayed in the figure below. In the pre-AI period, 54% of a worker’s monthly tasks on average were AI-exposed. As a result of AI adoption, this share increases by 1 p.p. – providing evidence of the latter hypothesis.

![Effect on share ai-augmenting tasks](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Effect-on-share-ai-augmenting-tasks.png)

To make these task effects concrete, we characterize the types of skills needed in various tasks. In the figure below, we display the share of non-AI exposed tasks that require technical, executive, and collaboration skills in light blue, and the equivalent shares for AI exposed tasks in navy. We observe that AI-exposed tasks are more likely to require technical skills, less likely to require executive skills, and less likely to require collaboration.

![percent of tasks with AI](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/percent-of-tasks-with-AI.png)

Taken together, our findings suggest that AI coding tools are not shifting engineers away from routine coding toward higher-level strategic responsibilities. Instead, they appear to amplify demand for coding output.

This shift may not only have implications for engineers’ day-to-day experiences at work, but also for long-term job outcomes. For instance, this shift may narrow workers’ opportunities to demonstrate executive judgment or collaborative skill – traits that are often helpful for career advancement. For firms, the reallocation of work implies a persistent need for engineers that are capable of helping with these coding processes, rather than simply a shift towards senior or managerial workers, as has been predicted by many speculators. In short, AI adoption is not only reshaping productivity, but also altering the balance of skills that are most valued in software organizations.

It’s important to keep in mind that the use of AI in engineering is rapidly evolving. The conclusions here are focused on the impacts of **interactive** AI coding tools (e.g., Copilot and Cursor). Agentic (non-interactive) coding tools (e.g. Codex, Devin) may have vastly different impacts. The opportunities with AI appear to be endless, and only time and the data will tell where we end up.

[\[1\]](https://jellyfish.co/blog/does-ai-assistance-mean-engineers-are-doing-less-coding-work-maybe-not/#_ftnref1) Specifically, we label a 1% sample of tasks, stratified by company. We use OpenAI’s GPT 4o-mini model, which we access through Microsoft Azure. We classify each task into one of twelve categories: feature development, user interface, bug, refactoring or optimization, testing or validation, devops, documentation, code review, system architecture, project management, administrative, and security. Then, we label each task according to three types of skills: technical skill (whether a task requires technical knowledge), executive skill (whether the task draws on executive functioning – such as decision-making under ambiguity, planning, or foresight), and collaborative skill (whether the task requires coordination or communication with others).

[\[2\]](https://jellyfish.co/blog/does-ai-assistance-mean-engineers-are-doing-less-coding-work-maybe-not/#_ftnref2) This supervised learning approach takes two steps. First, to represent task descriptions numerically, we extract semantic embeddings using the Sentence-BERT (SBERT) model all-MiniLM-L6-v2, a transformer-based architecture designed for sentence-level encoding. This model maps each input into a vector of 384 fixed dimensions. Second, we train a feedforward neural network in PyTorch to predict the GPT-assigned binary labels from the SBERT embeddings. The neural network takes the 384-dimensional embeddings as input, then passes it through three layers of sizes 256, 128, and 64, each of which is followed by a ReLU activation. The final layer outputs a vector of logits for each of the 19 target labels. We use the Binary Cross Entropy with Logits Loss (BCEWithLogitsLoss) function as our loss function. We train the model over 30 epochs.

[\[3\]](https://jellyfish.co/blog/does-ai-assistance-mean-engineers-are-doing-less-coding-work-maybe-not/#_ftnref3) To calculate this effect, we run a regression at the worker-month level, of productivity (percent of tasks of X category) on the treatment variable (binary variable indicating whether a firm has adopted AI) and controls for worker and month. We define a firm’s AI adoption date as the date at which it begins using a business license for either of two interactive AI tools, GitHub Copilot or Cursor, as measured by Jellyfish’s integrations with the two tools’ APIs.

About the author

![Fiona Chen](https://jellyfish.co/wp-content/uploads/2025/09/Fiona-Chen.jpg)

Fiona Chen is a Ph.D. candidate in economics at Harvard University. She completed her B.S. in mathematics and economics at MIT. She researches the impacts of AI on the labor market.

Follow: [LinkedIn](https://www.linkedin.com/in/fionaychen/)

About the author

![James Stratton](https://jellyfish.co/wp-content/uploads/2025/09/James-Stratton.jpg)

James Stratton is a Ph.D. candidate in economics at Harvard University. Prior to coming to Harvard, he completed an undergraduate degree in economics at the University of Sydney. James researches the impacts of AI on the labor market.

Follow: [LinkedIn](https://www.linkedin.com/in/james-stratton-a1809b129/)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified