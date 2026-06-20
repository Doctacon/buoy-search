---
url: "https://jellyfish.co/blog/are-you-still-eating-that-access-control-at-jellyfish/"
title: "“Are you still eating that?” (Access Control at Jellyfish) | Jellyfish Blog"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/are-you-still-eating-that-access-control-at-jellyfish/#content)

In this article

Background

## Background

Here at Jellyfish we make extensive use of Amazon Web Services (AWS). There are many use-cases, but just a few include:

1. The control and data plane for most of our production systems.
2. Logging and alerting systems used daily by engineers for debugging.
3. Data stores used by research teams for analytics
4. Lambdas used for internal process automation
5. And much more

One thing we care a _lot_ about is the security of our infrastructure and services. Our customer’s security is paramount, so almost immediately in Jellyfish’s history the need to add defenses to our AWS environment were evident.

One way we do this is by putting Identity and Access Management (IAM) to work. You can divide access risk into two groups:

1. What you have access to
2. How long you have access for

Many companies accomplish 1 using IAM groups. Simply come up with a set of “roles” representing what folks need access to (engineering, site reliability, security, support, etc.) and assign IAM policies that provide the needed functionality.

Fewer companies attempt 2, and often the model is “if you need access, add them to the group and forget about it”.

However, we didn’t feel this was appropriate. Sure, a Site Reliability Engineer (SRE) might _occasionally_ need the ability to replace secrets in Secrets Manager, but that should be rare. We didn’t want to have to manually update and add remove people from groups, since we know that’s easily forgotten. How can we do better?

### Desired State

Our solution is a “capability-based” access control model in IAM with time-boxed, just-in-time access. Let’s break down what this means:

1. “Capability-based” – By default, everyone gets approximately the same, limited access (accomplished by a base IAM group). We then come up with a list of “capabilities” that can accomplish particular activities.
1. For example:
      1. Secure Shell (SSH) into Production Bastions
      2. Read-only access to most resources
      3. The ability to deploy lambdas
      4. The ability to access Secrets Manager
      5. Etc.
2. Groups are created for each capability and are assigned to users as appropriate.
2. “Just-in-time” (JIT) – Almost no one is assigned persistently to these groups. Instead, our employees _request_ access to one or more of these capabilities as the need arises.
3. “Time-boxed” – Just because you received permission at some point doesn’t mean you can keep it. Instead, a “time limit” is included as part of the request and automation automatically revokes access.

### IAM solution

