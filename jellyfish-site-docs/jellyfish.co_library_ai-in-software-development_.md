---
url: "https://jellyfish.co/library/ai-in-software-development/"
title: "What is the Impact of AI on Developer Productivity?"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/ai-in-software-development/#content)

In this article

Yes, artificial intelligence has invaded every corner of the software development life cycle. That’s not breaking news anymore.

You’ve heard it from your CTO, read it in every tech newsletter, and probably discussed it in your last three leadership meetings.

But the pace is relentless. New models drop every week, existing tools release new “major” updates, and your competitors might already be using something you haven’t even evaluated yet.

To better understand the current impact, we ran our [State of Engineering Management report](https://jellyfish.co/blog/2025-software-engineering-management-trends/). One of the things we found was that 90% of software teams now use AI coding tools, which is a 61% increase from just a year ago.

But even with these impressive gains, developers on Reddit and other forums agree these tools have clear limits. They’re powerful, but they’re not quite “there” yet.

![AI in software development discussion](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/AI-in-software-developement_Reddit-discussion.png)

(Source: [Reddit](https://www.reddit.com/r/ArtificialInteligence/comments/1hjg7qd/comment/m36xd19/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button))

As usually happens with new technology, the truth is probably somewhere in the middle. Yes, AI tools are incredible and bring major benefits to development teams.

But that doesn’t mean it’s time to fire your entire engineering staff and replace them with a handful of AI assistants.

Below, we’ll go through everything engineering leaders need to know about the impact of AI in software development.

You’ll learn how AI fits into different parts of the development process, the main ways teams use it today, how to roll out AI without disrupting your workflow, and where AI-powered development is headed next.

What is the Role of AI in Software Development?

## **What is the Role of AI in Software Development?**

When we talk about AI in software development, we’re talking about two main technologies that help developers work faster and spot more bugs:

- **Machine learning models** analyze your code in real-time to catch security flaws, predict bugs, and flag performance issues. It’s automated quality control that runs while you code.
- **Large Language Models (LLMs)** like GPT-4 and Claude understand programming patterns from training on millions of code repositories. These power the tools developers use daily, like GitHub Copilot and Cursor.

These tools work through three main functions that include [**automation**](https://jellyfish.co/library/developer-productivity/automation-in-software-development/) (they handle repetitive tasks like boilerplate), **augmentation** (they make developers better at writing code), and **analytics** (they find patterns that humans miss).

Of course, developers who use these tools daily know they’re far from perfect. Here’s what this Reddit dev [points out](https://www.reddit.com/r/ArtificialInteligence/comments/1hjg7qd/comment/m36g9ev/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> Yeah, I’m always a bit surprised when I read people saying that software devs won’t have a job in a year.
>
> When I use LLMs to help me code, there is a very high probability that it somehow messes up and needs to be fixed by someone who actually understands code, or it hallucinates solutions that are not actually possible.”
>
> And those are usually pretty self-contained and rather small problems. For more complex stuff, there isn’t even a reason to try.

Some studies confirm this experience. Uplevel’s research on GitHub Copilot found that AI tools can lead to [41% more bugs](https://resources.uplevelteam.com/gen-ai-for-coding) when developers work with incomplete or vague requirements.

However, when used right, the benefits are clear. Jellyfish found that 62% of teams get [25% or better productivity gains](https://jellyfish.co/blog/2025-software-engineering-management-trends/) from AI, and expect those numbers to rise.

Here’s a practical breakdown of AI’s strengths and limits today, so you know what’s possible:

|     |     |
| --- | --- |
| **What AI Can Do** | **What AI Can’t Do (Yet)** |
| Generate working code from natural language processing | Understand your specific business logic without context |
| Convert code between programming languages | Architectural decision-making for complex systems |
| Write comprehensive unit tests | Debug intricate production issues |
| Spot common security vulnerabilities | Navigate company politics or stakeholder needs |
| Create documentation from code | Design user experiences from scratch |
| Suggest performance improvements | Know when a technical solution isn’t the right answer |

The reality is less “AI replaces developers” and more “developers with AI superpowers.” You still need programming skills to know when AI gets it right.

The difference is that now, you can automate the time-consuming tasks and write code faster.

Core Use Cases of AI in Software Development

## **Core Use Cases of AI in Software Development**

Here are the most common scenarios where modern teams rely on AI-powered tools to get work done:

- **Writing boilerplate and repetitive code**: About [75% of developers](https://dora.dev/research/2024/dora-report/) use AI systems for writing code, with much of that focused on standard patterns like CRUD operations, API endpoints, and configuration files. They describe what they need, and AI creates it in seconds.
- **Converting code between languages**: Companies use AI when they need to port software applications from one language to another or modernize legacy code. AI handles the syntax iterations while developers focus on architecture decisions.
- **Explaining unfamiliar codebases**: About [31% of developers](https://survey.stackoverflow.co/2024/ai#developer-tools-ai-ben) use AI to learn about codebases they work with. When they encounter complex functions or inherited code, AI breaks down what the code does in plain English.
- **Automated test creation**: Developers feed their code to AI tools that write unit tests, integration tests, and edge case scenarios. Teams use this to instantly build comprehensive test suites for new features or legacy code that lacks proper tests.
- **Documentation and Comments**: Developers use AI to turn their code into readable documentation, README files, and inline comments. Research shows that increased AI adoption correlates with roughly [7-8% improvements](https://dora.dev/research/2024/dora-report/) in documentation quality across development teams.
- **Reviewing code for security issues**: Organizations run AI scanners on every commit to check for vulnerabilities. The AI knows thousands of security patterns and outlines issues like SQL injection or exposed credentials.
- **Finding and fixing bugs during development**: [7% of engineers](https://www.statista.com/statistics/1401409/popular-ai-uses-in-development-workflow-globally/) use AI for debugging and to spot errors as they code. The AI flags undefined variables, recommends error handlers you forgot to add, and catches logic flaws before code review.
- **Writing SQL queries from natural language**: Teams let non-technical staff and developers describe the data they need in plain English. AI translates these requests into proper SQL queries with all the necessary joins and filters.

The Business Impact: Key Benefits of AI Adoption

## **The Business Impact: Key Benefits of AI Adoption**

Teams that adopt AI technologies see changes across their entire [software development life cycle](https://jellyfish.co/blog/sdlc-best-practices/).

Some are obvious from day one, others take months to surface. Below, we’ll break down the key benefits:

### **Developer Productivity** **and Development Speed**

**What teams face:** Developers waste countless hours on repetitive work that follows the same patterns every time. They write the same boilerplate code and build nearly identical API endpoints over and over. Meanwhile, the [complex problems](https://jellyfish.co/library/code-complexity/) that need human expertise sit in the backlog for weeks.

**How AI Changes This:** AI tools handle the predictable parts of coding so developers can focus on architecture and problem-solving. When developers describe what they need, AI writes the routine code in seconds.

It’s no surprise that [81% of developers](https://survey.stackoverflow.co/2024/ai#developer-tools-ai-ben) say productivity gains are the biggest benefit they get from AI tools. Here’s how one developer on Reddit [describes](https://www.reddit.com/r/webdev/comments/1ffw9lh/ai_is_tremendously_helpful_but_its_taking_the_joy/) the productivity boost:

> I’ve been able to significantly streamline my speed in delivering tasks. It helps with autocomplete or straight-up generates code for me, and it works great. I don’t really need to figure things out myself as much. Just ask the AI and boom – you have the (usually correct) answer.

**Common mistakes to avoid:** Expect a ramp-up period where productivity might even dip as developers learn the tools. The teams that succeed are selective – they use AI for routine tasks but stay hands-on for complex logic. Watch out for code bloat too, since AI loves to over-engineer simple problems.

### **Faster Time to Market**

**What teams face:** Development cycles stretch longer than planned as developers work through technical details that don’t directly add customer value. Teams spend time on infrastructure setup when they should be building prototypes. While they’re deep in implementation, market opportunities pass by and feature requests pile up in the backlog.

**How AI Changes This:** AI tackles the tedious setup work that usually slows teams down. It writes API integrations in minutes, creates test suites automatically, and catches common mistakes before they become problems. McKinsey’s research shows that GenAI [speeds up delivery by about 5%](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/how-generative-ai-could-accelerate-software-product-time-to-market) over six months.

**Common mistakes to avoid:** The temptation is to go full speed and skip the safety checks, but that’s how you end up with broken production code. AI helps you write fast, but you still need to test thoroughly.

**PRO TIP 💡:** Jellyfish’s [Life Cycle Explorer](https://jellyfish.co/platform/life-cycle-explorer/) shows exactly where AI tools reduce bottlenecks in your development process, from code review to deployment. You’ll see if AI-generated code actually ships faster or just creates different delays downstream.

![Lifecycle by phase](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Lifecycle-by-phase.png)

### **Code Quality** **and Reduced Technical Debt**

**What Teams Face:** Technical debt piles up as developers rush to meet deadlines and skip proper documentation, testing, and thorough code reviews. This creates a cycle where teams spend more time handling problems than building new features, while legacy code becomes increasingly difficult to maintain.

**How AI changes this:** AI catches the problems that slip through when developers are tired or rushed. It finds messy code, shows you cleaner ways to write it, and handles the documentation that nobody ever has time for.

Data shows that a 25% bump in AI usage leads to [3.4% better](https://dora.dev/research/2024/dora-report/) [code quality](https://dora.dev/research/2024/dora-report/) across the board. Here’s how this developer explains the benefit on [Reddit](https://www.reddit.com/r/singularity/comments/1j0w9kx/comment/mfewmbp/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> In my experience working on software architecture and design for many years, the main reason technical debt accumulates is not because developers don’t know how to refactor or improve the codebase. It’s because they don’t have time to prioritize it, or simply don’t bother.
>
> A developer who’s worked on the same system for several years has very clear ideas on things that could be improved. Well, now we have AI to help us.

**Common mistakes to avoid:** AI can write code that works, but breaks every rule of good design. Some teams create more debt when they use AI to clean up messy functions instead of fixing the bad architecture that caused the mess.

### **Developer Satisfaction and Retention**

**What teams face:** [Developer burnout](https://jellyfish.co/blog/engineering-burnout/) is at an all-time high, with talented engineers leaving the industry entirely. They’re exhausted from context-switching between dozens of small tasks and doing work that feels pointless.

Companies spend fortunes on perks and salary increases, but developers still quit because the actual day-to-day work is soul-crushing.

**How AI changes this:** Developers get to spend their time on interesting challenges like building new features and taking care of tricky performance issues. McKinsey found that developers who use AI tools are more than [twice as likely to feel happy](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/unleashing-developer-productivity-with-generative-ai) at work.

**Common mistakes to avoid**: Don’t force AI tools on developers without proper training or input on which tools to use. The worst thing you can do is take the time generative AI saves and fill it with more grunt work. That defeats the entire purpose.

**PRO TIP 💡:** Jellyfish [DevEx](https://jellyfish.co/platform/devex/) combines developer sentiment surveys with engineering metrics to reveal the actual friction points in your workflow. Teams can see if AI tools genuinely improve the [developer experience](https://jellyfish.co/blog/developer-experience-best-practices/) or just mask deeper workflow issues.

![tech debt](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/tech-debt.png)

The Best AI Tools for Coding Assistance: A Detailed Comparison

## **The Best AI Tools for Coding Assistance: A Detailed Comparison**

The [AI coding tool](https://jellyfish.co/blog/best-ai-coding-tools/) market exploded from a handful of options to dozens of specialized products.

And picking the right ones for your team means understanding what each category offers and how they fit into your workflow:

### **General-Purpose Language Models**

These AI chatbots weren’t built specifically for programmers, but they turned out to be surprisingly good at it.

They work through standard web browsers where you describe what you need in natural language, and they respond with code snippets, explanations, and troubleshooting advice.

- **ChatGPT:** The tool that started the AI coding revolution for millions of developers. It turns natural language into working code, explains cryptic error messages, and breaks down complex logic into steps anyone can follow.
- **Claude**: Produces clean, readable code with explanations that make technical sense. Developers choose it for complex projects where they need to keep track of multiple files and maintain consistent patterns throughout.
- **Gemini**: Integrates seamlessly with Google Cloud and related services, so it’s a natural choice for teams that already use Google’s infrastructure. It handles both code generation and technical documentation particularly well.
- **Perplexity**: While primarily a search tool, developers use it to research libraries, compare frameworks, and find solutions with real-time web data. It’s particularly helpful when working with newer technologies or recent updates.
- **Microsoft Copilot**: Available through Edge and Bing, it combines GPT-4 with web search to help developers find and adapt code examples. Works well for developers who need both code generation and up-to-date documentation.

### **IDE-Integrated AI Assistants**

These tools integrate directly into your editor, where they complete your code in real-time and generate functions without switching contexts.

They understand your current file, project structure, and coding patterns to offer contextually relevant help. It’s like a smart autocomplete system that happens to understand what you’re trying to build.

- **GitHub Copilot**: The market leader in AI code completion, built on OpenAI’s Codex model. It writes entire functions from comments, adapts to your coding style, and works across popular IDEs like VS Code and JetBrains. Most developers start here because of its massive training dataset and Microsoft
- **Cursor**: A VS Code fork that puts AI features directly into the editor interface. You don’t need any separate extensions or tools. It combines chat assistance with inline code completion and scans your entire project to understand context better than traditional autocomplete.
- **Amazon Q Developer**: Amazon’s answer to Copilot, optimized for AWS services and cloud development. It generates code, explains AWS best practices, and helps with infrastructure as code.
- **Tabnine**: Unlike some open-source alternatives, it focuses on privacy with options for on-premise deployment and training on your team’s code. It learns from your specific codebase patterns and keeps all data local if needed. Popular with enterprises that can’t send code to external servers.
- **Replit AI**: Built into Replit’s online IDE, it generates code, explains errors, and helps with debugging. Perfect for developers who prefer browser-based development or need to code on multiple devices.
- **Visual Studio IntelliCode**: Microsoft’s AI assistant that’s built specifically for Visual Studio and VS Code, with strong support for .NET development. While not as advanced as newer tools, it’s free and works well for teams already invested in Microsoft’s development ecosystem.

### **Documentation Tools**

Documentation AI tools take care of the writing work that most developers avoid.

They scan your codebase using computer science principles and produce readable explanations, API references, and project overviews without manual effort.

- **Mintlify**: Creates beautiful documentation sites from your codebase with AI-driven content generation. It watches your code for changes and updates docs automatically, plus it can answer questions about your docs in real-time.
- **so**: The fastest way to create README files with AI assistance. Type a few details about your project, and it generates complete documentation with proper sections, badges, and formatting.
- **GitBook**: Combines traditional documentation with AI features that help write, organize, and maintain technical docs. The AI assistant helps fill in gaps, improve clarity, and keep consistency across hundreds of pages.
- **Stenography**: Specifically built for code documentation, it scans your entire codebase and writes explanations for every function. It integrates with your DevOps workflow and CI/CD pipeline to keep documentation current with each commit.

### **Code Quality** **and Security Tools**

AI quality tools scan your code continuously for bugs, security gaps, and maintainability issues that could cause problems later. They act as a safety net that catches problems before your code goes live.

- **Snyk**: Specializes in finding security vulnerabilities in your code, dependencies, and container images with AI-powered threat detection. The tool integrates into your CI/CD pipeline to spot gaps before deployment.
- **Codacy**: Automatically reviews pull requests for code quality issues, security gaps, and style violations. The platform tracks [software quality](https://jellyfish.co/library/quality-metrics/) [metrics](https://jellyfish.co/library/quality-metrics/) over time and helps teams maintain consistent coding standards.
- **GitGuardian**: It detects and prevents secrets from leaking into your code. The AI catches API keys, passwords, and tokens in real-time, and alerts you before sensitive data gets exposed in public repositories.

Best Practices for Implementing AI in Your Workflow

## **Best Practices for Implementing AI in Your Workflow**

Rolling out AI tools across your engineering team requires more than buying licenses and sending a Slack announcement.

Here are the exact steps on [how to implement](https://jellyfish.co/blog/ai-coding-tool-adoption-best-practices/) [AI tools](https://jellyfish.co/blog/ai-coding-tool-adoption-best-practices/) without disrupting your team or wasting your investment:

### **Start Small: Pilot Programs and Gradual Rollout**

**Why this matters:** Teams that try to implement AI tools across the entire organization at once almost always fail. Starting with a small, motivated group lets you work out the kinks before scaling up, and early wins from pilot teams build momentum for broader adoption.

**How to implement:**

- Pick 3-5 developers who are already interested in AI tools, not the ones who roll their eyes when you mention ChatGPT
- Choose one specific use case, like code completion or documentation generation, not a dozen different AI use cases all at once
- Run the pilot for 4-6 weeks to give developers enough time to form real opinions and develop workflows
- Track [concrete](https://jellyfish.co/library/metrics-in-software-engineering/) [metrics](https://jellyfish.co/library/metrics-in-software-engineering/) like code review time, bug detection rates, or feature delivery speed during the pilot period
- Have pilot participants document what works, what doesn’t, and what workflows they developed
- Use pilot results to create guidelines and training materials before expanding to other teams

**Common pitfalls to avoid:**

- Don’t mandate that everyone use AI tools immediately without understanding which ones truly help your specific workflows
- Avoid measuring success only by adoption rates rather than actual [productivity improvements](https://jellyfish.co/library/engineering-productivity/) or developer satisfaction
- Don’t skip the feedback collection phase, where pilot users can honestly share what frustrated them about the tools
- Stop promising huge productivity gains that make your pilot team feel like they have to show dramatic improvements or they’ve failed

### **Team Training and AI Tool Adoption**

**Why this matters:** Throwing AI tools at developers without proper training only leads to frustration and eventual abandonment. Teams need to understand not just how to use these tools, but when to trust them and when to take control.

Reddit users often recommend getting your hands dirty with AI tools immediately, as this developer [explains](https://www.reddit.com/r/instructionaldesign/comments/1izulmk/comment/n2hd46r/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> Practical, hands-on training is key. Have your entire workforce build simple AI tools (like a custom productivity assistant or job role coach). This creates the ‘aha’ moment that drives confident adoption across their daily work.

**How to implement:**

- Run hands-on training sessions where developers use the tools on real-world code problems from your codebase, not generic examples
- Show developers specific prompting techniques that work well for your tech stack and coding patterns
- Create internal documentation with examples of good AI-generated code and bad suggestions that should be rejected
- Set up “AI office hours” where developers can ask questions and share tricks they’ve discovered with the tools
- Record short videos of developers using AI tools effectively so people can see real workflows in action

**Common pitfalls to avoid:**

- Don’t just send people links to tool documentation and expect them to [become productive](https://jellyfish.co/blog/how-to-measure-developer-productivity/) without hands-on guidance
- Stop treating AI tool training like a one-time workshop when it really needs ongoing support as people develop their skills
- Don’t ignore the developers who are having trouble with the tools or think they’re not smart enough to figure it out
- Avoid training that focuses on what the tools can theoretically do without showing practical applications to your actual work

**PRO TIP 💡:** Use analytics to personalize AI training for different teams. Jellyfish’s [AI Impact dashboard](https://jellyfish.co/platform/jellyfish-ai-impact/) shows that your frontend team might excel with Copilot while backend developers prefer Cursor for database work. This helps you tailor training sessions to each team’s actual needs instead of forcing everyone through the same generic program.

![AI tool comparison](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/AI-tool-comparison.png)

### **Set Clear Guidelines and Boundaries for AI Use**

**Why this matters:** Without clear rules, teams either avoid AI entirely out of fear or use it recklessly without considering security and quality implications.

Many development teams are currently operating without formal AI policies, as one Reddit user [describes](https://www.reddit.com/r/ExperiencedDevs/comments/1ksowr8/comment/mtneg9o/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> We have no real guidelines; we’re still trying to figure out the best approaches. We do have pretty much carte blanche to use AI, though, with no real concern about it operating on entire codebases. This hands-off approach often creates problems that clear boundaries can prevent.

**How to implement:**

- Define which types of code and data can be shared with AI tools and which are “human-only handling” for security or compliance reasons
- Create a list of approved AI tools that meet your security standards and discourage the use of random new AI services without evaluation
- Document which use cases work well for AI assistance, and which coding tasks should remain purely human-driven
- Set up escalation paths for when developers encounter AI suggestions that might violate coding standards or security policies

**Common pitfalls to avoid:**

- Don’t assume that developers will naturally know when AI suggestions are inappropriate for sensitive code or proprietary business logic
- Avoid creating AI policies without input from developers who are already using these tools and understand the practical issues
- Don’t write guidelines that are too vague and provide no actual guidance when developers face tough decisions about AI tool usage
- Stop treating AI guidelines as a one-time document when they need to evolve with your team’s experience and changing tools

### **Establish Code Review Processes for AI-Generated Code**

**Why this matters:** Traditional code review processes don’t account for AI assistance, so teams need new approaches to handle the volume and specific risks that come with AI-generated code. But also, don’t forget about basic review etiquette, as this Reddit dev [points out](https://www.reddit.com/r/ExperiencedDevs/comments/1jfhqye/comment/mir57la/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> Here’s a simple rule everyone should follow regardless of whether they use AI or not. You should review your own PR before requesting reviews. It’s simply rude to expect other people to point out your random logs or unnecessary line changes and advancements.

**How to implement:**

- Ask developers to mark which parts of their PR were AI-generated so reviewers know where to pay extra attention
- Create checklists specifically for reviewing AI code that focus on logic errors and security vulnerabilities
- Train code reviewers to look for common AI mistakes like hardcoded values, incomplete error handling, and security anti-patterns
- Document examples of good and bad AI-generated code to help reviewers spot problematic patterns more quickly

**Common pitfalls to avoid:**

- Don’t assume AI-generated code needs less review time just because it looks clean and follows standard formatting conventions
- Stop letting developers submit AI code for review without first checking it themselves for obvious errors
- Don’t treat all AI-generated code the same way when some use cases are riskier than others and need more thorough review
- Avoid creating review processes that are so burdensome they discourage developers from using helpful AI tools appropriately

Navigating the Technical Risks and Challenges

## **Navigating the Technical Risks and Challenges**

Every powerful tool brings new problems, and AI coding assistants are no exception. Teams discover these issues after deployment, usually at the worst possible moment.

Here’s what to watch for before AI-generated code breaks production:

### **Security Vulnerabilities and Data Privacy Concerns**

**The risk:** AI coding tools send your code to external servers for processing, which can expose proprietary algorithms, customer data, and security credentials. Even tools labeled “secure” might keep code snippets for training their models.

**Why it matters:** A single leaked API key or exposed customer database schema could cost millions in damages and destroy customer trust. Many developers share these concerns about data exposure, as one Reddit user [explains](https://www.reddit.com/r/cybersecurity/comments/1hx980d/comment/m67q6bi/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> As a software developer, I have zero desire to log in and use any built-in IDE AI since they send all that data to an outside source most of the time. It frankly scares me that it’s being put right in our faces in IDEs as well as OS level stuff. The potential for data leaks is skyrocketing.

**How to mitigate:**

- Use on-premise or local AI solutions for sensitive codebases, so you can keep all processing within your network boundaries
- Configure AI tools to exclude specific file types and directories that contain credentials, customer data, or proprietary algorithms
- Set up automated scanning to detect and flag common security anti-patterns in AI-generated code before it reaches production
- Create allow-lists of approved AI tools that meet your organization’s security and privacy standards
- Create separate development environments with sanitized data for AI-assisted work, so you don’t have to connect the AI tools to production systems

### **Performance Impact and Technical Debt**

**The risk:** AI generates code that works but often includes unnecessary complexity, inefficient algorithms, or patterns that slow down your application. Teams build technical debt quickly when they accept AI suggestions they don’t fully understand.

**Why it matters:** Code that seems fine during development can cause production servers to crash under load or make simple features take seconds to load.

This problem compounds when developers blindly trust AI output. One Reddit developer shared an interesting perspective on this:

![AI experience and from real engineers](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/AI-experience-and-from-real-engineers.png)

(Source: [Reddit](https://www.reddit.com/r/devops/comments/1ekusio/comment/lgnb3un/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button))

**How to mitigate:**

- Run performance benchmarks on AI-generated code before merging, especially for functions that will execute often or handle large datasets
- Set up automated performance regression tests that flag when new code makes existing features slower
- Review AI code for common inefficiencies like nested loops, redundant database queries, or memory leaks that AI tools often bring
- Create team guidelines that specify when to optimize AI code immediately versus accepting “good enough” solutions for non-critical features

### **Legal and Compliance Considerations**

**The risk:** AI tools might generate code with licensed snippets from their training data, which creates potential copyright violations in your product. Organizations often hit compliance issues when AI tools process regulated data or produce code that doesn’t meet standards for healthcare, finance, or government work.

**Why it matters:** Lawsuits about AI code ownership, copyright infringement, or data misuse burn through legal budgets and wreck partnerships. Many developers also don’t buy vendor claims about data protection, as one Reddit user [notes](https://www.reddit.com/r/webdev/comments/1jb2owt/comment/mhrct3t/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> The unfortunate reality is, they can easily train their LLMs using your code, even if you paid for Copilot, and you would have no idea. And even if you somehow found out, what are the chances of you going through with a lawsuit? And even if you won, they will simply eat the costs and keep doing it.
>
> In order for Copilot to do what they say they will do, there has to be a regulatory standard enforced by the government that is strictly monitored. So I don’t trust Microsoft when they say they won’t train their LLMs with your code.

**How to mitigate:**

- Choose AI tools that provide legal protection against copyright claims (they should assume liability, not your organization)
- Keep detailed logs of all AI-generated code with prompts, timestamps, and tool versions for audit purposes
- Set up code scanners that detect potential license violations or copyrighted snippets in AI output
- Consult legal counsel before you use AI tools in regulated industries like healthcare, finance, or government contracting

Understanding the Ethical Considerations

## **Understanding the Ethical Considerations**

While AI makes software development better in countless ways, there are some ethical questions that teams still need to think through.

One major worry for most teams is **how AI affects developer careers**, especially junior engineers. People fear AI will replace programmers, but that’s not what’s happening.

Instead, developer roles are changing. They spend less time on repetitive tasks and more time on nuanced problem-solving. Junior developers benefit from AI tools because they can learn faster, contribute code sooner, and get unstuck without constantly asking senior developers for help.

The challenge is making sure they still learn the fundamentals. We don’t want them dependent on AI for everything. Yet, some managers still misunderstand what these tools can do, as one Reddit user explains:

![ethical considerations in AI](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/ethical-considerations-in-AI.png)

(Source: [Reddit](https://www.reddit.com/r/developersIndia/comments/1cy065p/comment/l565xa7/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button))

Other than job concerns, there’s the tricky question of **where AI training data comes from**. One developer’s Reddit [post](https://www.reddit.com/r/selfhosted/comments/1cp3g5o/ethical_concerns_with_ai/) shows this confusion:

> It’s really confusing to understand the line between what is ethical and what isn’t whenever it comes to AI. On one hand, models are trained on real user data and monetized without any credit towards the users. On the other hand, there really isn’t a good way to credit anybody.

This bothers a lot of developers — 65% say source attribution is a [top ethical concern](https://survey.stackoverflow.co/2024/ai#3-most-important-ethical-issues-for-ai). And while we can’t fix this industry-wide problem ourselves, we can choose AI vendors who are transparent about their data and offer legal protection for their users.

Another issue that teams face is **bias in AI-generated code**. AI models learn from existing code, which means they pick up bad habits along with good ones. They might recommend outdated patterns or reproduce harmful biases.

In fact, [79% of developers](https://survey.stackoverflow.co/2024/ai#3-most-important-ethical-issues-for-ai) worry about misinformation and errors in AI results. The best approach is to treat AI suggestions skeptically and review them like any junior developer’s code.

Ultimately, developers are responsible for what ships. As this Reddit user [puts it](https://www.reddit.com/r/github/comments/128wxy4/comment/jekugn4/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> _The programmer is the one responsible (or should be), since they’re the one who wrote, checked, and shipped the code. It doesn’t matter they used Copilot, copied code from some other project, or even stole it from somewhere. This is exactly right. AI doesn’t remove accountability; it just changes how we exercise it._

These ethical considerations point the way forward, not backward. Set up oversight, create clear rules, and treat AI as a tool that makes developers better at their jobs.

The winners in AI adoption face these questions honestly and build their practices accordingly. That’s the path to responsible innovation.

Measuring Success: Is AI Worth the Investment?

## **Measuring Success: Is AI Worth the Investment?**

Your developers swear AI makes them more productive, and they’re probably right.

But “probably” doesn’t convince CFOs to keep paying for tools. The only way to prove AI’s worth is to [track what changes](https://jellyfish.co/blog/measuring-the-impact-of-generative-ai-coding-assistants/) when developers use it.

You need to watch four types of [engineering](https://jellyfish.co/platform/engineering-metrics/) [metrics](https://jellyfish.co/platform/engineering-metrics/) to understand what AI does for your team:

|     |     |     |     |
| --- | --- | --- | --- |
| **Metric Category** | **What to Measure** | **Target Change** | **Warning Signs** |
| **Productivity** | Cycle time, deploy frequency, PR velocity | 20-30% improvement | Speed up with no quality metrics |
| **Quality** | Bug escape rate, review cycles, test coverage | Maintain or improve | >10% increase in bugs |
| **Developer Experience** | Satisfaction scores, retention, onboarding time | Positive trend | Senior dev dissatisfaction |
| **Business Impact** | Feature delivery, time to market, customer issues | 15-25% improvement | No change despite other gains |

Let’s say your team of 10 developers costs $1.5 million annually. AI tools cost $200 per developer per month ($24,000 yearly).

If AI [improves productivity](https://jellyfish.co/library/engineering-productivity/) by just 15%, that’s $225,000 in extra capacity. Even with training time and the learning curve, you’re looking at 5-8x ROI within the first year.

Speed improvements only tell part of the story. You can also:

- Reduce bug fixes (each production bug costs $2,000-$5,000)
- Accelerate onboarding (new developers productive in 3 weeks instead of 6)
- Improve retention (replacing a developer costs $20,000-$30,000)

**And don’t fall into the trap of tracking vanity metrics.** Lines of code written is the worst offender because AI can write thousands of useless lines instantly. Engineering leads on Reddit [explain](https://www.reddit.com/r/ExperiencedDevs/comments/19awh25/comment/kinuynb/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) that this only leads to metric gaming:

> I’m a lead at my company, and I’ve been heavily pointing all story tickets since management wants to play the velocity game.

Another major mistake is over-indexing on velocity while ignoring everything else.

Teams celebrate writing code 50% faster, but don’t notice their bug rates doubled or their best developers are frustrated by constant AI corrections. Balance is everything.

The Road Ahead: The Future of AI in Engineering

## **The Road Ahead: The Future of AI in Engineering**

AI coding tools get sharper with every release. The clunky autocomplete from last year now handles complex refactoring. Next year’s versions will probably make today’s tools look primitive.

Here’s where we are now:

- [81% of developers](https://survey.stackoverflow.co/2024/ai) say that they’re seeing productivity improvements
- [87% of developers](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) report that AI frees up mental energy for more complex problems
- McKinsey’s study projects [3-hour daily time savings](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work) for software developers by 2030

Think about what three hours means. That’s entire afternoons freed from debugging syntax errors and writing boilerplate. Time you can spend on the architectural redesign that’s been postponed for months.

But we also need to be clear about what AI can and can’t do. Here’s how one developer on Reddit [put it](https://www.reddit.com/r/ExperiencedDevs/comments/1hm8gxj/comment/m3sbt3m/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> AI will replace software engineers who only copy-paste from Stack Overflow. AI will most probably not replace software engineers who find scalable solutions to problems or understand the design of things.
>
> But let’s face it: the majority of the tasks of a software engineer aren’t related to writing from scratch a lot of things, but fitting new requirements in layers of code that have been stratified by generations of other software engineers.
>
> In those situations, what you actually need is patience and understanding of how other people built things and a lot of memory to remember why Jeff put that ‘useless’ if.

That’s the reality. Most engineering work involves understanding existing systems and knowing why that weird edge case matters. AI handles the mechanics, but developers handle the context.

Soon, **AI tools will probably understand how your whole system fits together**. They’ll trace data flow from frontend to database and recommend architectural improvements. Automated agents will take a [Jira ticket](https://jellyfish.co/library/jira-performance-metrics/), write the feature, test it, and open a pull request without you watching.

But adoption will be messy. Some teams will upgrade their workflows next quarter, while others will still ban ChatGPT in 2030. We’ve seen this before. Cloud computing launched in 2006, yet enterprises still migrate from on-premise servers today.

The question is **how your team adapts**. Engineers need hands-on practice with AI tools now, before they become mandatory. Managers should experiment with [new work structures](https://jellyfish.co/solutions/people-management/) when basic coding drops from hours to minutes.

**Bottom line →** Teams that start experimenting today will have huge advantages tomorrow. AI multiplies what talented developers can build. It doesn’t replace the need for talented developers.

Measure the AI Impact on Your Software Development Team with Jellyfish

## **Measure the AI Impact on Your Software Development Team with Jellyfish**

You’ve invested in AI tools for your developers. GitHub Copilot, Cursor, maybe some ChatGPT licenses. But you have no idea if they’re working.

Sure, developers say they feel more productive, but where’s the proof? How do you know which tools deliver value and which ones just burn budget?

That’s where **Jellyfish** comes in. Our [AI Impact](https://jellyfish.co/platform/jellyfish-ai-impact/) feature shows you exactly what AI tools do for your team – which developers use them, how much faster they ship, and whether you’re getting your money’s worth.

With Jellyfish, you can track:

- **How AI tools affect productivity across your teams**: The platform measures the impact of Copilot, Cursor, and Gemini on [delivery speed](https://jellyfish.co/solutions/software-delivery-management/), workflow patterns, and how developers spend their time. You’ll see if teams using AI ship faster, spend less time on boilerplate, or get stuck debugging AI-generated
- **Which tools work best for specific tasks and roles**: Jellyfish breaks down usage by team, work type, and even individual developers. Maybe your frontend team thrives with Copilot while backend developers get more value from Cursor. The data shows you exactly who uses what and how effectively.
- **Where AI delivers value versus where it wastes money**: Compare tool performance side by side to understand each one’s contribution to your AI development If Sourcegraph saves 10 hours weekly on code reviews but Gemini sits unused, you’ll know where to plan your spending.
- **How AI agents integrate into your development workflow:** Track adoption and performance metrics for code review bots and other automated agents. See completion rates, accuracy scores, and how agent performance compares to human developers on similar tasks.
- **Whether your AI investment pays off**: Drill down to see AI costs per developer, per team, or per project. Jellyfish connects spending to specific outcomes – if you paid $5,000 for AI tools last quarter, did they deliver $20,000 in productivity gains? The platform calculates the actual ROI based on time saved and output

The platform also [integrates](https://jellyfish.co/platform/integrations/) with your existing AI tools through simple API connections. Once connected, Jellyfish automatically collects usage data and correlates it with your engineering metrics.

You get dashboards that show AI adoption trends, productivity impacts, and detailed breakdowns by team and project.

[**Schedule an AI impact demo**](https://jellyfish.co/get-an-ai-impact-demo/) with Jellyfish if you want to see the actual data on your AI investment.

Frequently Asked Questions (FAQs)

## **Frequently Asked Questions (FAQs)**

### **What’s the difference between AI coding tools and AI agents?**

**AI coding tools** work alongside you while you write code. Tools like GitHub Copilot and Cursor suggest completions and generate functions from comments, but you’re still driving. You decide what to accept, what to modify, and what to ignore. They’re sophisticated autocompletes that understand context.

**AI agents** work independently on complete tasks. Give an agent a Jira ticket, and it writes the code, creates tests, opens a pull request, and responds to review comments without your involvement. Agents make decisions about implementation, handle errors, and complete multi-step workflows on their own.

### **Will AI replace software developers?**

No. AI changes what developers do, not whether we need them.

Think about what happened with compilers. They automated assembly code writing, but we didn’t fire all the programmers. Instead, developers moved up the stack and built more complex systems. The same pattern is happening now with AI.

### **Should we standardize on one AI tool or let developers choose their own?**

Start with standardization for security and cost control, then loosen up once you understand what works. Most teams pick one primary tool (usually GitHub Copilot or Cursor) that everyone gets, and then let developers ask others for specific needs.

This keeps licensing costs predictable and simplifies your security reviews. The sweet spot is usually one approved tool for everyone, plus a budget for teams to experiment with alternatives that suit their tech stack or workflow.

### **How long does it take to see ROI from AI coding tools?**

Expect 4-6 weeks before you see real productivity changes, and 3-4 months to hit positive ROI. The first month is rough. It’s when developers test the tools, make mistakes, and figure out workflows.

After that, you’ll notice faster [feature delivery](https://jellyfish.co/library/software-delivery-management/) and fewer hours spent on boilerplate code. Most teams cover their tool costs through time savings by the end of month three.

Learn More About AI in Software Development

## Learn More About AI in Software Development

- [Benefits of AI in Software Development](https://jellyfish.co/library/ai-in-software-development/benefits/)
- [The Risks of Using AI in Software Development](https://jellyfish.co/library/ai-in-software-development/risks-of-using-generative-ai/)
- [How to Measure the ROI of AI Code Assistants in Software Development](https://jellyfish.co/library/ai-in-software-development/measuring-roi-of-code-assistants/)
- [How to Use AI in Software Development: 7 Best Practices & Examples for Engineering Teams](https://jellyfish.co/library/ai-in-software-development/use-cases-and-best-practices/)
- [AI in Software Testing and Quality Assurance](https://jellyfish.co/library/ai-in-software-development/software-testing-qa/)
- [Will AI Replace Software Engineers? No and Here’s Why](https://jellyfish.co/library/ai-in-software-development/will-ai-replace-software-engineers/)
- [What’s The Future of Software Engineering with AI?](https://jellyfish.co/library/ai-in-software-development/future-trends/)
- [What is the Responsibility of Developers Using Generative AI? Key Ethical Considerations & Best Practices](https://jellyfish.co/library/ai-in-software-development/responsibility-of-developers-generative-ai/)

About the author

![Lauren Hamberg](https://jellyfish.co/wp-content/uploads/2025/03/Lauren-Hamburg.jpg)

Lauren is Senior Product Marketing Director at Jellyfish where she works closely with the product team to bring software engineering intelligence solutions to market. Prior to Jellyfish, Lauren served as Director of Product Marketing at Pluralsight.

Follow: [LinkedIn](https://www.linkedin.com/in/laurenhamberg/)

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-Data-Hub-1024x610.png)](https://jellyfish.co/blog/dora-metrics-tools/)[**8 Top-Rated Tools for Measuring DORA Metrics**](https://jellyfish.co/blog/dora-metrics-tools/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-tools/)

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

Qualified