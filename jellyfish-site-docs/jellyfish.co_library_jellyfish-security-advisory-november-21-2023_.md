---
url: "https://jellyfish.co/library/jellyfish-security-advisory-november-21-2023/"
title: "Jellyfish Security Advisory  November 21, 2023 - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/jellyfish-security-advisory-november-21-2023/#content)

**Advisory ID: JELLY-SA-2023-001**

CVSS v4.0 Score: 2.1/Low

Publication Date: 2023-11-21

Last Revision Date: 2023-11-21

Status: Fixed

Document Revision: 1

**\# Overview**

Jellyfish has improved the Jellyfish Agent such that it no longer prints 2 characters of the supplied JIRA password to stdout. Customers unaware of the old behavior may have had 2 characters of their integration’s JIRA passwords logged more broadly than intended in their environment.

The issue was discovered internally by Jellyfish team members.

**\# Description**

Jellyfish has improved the Jellyfish Agent such that it no longer prints 2 characters of the supplied JIRA password to stdout. Previous versions of the agent printed 2 characters to help customers debug issues. However, this may not have been expected and customers who executed their agents in permissive locations may have revealed more information than desired.

It was discovered that bearer tokens were not affected by this vulnerability.

**\# Impact**

This issue only affects customers who used a JIRA username and password as their integration method. Customers using Bearer Tokens are unaffected.

Only 2 characters of the password are logged to stdout. No part of the passwords leaves your local environment.

Customers are at risk only if:

_1\. They’re running their agent in a location where stdout can be observed by people other than who they intend to be able to view the JIRA password._

_2\. Those people can’t view the JIRA password elsewhere._

**\# Affected Product(s)**

This affected the Jellyfish Agent (jf\_agent) prior to February 8th, 2023. It was fixed in _https://github.com/Jellyfish-AI/jf\_agent/commit/6ce761d786157de7e93399612d764bd1553e62d2_

**\# Solution**

To prevent this issue, Jellyfish Agent administrators should ensure they are running an up-to-date version of the agent:

_1\. If you’re using Docker images: ensure you’re pulling the current \`latest\` or \`stable\` tag._

_2\. If you’re running from source, ensure your HEAD includes 6ce761d786157de7e93399612d764bd1553e62d2_

If you have been storing/displaying the agent’s stdout and want to determine if 2 characters of your JIRA password has been displayed you can search for the string:

”  Password: “

(Excluding the quotes)

**\# Vulnerability Metadata**

Severity/Urgency: Green (Low)

CVSS v4.0 Vector: CVSS:4.0/AV:L/AC:L/AT:P/PR:N/UI:N/VC:N/VI:N/VA:N/SC:L/SI:L/SA:N/S:N/AU:Y/R:U/V:D/RE:L/U:Green

**\# Timeline**

\## February 8, 2023

1:43PM Eastern – Pull request is updated to include fix and is merged. Issue is resolved.

10:21AM Eastern – Jellyfish engineer reaches out to security. Security recommends masking the password entirely instead of printing 2 characters of the password.

\## February 6, 2023

6:13PM Eastern – Pull request is posted which updates code near where the printing of 2 characters was happening

11:37PM Eastern – Reviewer recommends reaching out to security to determine if we should stop printing any characters of the password.

**\# Credits/Contact**

If you have questions regarding this issue, please contact us at:

support@jellyfish.co.

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-Data-Hub-1024x610.png)](https://jellyfish.co/blog/dora-metrics-tools/)[**8 Top-Rated Tools for Measuring DORA Metrics**](https://jellyfish.co/blog/dora-metrics-tools/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-tools/)

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

Qualified