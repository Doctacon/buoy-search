---
url: "https://jellyfish.co/blog/what-data-from-20-million-pull-requests-reveal-about-ai-transformation/"
title: "What Data from 20 Million Pull Requests Reveal About AI Transformation - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/what-data-from-20-million-pull-requests-reveal-about-ai-transformation/#content)

_**Editor’s Note:** The following is a talk from [AI Engineer Code Summit](https://www.ai.engineer/code) given by Jellyfish’s Head of Research, Nicholas Arcolano, Ph.D. In this talk you’ll learn:_

- _What “good” AI adoption looks like_
- _What productivity gains you should expect_
- _What some of the side effects are, and_
- _What you can do if your expectations are not matching your reality_

_You can watch the talk below or keep scrolling to read through a transcript. For more AI research and insights, visit the [Jellyfish AI Research Library here](https://jellyfish.co/research/ai-coding/)._

What Data from 20m Pull Requests Reveal About AI Transformation — Nick Arcolano, Jellyfish - YouTube

Tap to unmute

[What Data from 20m Pull Requests Reveal About AI Transformation — Nick Arcolano, Jellyfish](https://www.youtube.com/watch?v=WqZq8L-v9pA) [AI Engineer](https://www.youtube.com/channel/UCLKPca3kwwd-B59HNr-_lvA)

AI Engineer513K subscribers

[Watch on](https://www.youtube.com/watch?v=WqZq8L-v9pA)

**Transcript**

Hi, my name is Nicholas Arcolano and I’m the Head of Research at Jellyfish. Today I’d like to talk to you about AI transformation, specifically, what real world data can tell us about what’s actually happening in the wild. Now, a lot of AI native companies are being founded right now, and there are many more existing companies that are trying to transform themselves into being AI native.

I’ve talked to many folks from these companies and they all have the same big questions. Number one, what does good adoption of AI coding tools and agents actually look like? Number two, what productivity gains should I be expecting as we transform our team and the tools that we use? Three, what are the side effects of this transformation? And perhaps most importantly, if AI transformation isn’t delivering as advertised, what’s going on and what can you do about it?

Now at Jellyfish, we believe the best way to get answers is with data. So in the next 15, 20 minutes or so, I’m gonna give you some data backed insights from studies we’ve done to help you tackle these big questions.

Okay. Before we jump in though let’s take a minute to talk about the data behind the rest of the stuff in this talk. Uh, now at Jellyfish we provide analytics and insights for software engineering leaders. And to do this, we combine information from multiple sources, including usage and interactions with AI coding tools like Copilot, Cursor, Claude Code, interactions, with autonomous coding agents, things like Devon and Codex, as well as PR review bots.

We also combine this with data from source control platforms like GitHub, so we can understand things about the actual code base, where the work is happening. We also pull in data from task management platforms, things like Linear or Jira. And that tells you about what the actual goal of the work being done is.

So for the rest of this talk, we’re gonna be looking at findings from a dataset with data like this across our customers comprises about 20 million pull requests. These were written and merged by about 200,000 developers from around a thousand companies. We’ve been collecting this data for more than a year. So today we’ll be looking at results that span from June, 2024 to the present. Okay.

So let’s dig in. Question one. What does good adoption look like? Well, let’s start with lines of code. I don’t think this is a great metric, but it’s one we all hear about in the media a bunch. So it’s worth talking about.

Here’s data from a cohort of companies we’ve been tracking since June of last year. The purple bar represents the fraction of those companies that are generating 50% or more of their code with AI. So if you look at that purple bar. You can see that starting last summer, only about 2% of these companies were generating 50% or more of their code with AI.

But you can see this has been steadily growing, and as of last month, among these same companies, now nearly half are generating 50% or more of their code with AI.

Now, I think a more useful thing to look at actually is developer adoption because. This gets at the actual behavior change that you wanna see in your team. It’s also the thing I’ve seen that correlates most directly with good productivity outcomes, and we’re gonna talk about this a lot more later. But first we define an AI adoption rate for developers by computing the fraction of time that they use AI tools when they code. So, a hundred percent for developer, that means you’re using AI tools every time you code. A ompany’s adoption rate for the whole company that’s just the average of the adoption rates for all their individuals. So a hundred percent for a company means that every developer is using AI every time they code. So what you see here, this is a plot of the 25th 50th and 75th percentile of company adoption rates, uh, by a week for the developers and companies that we’ve been tracking.

And if you look at the AI adoption rates as of last summer, you can see the median adoption rate was around 22%. So, median company developers are using AI 22% of the time that they code. It’s grown steadily since then. Today, we’re seeing median adoption rates close to 90%. Now, if you’re like me and you’re using multiple tools constantly in parallel, both synchronous and asynchronous modes, you’re, you’re at a hundred percent. It might seem crazy to you that not everyone else is at a hundred percent. However, the reality is that for many teams, there are still real technical, organizational, and cultural barriers to adopting these tools more completely. So that brings me to my final point on adoption.

You might ask, what about autonomous coding agents? Now, the results I’ve just shown you, those are overwhelmingly from interactive coding tools, things like Copilot, Cursor, Claude Code. Now, we know that these tools all have interactive agentic modes, but what about your, your kind of true, fully autonomous agents like your Devons, your Codex, maybe you’re using agents like these or something else to go to effect, or maybe you haven’t really gotten going with autonomous agents yet.

It’s fine, you know, wherever you are in your journey. But if, if it feels like you’re slow going, getting off the ground with autonomous agents, I’m here to tell you you’re not alone. So in our dataset, we only see about 44% of companies have done anything with autonomous agents at all in the past three months.

The vast majority of that work is what you’d consider trialing and experimentation type stuff, like not full scale production. And ultimately it all amounts to less than 0.2% of the millions of PRs that were merged over that timeframe. Uh, so, you know, still very early days. All right, let’s move on.

And I’d like to talk about productivity. So even though autonomous agents aren’t yet delivering at scale, we’re still seeing big gains from adoption of interactive coding agents. So let’s talk about what we’re seeing. First though, what do we mean by productivity? This can be a very loaded term. Kind of squishy, overloaded. There’s many ways to attack it. A good place to start though is plain old PR throughput. How many pull requests does the average engineer merge per week? Not the most exotic metric, but it’s proven, it’s widely accepted. Do note that the absolute level of PR throughput is something that varies, right? It depends on. Things like how you like the scope work. It actually also depends on your architecture and put a pin in that, ’cause we’re gonna talk about that more later. However, measuring the change in PR throughput especially to keep all these other things constant, measuring that for your team is a good way to track productivity gains.

Another good one cycle time. You know, lots of different ways to define that one. But basically the latency or lead time to code getting deployed. For our purposes, we’ll take each PR and we’ll measure the timeframe from the first commit in the PR until it was merged.

Okay. So here’s what we’re seeing for changes in PR throughput, and let me explain this chart. Every data point here is a snapshot of a given company on a given week. The x axis is the company’s AI adoption rate that we discussed earlier. The y axis is the company’s average PRs per engineer that week. So you can see here a clear correlation between AI adoption and PR throughput. The average trend here is about a two x change as you go from zero to full adoption. So on average a company should expect to double their PR throughput if they go from not using it at all, which not really anybody’s doing anymore to a hundred percent adoption of AI coding tools.

Now we also see some gains in cycle time. So more work is happening and it’s happening faster. This is similar to the previous chart, but now in the Y axis we’re looking at median cycle time for PRs merged each week instead of PR throughput. This is a cool chart. As an aside, I like the cycle time distribution because you can see these two clear bands horizontally. So that lower horizontal cluster that corresponds to tasks that take less than a day, and then you see sort of a valley, and then there’s a band in the middle for tasks that take about two days. Then there’s a long tail of stuff going up. The wax is it takes much longer. I’ve truncated it here because as we all know, some things can take quite a while to, to get merged. Um, but you know, what’s exciting here is the average trend is a 24% decrease in cycle times as you go from 0% to a hundred percent adoption of AI coding tools.

So big picture, this is good news for productivity gains and maybe you’re seeing these things in your own organization, but what about the side effects? We all know there’s no free lunch, so what other things change as you go through an AI transformation? Well, one thing we’ve observed is that PRs are getting bigger. So here’s a plot, like the previous ones I’ve showed, except now the y axis is PR size. So, on average, teams that have fully adopted AI coding tools are pushing PRs that are 18% larger in terms of net lines of code added. Now that size change is due much more, you know, when I say net, it’s due more to additions than deletion. So that means that the combined change is primarily coming from net new code, not necessarily just, you know, fully rewritten or heavily reworked code. Another kind of interesting detail. Is that the average number of files touched is about the same. So this change is more about code that’s, it’s more thorough or maybe just more verbose. But it’s not the case that AI is touching more files and changing code in more different places in the code base. It’s largely happening within the same files.

Well now if teams are pushing more PRs and writing, emerging them faster and the PRs are getting bigger, then you might be wondering about quality. So are we seeing effects on quality as we use more AI and push code faster? Well, right now the answer is not really, we’re not really seeing any big effects. We’ve looked at bug tickets created and we looked at rates of PR reverts code that had to be rolled back, and we haven’t found any statistically significant relationship with the rate of AI adoption.

Interestingly, we have found increases in the rates of bugs resolved. When you dig into the data, you find this has become, teams are disproportionately using AI to tackle bug tickets in their backlogs. So you see a lot more bug tickets being addressed by AI, but not necessarily being caused by AI.

This makes sense. You know, bugs are often well scoped, verifiable tasks that AI coding tools can be set up well to succeed at. And we’re seeing a lot of people having success throwing AI at those kinds of tasks. But basically there’s, there’s no smoking gun on quality yet, though, you know, we’re gonna keep digging in here, especially as usage of asynchronous agents grows.

All right, last question. What if what you’re seeing at your org doesn’t align with the kind of results we’ve been talking about here so far? You know what if you’re listening to this and it is just not your reality. Well, I think I’ve made it clear so far that the most important thing to focus on first is adoption.

You’re not gonna see gains until you get folks using these tools at scale. I think that’s common sense, but maybe you are seeing high adoption. And you’re still not seeing the kind of productivity gains that all your friends on LinkedIn are crowing about. So what’s going on? Well, we’ve looked at a lot of things here and there’s plenty more to investigate, but I’d like to share one that’s particularly interesting and that’s code architecture.

By code architecture what I mean is how are the code for your products and services organized across your repositories? So, think about code being organized into mono repos versus poly repos, and that arrangement of your code it could be indicative of monolithic services versus microservices. It could be the difference between a centralized versus a more federated product strategy. And the way that we actually measure this, you know, one key metric for understanding it is active repos per engineer. This is actually a pretty straightforward one. It’s just how many distinct repos a typical engineer pushes code due in a given week.

One really cool thing about this metric is that it’s scale independent. So it turns out that, you know, by computing is per engineer, normalizing by the number of engineers you remove any correlation with the size of, of the company, with the size of the team. So in other words, this metric, it tells you something about the shape of the code that your engineers have to work with on a daily, weekly basis. And it tells you that regardless of how big your company is.

So, you know, this metric that, that I’m introducing here, this is what the distribution of that metric looks like. Here’s a probability distribution across the companies in our study. The more centralized architectures you can see on the left. Then there’s a long tail of highly distributed architectures to the right and then more balanced architectures, you know, balanced and lightly distributed line between these two extremes. So we’ve got these four regimes as you increase the active repos per engineer.

So, you know, here’s where it gets really interesting. So remember those two X gains and PR throughput that I showed you before? Here’s a flashback. Remember this? Well if we take this plot, you know, take all these data points, all these different companies, and you segment on this active repos per engineer. We’ve got, you know, four different regimes that we can do this analysis in.

So we’ve got centralized, balanced, distributed, and highly distributed. And if we perform that same analysis, we see big differences. So looking at that top row, you can see centralized and balanced code architectures. They trend more like four x, not like two x. So they’re doing much better than the average and the distributor architecture there in the the lower left hand corner in the teal that, that looks more like that global two x trend that we see when you look at all the data. What’s really interesting is this highly distributed case. There’s essentially no correlation here between AI adoption and PR throughput. And actually the, the weak trend that does exist is actually slightly negative.

So what’s going on here? Like, why are teams of highly distributed architectures struggling? They don’t seem to be getting real gains, at least not on average from AI. Well, a big part of what you’re seeing here is really the problem of context. So most of today’s tools are really set up best to work with one repo at a time.

You know, we’ve used these, you know, you, you pick a repo and you dive in and combining context across repos, it’s often challenging. It’s challenging for humans as well as for coding tools and for agents. Moreover, the relationships between these repos and the systems and products they relate to, they’re often not even written down very clearly. They might be largely locked in the heads of senior engineers. They’re definitely not accessible often to coding tools and agents. So it’s gonna take some time for, for teams to invest in the context engineering that’s needed here. It’s an interesting challenge and it especially, you know, in light of the fact that, uh, a lot of folks are saying, you may have heard this too, that microservices are the right way to go for a native development. So I could see a world certainly where we solve these context challenges. We adopt autonomous agents at scale, they’re set up for success, and this whole thing flips and this highly distributed category becomes the most productive way to do things. But right now, this is what we’re seeing.

As an aside, another thing you may notice here is that all of these distributions, they, you know, as you go from the most centralized to most distributed. These PRs per engineer shifts upward. You know what’s happening is the absolute number of repos increases as architectures get more distributed, basically in a highly distributed architecture.

It just takes more PRs overall to get things done due to things like migrations, cross coordination. And I bring this up because this is one of the many reasons why counting PRs in the absolute sense isn’t, isn’t a great metric. You really need to be tracking change in PR throughput to understand productivity because these things vary due to to factors like architecture choices.

Okay, so that’s it. To recap, you know, probably not news to anyone watching this, but AI coding tools are being used in a big way. Autonomous agents, though not so much, it’s still early days. Uh, we’re seeing big productivity gains with mo more code being shipped and faster, even though you’re using is interactive AI coding tools like Copilot, Cursor and Claude Code.

You feel like maybe, you know, you’re not, uh, as up on agentic, you know, fully autonomous agentic coding as you ought to be to exchange of PR throughput, should be your, your expectation. You should, you should be seeing that or more. But also you should expect bigger PRs. But maybe we can all ease up on some extreme quality anxiety.

Like we wanna keep an eye on that, but we’re just not seeing big issues there. At least not yet. And finally, there are a lot of reasons why your mileage may vary, and we’re gonna continue looking at this, but one place you can start is to think about your code architecture, how it might be holding you back, what you can do you know to compensate for some of the context limitations you have, and ultimately try to unlock some of those, the sweet AI productivity gains.

So, that’s it. That’s all I’ve got. I’m Nicholas Arcolano, Head of Research at Jellyfish. Thank you so much for listening.

About the author

![Nicholas Arcolano](https://jellyfish.co/wp-content/uploads/2026/01/Nicholas-Arcolano-Edited.jpg)

Nicholas Arcolano, Ph.D. is Head of Research at Jellyfish where he leads Jellyfish Research, a multidisciplinary department that focuses on new product concepts, advanced ML and AI algorithms, and analytics and data science support across the company.

Follow: [LinkedIn](https://www.linkedin.com/in/arcolano/Nicholas%20Arcolano,%20Ph.D.)

## Dive Deeper with Jellyfish Content

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

[![Jellyfish MCP Updates](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-MCP-Updates-1024x536.webp)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)[**Product Update: The Jellyfish MCP Is Now Documentation-Aware**](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/jellyfish-mcp-documentation-aware/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified