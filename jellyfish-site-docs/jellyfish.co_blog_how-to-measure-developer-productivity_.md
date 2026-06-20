---
url: "https://jellyfish.co/blog/how-to-measure-developer-productivity/"
title: "How To Measure Developer Productivity (+Key Metrics)"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/how-to-measure-developer-productivity/#content)

In this article

If you want to improve your engineering organization – whether it’s code quality, tech debt, or customer satisfaction – then you must first learn how to measure it.

On an individual or team level, you can evaluate the quality and quantity of output from a given engineer. How many lines of code did your team write? How many bugs did you catch during QA?

But if you want to evaluate the overall success of your software development team – and think through a realistic timeline for your product roadmap moving forward – you have to look at the big-picture metric: Developer productivity.

Can Developer Productivity Be Measured?

## **Can Developer Productivity Be Measured?**

**TLDR: Yes, but it’s complicated**. Measuring developer productivity isn’t as easy as counting lines of code or number of to-do’s checked off. Unlike other corporate functions that can be measured in one or two key metrics (like revenue or customer satisfaction), engineering teams often struggle to connect their creative, collaborative work to business outcomes.

Because of this, [**the idea of tracking developer productivity**](https://jellyfish.co/blog/can-you-measure-software-development/) is often met with resistance. Without thinking through the full picture of what productivity looks like – efficiency, alignment, and consistency – teams risk micromanagement or a focus on vanity metrics that don’t actually achieve business goals. Because development is such a collaborative process, factors outside an individual’s control, like missing requirement information, team dependencies, or a bloated backlog can all impact their performance.

Yes, it’s a complex, inter-connected process to bring a product from a wireframe to life through code. But you can measure this process in different ways, starting by defining what “a productive developer” looks like.

Broadly speaking, engineering teams focus on two types of tasks – what [**McKinsey**](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/yes-you-can-measure-software-developer-productivity) [**& Company**](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/yes-you-can-measure-software-developer-productivity) calls “inner loop tasks” like building and testing code and “outer loop tasks” like meetings and security/compliance work. The top tech companies aim for 70% of engineering time focused on these “inner loop” tasks.

When we think about measuring developer productivity, it’s important to take a thoughtful and balanced approach that focuses on outcomes and value delivery – so that the data you collect is used to motivate and support your team. The more they can focus on those “inner loop” tasks, the better.

In this piece, we’ll talk through how you can measure developer productivity in a holistic, nuanced way – and ways to improve your developer productivity once you have a baseline in place.

Which Problems Get Solved by Measuring Developer Productivity?

## **Which Problems Get Solved by Measuring Developer Productivity?**

Software engineering teams have a metrics problem (and not just because CEOs and CTOs increasingly demand answers beyond “it’s just too nuanced to measure.”) Your developer productivity is directly linked to the viability of the business – without developers, you don’t even have a product to sell – yet too many teams get distracted by aspects of development that are easier to define, like deployment dates. Instead, it’s about understanding the factors that drive performance, identifying bottlenecks, and creating a work environment where developers can thrive.

The benefits of measuring developer productivity include:

- **Align development with business goals:** No one likes busy work. Measuring developer productivity allows you to directly [**connect your efforts with real**](https://jellyfish.co/solutions/businesss-alignment/) [**business value**](https://jellyfish.co/solutions/businesss-alignment/) and allows you to more easily track your progress and create more predictable timelines – so you can better collaborate with your external stakeholders in product, marketing, or customer support.
- **Identify and address bottlenecks:** Map out your complete development workflow to see what points slow down your development team. Is your code review process inefficient? Are you spending too much time bug hunting manually instead of automating the process? Understanding your bottlenecks is the first step to streamlining your processes and determining how to better support your team.
- **Improve developer experience and morale**: You can’t support your team if you don’t know what’s impacting their well-being. Understanding how the team performs as a whole – and individual developer productivity – can help you motivate the team and prevent burnout. By making the entire process more transparent, you can celebrate the accomplishments of your high performers and better allocate resources to help the rest of your team catch up.

Without measuring your team’s productivity, you won’t be able to advocate for them with the rest of the organization or support individual developers by providing the resources they need. Knowing what is working and what’s not is the first step toward creating a culture of continuous improvement, where your engineers can get development work done quickly and efficiently.

![10 KPIs every engineering leader should track ebook](https://jellyfish.co/wp-content/uploads/2023/10/thumbnail-10KPIs-ebook.png)

#### 10 KPIs Every Engineering Leader Should Track

[Get eBook](https://jellyfish.co/resources/10-kpis-engineering-leaders-should-track/)

Key Developer Productivity Metrics to Track

## **Key Developer Productivity Metrics to Track**

It’s a longstanding joke in the engineering community that one of the best ways to get software engineers to argue (besides asking them whether it’s “GIF” or “JIF”) is to determine how to measure their work. The key is to avoid vanity metrics that emphasize quantity over quality and instead focus on data that [**reveals the health of your**](https://jellyfish.co/library/developer-experience/) [**developer teams**](https://jellyfish.co/library/developer-experience/).

The most effective approach is to use a combination of high-level outcome metrics and diagnostic flow metrics. Start by understanding your overall system health with the industry standard, then use a second set of metrics to drill down and diagnose the root cause of any inefficiencies.

### **DORA Metrics**

[**DevOps**](https://www.jellyfish.co/blog/dora-metrics-101/) [**Research and Assessment (DORA)**](https://www.jellyfish.co/blog/dora-metrics-101/) [**metrics**](https://www.jellyfish.co/blog/dora-metrics-101/) are the accepted industry standard for evaluating the performance of a software delivery lifecycle. They provide a balanced, high-level view of your engineering team’s output by measuring both speed and stability. Think of these as your primary health indicators.

- **Deployment Frequency** **(DF):** How often you successfully deploy code to production. Higher frequency generally indicates a more agile and responsive team.
- **Lead Time** **for Changes (MLT):** The average time it takes for a code change to go from commit to deployment. This measures the end-to-end speed of your delivery pipeline.
- **Change Failure Rate** **(CFR):** The percentage of code deployments that result in a failure in production. This is a critical measure of the quality and stability of your releases.
- **Mean Time** **to Recovery (MTTR):** The average time it takes to recover from a system failure or service interruption. This demonstrates your team’s resilience.

### **Flow Metrics**

While DORA metrics tell you what is happening, [**Flow**](https://jellyfish.co/library/agile-metrics/) [**metrics**](https://jellyfish.co/library/agile-metrics/) help you understand why. These metrics, often used in Agile methodologies, map the flow of work from start to finish and are the perfect diagnostic tools for investigating your DORA results.

For example, if your Lead Time for Changes (a DORA metric) is high, your Cycle Time (a Flow metric) is the first place to investigate.

- **Cycle Time**: The time it takes for a task to be completed, from the first commit to deployment. The real diagnostic power of cycle time comes from breaking it down into its component parts: Time to PR, Time to First Review, Rework Time, and Time to Deploy. This allows you to pinpoint the exact stage in your workflow that is causing delays.
- **Work-in-Progress (WIP):** The number of work items being actively worked on at a given time. High WIP is a leading indicator of context switching and is strongly correlated with longer cycle times.
- **Throughput** **:** The number of work items completed in a given time period (e.g., a week or a sprint). This provides a factual measure of your team’s rate of delivery.

By using DORA to monitor health and flow metrics to diagnose issues, you create a powerful, actionable framework for continuous improvement.

How to Improve Developer Productivity

## **How to Improve Developer Productivity**

Measuring your developer productivity is only the first step. Once you’ve established a baseline, it’s up to you and your team to work together to improve it. That might mean addressing complaints like wait times or team dependencies or implementing a completely new system for organizing and distributing tasks.

Here are a few ways you can help your teams become more efficient:

### **Optimize** **the Developer Environment**

Your developers are only as good as the tools they use. If you want to improve your developer productivity, start with the raw materials:

- **Fast hardware:** Make sure your team has access to the most up-to-date computers, multiple monitors, a fast and stable Internet connection, and enough memory.
- **Collaborative software:** Don’t skimp on the software your team uses to produce, document, and deploy your code, either. High-quality IDEs, debuggers, version control systems, and other collaboration tools streamline your workflow and make the process more measurable.
- **Automation** **wherever possible:** Routine tasks like testing and deployment free up your team for more creative and challenging work. Artificial intelligence can also give teams a boost by generating a baseline to work from (or noting errors ahead of any other testing.)

The best way to know what your software development team needs? Ask them. Most developers have strong opinions on their hardware and tools they use, especially if they’re more experienced. Use their knowledge to help build a standardized set of tools for the entire team.

### **Foster a Culture of Collaboration and Learning**

If every team member is off doing their own thing, you’re missing out on learning opportunities.

Pair programmers together for projects or set up a mentorship network to share knowledge. Let your team nerd out on programming updates or code changes with lunch and learns, lectures from thought leaders in your industry, or attending conferences or training sessions together. Taking time away from the daily grind to learn something new is a great way to build camaraderie and gain new skills to apply to the next sprint cycle. This is a great example of how increasing developer performance can also increase employee retention.

### **Streamline** **Processes and Workflows**

Your systems define your productivity just as much as individual skill. Whether you’re using a kanban or agile methodology to break down projects into more manageable tasks or taking in tickets as you receive them, map out your workflow from start to finish to identify where you can support your team.

Use what you’ve learned from your data collection on bottlenecks in your workflow to optimize how you get the work done. This means taking a hard look at the number of meetings your team attends each week (those standups really add up.)

Reducing [**context switching**](https://jellyfish.co/blog/less-is-more-an-action-plan-for-reducing-context-switching/) and interruptions can help your team focus, too – that might mean working with the rest of your organization to eliminate random Slack pings or setting designated “developer office hours” for folks to come ask questions or work on a task together.

### **Invest in Proper Documentation**

Everybody loves to hate on documentation, but it’s a crucial step in the development process, especially as your team expands. Whether you assign one team member or project manager the responsibility to maintain the documentation or it’s up to each individual, remind your team that it’s a step you can’t miss.

Good documentation includes:

- **Clear explanations:** Explain what the code does, how it works, and why it was designed that way.
- **Up-to-date information:** Keep documentation current with code changes.
- **Easy to find and access:** Use a centralized, organized repository to make it easy for developers to find what they need.
- **Different types of documentation:** Include API documentation, tutorials, code examples, and FAQs to cater to different needs.

Good documentation takes time, but it will save plenty of effort and hours later on when new bugs need to be fixed, you have a question about a specific technique, or the product team requests a similar feature. It also provides a clear statement of record so if there is an error or a feature needs to be reworked, you can easily find the problem and fix it.

### **Minimize Technical Debt**

Technical debt is a fact of software development. But you never want it to get so problematic that you have to put off strategic initiatives or new product features in order to fix it. As tech debt accumulates in your codebase, it becomes harder and slower to add features, fix bugs, and maintain your code base. This can slow down development – and it’s frustrating for developers to spend time fixing code when they could be doing interesting or creative work.

The best way to minimize technical debt is to write clean code the first time (more on that below) and to address issues as soon as you identify them. Include refactoring as part of each sprint cycle or dedicate a week each quarter to cleaning up the code base. Automated tools can also help you catch areas for improvement more quickly.

### **Keep Code Clean and Maintainable**

Keeping your code as clean as possible makes it easier to work with so your team can move faster (and so no one is stuck on code cleanup duty all the time.) To keep your code clean, consider using:

- **Meaningful names:** Use descriptive names for variables, functions, and classes that make sense to someone outside your immediate team.
- **Consistent formatting:** Follow consistent formatting conventions to improve readability.
- **Small, focused functions:** Break down complex tasks into smaller, more manageable functions.
- **Minimal dependencies:** Reduce dependencies between modules to make the code easier to change and test.

4 Best Practices for Measuring Developer Productivity

## **4 Best Practices for Measuring Developer Productivity**

Measuring developer productivity can easily veer into micromanagement territory. You don’t want to make your team feel like you’re watching every click of their mouse or keyboard strokes. Focus your efforts on strategic alignment, deliverable timelines, and the overall effectiveness of your workflow. The more data you have on these themes, the better you can craft a process that achieves business outcomes and supports your team.

Here’s how to measure developer productivity in a nuanced – and ethical – way:

### **Choose the Right Metrics**

It can be easy to get caught up in metrics that reflect the volume of work your team handles, like number of commits or lines of code written. That’s the equivalent of your sales team celebrating the number of phone calls they make instead of their closed deal value. Instead, prioritize metrics that reflect the value delivered to your internal and external stakeholders of the business.

But you don’t have to go all-in on quantitative metrics, either. Your team performance doesn’t come down to one single metric. Combine objective measures like code commits or cycle time with subjective assessments like code reviews or developer feedback for a more holistic view of where your team shines and where they can improve.

### **Implement a Balanced Measurement System**

Your success doesn’t depend on one number. Once you establish a baseline for your developer productivity, track trends over time to analyze seasonality and team-wide areas for improvement.

You’ll also want to take a segmented view of each team, project, or individual developer to determine strengths and weaknesses – as well as any external factors impacting specific initiatives that might be missed in a wider analysis.

It’s important to evaluate quantitative and qualitative metrics. There are multiple frameworks that DevOps teams can adopt to measure their productivity, but the best approach combines elements from all of them. Consider using a combination of DORA and Flow metrics to get a more comprehensive view of team performance.

### **Prioritize Developer Experience and Well-Being**

Just as you encourage your team to work together in the software development process as much as possible, include them as you look to improve productivity, too. Solicit feedback from them about the workload, process, and their ideas on how to improve. They may already have ideas on which metrics are the most relevant to measure and why you may not be seeing results. The more transparent and collaborative you can make the process, the more likely your team will buy-in to the initiative – you want them to be motivated to improve, not afraid of being punished.

You’ll also need to be mindful of data privacy and ethical considerations when it comes to measuring productivity, especially for individual performance. The rest of your team doesn’t need to know about work-around accommodations for disability, pregnancy, or health-related issues that might impact an individual’s productivity. Consider anonymizing your individual-level data on dashboards or removing it from public-facing visuals altogether.

### **Communicate Effectively and Transparently**

Make the effort of tracking these metrics worth it by regularly sharing the results with your team. When you go through a retrospective on a project, include the productivity metrics and how they compare against other projects.

Consider adding a teamwork process retrospective to the regular cadence of meetings, outside of specific projects, so your developers can connect their work to broader business impact. Most importantly, celebrate your successes. Highlighting wins as a team and on an individual level brings you together and makes work feel more fun as you complete your goals.

This is also a great space to collect additional feedback from your team about what’s working and what needs improvement on a team level, and encourage engineering managers to include these metrics in 1:1 discussions so individuals can get the support they need before it becomes an issue on a project as a whole.

The Data-Driven Approach to Engineering Productivity with Jellyfish

## **The Data-Driven Approach to Engineering Productivity with Jellyfish**

Measuring what matters is the first step, but gaining true visibility into a complex development process requires the right platform. Jellyfish provides a complete, data-driven view of your engineering organization, allowing you to move beyond guesswork and start making decisions that improve both productivity and business impact.

Our platform automatically [**integrates**](https://jellyfish.co/platform/integrations/) with your existing toolchain—including Jira, GitHub, GitLab, and more—to collect data on commits, pull requests, and projects. From there, Jellyfish [**tracks the critical**](https://jellyfish.co/platform/engineering-metrics/) [**metrics**](https://jellyfish.co/platform/engineering-metrics/) you need, such as DORA metrics, cycle time, and work allocation, presenting them in interactive dashboards that are easy to understand.

This ability to connect engineering work to business impact is why leaders at top companies choose Jellyfish.

For example, after implementing the platform, Jeff Sing, Director of Engineering at Iterable, noted,

“One of the things I love about Jellyfish is this concept of high-level alignment. It tells you right away where your resources are deployed… Utilizing Jellyfish allows us to immediately ‘debug’ things. We can tell if the cost of something is too high.”

By identifying and addressing bottlenecks, [**Iterable**](https://jellyfish.co/case-studies/iterable/) was able-to make their workflow more efficient and predictable. This data-driven approach resulted in a 98% reduction in the time their team spent on software capitalization worksheets, freeing up nearly 24 hours of engineering time each month.

See how Jellyfish can provide the visibility you need to optimize your engineering team. Book a 1:1 demo today.

Frequently Asked Questions (FAQs)

## **Frequently Asked Questions (FAQs)**

### **My team currently uses story points. Isn’t that a good way to measure developer velocity?**

While [**story points**](https://jellyfish.co/blog/do-story-points-work/) are a useful tool for sprint planning and estimation, they are [**not an effective measure of productivity**](https://jellyfish.co/blog/the-case-for-not-counting-story-points-2/). They are subjective, vary between teams, and don’t capture the actual value or quality of the work delivered. True [**developer velocity**](https://jellyfish.co/blog/how-to-measure-developer-productivity/) is better measured by outcome-oriented metrics like Throughput (the number of work items completed) and Cycle Time, which focus on the actual delivery of quality software to users.

### **Are there industry benchmarks for DORA metrics that my team should aim for?**

Yes, the annual [**DORA report**](https://dora.dev/publications/) provides a benchmark that categorizes teams as “low,” “medium,” “high,” or “elite” performers. While this can provide some context, it’s more important to focus on improving against your own historical data. The goal of productivity measurement is continuous improvement. A team that improves its own cycle time by 20% has achieved a more meaningful result than a team that simply matches an external benchmark.

### **How often should we review developer productivity dashboards?**

It depends on the role. Engineering managers might review metrics more frequently, even in near real-time, to manage active development cycles and unblock their teams on a weekly basis. On the other hand, senior engineering leaders typically focus on monthly or quarterly trends. They use metrics to inform strategic decisions, track the impact of process changes, and ensure overall engineering productivity is improving over time.

### **We are just starting out. Which metric gives the most value for the least amount of effort?**

The single most valuable metric to start with is Cycle Time. It measures the entire process from the first commit to production deployment. Investigating why cycle time is high will naturally lead you to discover bottlenecks in your code review, testing, or deployment processes, providing a clear path for making impactful improvements to how you build and ship new features.

![Request a Jellyfish Demo](https://jellyfish.co/wp-content/uploads/2023/08/Jellyfish_Request-A-Demo_Featured-Image_450x200.webp)

#### See Jellyfish in Action

Book a demo today and discover how we can help you transform your engineering organization.

[Book a demo](https://jellyfish.co/request-a-demo/)

About the author

![Lauren Hamberg](https://jellyfish.co/wp-content/uploads/2025/03/Lauren-Hamburg.jpg)

Lauren is Senior Product Marketing Director at Jellyfish where she works closely with the product team to bring software engineering intelligence solutions to market. Prior to Jellyfish, Lauren served as Director of Product Marketing at Pluralsight.

Follow: [LinkedIn](https://www.linkedin.com/in/laurenhamberg/)

## Dive Deeper with Jellyfish Content

[![Jellyfish G2 Summer 2026 Grid](https://jellyfish.co/wp-content/uploads/2026/05/blog-g2-summer26-featured-1024x582.webp)](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-summer-2026/)[**16 Quarters at the Top: Jellyfish Continues to Lead G2’s Software Development Analytics Tools Grid**](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-summer-2026/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-summer-2026/)

[![Jellyfish State of Engineering Management](https://jellyfish.co/wp-content/uploads/2026/05/blog-semr26-1024x561.webp)](https://jellyfish.co/blog/ai-adoption-improving-engineering-productivity-and-job-satisfaction-jellyfish-report-finds/)[**AI Adoption Improving Engineering Productivity and Job Satisfaction, Jellyfish Report Finds**](https://jellyfish.co/blog/ai-adoption-improving-engineering-productivity-and-job-satisfaction-jellyfish-report-finds/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/ai-adoption-improving-engineering-productivity-and-job-satisfaction-jellyfish-report-finds/)

[![Pensero Alternatives](https://jellyfish.co/wp-content/uploads/2024/11/blog-12-Best-GetDX-Alternatives-1024x561.webp)](https://jellyfish.co/blog/pensero-alternatives/)[**The Top 8 Alternatives to Pensero for 2026**](https://jellyfish.co/blog/pensero-alternatives/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/pensero-alternatives/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified