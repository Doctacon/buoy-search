---
url: "https://jellyfish.co/library/pull-request/"
title: "What is a Pull Request? | Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/pull-request/#content)

![Jellyfish](https://jellyfish.co/wp-content/uploads/2023/08/Jellyfish_General_Featured-Image_Logo_Electric-Seaweed_Green_450x200.webp)

## What is a Pull Request?

A **pull request** is a formalized way for developers to propose and collaborate on code changes before merging them into a shared codebase.

Pull Requests allow for easy, distributed management of collaborative software projects and provide a structure for quickly proposing and approving changes in a code base. The typical process for introducing such changes begins with a developer modifying the code on a local branch of a repository, followed by the developer “requesting” that said local branch be “pulled” into the repository’s main one. The PR is then reviewed by another developer who provides comments and who requests additional changes before the original change is finally merged into the main branch.

Rather than direct alterations to a code base, a pull request solicits reviews and feedback before amalgamation into the primary code repository. This process minimizes the risk of introducing destabilizing elements or impairing the project’s functionality.

Distinguishing between “pull request” and “ **merge request**” can be subtle but significant. Although often used interchangeably, the two phrases are subtly different —almost akin to two dialects of the same language. A merge request, while similar to a pull request, contains an implicit concept wherein the request originates from a branch in the same repository.

Jellyfish Research

#### Do Larger Pull Requests Receive More Extensive Reviews?

[Read Post](https://www.jellyfish.co/blog/larger-pull-requests/)

![](https://jellyfish.co/wp-content/uploads/2023/07/Blog-Large-Pull-Req.jpg)

## Creating a Pull Request

Creating a pull request involves several steps, and the exact process may vary depending on the platform you’re using for version control (e.g., GitHub, GitLab, Bitbucket). Below is a general guide using GitHub as an example:

1. **Fork the Repository:**
   - Click “Fork” on the top right of the repository’s page. This makes a copy under your GitHub account.

2. **Clone Your Fork:**
   - Clone the forked repository to your local machine: \`git clone https://github.com/<your-username>/<repository>.git\`

3. **Create a New Branch:**
   - Create a new branch for your changes: \`git checkout -b feature-branch\`

4. **Make Changes and Commit:**
   - Make your changes to the code.
   - Stage and commit your changes: \`git add .\` and \`git commit -m “Add feature or fix issue”\`

5. **Push Changes and Create Pull Request:**
   - Push changes to your fork on GitHub: \`git push origin feature-branch\`
   - Visit your fork on GitHub, switch to the new branch, and click “New Pull Request.”
   - Set the base and compare branches, add a title and description, then click “Create Pull Request.”

## The Pull Request Review Process

The pull request review process essentially allows errors to be detected and rectified before deployment, eliminating the risk and overhead of dealing with unpredicted issues in a live production environment. The best part of the pull request review lies in its collaborative nature. It allows for a community of developers to offer constructive feedback, suggest improvements, and refine the proposed changes until they are deemed suitable for integration. This not only enhances the overall quality of the code but also fosters a culture of shared responsibility and mutual learning among the team members.

When a pull request is made, it commonly undergoes various stages of the review process. While these stages might differ from one project to another, a basic pull request review often involves an initial self-review by the code author, followed by peer reviews from fellow developers, and finally, an approval or rejection from a project maintainer or a dedicated reviewer. Notably, using the correct pull request command is integral to the review process. Different commands can trigger specific actions during the process, such as pushing changes, fetching data, and merging the approved code.

Mastering these commands in the respective version control system, such as Git, is indispensable for an efficient and comfortable review workflow. In the broader perspective of the [DevOps lifecycle](https://www.jellyfish.co/library/devops-lifecycle/), the pull request review process also plays a significant role in maintaining and improving [DevOps metrics](https://www.jellyfish.co/library/devops-metrics/): [deployment frequency](https://www.jellyfish.co/blog/breaking-down-deployment-frequency/), [change failure rate](https://www.jellyfish.co/blog/change-failure-rate/), [change lead time](https://www.jellyfish.co/library/change-lead-time/), and [mean time to recovery](https://www.jellyfish.co/library/mean-time-to-recovery-mttr/).

By ensuring that only thoroughly vetted and high-quality code makes it to the deployment, the review process contributes towards more frequent, stable, and reliable deployments. This ultimately culminates in improved performance, productivity, and satisfaction both for the development team and the end-users.

## Merging and Deploying Pull Requests

Once a pull request is approved, it enters the merging and deploying phase. Here, the changes made in the pull request are integrated into the main code branch, making it part of the product’s live version. Navigating through the merging and deployment processes responsibly unveils the strategic value of continuous integration continuous deployment systems. In a [CI/CD](https://www.jellyfish.co/library/ci-cd/) environment, every change to the codebase undergoes automated testing to ensure it doesn’t introduce errors.

After the tests have passed, the changes can be deployed to the production environment for real-world use. These automated processes tout a few business advantages, including quicker release times, a reduction in errors, and the capacity to catch and resolve issues swiftly. Nonetheless, deploying changes doesn’t signify the end of responsibilities.

After deploying the changes, continual monitoring is enforced as a critical part of the life cycle to ensure that the integration of new code into the main branch doesn’t introduce unwanted glitches or hiccups in the system. Indeed, in an era where software underpins operations across industry verticals, flawless merging and deploying pull requests and continuous monitoring become imperative.

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-Data-Hub-1024x610.png)](https://jellyfish.co/blog/dora-metrics-tools/)[**8 Top-Rated Tools for Measuring DORA Metrics**](https://jellyfish.co/blog/dora-metrics-tools/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-tools/)

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

Qualified