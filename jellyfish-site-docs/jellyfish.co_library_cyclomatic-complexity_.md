---
url: "https://jellyfish.co/library/cyclomatic-complexity/"
title: "Cyclomatic Complexity Definition, Calculation & Examples"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/cyclomatic-complexity/#content)

In this article

The art of software development often involves striking a delicate balance between creating intricate, powerful applications and maintaining clean, efficient code. That balance is getting recalibrated today, as engineers are wrangling with the best ways to use AI. To pull off this ever-changing balancing act, software engineers must first understand cyclomatic complexity in software engineering.

But what is cyclomatic complexity? What can it tell you about the complexity of your code? How can software programmers use it to drive value and efficiency in their projects?

What is Cyclomatic Complexity?

## **What is Cyclomatic Complexity?**

**Cyclomatic complexity** **is a** [**software metric**](https://jellyfish.co/library/software-development-kpis/) **that quantitatively measures the complexity of a program’s code. It helps developers build an understanding of the intricacy of their programs, enabling them to make decisions about code changes and maintenance.**

Backed by this deeper understanding of their program’s structure, programmers can measure the code’s intricacy with greater accuracy and understand the implications that intricacy may have on the maintainability, reliability, and overall quality of a piece of software across various programming languages, such as Python, Java, or JavaScript.

First developed by Thomas J. McCabe Sr. back in 1976, cyclomatic complexity is based on graph theory and the evaluation of control flow graphs. The underlying principle behind his work was to provide programmers with an easily understood way to identify potential areas of complexity in a program.

McCabe accomplished this by creating a metric that examined the possible paths through which code execution can take place. This analysis would then provide insights into the code’s structural intricacies, revealing how challenging it may be to test and debug programs since more complex code would naturally require more extensive testing procedures.

It is important to note that the sole determinant of code efficiency cannot only be cyclomatic complexity, meaning other factors must also be taken into account.

These factors may include code readability, [**code complexity**](https://www.jellyfish.co/library/code-complexity/), and [**cognitive complexity**](https://www.jellyfish.co/library/cognitive-complexity/). However, cyclomatic complexity is a valuable tool for assessing software quality and provides a useful starting point when identifying areas for improvement or refactoring.

While measuring cyclomatic complexity can help engineers understand the technical intricacy of their code, it is important for leaders not to get too caught up in tactical metrics. Engineering leaders must focus on connecting the dots back to quantifiable business impact, rather than meddling too deeply in the weeds with tactical tasks.

Cyclomatic Complexity Calculation

## **Cyclomatic Complexity Calculation**

Now that we understand the overall purpose of this important metric, let’s find out how to calculate cyclomatic complexity. Calculate the number of linearly independent paths through a program’s source code, which corresponds to the number of decision points within the code plus one.

**Essentially, this formula helps to gauge how much branching occurs via decision structures within a program, as each branch introduces more potential paths for execution.**

To effectively apply this formula in software testing, it is essential to first represent your source code as a control flow graph (CFG). A CFG is a directed graph where each node represents a basic block or sequence of non-branching statements, and edges signify control flow between those blocks. Once you have created the CFG for your source code, you can start calculating cyclomatic complexity using any of the three methods we will discuss.

The key components of a program’s CFG include:

- **Nodes**: Individual commands or statements.
- **Edges**: Connect nodes.
- **Connected components**: Isolated sections of the graph.

When calculating cyclomatic complexity, you can use 3 different approaches:

1. **Basic cyclomatic complexity formula**: Cyclomatic Complexity = E – N + 2P, where E corresponds to edges, N to nodes, and P to connected components.
2. **Counting decision points**: Cyclomatic Complexity = Number of decision points + 1.
3. **Summing up predicate nodes**: Cyclomatic Complexity = Sum of all predicate nodes + 1.

In each approach, you will calculate an integer cyclomatic complexity value that represents the number of unique pathways through your code.

This value indicates not only how difficult it might be for developers to understand but also impacts testers’ ability to ensure optimal performance from their application or system properly.

Higher values suggest greater intricacy and reduced comprehensibility, while lower numbers imply a more straightforward, easy-to-follow structure.

For example, consider this very straightforward function:

def simple\_function(x):

if x > 0:

print(“X is positive”)

else:

print(“X is not positive”)

In this case:

- E = 2 (number of edges)
- N = 3 (number of nodes)
- P = 1 (single connected component)

Using the formula, the cyclomatic complexity is: _CC = 2 – 3 + 2\*1 = 1_

So, the cyclomatic complexity of this function is 1, indicating very low complexity.

By understanding how to calculate cyclomatic complexity, developers and software testers can better manage code quality and ensure that their testing efforts focus on the most critical areas of the program.

Practical Calculation Examples

## **Practical Calculation Examples**

Let’s look at a few more examples of cyclomatic complexity and illustrate how it can increase:

### **1\. Multiple Conditions**

def check\_grade(score):

\# Decision Point 1:

if score >= 90:

grade = ‘A’

\# Decision Point 2:

elif score >= 80:

grade = ‘B’

\# Decision Point 3:

elif score >= 70:

grade = ‘C’

\# Decision Point 4:

elif scope >= 60:

grade = ‘D’

else:

grade = ‘F’

print(f”Grade is: {grade}”)

\# Calculation using Decision Points:

\# Number of decision points = 3 (‘if’, ‘elif’, ‘elif’, ‘elif’)

\# Cyclomatic Complexity = 4 + 1 = 5

This function has a cyclomatic complexity of 5, indicating five distinct paths through the code, corresponding to the different grade assignments.

### **2\. Loop with a Condition**

def process\_items(items):

count = 0

\# Decision Point 1: loop condition (implicit)

for item in items:

\# Decision Point 2:

if item > 10:

count += 1

print(f”Found {count} items > 10″)

\# Calculation using Decision Points:

\# Number of decision points = 2 (‘for’ loop check, ‘if’ statement)

\# Cyclomatic Complexity = 2 + 1 = 3

This function has a slightly lower complexity of 3. The loop itself introduces a decision (continue looping or exit), and the if statement inside adds another branching point.

### **3\. Nested Conditions**

def check\_access(user\_role, resource\_level):

\# Decision Point 1: user\_role == ‘admin’

if user\_role == ‘admin’:

access = True

else:

\# Decision Point 2: resource\_level <= 1 (nested)

if resource\_level <= 1:

access = True

else:

access = False

print(f”Access granted: {access}”)

\# Calculation using Decision Points:

\# Number of decision points = 2 (outer ‘if’, inner ‘if’)

\# Cyclomatic Complexity = 2 + 1 = 3

This function has a cyclomatic complexity of 3. Each ‘if’ statement represents a decision point, contributing to the overall complexity. Nested structures like this can quickly increase the number of paths.

Each example of cyclomatic complexity above demonstrates how different code structures contribute to the overall calculated value.

Cyclomatic Complexity Benefits

## **Cyclomatic Complexity** **Benefits**

Analyzing cyclomatic complexity offers several distinct advantages for software development teams aiming to improve code quality and efficiency. By quantifying the number of logical paths in code, this metric provides valuable insights that translate into tangible benefits:

- **Improved risk identification:** It highlights complex code sections that are statistically more likely to contain defects or be difficult to test thoroughly, allowing teams to proactively identify and manage high-risk areas.
- **Enhanced code maintainability:** By pinpointing overly complex functions or modules, it guides efforts towards simplification, resulting in code that is easier to understand, modify, and debug, ultimately reducing long-term maintenance overhead.
- **More accurate test effort estimation:** The complexity score offers a quantitative basis for estimating the minimum number of test cases required to cover the logical paths within a piece of code (aiming for path coverage), aiding in more realistic test planning and scheduling.
- **Optimized resource allocation:** Knowing which parts of the codebase are most complex allows managers and team leads to direct [**resources more effectively**](https://jellyfish.co/blog/engineering-resource-planning/), ensuring that the most intricate or critical areas receive adequate attention.
- **Foundation for increased reliability:** By indicating the number of independent paths, it helps ensure that test strategies can be designed for more comprehensive validation and better code coverage, contributing to a more stable, predictable, and reliable final product.
- **Objective basis for refactoring:** Cyclomatic complexity provides a clear, data-driven trigger for identifying specific code segments that are prime candidates for refactoring, helping teams prioritize efforts to improve the codebase’s internal structure and quality.
- **Quantitative quality insight:** It offers an objective, measurable indicator of code complexity, complementing subjective code reviews and providing concrete data points for [**tracking** **code quality**](https://jellyfish.co/library/quality-metrics/) trends over time.

Uses of Cyclomatic Complexity

## **Uses of Cyclomatic Complexity**

Beyond its general benefits, cyclomatic complexity is applied in several specific ways throughout the software development lifecycle:

- **Test planning and prioritization:** Teams use complexity scores to identify modules or functions that require more rigorous testing efforts and conduct [**capacity planning**](https://jellyfish.co/blog/engineering-capacity-planning/) Highly complex units often receive higher priority for test case design.
- **Risk assessment:** High cyclomatic complexity is often correlated with a higher likelihood of defects. It serves as an indicator to flag potentially risky areas of the codebase that might need preemptive reviews or refactoring.
- **Code review** **focus:** During peer reviews, reviewers can use complexity metrics to quickly pinpoint code sections that might be difficult to understand, maintain, or test, ensuring these areas receive closer scrutiny.
- **Refactoring** **guidance:** The metric directly highlights functions or methods that are prime candidates for refactoring. A high score suggests a piece of code could likely be broken down into smaller, simpler, and more manageable units.
- **Measuring maintainability:** Cyclomatic complexity is frequently used as a key input when calculating broader software maintainability indices, providing a quantitative measure of how easy (or difficult) it might be to modify or extend the software.
- **Enforcing coding standards:** Some development teams or organizations incorporate maximum acceptable cyclomatic complexity thresholds into their coding standards or automated quality gates to prevent overly complex code from being committed.

For software developers, testers, and [**engineering project managers**](https://jellyfish.co/library/engineering-management-vs-project-management/) seeking to optimize code quality and performance, maximizing the benefits of cyclomatic complexity is vital. Incorporating this metric into a suite of other quality metrics empowers better, more strategic choices regarding both development priorities and resource allocation.

How to Test Cyclomatic Complexity

## **How to Test Cyclomatic Complexity**

While you don’t technically “test” cyclomatic complexity itself (as it’s a metric, not a feature), the metric is a fundamental tool used within the software testing process. It provides quantitative data that helps guide testing strategy, design effective test cases, and assess risk.

Here’s how testers typically leverage the cyclomatic complexity value.

### **Defining Test Scope with Basis Path Testing**

- **Determine the minimum number of paths:** The primary application of the cyclomatic complexity value in white box testing is determining the number of linearly independent paths through a module’s source code.
- **Guide test case design:** This value indicates the theoretical minimum number of test cases required to ensure that every independent execution path is exercised at least once. This technique, known as Basis Path Testing, aims for structural code coverage. Testers use the control flow graph (implied by the CC calculation) to design inputs that force execution along these specific paths.

### **Prioritizing Testing Efforts**

- **Focus testing on high-risk areas:** Modules or functions exhibiting higher complexity are often prioritized for more intensive testing and scrutiny during the testing process.
- **Allocate resources effectively:** Testers and QA managers can use the complexity metric to justify allocating more time, personnel, and testing tools towards complex components, as these areas statistically have a higher probability of containing defects.

### **Assessing Code Testability**

- **Identify code that is difficult to test:** An extremely high cyclomatic complexity score can signal that a piece of code is inherently difficult to test comprehensively due to its numerous paths and intricate decision structures.
- **Inform refactoring needs:** This assessment might lead testers to collaborate with developers and recommend refactoring the complex module before extensive testing is feasible, thereby improving the overall efficiency and effectiveness of quality assurance activities.

### **Leveraging Automation Tools**

- **Integrate automated calculation:** Most modern static analysis testing tools, and many integrated development environments (IDEs), can automatically calculate cyclomatic complexity for various programming languages like Python, Java, or JavaScript.
- **Streamline the testing process:** This automation makes the metric readily accessible to testers, eliminating the need for manual calculation or graph analysis. This allows them to easily incorporate complexity insights into their daily workflows and reporting.

How to Reduce Cyclomatic Complexity

## **How to Reduce Cyclomatic Complexity**

Fortunately, several strategies exist for reducing cyclomatic complexity within an application’s source code. These approaches focus on decreasing the number of distinct execution paths and simplifying the decision-making logic within functions or methods.

### **Break Down Large Functions (Modularization)**

One highly effective method is to decompose large, monolithic functions into smaller, more focused units, each responsible for a single, specific task.

Modularizing code this way significantly improves comprehension and [**debugging**](https://jellyfish.co/blog/developer-experience-best-practices/), as each smaller function is easier to grasp in isolation. It also promotes code reusability across different parts of the application.

### **Simplify Branching Logic**

Another key technique involves adopting clear and concise branching structures. Aim to minimize nested conditional statements, such as deeply layered if-else blocks or loops within loops, as these decision structures directly increase complexity

Instead, favor simpler constructs where possible, like using switch-case statements (or their equivalents) for multiple condition checks on the same variable, or implementing early returns (guard clauses) to exit a function as soon as a condition fails, reducing nesting depth.

### **Apply Design Patterns**

You can also leverage established design patterns, particularly those emphasizing the separation of concerns and encapsulation.

Patterns like Strategy, Command, or decomposing complex logic into smaller classes help ensure that each class or module has a single, well-defined responsibility.

This minimizes interdependencies and naturally leads to simpler control flow within individual methods, thus reducing complexity.

### **Leverage Automated Testing**

While [**automated testing**](https://jellyfish.co/blog/sdlc-best-practices/) itself doesn’t directly reduce complexity, it plays a vital role in managing it. Implementing thorough unit tests allows developers to refactor complex code with confidence, knowing that the functionality remains correct.

Rigorous testing often highlights areas where logic is convoluted or hard to test, pinpointing specific functions or modules that could benefit from simplification or refactoring to improve both complexity scores and overall maintainability.

Understanding how to apply these techniques to reduce cyclomatic complexity is crucial for crafting efficient, maintainable software applications that are easier to comprehend and modify.

Cyclomatic complexity analysis, combined with these reduction strategies, serves as an invaluable tool for guiding program optimizations and simplifying future development efforts.

Ready to Drive Engineering Impact?

## **Ready to Drive Engineering Impact?**

See how Jellyfish can [**enable your teams**](https://jellyfish.co/platform/engineering-management-platform/) to work smarter, feel empowered, and deliver better outcomes for the business.

About the author

![Marilyn C. Cole](https://jellyfish.co/wp-content/uploads/2022/11/Marilyn-Cole.jpg)

Marilyn is an Engineering Manager at Jellyfish. Her specialities include communicating, programming, researching, working well with others and with the command line, leading, being independently motivated to learn and to create.

She primarily works in Java, JS (mostly React/Redux, some NodeJS, MongoDB, and Angular), and python, with previous experience in PHP, Haskell, C, Perl, and Ruby. Diverse interests along the full stack have led to a plethora of other familiarities, including git, AWS (mostly ECS, S3, RDS, Dynamo, and Cost Explorer), Jenkins, TravisCI, PostgreSQL, Spring, mvn, svn, MySQL, XML, XSLT, CSS, sed, yacc, x86 assembly, and many other acronyms.

Follow: [LinkedIn](https://www.linkedin.com/in/marilynccole/)

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-Data-Hub-1024x610.png)](https://jellyfish.co/blog/dora-metrics-tools/)[**8 Top-Rated Tools for Measuring DORA Metrics**](https://jellyfish.co/blog/dora-metrics-tools/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-tools/)

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

Qualified