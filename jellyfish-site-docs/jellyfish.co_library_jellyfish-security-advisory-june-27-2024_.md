---
url: "https://jellyfish.co/library/jellyfish-security-advisory-june-27-2024/"
title: "Jellyfish Security Advisory June 27, 2024 - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/library/jellyfish-security-advisory-june-27-2024/#content)

Advisory ID: JELLY-SA-2024-002

CVSS v4.0 Score: 7.7/High

Publication Date: 2024-06-27

Last Revision Date: 2024-06-27

Status: Fixed

Document Revision: 1

#### Overview

Jellyfish is aware of the ongoing supply-chain compromise relating to the polyfill.io domain and polyfill.js’s GitHub account \[1\]\[2\]. On June 26th, Jellyfish security performed a thorough audit of our supply-chain to determine whether we were affected. We determined that one dependency we rely on, CommandBar, included code that, under very special circumstances, would cause scripts to load from polyfill.io.

Jellyfish Security reached out to CommandBar at 2:18 PM Eastern the same day to let them know of the issue. CommandBar confirmed Jellyfish’s impact assessment (see below) and informed Jellyfish that a fix was underway.

By 3:30 PM CommandBar had removed the reference to polyfill.io and Jellyfish Security validated that Jellyfish users were no longer vulnerable.

In addition, Jellyfish security has determined that over 97% of users we’ve served since February 2024 are not affected. The remaining 3% we are unable to determine impact for due to privacy controls that prevent us from determining the browser version. Customers are encouraged to review their network traffic and clients to confirm they are unaffected. Refer to the “Affected Product(s) and Users” section below for more information.

#### Impact

Information regarding the specific malware distributed by polyfill.io is constantly changing \[2\]. While at the time of this writing the domain is being served by a Cloudflare mirror \[1\] we can not be certain that will persist or has been the case previously. Therefore, out of an abundance of caution, Jellyfish is not ruling out that malicious JS could have been served to a small subset of our users between February 2024 and June 26th at 3:30PM Eastern.

In the worst case, this could’ve allowed an attacker to view and change data available to the compromised Jellyfish user.

#### **Affected Product(s) and Users**

CommandBar is only used by https://app.jellyfish.co so only users who have logged into that service had a chance of being affected.

In addition, code from polyfill.io was only loaded by CommandBar under very specific circumstances. In particular, it would only load the script if the user’s browser did not support one of the following Web APIs:

1. Object.assign() \[3\]
2. Symbol.for() \[4\]
3. Symbol() \[5\]

Which is only the case for very old web browsers. Here is a list of the latest vulnerable version of various web engines:

Chrome: 44

Safari: 8

Internet Explorer: 11

Firefox: 35

Opera: 31

Android WebView: 44

In addition, “Login with Google” and “Okta”-based SSO logins have been confirmed to not work in vulnerable clients.

Therefore, only users:

1. Who logged into https://app.jellyfish.co succesfully
2. Were using a browser engine older than or equal to one in the aforementioned list
3. Who are using username/password-based logins to Jellyfish or non-Okta SSO providers .
4. And whose network settings allowed outgoing connections to polyfill.io

Could be affected. We determined this is, in the absolute worst case, less than 3% of our users.

#### Solution

Thanks to quick work by CommandBar, the issue has already been contained and current users of Jellyfish are not at risk.

Customers are encouraged to review logs to rule out exploitation completely. Jellyfish is able to help customers determine the specific users who might have been running vulnerable clients, and we are happy to work with you. Reach out to us using the details in the “Credits/Contact” section below.

In addition, consider monitoring for the indicators of compromise provided by sansec.io here: [https://sansec.io/research/polyfill-supply-chain-attack](https://sansec.io/research/polyfill-supply-chain-attack)

#### Vulnerability Metadata

Severity/Urgency: Amber (Medium)

CVSS v4.0 Vector:

CVSS4.0/AVN/ACL/ATP/PRN/UIP/VCH/VIH/VAH/SCL/SIL/SAL/EA/AUY/RU/VD/REM/UAmber

#### Timeline

##### June 26, 2024

2:00 PM Eastern – Jellyfish security performed an audit of our app’s supply chain and determined that one vendor we depend on could, under special circumstances, load scripts from https://polyfill.io. As such, Jellyfish security started an incident.

2:18 PM Eastern – Jellyfish security reached out to the affected vendor. The vendor confirmed Jellyfish’s impact analysis and reported that a fix was underway.

3:30 PM Eastern – Our vendor let us know the issue was fixed. Jellyfish security validated that the code that could make requests to https://polyfill.io no longer appeared in our app.

3:58 PM Eastern – Jellyfish security determined the list of affected browser versions that users would have needed to use to be affected. Jellyfish confirmed that over 97% of our users do not user vulnerable browser versions.

#### Credits/Contact

If you have questions regarding this issue, please open a support case at [https://help.jellyfish.co/](https://help.jellyfish.co/)

#### References

\[1\] [https://www.sonatype.com/blog/polyfill.io-supply-chain-attack-hits-100000-websites-all-you-need-to know](https://www.sonatype.com/blog/polyfill.io-supply-chain-attack-hits-100000-websites-all-you-need-to%20know)

\[2\] [https://sansec.io/research/polyfill-supply-chain-attack](https://sansec.io/research/polyfill-supply-chain-attack)

\[3\] [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Object/assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)

\[4\] [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Symbol/for](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/for)

\[5\] [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-Data-Hub-1024x610.png)](https://jellyfish.co/blog/dora-metrics-tools/)[**8 Top-Rated Tools for Measuring DORA Metrics**](https://jellyfish.co/blog/dora-metrics-tools/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-tools/)

[![roadmap](https://jellyfish.co/wp-content/uploads/2025/02/blog-software-engineering-roadmap-1024x561.webp)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)[**Your Roadmap for AI Transformation with Jellyfish**](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/your-roadmap-for-ai-transformation-with-jellyfish/)

[![Jellyfish SEMR](https://jellyfish.co/wp-content/uploads/2026/05/Jellyfish_Resource-Card_SEMR26.webp)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)[**In 2026 Engineering Leaders Are Shifting from AI Adoption to AI Accountability**](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/2026-engineering-leaders-shifting-from-ai-adoption-to-ai-accountability/)

Qualified