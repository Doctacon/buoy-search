---
url: "https://jellyfish.co/blog/case-study-does-copilot-make-a-difference-for-engineering-productivity/"
title: "Copilot Case Study for Engineering Productivity | Jellyfish Blog"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/case-study-does-copilot-make-a-difference-for-engineering-productivity/#content)

![](https://jellyfish.co/wp-content/uploads/2024/02/Bench-Copilot-Trial.webp)

![](https://jellyfish.co/wp-content/uploads/2023/04/Lena-Chretien.webp)

Lena Chretien – Jellyfish Research

February 05, 2024

**Our research found cycle time decreased by 5% but the time spent coding decreased by 11%, which shows a shift in the importance of coding towards code reviews. This has business and career implications for engineers who no longer need to code well but need to be able to understand and review code.**

At Jellyfish, we don’t believe productivity can be measured by simply counting PRs and lines of code. Instead, developer productivity is reflected in how well they can complete their responsibilities and how they impact the success of their team and their company as a whole. GenAI is redefining how we perceive productivity and over the past year, developers worldwide have continued to experiment and adopt AI-powered coding tools.

In particular, GitHub Copilot offers real-time code suggestions and contextual guidance, making it easy for engineers to improve their [productivity](https://www.jellyfish.co/library/engineering-productivity/) and efficiency. [Tools like Copilot will have a huge impact on the everyday lives of software developers](https://arxiv.org/abs/2406.07683), not just by increasing coding speed but also by improving workflows and job satisfaction.

GitHub has already published [surveys](https://arxiv.org/pdf/2302.06590.pdf) and [studies](https://arxiv.org/pdf/2302.06590.pdf) pointing to the impact of Copilot in controlled environments. However, we have seen less research regarding how Copilot is changing engineering work with real data from live deployments. Other perspectives from GitClear, point towards the potential for “AI-induced tech debt.”  [Leading VCs](https://twitter.com/edsim) are [speculating the implications](https://www.geekwire.com/2024/new-study-on-coding-behavior-raises-questions-about-impact-of-ai-on-software-development/) of all this newly AI-generated code: Larger surface area creates risk, more code review and more sloppy code”.

In Q4, we conducted a one-month study in collaboration with with the engineers at [Bench](https://www.bench.co/) — an online bookkeeping service and Jellyfish customer. Using Jellyfish data, we were able to investigate the changes that Copilot brought on both an individual level and an organizational level.

For both individuals and the organization, we established four hypotheses regarding changes we expected to observe due to integrating Copilot into engineering workflows. Using Jellyfish data (i.e. metrics, coding time, [life cycle explorer](https://www.jellyfish.co/platform/life-cycle-explorer/)) and internal Jellyfish analysis (i.e. context switching, flow time), as well as our Jellyfish [DevEx surveys](https://www.jellyfish.co/platform/devex/), we could investigate these hypotheses in the context of Bench’s engineering operations.

Granted this is a data point of one.  Our early read is that developer happiness goes up. And more strategic and creative work will have to happen on the front end of an initiative.

![](https://lh7-us.googleusercontent.com/novTxmCfafgP_LAtpkLXA2N5XhmGlA_Y_zd_hutVrqg9rnLsLbjRe0Ggtl16Zp00XyLvOO5nKcbs6EbzEjpXDycMyN50mc8I090x8vJyYG-nBFXq3YCEu5x5NikjN1RrPwfDYkEkhgik6J92XYsWb48)![](https://lh7-us.googleusercontent.com/BXBkqD5eFBnuR5jY6DJHtDVIc8lv6CCUbA7kveGPh6SPCx1ozyNryFUha53x3uX24p2c6CIY4Eakjz8yJxcAyKidhan8L9_iuwzVdgzJdfMcdG6Fsg0R8f89COdhYuJUVqk-CiqjyZwIPSD7LqoednA)

##### **Bench’s Copilot trial**

Bench rolled out Copilot to all active engineers, and they were encouraged to use Copilot for everyday tasks over a month-long period. We sent out a DevEx survey on the first day of the Copilot trial period to ask questions about general satisfaction and workflow; these answers provided us with a benchmark to compare the post-trial results. At the end of the month-long experiment, we sent a similar survey that included some questions about their use of Copilot.To test some of our hypotheses, we compared the month before the experiment to the month of the experiment.

Here are the biggest takeaways:

- _The perceived impact is more significant than we measured in the data:_ Bench’s engineering team reported a wide range of positive feedback after the experiment, stating that their work was significantly easier and more enjoyable. However, the reported results from the survey were less pronounced than the actual data observed in workflows and day-to-day signals — many of the changes we expected to see were more subtle in a real-life work environment than in GitHub’s controlled environments.

- _Coding time generally decreased:_ Bench’s coding time — the amount of time spent writing code per ticket — decreased by 11% during the month of the experiment. However, this decrease only applied to certain aspects of the work — coding time for tasks decreased by 40%, while time spent on bugs and defects saw no change. This reinforces our hypothesis that AI coding tools will have a more significant impact on repetitive tasks than bug work, which is highly codebase-specific.

- _Individual contributors found it easier to write code with Copilot and enjoyed their work more:_ Questions about [developer experience](https://www.jellyfish.co/library/developer-experience/) saw overwhelming positive feedback. In general, Bench engineers were 5% more satisfied with their work during the trial period. Engineers were particularly enthusiastic about the ease of writing code in the current environment, which saw survey scores increase by 9%.

- _PR review time and number of comments decreased:_ One of the most common assumptions when it comes to AI and coding is that developers will spend less time generating code and more time reviewing. The Bench experiment proved otherwise, as both PR cycle time and number of reviews decreased during the trial period. Additionally, the reviews were 3% more likely to feature positive comments than before the implementation of Copilot.

- _Effort spent in refinement increased:_ Software development can be divided into four phases — the definition and refinement period, in which work is planned and tickets are created; the work period, during which most of the code is written; the review period; and the deployment period. We expected there to be a shift regarding the periods in which developers spent most of their time, and we found that engineers were able to spend less time writing code and more time doing creative work during the refinement period.

##### **New hypotheses for an AI-enabled future**

It’s clear that Bench’s developers were more satisfied while using Copilot. But was the team more productive?

At Jellyfish, we don’t believe that productivity can be measured by simply counting PRs and lines of code. Instead, developer productivity is reflected in how well they can complete their responsibilities and how they impact the success of their team and their company as a whole. We can track this type of productivity by looking at the amount of context switching, focus/flow time, and perceived productivity towards product roadmap work. The post-experiment survey saw a 5% increase in perceived productivity.

But more importantly, the ability to work more effectively will leave more time for the important work that takes place before code generation — creative idea development and work refinement.

Will Copilot enable engineering teams to generate more lines of code? Maybe. But the Bench case study shows that it can already free up engineers to spend more time on planning and refinement, which will in turn result in more creative, innovative software solutions.

## Dive Deeper with Jellyfish Content

[![How to Align Product and Engineering to Drive Better Planning](https://jellyfish.co/wp-content/uploads/2024/12/blog-How-to-Align-Product-and-Engineering-2026-1024x561.webp)](https://jellyfish.co/blog/how-to-align-product-and-engineering-to-drive-better-planning/)[**How to Align Product and Engineering to Drive Better Planning in 2026**](https://jellyfish.co/blog/how-to-align-product-and-engineering-to-drive-better-planning/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/how-to-align-product-and-engineering-to-drive-better-planning/)

[![Jellyfish API](https://jellyfish.co/wp-content/uploads/2024/11/blog-Exploring-Jellyfish-Data-with-Amazon-Q-Business-1024x561.webp)](https://jellyfish.co/blog/exploring-jellyfish-data-with-amazon-q-business/)[**Exploring Jellyfish Data with Amazon Q Business: How we Leveraged Amazon’s GenAI Assistant and Jellyfish’s API to Gain In-depth Insights**](https://jellyfish.co/blog/exploring-jellyfish-data-with-amazon-q-business/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/exploring-jellyfish-data-with-amazon-q-business/)

[![Navigating Flux and Embracing Change_Jellyfish](https://jellyfish.co/wp-content/uploads/2024/08/blog-Navigating-Flux-and-Embracing-Change-1024x561.webp)](https://jellyfish.co/blog/engineering-management-in-2024-and-what-to-expect-in-2025/)[**Navigating Flux & Embracing Change: Engineering Management in 2024 and What to Expect in 2025**](https://jellyfish.co/blog/engineering-management-in-2024-and-what-to-expect-in-2025/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/engineering-management-in-2024-and-what-to-expect-in-2025/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified