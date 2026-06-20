---
url: "https://jellyfish.co/library/code-smells/"
title: "What are Code Smells? | Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/code-smells/#content)

![Jellyfish](https://jellyfish.co/wp-content/uploads/2023/08/Jellyfish_General_Featured-Image_Logo_Electric-Seaweed_Green_450x200.webp)

## What are Code Smells?

Code smells are specific signals or symptoms in a coding environment that raise red flags for potential issues.

Programmer and thought leader Kent Beck coined the term “code smells” to describe code-related symptoms requiring attention. They point to deeper problems in a system and can significantly impact your software’s sustainability, maintainability, and readability.

Code smells highlight areas in a codebase that could potentially be problematic and impact the program’s performance. These warning signs don’t necessarily imply a bug in the system; rather, they suggest weaknesses in design that may slow down development or increase the risk of bugs or system failures in the future.

Code smells can manifest in various forms and are often subjective, making their identification challenging. Despite this subjectivity, several commonly agreed-upon code smells consistently appear in discussions on best coding practices. These include excessively long methods, duplicated code, and overuse of comments, among others.

eBook

#### 10 KPIs Every Engineering Leader Should Track

[Read Now](https://www.jellyfish.co/resources/10-kpis-engineering-leaders-should-track/)

![](https://jellyfish.co/wp-content/uploads/2023/10/thumbnail-10KPIs-ebook.png)

## Types Of Code Smells

Code smells are not problems per se, but they can hinder the smooth running of the code and, hence, the ultimate performance of the software. There are various types of code smells. Examples of code smells include but are not limited to the following:

- **Long Method**: a programming method that is excessively long and spans many lines, making it difficult to read and understand. Long methods can pose a serious threat to effective debugging and maintenance, as they can make it challenging to identify and resolve issues. To avoid long methods, programmers should aim to break down complex tasks into smaller, more manageable pieces of code.
- **Large Class:** a class that has assumed too many responsibilities, making it overly complex and difficult to maintain. By taking on too many responsibilities, large classes can pose a significant challenge to the Single Responsibility Principle, which is a fundamental principle of software development. To avoid large classes, programmers should aim to create classes that have a clear and well-defined responsibility.
- **Data Clumps**: a group of variables or data fields that appear together frequently and are often used together. This grouping of data is often necessary for the functionality of a particular feature or system.
- **Primitive Obsession**: the practice of relying heavily on primitive data types, such as integers, strings, and booleans, to represent complex domain concepts. This can lead to code that is difficult to understand and maintain, as well as potential bugs and limitations in functionality.
- **[Duplicate Code](https://www.jellyfish.co/library/duplicated-code/):** code declarations that are replicated in multiple locations within a program but are no longer referenced elsewhere. Duplicate code can lead to confusion and errors in the codebase, as changes made to one instance of the code may not be reflected in the other instances. To avoid duplicate code, programmers should aim to create reusable functions and modules that can be used throughout the program.
- **[Dead Code](https://www.jellyfish.co/library/dead-code/):** code declarations that are no longer referenced elsewhere in the program. Dead code is a common issue in software development and can pose a serious threat to program performance, as it can take up valuable resources without providing any benefit. To avoid dead code, programmers should regularly review and remove any code that is no longer required.

When you identify code smells in your code, it’s important to choose the best process for refactoring. This involves recognizing the type of smell and using a suitable technique to reduce or eliminate its impact.

For example, if you encounter a Long Method, you can apply the Extract Method refactoring technique. This involves breaking down the lengthy method into smaller, more manageable ones.

In the case of a Large Class, you can move methods to other classes using the Extract Class technique. This helps reduce the burden on the class. Similarly, for duplicate code, you can use the extract or Pull-up methods to remove redundancy. And when dealing with Dead Code, safely deleting it through the Safe Delete technique is recommended.

Refactoring code smells is crucial for maintaining and improving software quality. Each type of code smell represents a unique aspect of the code structure that requires attention, and different refactoring techniques are applicable.

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-Data-Hub-1024x610.png)](https://jellyfish.co/blog/dora-metrics-tools/)[**8 Top-Rated Tools for Measuring DORA Metrics**](https://jellyfish.co/blog/dora-metrics-tools/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-tools/)

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

Qualified