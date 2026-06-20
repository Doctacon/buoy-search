---
url: "https://jellyfish.co/blog/when-is-it-going-to-ship-how-we-engineered-a-delivery-predictability-scoring-model/"
title: "When is it Going to Ship? How We Engineered a Delivery Predictability Scoring Model - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/when-is-it-going-to-ship-how-we-engineered-a-delivery-predictability-scoring-model/#content)

![](https://jellyfish.co/wp-content/uploads/2024/07/blog-When-is-it-Going-to-Ship.webp)

![](https://jellyfish.co/wp-content/uploads/2023/08/cropped-jellyfish-favicon.png)

Jellyfish Research

July 10, 2024

One of the most common questions software leaders are asked is, “When is it going to ship?” The answer is important for all sorts of reasons from coordinating marketing campaigns, keeping commitments to customers, and unlocking sales opportunities. The focus on dates creates an incentive for leaders to look for ways to measure and improve the predictability of their organization, however, software delivery is notoriously difficult to predict, and efforts to measure teams on their predictability risk promoting unhealthy cultures and incentivizing the wrong behaviors. We challenged ourselves to build a scoring system that rewards the behaviors that we believe lead to predictable delivery and want to share that with others who may be struggling with a similar challenge.

#### **Discovering No One Ships On Time**

The easiest way to start constructing a predictability score was to look at the number of deliverables shipped on time over the total number of deliveries. Having been part of teams doing estimation on big projects we know how challenging it is and we were suspicious of such a simple score providing a useful measure. To test it out we ran an analysis of over 25K deliverables produced by 3,600 teams on our platform. We found only 24% of deliverables with a due date were delivered “on time” and just 9% of teams delivered consistently on time.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXepy01ramOkFXU9SuQDQB-7Zm9Jo_dV0q-c0m9FSrN6WPJm92ayZqGTuNu-MeordtloMF8qKKvqYQL079WfvVoPFOeX_wNxrvgEQxRqXkN-IDb2UlKY4BbchrDBc6zLGfoDVq_WFKwJstOBB_KLnqgf5Y0t?key=tDzzMrd086QlG0hkeXa1Aw)

Looking at such skewed results led us to ask “Can predictability really be this bad for everyone?” and “How could this score eventually point to where to start improving things?” To make any progress a different way of looking at the data was needed.

#### **Reflecting on Past Delivery Lessons**

When we started thinking about building a better predictability score, we leaned heavily on our past experiences running software projects. Here are some of the common pitfalls we’ve seen:

- Committing to a date too soon
- Reluctance to change dates early
- Date thrashing (particularly late in the game)
- Big surprises at the end (missing by quarters)

We believe the first two pitfalls are the root causes of the second two. To avoid these pitfalls, we recommend teams to turn the first two around and:

- Focus on small timeboxed tasks at the start of a project to learn and de-risk so that you’re estimating and committing on the things you understand
- Change dates early based on what you learn along the way

#### **Building and Testing the Model**

Our second iteration on a predictability score factored in those pitfalls, by considering the difference between the actual delivery date and its estimation, along with when and how often the estimated delivery date was changed. (The specifics of how are detailed later in this post.) Led by our intuition we were eager to see how our hypothesis fared when presented with data from actual teams.

We calculated scores for over 4,350 teams on our platform. Teams are scored across a scale that runs from 0 (completely unpredictable) to 100 (perfectly predictable). We found that most teams had a predictability score that fell in the middle of the scoring range. About 10% (435 teams) of teams had scores that were in the 90th percentile, and 14% (610 teams) with scores in the lowest percentile.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeh_63i5PhwntnuZJ5YLt1hzHbXwvw_Zc020ooORKWbvpPeDBco7kEIQ2jeocfjxWknxMyeDWAtpnu3ss5iCC7WrwFAJnsIW0FENTbVoMLfRa2lk_XySowKQW4RMNa7v5_wNKpmHQlyTO_o4dh7NTtH6x5l?key=tDzzMrd086QlG0hkeXa1Aw)

Compared to the simple score (where virtually everyone is failing) the V2 score is more of a normal distribution where we can see the highly unpredictable outliers we need to engage and the highly predictable teams we’d want to reward and learn from. We get this clearer view as a result of focusing the score on a set of behaviors vs. a binary measure of the outcome hitting or missing a delivery date.

#### **Continuing to Improve Predictability Scoring**

Where do we want to take this next? We have a score that is good at identifying team behaviors around delivery management so our next step will be to analyze whether predictability scores are correlated with other team measures. For instance, we think there’s a lot of fertile ground in examining predictability scores and Developer Experience survey results. We’re also interested in understanding how we might understand the impact of predictability on a team’s velocity and productivity. There’s a lot to explore so stay tuned!

#### **Model Deep Dive**

Now that we’ve shared the motivations and the results we’ve observed from our model we’ll spend some time describing how the model is constructed.

Two factors are the base of our score:

- Did you deliver on time?
- How often and how much did the target dates change?