Up until 2023, we used classic IAM (users get assigned to groups, groups have policies, etc.) for our employees. To accomplish our desired solution, we created IAM groups associated with each capability. To accomplish JIT and time-boxing, [we used a neat tool call Sym](https://blog.symops.com/post/sym-and-jellyfish) ( [symops.com](http://symops.com/)). Basically, users would make requests via Slack for resources with some time-duration and Sym would handle adding/removing IAM users to our groups as appropriate.

The Problem: AWS SSO (aka Identity Center)

## The Problem: AWS SSO (aka Identity Center)

During one of our 2023 security initiatives, we decided that we wanted to modernize access to AWS. Instead of managing IAM users the classic way, we wanted to switch to using AWS single sign-on (SSO). This had a number of advantages including:

1. **Easier management:** We already managed our users via Okta, so being able to assign folks to appropriate groups or AWS accounts via Okta was appealing
2. **More consistent experience for devs:** They SSO all the time. Having an extra set of credentials and multi-factor authentication (MFA) for AWS is annoying
3. **Security:** One big issue with classic IAM is that each user (usually) stores [long-lived IAM access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) on their machine. If these keys are lost, the results can be quite devastating. We had a mitigation for that (make people rotate their keys every few months) but that was a frustrating experience for everyone. By using AWS SSO, long-lived keys disappear. Short-lived session tokens are generated after logging in.

We figured it would be pretty simple to transfer our prior IAM model over to Identity Center. After all, as long as we can dynamically assign and remove some sense of a “group” to our users, everything will work great. Right?

Wrong.

### Permission Sets

Let’s compare access control in classic IAM vs. identity center. This is best represented using the following picture:

![Permission Sets](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/11/Permission-Sets.png)

_Diagram comparing the access control model of classic IAM on the left and SSO-based on the right_

The important thing to note is that the idea of “Groups” is essentially gone. Instead, users are assigned to “ [permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html)” which have policies attached.

At first glance you might not see the problem. If before you accomplished JIT access by adding/removing groups, why don’t you just add/remove permission sets?

The answer lies in the arrow coming out of each _session_. In the classic world, a session automatically “inherits” all the IAM groups attached to the user. If you change the groups, you don’t need to alter your session, you just get (or lose) the corresponding group access.

However, in the identity center world, a session is bound to _one specific_ permission set. If you are granted additional permission sets, your existing sessions won’t “see” that. If you want to perform elevated actions, you’ll have to refresh your session and pick a different permission set.

This isn’t a huge problem if each permission set encapsulates all actions needed for some role (e.g. an “SRE” permission set) but this doesn’t work in our capability model. We want users to be able to request multiple capabilities and have them all apply at once.

## The Solution: Attribute-based Access Control + Okta

Due to the aforementioned reasons, our old approach (IAM groups + Sym) was not going to work and we needed to design a new system to get the same benefits as before. After much brainstorming, we came up with a solution that looks like this:

![Attribute based access control](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/11/Attribute-based-access-control.png)

_Bounce diagram showing how access requests are created, approved, and handled by IAM policies_

### Solving the Capabilities Problem

So we can’t just add or remove permission sets to dynamically change access. What does that leave us? Well, looking at the comparison diagram you can see we only have two boxes left: “IAM Policies” and “AWS Resources”.

Obviously, solving this via the resources themselves is a no-go. In theory, there could be a world where you create new versions of resources specific for a user but that would be so immensely costly it’s not even funny.

So we’re left with the policies themselves. Two options come to mind:

1. Add and remove policies to the permission set on the fly
1. Theoretically, once a user receives permission we could have some service generate new IAM policies specific for the user and attach to the base permission set.
2. [Attribute-based access control](https://docs.aws.amazon.com/singlesignon/latest/userguide/abac.html)
1. It turns out AWS does provide a way to restrict IAM policies based on attributes relevant to the calling identity.
2. If we could update user _attributes_ on the fly, then all we’d need to do is have IAM policies filter based on these

Option 1 was quickly ruled out after learning that permission sets are limited in how many policy attachments you can have. Generating a new policy for each IAM user could easily result in hundreds of policies needing to be added to the permission set, which just wasn’t feasible.

Thankfully, attribute-based access control was the perfect solution.

You can configure Identity Center to receive certain Security Assertion Markup Language (SAML) attributes (like Division) “passed through” from your SSO provider to itself. These attributes then become available via the aws:PrincipalTag/division condition variable. As such, we can write policies limited to certain capabilities by writing policies like:

data “aws\_iam\_policy\_document” “abac-run-app-locally” {

statement {

effect = “Allow”

actions = \[\
\
“dynamodb:Query”,\
\
\]

resources = \[\
\
data.aws\_dynamodb\_table.pending\_data\_refreshes.arn,\
\
\]

condition {

test     = “ForAnyValue:StringLike”

variable = “aws:PrincipalTag/division”

values   = \[“\*abac\_dev\*”\]

}

}

}

This policy allows querying certain DynamoDB tables for anyone with the “abac\_dev” permission set in their Division.

It’s important you carefully document all the different “capability” identifiers. Once that’s done though, enabling fine-grained access is a simple matter of updating the user’s Division in Okta (or your SSO solution of choice). Every time the user SSOs their current set of capabilities will be passed to AWS and respected.

### Solving “Just in Time” and “Time Boxed”

Now that we have the AWS-perspective done, it’s time to tackle user experience. We need some way:

1. For users to request permission to capabilities (and allow them to indicate how long they need access)
2. A mechanism to notify our IT/security team that a request came in so they can approve or reject it
3. A way to automatically update the user’s “Division” in Okta based on the set of approved capabilities
4. The ability to automatically revoke the added capabilities to “Division” in Okta after the time limit expires.

There are tons of ways to accomplish this. Sufficiently resources orgs may choose to build a dedicated app or Slack app for this.

In our case though, we didn’t want to have to build something nor did we want a third-party solution to be given any access to Okta given Okta’s sensitivity here at Jellyfish. Thankfully, Okta rolled out a new feature in 2023 that allowed us to build what we wanted – the ability to leverage [Okta Workflows](https://www.okta.com/resources/webinar-automate-critical-it-and-security-tasks-at-scale-with-okta-workflows/?utm_source=google&utm_campaign=amer_mult_usa_all_wf-all_dg-ao_a-wf_search_google_text_kw_brand-general-T2_utm2&utm_medium=cpc&utm_id=aNK4z000000UAtkGAG&gad_source=1&gclid=Cj0KCQiAwvKtBhDrARIsAJj-kTibKwqOVYA2mLrAiRjHRUuky-wqBCiaOZIZIJcQdUJmUmxDiI24k1kaAir2EALw_wcB) in Okta Identity Governance (OIG) Access Requests.

![Okta workflows](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/11/Okta-workflows.png)

_Screenshot showing the requesting user’s experience_

If you are unaware of the Okta Workflow toolset, it can be best compared to commercial tools like Zapier, or my personal favorite – IFTTT (If this, then that). The tool runs on the trigger and action model, allowing you to kick off actions to Okta (or other app) settings based on the specific trigger defined.

Prior to this feature, Okta Identity Governance (OIG) access requests had a fairly limited set of things you could do within the request itself – you could add and remove users from groups, add and remove applications assigned to users, and that’s really it (outside of being able to list groups assigned to users and apps). With the introduction of running workflows in Access Requests, it opened up the possibility of doing whatever we wanted to with an Access Request.

Given this, we were able to develop an access request that (once approved) would kick off an Okta Workflow, which in turn would update a custom field (in our case, named AWS\_ABAC on the user’s Okta profile with the elevated permission set that they required. We then concatenate AWS\_ABAC (along with the users Division and Department) into the Division profile field in AWS.

By bundling the custom field with Division in AWS, we now have a single profile field that determines all access required for the user, whether it is permanent (Department/Division) or temporary (AWS\_ABAC)

![AWS_ABAC](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/11/AWS_ABAC.png)

_Screenshot of the approval workflow in Okta_

Limitations

## Limitations

The solution we ended up with works very well and we’ve successfully rolled it out across our organization without significant issues. Still, there are some limitations worth describing if you’re thinking about building a similar system:

1. [Just because your access request expired doesn’t mean you will lose access immediately](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html). Since the Division attribute is bound to your SSO session you will have to wait for your session to expire before elevated access is fully revoked.
2. Likewise, the UX when receiving new capabilities is clunkier than we’d like.
1. In our old IAM model, access immediately applied and users needed to do nothing. Simply repeating an action that previously failed would now work.
2. With the identity center model, users need to refresh their session. This must first be done in the AWS console, then locally. If you try refreshing only the Command Line Interface (CLI) session, you will receive outdated privileges because the login will use your current AWS console session which will not have received updated attributes from your SSO provider.
3. [Permission set policy attachment size is limited](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html). Combined with the fact that policies have a maximum size, there is an upper bound to how much you can add to a single Permission Set. In our case we were able to make this work, but for much larger or complicated orgs this may not be feasible.
4. Using the Division field as our store for allowed capabilities is a little clunky. Ideally a more descriptive custom field would be used (GrantedPermissions) but as of 2024 you can’t have custom attributes elegantly passed through from Okta to AWS via system for cross-domain identity management (SCIM).

Cost/Benefit Analysis

## Cost/Benefit Analysis

One advantage of being a security team at Jellyfish is that we’re able to use our own product to help us understand the cost/benefit analysis of new initiatives. In particular, we’re able to see if our prediction of the cost to build was accurate.

For example, we have data to suggest that migrating IAM policies over to AWS SSO took the equivalent of 0.2 person months:

![Cost benefit analysis](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/11/Cost-benefit-analysis.png)

_Screenshot of Jellyfish showing the work that went into migrating IAM policies_

And that building and testing the Okta workflows piece + replacing the third-party solution took 0.3 months:

![Replace third party solution with Jellyfish](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2025/11/Replace-third-party-solution-with-Jellyfish.png)

_Screenshot of Jellyfish showing the work that went into replacing Sym_

So this initiative took about 15 full engineer days. Even if you add some buffer for one-off bug fixes and related work that Jellyfish can’t so easily track (Slack discussions) this wasn’t more than a 1 month effort.

Compare this to the risk reduction obtained by:

1. Switching from long-lived AWS creds to short-lived via SSO
2. Better enforcement and control of MFA into AWS
3. Providing fine-grained, time-limited access to AWS resources

We estimated a reduction in risk that was the equivalent to ~2 engineer _years_.

Now that’s a project worth doing.

About the author

![Josiah Bruner](https://jellyfish.co/wp-content/uploads/2025/11/Josiah-Bruner.jpg)

Josiah Bruner is a Staff Security Engineer at Jellyfish.

Follow: [LinkedIn](https://www.linkedin.com/in/josiah-bruner-02690380/)

About the author

![Phil Kelly](https://jellyfish.co/wp-content/uploads/2025/11/Phil-Kelly.jpg)

Phil Kelly is Head of IT at Jellyfish.

Follow: [LinkedIn](https://www.linkedin.com/in/philipjkelly/)

## Dive Deeper with Jellyfish Content

[![](https://jellyfish.co/wp-content/uploads/2026/06/Jellyfish-Data-Hub-1024x610.png)](https://jellyfish.co/blog/dora-metrics-tools/)[**8 Top-Rated Tools for Measuring DORA Metrics**](https://jellyfish.co/blog/dora-metrics-tools/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/dora-metrics-tools/)

[![Jellyfish State of Engineering Management](https://jellyfish.co/wp-content/uploads/2026/05/blog-semr26-1024x561.webp)](https://jellyfish.co/blog/ai-adoption-improving-engineering-productivity-and-job-satisfaction-jellyfish-report-finds/)[**AI Adoption Improving Engineering Productivity and Job Satisfaction, Jellyfish Report Finds**](https://jellyfish.co/blog/ai-adoption-improving-engineering-productivity-and-job-satisfaction-jellyfish-report-finds/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/ai-adoption-improving-engineering-productivity-and-job-satisfaction-jellyfish-report-finds/)

[![Jellyfish Data Hub](https://jellyfish.co/wp-content/uploads/2026/04/blog-data-hub-featureV2-1024x561.webp)](https://jellyfish.co/blog/introducing-jellyfish-data-hub-flexible-curated-engineering-insights/)[**Introducing Jellyfish Data Hub: Flexible, Curated Engineering Insights**](https://jellyfish.co/blog/introducing-jellyfish-data-hub-flexible-curated-engineering-insights/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/introducing-jellyfish-data-hub-flexible-curated-engineering-insights/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified