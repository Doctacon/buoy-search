---
url: "https://jellyfish.co/library/ai-in-software-development/risks-of-using-generative-ai/"
title: "The Risks of Using AI in Software Development"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/ai-in-software-development/risks-of-using-generative-ai/#content)

In this article

If your team doesn’t use AI yet, you’re in the minority. Most engineering organizations already integrate AI into their core workflow.

They use it to write code, catch bugs, and ship features at speeds that seemed impossible two years ago.

But faster doesn’t always mean safer.

When researchers at FormAI analyzed 112,000 C programs using ChatGPT, they found that [51.24% contained](https://arxiv.org/abs/2307.02192) [_at least_](https://arxiv.org/abs/2307.02192) [one security vulnerability](https://arxiv.org/abs/2307.02192). That means over half the AI-generated code had potential security holes.

And this is just one risk category. Development teams may also run into:

- Code quality issues and mounting technical debt
- Rubber-stamp reviews and missing business context
- Copyright violations and licensing conflicts
- Over-reliance on AI and skill degradation
- Data privacy leaks and exposed secrets

You don’t have to choose between AI adoption and risk management anymore. This guide breaks down each risk category and shows you practical ways to use AI tools safely.

We’ll cover what can go wrong, why it happens, and how to prevent it while keeping your development velocity high.

Technical Risks: When AI-Generated Code Goes Wrong

## Technical Risks: When AI-Generated Code Goes Wrong

The technical flaws in AI code aren’t always obvious. [Studies by the CSET](https://cset.georgetown.edu/publication/cybersecurity-risks-of-ai-generated-code/) show that AI models regularly create code with security flaws, even in controlled testing environments.

Let’s take a look at where these technical risks usually appear and what they mean for your codebase:

### Security Vulnerabilities

Your AI assistant never took a security course. It produces functional code, but it doesn’t always protect your data or your users.

When Veracode tested over 100 LLMs across Java, Python, C#, and JavaScript, [45% of the generated code](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report) failed security tests. These vulnerabilities range from SQL injection points to exposed API keys and insecure authentication patterns.

**Why it matters:** A single vulnerability can expose your entire system to attacks, data breaches, and [compliance violations](https://jellyfish.co/blog/prepare-for-technical-due-diligence/). Security flaws in production code cost companies millions in incident response, legal fees, and lost customer trust.

If malicious actors spot these gaps, they can steal intellectual property and take down your entire service. Plus, the tools themselves create risk. As one developer on Reddit [put it](https://www.reddit.com/r/cybersecurity/comments/1hx980d/comment/m67q6bi/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> As a software developer, I have zero desire to log in and use any built-in IDE AI since they send all that data to an outside source most of the time. It frankly scares me that it’s being put right in our faces in IDEs as well as OS level stuff. The potential for data leaks is skyrocketing.

**Warning signs:**

- AI concatenates strings to build SQL queries instead of using prepared statements that prevent injection attacks
- Authentication logic runs in frontend JavaScript, where anyone can view and bypass it through browser dev tools
- Passwords, API keys, and tokens sit in plain text variables or config files without any encryption or secure storage
- The code accepts user input directly without validation, or only checks if an email “looks right” instead of sanitizing dangerous characters
- Generated code imports old library versions with known CVEs or calls deprecated functions that vendors marked unsafe years ago

**How to prevent:**

- Set up security scanners to check every PR that contains AI-generated code before it merges
- Make senior developers review all authentication, payment, and data-handling code snippets that AI touches (even if it seems simple)
- Write security-specific unit tests that try to break AI functions with malicious input, SQL injection attempts, and edge cases
- Build a regex filter that blocks commits containing dangerous patterns like “eval(“, “innerHTML”, or hardcoded connection strings

**Example:** A startup uses AI to generate its password reset feature. The code worked great until security researchers found tokens in their client-side JavaScript. Anyone could generate valid reset tokens for any user account.

The company had to move that logic server-side and notify 50,000 users about the breach. Their security scanner would have caught this if they’d run it on AI output.

### Code Quality Degradation

AI prioritizes “it works” over “it’s maintainable,” so the code often needs refinement. Developers find oversized functions, vague naming, and logic that could be simpler.

Stack Overflow research shows that [66.2% of developers](https://survey.stackoverflow.co/2024/ai#3-challenges-with-ai-at-work) don’t trust AI code, and the quality issues explain why.

**Why it matters:** Poor code quality compounds over time until your codebase becomes impossible to maintain. One developer [explained the problem](https://www.reddit.com/r/devops/comments/1ekusio/comment/lgnb3un/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) perfectly:

> In my experience, AI makes good software engineers better and bad engineers worse. Many folks rely on that auto-generated code as if it is automatically correct and optimal, which is often not the case.

This blind trust can create problems. Developers waste hours deciphering AI-powered functions, bug fixes take longer, and refactoring becomes risky.

New team members can’t understand the codebase, and technical debt accumulates faster than you can pay it down.

**Warning signs:**

- Functions exceed 100 lines and try to handle multiple responsibilities in a single block of tangled logic
- Variable names like “data”, “temp”, “result”, or “x” appear throughout the code without a clear purpose
- The same logic appears copy-pasted across multiple files instead of extracted into reusable functions
- Comments are missing entirely or just restate what the code does (“increment counter”) without explaining why
- Code uses inconsistent patterns where one function returns early, while another uses deeply nested if-else chains

**How to prevent:**

- Set strict limits on function length and complexity scores that reject AI code exceeding those thresholds
- Run linters that apply naming conventions and outline generic variable names before code reaches review
- Use AI for small, focused coding tasks (“write a validation function”) rather than entire features or modules
- Ask developers to refactor AI output before submitting PRs, not just paste and commit
- Track [metrics](https://jellyfish.co/library/metrics-in-software-engineering/) like cyclomatic complexity and code duplication to catch quality degradation early

**Example:** A developer asks AI to “create a user management system” and gets 500 lines of tangled code in a single file. But when they break it into smaller requests (“write a function to validate email,” “create a password strength checker”), they get clean, testable modules instead.

### Increased Technical Debt

Developers merge AI-generated code without truly understanding how it works. Teams build on top of [mysterious functions](https://jellyfish.co/blog/software-capitalization-best-practices/), quick patches become core infrastructure, and the codebase fills with logic nobody can confidently modify or explain.

**Why it matters:** This isn’t normal technical debt that you can plan to pay down. A senior developer on Reddit [put it bluntly](https://www.reddit.com/r/programming/comments/1it1usc/comment/mdmvebv/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> AI tech debt is created because no one really understands those systems. So we will have systems that no one understands, not even the person who submits the PR. So when something breaks or needs to change, where do we go?

This creates a nightmare scenario where the original developer has no more insight than a newcomer. Every bug fix becomes an investigation, and your team loses control of its own codebase.

**Warning signs:**

- Developers can’t explain how their own merged code works when asked about it weeks later
- The same AI-generated boilerplate appears across multiple services with slight variations that nobody can justify
- Bug fixes take longer because developers need to reverse-engineer AI code before making changes
- Team members avoid certain parts of the codebase because “AI wrote that part,” and nobody wants to touch it

**How to prevent:**

- Ask developers to explain any AI-generated code during review as if they wrote it themselves
- Add documentation rules that force developers to understand what they’re committing
- Track “time to fix” metrics on AI-generated code versus human-written code to spot problematic areas
- Create knowledge-sharing sessions where developers walk through AI code they’ve integrated

**Example:** A team uses AI to quickly generate database migration scripts for a major update. When data corruption occurred months later, nobody could trace the problem because nobody understood the migration logic. They had to hire consultants to decode their own AI-driven code.

**PRO TIP 💡:** With Jellyfish’s [Resource Allocation](https://jellyfish.co/platform/resource-allocations/), you can track where your engineering hours go – features, bugs, or technical debt. You see which teams spend 80% of their time fighting AI mistakes versus those who balance new work with cleanup. This data helps you force debt reduction before codebases become unworkable.

![Jellyfish Resource Allocation](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Jellyfish-Resource-Allocation.png)

Process Risks: The Dangers of Overreliance on AI

## Process Risks: The Dangers of Overreliance on AI

The technical risks are visible in your code, but process risks hide in your team’s daily habits.

Developers might [review code](https://jellyfish.co/blog/impact-of-ai-code-review-agents/) less thoroughly, skip some documentation, or rely too heavily on artificial intelligence for problem-solving. Bad habits form faster than you realize, and they’re much harder to fix than bad code.

### Erosion of Fundamental Skills

The more developers use AI, the less they exercise their own problem-solving muscles. Microsoft and CMU researchers found that increased AI tool usage [directly reduces critical thinking skills](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf).

New developers never learn to think through problems, and veteran developers slowly forget how.

**Why it matters:** Use it or lose it might apply to coding skills more than most realize. Here’s how this Reddit developer [summed it up](https://www.reddit.com/r/technology/comments/1i2c62j/comment/m7ds9bv/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> Your brain is incredibly good at losing whatever it recognizes as unnecessary. Offloading your thinking altogether to AI is scary with that in mind.

When GitHub goes down or API limits hit, teams suddenly discover they can’t function properly without AI assistance.

### Blind Trust and Lack of Critical Review

Developers copy AI code without checking if it works for their specific needs. They see clean code that runs and assume it must be correct. Nobody questions whether the AI understood the requirements or caught all the edge cases.

**Why it matters:** This trust without verification creates serious problems down the line. One senior developer [shared their frustration](https://www.reddit.com/r/ExperiencedDevs/comments/1j9ryjx/comment/mihz1ct/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> AI is powerful, but blind trust in it without critical thinking is a problem. The overconfidence without comprehension is especially frustrating, and it sounds like these juniors are skipping the fundamental learning process.

Teams ship code that works in tests but fails real-world [scenarios](https://jellyfish.co/solutions/scenario-planner/) because nobody thought to question the AI’s approach.

**Warning signs:**

- Developers copy-paste AI output without reading through the logic or understanding what each part does
- Code reviews focus only on syntax and formatting instead of questioning business logic or architectural decisions
- Junior developers can’t explain why the code works or what alternatives they considered before accepting the AI’s solution
- Bug reports increase for edge cases that human review would have easily anticipated, but AI missed

**How to prevent:**

- Set a 30-minute minimum review time for AI-generated PRs so reviewers read the code instead of skimming
- Assign your most experienced developers to spot-check AI code weekly and share what they find with the team
- Write test cases that deliberately break assumptions, like testing payment systems with zero, negative, and massive amounts
- Ask developers to trace through the code with real data on paper or a whiteboard before they merge anything

**Example:** AI generates a date validation function that handles every format perfectly. However, nobody noticed that it accepted February 30th as a valid date until financial reports started breaking. The AI focused on format parsing but ignored calendar logic.

### Loss of Context and Domain Knowledge

When AI does the thinking, human developers stop learning their own codebase. They know what prompts to use, but not why the database schema looks weird or why certain services communicate indirectly.

The tribal knowledge that helps teams make good decisions evaporates, leaving behind operators who can’t explain their own system.

**Why it matters:** Without deep system knowledge, teams can’t make informed decisions about the future. One Reddit developer [warned](https://www.reddit.com/r/ChatGPTCoding/comments/1h4f6ff/comment/lzygcht/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> When I am coding/building, I’m always asking myself, ‘Is there a better way?’ If I don’t have domain knowledge or do my research to gain said knowledge, then I can’t rely on the large language models (LLMs) to provide accurate guidance.

Teams go from owners to operators in their own system. They can follow AI instructions to add features, but can’t debug [complex issues](https://jellyfish.co/library/code-complexity/) or see when AI violates core principles they’ve forgotten.

**Warning signs:**

- Senior developers can’t answer basic questions about their own system’s design philosophy
- Nobody updates documentation because “AI will figure it out and streamline it when we need changes”
- Team members can’t draw a system diagram or explain how services communicate with each other
- Product managers make roadmap decisions without knowing which features are quick wins versus architectural overhauls

**How to prevent:**

- Document the “why” behind major decisions and make developers read it before using AI for related features
- Rotate developers through different parts of the codebase so everyone maintains broad system knowledge
- Create onboarding programs that focus on system understanding and advancements before [AI tool training](https://jellyfish.co/blog/ai-coding-tool-adoption-best-practices/)
- Build system maps and keep them updated so teams never lose sight of the full picture

**Example**: A team used AI extensively for two years and lost track of why their payment system had unusual validation rules. When regulations changed, nobody knew if the old rules were legal requirements or just preferences. They had to hire consultants to reverse-engineer their own business logic.

**PRO TIP 💡:** Teams losing domain knowledge don’t realize it until something breaks, and nobody understands the system. Jellyfish’s [engineering metrics](https://jellyfish.co/platform/engineering-metrics/) show when documentation updates stop, system knowledge concentrates in fewer people, and teams become unable to explain their own architecture. These signals predict future disasters months before they happen.

![Jellyfish Total Cycle Time](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Jellyfish-Total-Cycle-Time.png)

Ethical and Legal Risks: Bias, IP, and Data Privacy

## **Ethical and Legal Risks: Bias, IP, and Data Privacy**

AI tools might also bring legal and ethical considerations that need careful attention.

Models trained on public code can include copyrighted material, carry hidden biases, and handle sensitive data in ways that might violate privacy rules.

### Copyright Infringement and IP Tainting

Your codebase might contain snippets from GPL-licensed projects, proprietary algorithms from other companies, or verbatim copies of Stack Overflow answers with restrictive licenses.

In a 2025 survey, [38% of enterprise engineering teams](https://www.tabnine.com/blog/ai-copyright-risk-and-the-path-to-secure-ai-code-assistance) listed copyright infringement as their top concern when adopting AI tools.

**Why it matters:** Using copyrighted code without proper licensing can lead to expensive lawsuits and forced rewrites of core features. Trust is another casualty, as one developer noted:

> The unfortunate reality is, they can easily train their natural language models using your code, even if you paid for Copilot, and you would have no idea.
>
> _And even if you somehow found out, what are the chances of you going through with a lawsuit? And even if you won, they will simply eat the costs and keep doing it.”_
>
> _In order for Copilot to do what they say they will do, there has to be a regulatory standard enforced by the government that is strictly monitored. So I don’t trust Microsoft when they say they won’t train their LLMs with your code._

This means that your proprietary code might even end up training models that help competitors.

**Warning signs:**

- Function implementations match open-source projects exactly, including quirky workarounds or unusual approaches
- Generated code includes copyright headers, license text, or attribution comments from other projects
- AI produces complex algorithms or data structures that work perfectly on the first try without explanation
- Legal teams outline similarities between your AI-generated code and known proprietary implementations

**How to prevent:**

- Run code similarity scanners that compare AI output against known open-source and proprietary codebases
- Set up clear policies about which AI tools developers can use and what types of code they can generate
- Document the origin of all AI-generated code with prompts used and timestamps for potential legal defense
- Train developers to recognize and reject code that looks too polished or specific to be original

**Example:** A team’s AI-generated authentication code included comments and variable names from a popular MIT-licensed library, but they were using it in a way that violated the license terms. They had to refactor the code and add proper attribution after their legal team marked it during review.

### Perpetuating Hidden Bias

AI models absorb [biases](https://jellyfish.co/blog/how-to-identify-and-reduce-bias-all-types-of-bias-in-your-engineering-organization/) from their training data and pass them into your code.

What looks like neutral logic might actually discriminate — validation rules that reject non-English names, algorithms that favor certain zip codes, or scoring systems that penalize specific groups.

**Why it matters:** Biased algorithms create legal nightmares and PR disasters that can quickly spiral out of control. A single discriminatory feature can spark class-action lawsuits, regulatory investigations, and viral social media campaigns against your company.

**Warning signs:**

- Recommendation algorithms show different results based on zip codes that correlate with race or income
- Generated code uses “male/female” binary options without considering non-binary users or cultural contexts
- Credit scoring or risk assessment functions produce different results for similar profiles from different demographics
- Image processing code performs poorly on darker skin tones or assumes Western facial features as defaults

**How to prevent:**

- Test AI-generated code with diverse datasets that include edge cases from different demographics and cultures
- Include diverse team members in code reviews who can spot assumptions others might miss
- Create user personas from underrepresented groups and [test every feature](https://jellyfish.co/solutions/software-delivery-management/) against their needs
- Document and review all AI-generated decision-making code with your legal and ethics teams

**Example:** A loan application system’s AI-written code consistently offered lower credit limits to applicants with certain zip codes.

After customers complained on social media, the company found that the AI had learned biased patterns from historical lending data. They had to rebuild the system and offer remediation to affected users.

### Data Exposure and Privacy Violations

Developers paste production database schemas, customer information, API keys, and proprietary algorithms into AI systems without realizing that this data gets processed and stored externally.

Research shows that while 93% of organizations use AI, only [8% have governance fully embedded](https://www.itpro.com/technology/artificial-intelligence/organizations-face-ticking-timebomb-over-ai-governance). Not only that, but 54% have no formal AI risk policies in place.

**Why it matters:** Data breaches through AI tools violate GDPR, CCPA, and other privacy regulations that carry massive fines.

Your company’s trade secrets, customer PII, and security credentials become training data for models that competitors might access. Here’s how this Reddit developer [explained it](https://www.reddit.com/r/cybersecurity/comments/1hx980d/comment/m67q6bi/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> As a software developer, I have zero desire to log in and use any built-in IDE AI since they send all that data to an outside source most of the time. It frankly scares me that it’s being put right in our faces in IDEs as well as OS level stuff. The potential for data leaks is skyrocketing.

**Warning signs:**

- Support engineers paste customer emails, support tickets, and account details into AI to draft responses faster
- The infrastructure code containing database schemas, network topology, and cybersecurity group rules gets shared for AI review
- [AI coding assistants](https://jellyfish.co/blog/best-ai-coding-tools/) installed company-wide have read access to source code, documentation, and internal wiki pages
- Developers switch between personal and work contexts in the same AI session, so they mix confidential and personal data
- Proprietary algorithms, trade secrets, and competitive intelligence in code comments get sent to AI for explanation

**How to prevent:**

- Deploy DLP tools that scan outgoing requests and block prompts that contain SSNs, credit cards, or API keys before they reach AI
- Build synthetic datasets that replicate production patterns without using real names, emails, or account numbers
- Host AI models on your own servers or use enterprise agreements that guarantee data stays in your region and control
- Write explicit policies listing approved AI tools, forbidden data types, and consequences for violations

**Example:** A developer shared their company’s database schema with AI to get help with query optimization. Months later, a competitor’s developer received suspiciously similar table structures from the same AI tool.

While they couldn’t prove the leak, the company now wonders if their data model helped train the AI that assists their competition.

Risk Mitigation Strategies: 4 Best Practices for Engineering Leaders

## Risk Mitigation Strategies: 4 Best Practices for Engineering Leaders

These risks sound overwhelming, but you can manage them without slowing down the [development lifecycle](https://jellyfish.co/blog/sdlc-best-practices/). A few simple guardrails and boundaries can make all the difference.

Here are four strategies that protect your codebase without killing [productivity](https://jellyfish.co/blog/how-to-measure-developer-productivity/):

### 1\. Establish a Clear AI Usage Policy

Most AI policies fail for one of two reasons – they’re either so vague that nobody follows them (“use AI responsibly”) or so restrictive that developers ignore them entirely (“get written approval for every AI interaction”).

The policies that work give developers [clear boundaries](https://jellyfish.co/blog/how-to-talk-to-your-software-team-about-ai/) without treating them like children.

Your policy needs three core pillars that developers can remember and follow:

- **What you can use (approved tools):** List specific tools, versions, and subscription tiers that meet your security requirements. Update this monthly as new tools come out and existing ones change their data handling.
- **What you can’t share (data boundaries):** Draw clear lines around sensitive data – customer PII, production credentials, and proprietary algorithms never go into prompts. Create a simple classification system (green/yellow/red) so developers know what’s safe to share.
- **When you need review (risk triggers):** Authentication code, payment processing, and anything touching user data gets mandatory human review. Set these triggers in your PR templates so developers can’t accidentally skip them.

One person shared their comprehensive approach on Reddit that covers all the bases without overwhelming developers:

![Sample Acceptable Use Policy for AI Systems](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Sample-Acceptable-Use-Policy-for-AI-Systems.png)

(Source: [Reddit](https://www.reddit.com/r/cybersecurity/comments/1iynfc9/comment/mevudz4/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button))

This policy works because it’s specific enough to prevent problems but simple enough to remember. Developers don’t need a law degree to understand what’s allowed.

And to roll it out without resistance, you should keep these practices in mind:

- Start with a pilot group of senior developers who help refine the rules based on real-time usage
- Create a one-page quick reference that developers can pin to their monitors
- Run brown-bag sessions showing real examples of good and bad AI use
- Make compliance easy with IDE plugins that warn about sensitive data before it leaves your network

For example, let’s say a startup’s developer almost pasted their entire user authentication module into ChatGPT to debug a session issue. Their IDE plugin flags the code as high-risk and recommends using synthetic data instead.

The developer then creates a minimal test case without real user data, gets their answer, and avoids exposing their entire auth system to OpenAI’s training pipeline.

**PRO TIP 💡:** Policies only work if developers actually follow them. Jellyfish’s [AI Impact dashboard](https://jellyfish.co/platform/jellyfish-ai-impact/) shows you which teams use approved AI tools versus shadow IT alternatives, so you can see where your policies succeed (or get ignored). When you see a team using consumer ChatGPT despite having Copilot licenses, you know exactly where to focus compliance training.

![Jellyfish AI Impact](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/09/Jellyfish-AI-Impact-1.png)

### 2\. Mandate Rigorous Human Oversight

When developers write bad code, it usually looks bad too – messy formatting, confusing names, obvious shortcuts. But with AI, you have the opposite problem.

Every function looks professional with perfect indentation and thoughtful variable names, but underneath that polish, you’ll find SQL injections, client-side auth, and [edge cases](https://jellyfish.co/blog/unit-testing-automation/) that crash everything.

The best reviewers check AI code in three stages:

- **Quick scan (30 seconds):** Check formatting, syntax, and obvious red flags. Does the code compile? Are there hardcoded credentials or TODO comments left behind?
- **Logic check (5 minutes):** Verify the code solves the actual problem, not what the AI thought you meant. Walk through the main use case with real data to verify it works.
- **Deep analysis (15+ minutes):** Hunt for security risks, performance blockers, and edge cases the AI missed. Test with malicious input, null values, and boundary conditions to break assumptions.

Here’s a review checklist that catches most AI-generated problems:

|     |     |     |
| --- | --- | --- |
| **Code type** | **Must-check** | **Common AI failures** |
| **Authentication** | Password hashing algorithm, session token generation, brute force protection, timing attack resistance | AI often uses MD5/SHA1 instead of bcrypt, stores tokens in localStorage, or validates credentials client-side |
| **Database queries** | SQL injection prevention, query performance (EXPLAIN), transaction boundaries, index usage | AI concatenates strings instead of using prepared statements, creates N+1 query problems, or forgets indexes |
| **API endpoints** | Input validation completeness, rate limiting, error message leakage, CORS configuration | AI exposes stack traces in production, accepts any JSON without validation, or sets CORS to allow all origins |
| **Payment processing** | Decimal precision handling, idempotency keys, audit logging, error recovery | AI uses floating point for money, doesn’t handle duplicate charges, or logs sensitive card details |
| **Data processing** | Memory usage at scale, null/undefined handling, type coercion bugs, off-by-one errors | AI loads entire datasets into memory, crashes on unexpected nulls, or silently corrupts data through bad type conversion |

Make sure to rotate reviewers weekly so nobody gets stuck checking AI code all day. Fresh eyes catch more bugs than tired ones, and spreading the load prevents your best reviewers from burning out.

Also, set a maximum AI-generated code per PR. When developers submit 500+ lines of AI code at once, reviewers can’t possibly catch every issue. Smaller chunks get better scrutiny.

### 3\. Implement a Continuous Validation Strategy

Code review catches the obvious things, but AI code has subtle quirks that only show up later.

Maybe it handles 100 users perfectly but struggles at 1,000, or works great with test data but stumbles on real-world edge cases.

Build your validation strategy in three layers:

- **Pre-commit hooks (catch before commit):** Stop problems before they enter your repository. Run security scanners, check for hardcoded secrets, and verify code meets basic [quality standards](https://jellyfish.co/library/quality-metrics/).
- **CI/CD pipeline checks (catch before merge):** Run deeper analysis here with full test suites, performance benchmarks, and dependency vulnerability scans. This layer catches problems that need more time or resources to detect.
- **Production monitoring (catch in real-world use):** Watch how AI code behaves with real data and actual users. Monitor for performance degradation, unexpected errors, and security anomalies that only appear at scale.

Here’s what to run at each layer and what problems they catch:

|     |     |     |
| --- | --- | --- |
| **Validation layer** | **Tools to use** | **What they catch** |
| **Pre-commit** | Git secrets, ESLint, Prettier, basic security scan | Hardcoded credentials, API keys, obvious vulnerabilities, style violations |
| **CI/CD Pipeline** | SonarQube, Snyk, SAST tools, full test suite, load tests | Security vulnerabilities, code smells, test failures, and performance regression |
| **Production** | Datadog, Sentry, custom metrics, anomaly detection | Memory leaks, slow queries, error spikes, unusual patterns |
| **Weekly Audits** | Dependency check, license scanner, code complexity analysis | New CVEs, license violations, and technical debt accumulation |
| **Monthly Deep Scan** | Penetration testing tools, architecture review, and cost analysis | Advanced security issues, architectural drift, and cloud spend increase |

Set non-blocking warnings for minor issues. Developers see yellow flags for code smells but can still ship urgent fixes. Save hard blocks for more serious security problems and broken tests.

And provide clear fix instructions. When validation fails, show developers exactly what’s wrong and how to fix it. Generic “security scan failed” messages waste everyone’s time.

### 4\. Invest in Training and Critical Thinking

AI helps developers write more code, but more isn’t always better. Ten thousand lines of AI spaghetti cause more problems than a hundred lines of thoughtful code.

But with training, you can teach them the difference between shipping fast and [shipping smart](https://jellyfish.co/blog/when-is-it-going-to-ship-how-we-engineered-a-delivery-predictability-scoring-model/).

You can create the right mindset if you start with these three principles:

- **Question everything AI generates:** Build the reflex to doubt first, trust later. Developers should spot-check AI logic against real scenarios before accepting anything.
- **Understand before committing:** No more “it works but I don’t know why” in your codebase. Make sure that developers understand every line they commit, AI-generated or not.
- **Learn from AI failures:** Create a “failure library” of AI mistakes. Real examples from your own codebase teach better than any documentation.

If you run training sessions, start with volunteers who will eventually become champions. Let your most enthusiastic developers try the training first. When they catch bugs and share their wins, others will want in too.

But keep sessions short and practical. Nobody wants another three-hour workshop on theoretical concepts. Quick, focused sessions with immediate application beat lengthy lectures every time.

From Risk Mitigation to Engineering Intelligence with Jellyfish

## From Risk Mitigation to Engineering Intelligence with Jellyfish

You can build the best AI policies in the world, but they mean nothing if you can’t verify whether your teams really follow them.

That gap lets problems compound. Security flaws pass review, bad code piles up, and budget disappears into tools nobody uses.

You need [engineering intelligence](https://jellyfish.co/platform/engineering-management-platform/) to close this gap. In other words, you need **Jellyfish**.

Jellyfish connects to your engineering stack (Git, Jira, CI/CD pipelines, and AI coding tools) and analyzes every commit, PR, ticket, and deployment to show how your teams ship software from concept to production.

Here’s what our [AI Impact product](https://jellyfish.co/platform/jellyfish-ai-impact/) brings to the table:

- **Expose the gap between licenses and usage**: See exactly who codes with AI daily and who activated licenses once, then forgot about them. Break down usage by team, seniority, and project type to understand why some developers embrace AI while others avoid it completely.
- **Track productivity changes with engineering metrics**: Measure how AI affects [cycle times](https://jellyfish.co/platform/life-cycle-explorer/), PR velocity, and feature delivery rates with hard data instead of survey responses.
- **Identify risk patterns before they become incidents**: Spot teams over-relying on AI for critical code, developers who skip reviews on AI-generated PRs, or projects where AI usage correlates with increased bug rates.
- **Compare tool effectiveness across different contexts**: You might learn that GitHub Copilot accelerates your frontend team by 30% but slows down DevOps engineers who spend more time fixing its infrastructure code.
- **Calculate true ROI on AI investments**: Connect your $10,000 monthly AI spend to specific outcomes like reduced cycle times or increased throughput. If those Cursor licenses cost $5,000 but only save 10 developer hours monthly, you know where to cut.
- **Verify whether your AI policies work in practice**: Track whether teams follow review requirements for AI-generated authentication code and if developers can explain the code they commit.

The platform [connects to your development stack](https://jellyfish.co/platform/integrations/) through simple API integrations, pulling data from Git, Jira, CI/CD, and AI tools without disrupting workflows.

You get hard data on what works for your teams and your codebase, not advice based on what worked for someone else.

[**Schedule an AI Impact demo**](https://jellyfish.co/get-an-ai-impact-demo/) to get visibility into your team’s AI usage patterns and their actual effect on delivery.

FAQs About the Risks of AI in Software Development

## FAQs About the Risks of AI in Software Development

### What is the single biggest risk of using generative AI in a development process?

The biggest risk is AI-generated security vulnerabilities that pass code review because they look correct.

AI produces authentication code that validates on the client side, SQL queries vulnerable to injection, or encryption implementations that seem secure but use outdated algorithms. These flaws hide behind clean syntax and proper formatting until attackers find them first.

### How can we safely use open-source AI models if they are prone to package hallucinations?

Treat every AI package suggestion as potentially fake or malicious. AI models hallucinate convincing library names that don’t exist or worse, match malicious packages that attackers created to exploit this exact vulnerability.

Always verify packages exist on official repositories, check download counts and maintenance history, and validate the package does what you need before you install anything.

### Is it possible to completely eliminate the risks of using AI?

No, you can’t eliminate all AI risks any more than you can eliminate all risks from hiring developers.

You can reduce risks to acceptable levels through policies, scanning automation, and human oversight, but some AI-generated bugs will eventually slip through.

Learn More About AI in Software Development

## Learn More About AI in Software Development

- [What is the Impact of AI on Software Development?](https://jellyfish.co/library/ai-in-software-development/)
- [Benefits of AI in Software Development](https://jellyfish.co/library/ai-in-software-development/benefits/)
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