Let’s dive into both with a little more detail to highlight why they are important in understanding team predictability.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdiZv9g9yqs0o3Te87T8IUDjhOARF2JQgq7HcbYLFVdyf3K_vHgJoiJmtCBx0xZ_Zj5r0yZzyLx6V4fYU7bRqQiVzwYtpQXfZdqq4-296fTXz1JK67MeXoDx8UZmpSMHV_83_w060ulY33QQCE0DnSnocGs?key=tDzzMrd086QlG0hkeXa1Aw)![](https://lh7-us.googleusercontent.com/docsz/AD_4nXesGyiN71pa5gQTmy-eu635Er_Ra3GcXX906xM5V-rB29W6aV7dlGmeYNv4aWjs9mL4SVyWbtZFBuScsFd176FBCGpq9SBEzcILy9IjY0OLHHAbTzJKVTh1ucwBHKvqQqDEq6vxj2RXodu3CrTgCamPjrNt?key=tDzzMrd086QlG0hkeXa1Aw)

##### **Did you deliver on time?**

Delivering on time is, of course, the main focus here. Your team is expected to deliver on time. Looking at finished deliverables helps us understand how well you estimate and how wrong you were if your target date was incorrect.

To include this in our score, we look at the **average number of weeks** the team deviated from the target, early or late. The severity of time you are late/early depends on how long you planned your deliverable to be. Think about it: Being 2 weeks late for a 2-week deliverable is much worse than being 2 weeks late for a 12-week deliverable.

##### **How often and how much did the target dates change?**

Of course, the “how many weeks are you off target” metric is based on the _last set target date_. But what if you changed your target date many times over the lifespan of the deliverable?

Hence, we consider **how often you changed your target dates** as well as **when in your deliverable** you changed them and **how big they were**. In particular, changes made early are weighted less as are changes that are small compared to the length of the deliverable.

So, to do this, the model:

1. “Encourages” date changes made early.
2. Weighs changes by size so small, late changes are not counted as heavily as large late changes.
3. Allows a change or two, especially if the change is early or small. But doing this often and thrashing dates will be penalized.

#### **7 Learnings from Analyzing Predictability Scores**

When digging into the specifics of teams in the top and bottom quartiles of predictability scores, we learned the following:

1. Low-scoring teams estimate the time to delivery to be almost half as long as the teams with high predictability. Hence they assume their projects can be completed quicker than they are usually able to accomplish.
2. The low predictability teams have more pieces of work per developer included in the delivery. In other words, considering point (1) they plan **more work** but budget **less time!**
3. In addition, these teams also plan a huge amount of work very early leaving them little room to react to unforeseen circumstances. 2.5x times more tickets are never even started!
4. The high-scoring teams on the other hand add tickets for work almost uniformly throughout the lifetime of the deliverables adjusting and replanning as work progresses.
5. While delivering on time, teams with high predictability change their delivery dates almost three times less often than teams with low predictability.
6. Low-scoring teams not only change their target dates more often, they also do so more often late. In addition, those late changes are much larger than earlier changes, showing a sign of “oh-shoot” panic and date thrashing.
7. Highly predictable teams also make changes, however they are not only fewer, but also smaller (7x smaller on average). This shows that these teams are adapting to changing requirements, or unforeseen obstacles in a controlled and well thought out way.

#### **Recap: Ways Your Team Can Improve Their Predictability**

Planning is a necessary tool to estimate a target date, but committing too soon and not adjusting to the circumstances will lead to date thrashing late in the lifetime of a deliverable.

Not being able to adjust because of too much commitment too early might lead to reluctance to change dates early and date thrashing late in the game. Instead, teams that take time to plan, even when the original plan goes astray, before commiting to a new date will help teams to be more predictable.

With a focus on learning at the start of a project to de-risk and making date changes based on what is learned not only at the beginning but also during the lifetime of the deliverable will help teams structure their work better and be more successful.

Lastly, we see that teams with low scores in general have more deliverables in progress at the same time. Limiting the focus of a team on the most important deliverables will help them stay on track with their work and deliver on time!

![](https://www.jellyfish.co/wp-content/uploads/2023/04/Jellyfish_Blog-Author-Headshots_Lena-Chretien.png)

Lena Chretien, Senior Data Scientist at Jellyfish

![](https://www.jellyfish.co/wp-content/uploads/2024/07/Jellyfish_Blog-Author-Headshots_Jim-Krygowski.png)

Jim Krygowski, Director of Software Engineering at Jellyfish

## Dive Deeper with Jellyfish Content

[![Jellyfish Data Hub](https://jellyfish.co/wp-content/uploads/2026/04/blog-data-hub-featureV2-1024x561.webp)](https://jellyfish.co/blog/introducing-jellyfish-data-hub-flexible-curated-engineering-insights/)[**Introducing Jellyfish Data Hub: Flexible, Curated Engineering Insights**](https://jellyfish.co/blog/introducing-jellyfish-data-hub-flexible-curated-engineering-insights/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/introducing-jellyfish-data-hub-flexible-curated-engineering-insights/)

[![Jellyfish Integrations](https://jellyfish.co/wp-content/uploads/2025/12/blog-new-integreationsv2-1024x561.webp)](https://jellyfish.co/blog/new-data-integrations/)[**Jellyfish Offers Richer Engineering Insights With 25+ New Data Integrations Across Major Dev Tools**](https://jellyfish.co/blog/new-data-integrations/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/new-data-integrations/)

[![blog-g2-winter26-featured](https://jellyfish.co/wp-content/uploads/2025/12/blog-g2-winter26-featured-1024x582.webp)](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-winter-2026/)[**Jellyfish Tops G2’s Software Development Analytics Tools Grid 14 Quarters and Counting**](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-winter-2026/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-winter-2026/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified