---
url: "https://jellyfish.co/blog/ghost-engineers/"
title: "Are 10% of Devs Actually \"Ghost Engineers\"? Not Likely. - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/ghost-engineers/#content)

![blog-ghost-engineers](https://jellyfish.co/wp-content/uploads/2024/12/blog-ghost-engineers-1.webp)

![](https://jellyfish.co/wp-content/uploads/2023/08/Jellyfish_Blog-Author-Headshots_Glenn-Barnett.webp)

Glenn Barnett

January 16, 2025

_**Editor’s Note:** This article first appeared in The Current, Jellyfish’s LinkedIn newsletter. You can subscribe for monthly updates and articles like this one [here](https://www.linkedin.com/newsletters/the-current-7201988628695130112/)._

_“I’m at Stanford and I research software engineering productivity. We have data on the performance of >50k engineers from 100s of companies… Our research shows: ~9.5% of software engineers do virtually nothing: Ghost Engineers (0.1x-ers)”_

That was the [hot take](https://x.com/yegordb/status/1859290734257635439) posted by Yegor Denisov-Blanch last month. The claim was inspired by an [earlier tweet](https://x.com/deedydas/status/1858929066264379629) from Deedy Das, a principal at Menlo Ventures, which asserts that there are “so many software engineers” who “make ~2 code changes a month and work <5 hours/week.”

Yegor Denisov-Blanch is one of the paper’s authors. The research, which isn’t peer reviewed, aims to build a model that can automatically rate code based on a number of dimensions including time required to produce, quality, maintainability, and other attributes. The researchers built the model using a small dataset: 70 commits of Java source code by 18 engineers, and trained the model to automatically grade those 70 commits similar to how a recruited panel of Java experts did.

The model achieved correlations as high as 0.86 on dimensions such as “time required to produce the Java commit” and correlations as low as 0.30 on dimensions such as “code maintainability.” They noted that a larger dataset – 1.73 million commits from 50,935 engineers – was used to guide the research, but apparently not to train the model itself. Neither the paper nor the researcher’s tweet describe a methodology, but the researcher concludes that roughly 4,800 of those 50,935 engineers (9.5%) have the performance of “<0.1x median engineer.”

That’s a big claim with big implications for engineering organizations. It’s also wrong – here’s why.

## Flawed claims and flawed data

Jellyfish has worked with thousands of software teams over the years, and we’ve learned a lot about the benefits and perils of measuring system data like commits.

- **Never assume you’re seeing the total picture** of a developer’s efforts. There are often other repos that are outside the scope of your access, and multiple accounts can express the actions of a single person (for example due to inconsistent git –config). Pair programming can also make it look like the work of a pair is coming from just one developer.
- **Commit patterns vary based on the role** of the individual. Many devs grow into hybrid “player/coach” roles – jobs whose primary responsibilities aren’t about making commits every day. These folks are involved in designing and configuring architecture and infrastructure or leading and mentoring teams. These engineers often stay connected by doing a few commits every once in a while, but it would be foolish to make assertions about their value based on that one metric alone.
- **Commit cadences vary widely** by individual style and also by the nature of the work. Some folks ship multiple PRs per day, often with multiple commits per PR. Other folks work on longer running tasks, and may make just a single commit at the end of the week or sprint. Still others may be squashing commits on the branch in order to yield a cleaner changeset. All these phenomena can yield commit shapes that are not representative or indicative of time spent coding.
- **The paper’s 70-commit model is too limited** to be useful for more general assumptions. These “severe limitations” are acknowledged by the paper’s authors – they also recognize that their focus on Java commits limits the applicability of their insights to other programming languages and technologies.

## Why “ghostbusting” is a trap for engineering teams

The original tweet – arguing that nearly 10% of engineers are “ghost engineers” – can set engineering managers’ minds racing. Can they identify the 10% of their team that isn’t contributing anything? Can they save resources by letting those engineers go? What do we need to go ghostbusting?

Starting a “ghost hunt” in your organization is a recipe for disaster – one that will likely leave a toxic aftermath for years. Using system data to identify folks who “aren’t contributing enough” will destroy trust among your team and accelerate burnout as engineers over-index on gaming metrics to prove they’re making an impact. That burnout leads to increased turnover, resulting in staggering costs to recruit replacements. According to [McKinsey](https://www.mckinsey.com/featured-insights/sustainable-inclusive-growth/charts/the-cost-of-unhappy-workers), “worker attrition and disengagement cost median S&P 500 companies about $282 million annually.”

Relying solely on system data to make judgments about individual engineers does not lead to good outcomes. Engineering contributions come in many different shapes, sizes and frequencies – not to mention coding languages.

While there are no doubt individuals out there who are attempting to get paid for no work or to be deceptive in their actual contributions, these folks aren’t the norm, and definitely aren’t 10% of your team. The best way to understand whether and where this might be happening is by listening to your teams.

## How to actually measure engineering effectiveness

So how should an engineering leader measure developer performance? Here are some tips:

- **Be clear about role expectations.** If you’re surprised by some devs delivering code changes infrequently, take a look at the other contributions they may be making. Are they involved in scoping and shaping work? Are they playing a key role in turning around reviews quickly? Are they mentoring more junior members of the team? If you know an individual’s expected code contributions are fractional, [engineering management platforms](https://jellyfish.co/platform/engineering-management-platform/) like Jellyfish allow you to formalize that role in the roster configuration so you don’t overindex on a subset of data.
- **Pay attention to how work output aligns with team mission.** If a team with a KTLO mission is spending more and more time on experiments and growth opportunities, engage the team to figure out why. The same holds in the opposite scenario when a growth-focused team hits an uptick in KTLO work. Contrasting the nature of the work being shipped with the stated mission of the team allows you to hone in on teams working in a way that’s not aligned with the organizational plan.
- **Keep an eye on Unlinked PRs.** If your devs are consistently shipping code that has no connection to ticket systems like Jira, then you have some problems in your [Software Development Lifecycle](https://jellyfish.co/blog/sdlc-best-practices/) (SDLC) process. This code is essentially “off the books”. Engage these teams on the need to and benefits of linking code changes to issue tracking systems.
- **Listen to your engineers.** It’s important to understand the qualitative [Developer Experience](https://jellyfish.co/platform/devex/) of your teams with periodic check-ins and surveys; give them opportunities to speak up if they feel like a teammate is unfairly dodging work and putting an undue burden on the rest of the team.
- **Above all, assume good intent on the part of your engineers.** Just because the metrics indicate inactivity, it doesn’t mean an engineer isn’t doing important work. The vast majority of engineers want to build software that helps the business – very few are trying to coast along under the radar.

Engineering productivity is important, and managers have a responsibility to ensure their teams are doing good work. But chasing ghosts and looking for scapegoats is never a good solution for boosting performance. If you really want to understand what’s going on in your engineering organization, follow the data and talk to the engineers themselves.

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish Kiro Integration](https://jellyfish.co/wp-content/uploads/2026/06/blog-Jellyfish-Kiro-1024x561.webp)](https://jellyfish.co/blog/jellyfish-partners-with-kiro-to-measure-ai-engineering-impact/)[**Jellyfish Partners with Kiro to Measure AI Engineering Impact**](https://jellyfish.co/blog/jellyfish-partners-with-kiro-to-measure-ai-engineering-impact/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-partners-with-kiro-to-measure-ai-engineering-impact/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified