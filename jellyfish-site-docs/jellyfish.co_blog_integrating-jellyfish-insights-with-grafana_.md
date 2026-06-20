---
url: "https://jellyfish.co/blog/integrating-jellyfish-insights-with-grafana/"
title: "Engineering Management Reimagined: Integrating Jellyfish Insights with Grafana Using Our New API - Jellyfish"
---

New episode: Building Safe, Useful AI for 500M+ Users, with Flo Health's Director of Engineering. [Watch now](https://jellyfish.co/glow-2026-video-series/?utm_content=topbar_cta)

[Skip to content](https://jellyfish.co/blog/integrating-jellyfish-insights-with-grafana/#content)

![blog-Jellyfish + Grafana](https://jellyfish.co/wp-content/uploads/2024/12/blog-Jellyfish-Grafana.webp)

![](https://jellyfish.co/wp-content/uploads/2024/12/john-duffy-mclaughlin.png)

John McLaughlin

December 05, 2024

Being an Engineering Manager is no small feat – believe me, I’ve learned firsthand. Transitioning from individual contributor to a leadership role comes with new challenges, broader responsibilities, and the constant pressure to deliver measurable outcomes. The hardest part? Gaining a clear view of my team’s performance, impact, and priorities. Jellyfish’s [Engineering Management Platform](https://jellyfish.co/platform/engineering-management-platform/) helps me navigate the complexity of my role while staying laser-focused on what matters most.

Jellyfish goes beyond Jira tickets and pull requests, offering a comprehensive lens into team performance. It answers critical questions like:

- Are key deliverables on track, or do we need to adjust priorities?
- How is our time allocated – what share is spent on innovation versus Keeping the Lights On (KTLO)?
- Are we consistently meeting performance metrics like closing epics or maintaining collaborative PR reviews?

While my focus as the Engineering Manager for Jellyfish’s Infrastructure and Scalability team often shifts from team performance to tackling system emergencies –because, let’s face it, if the database is on fire, nothing else matters – having the right insights at the right time is critical to navigating these challenges effectively.

That’s why I’m excited to introduce the Jellyfish API.

## The Jellyfish API: Critical Engineering Insights – Everywhere

Every Engineering Manager has unique priorities, but one constant remains: the need for actionable insights. That’s where the new Jellyfish API comes in. It provides seamless access to data across three core domains:

1. Deliverables
2. Allocations
3. Metrics

Our new API enables engineering leaders to integrate Jellyfish insights into the tools they rely on most. For me, that’s Grafana.

## Grafana: A Command Center for Engineering Managers

For infrastructure managers like me, Grafana is a daily staple. It visualizes streams of data from various sources, offering dashboards for everything from system performance to team deliverables. When the database is struggling, Grafana is where I monitor the crisis. It’s also where I’ve built my personal “command center,” blending operational signals with Jellyfish insights for a holistic view of my team and systems.

### The Power of Centralized Insights

Co-locating diverse data streams in one place simplifies decision-making and reduces cognitive load. My Grafana dashboard prioritizes urgent signals (like database CPU usage) at the top, followed by Jellyfish data on deliverables, allocations, and metrics. This intentional setup allows me to focus on solving problems instead of wasting time deciding which problem to tackle.

![Jellyfish_Grafana](https://test-jellyfish-co.pantheonsite.io/wp-content/uploads/2024/12/Jellyfish_Grafana.png)

Even more powerful are the connections this approach fosters. For instance, noticing an improvement in task burndown might lead me to Jellyfish deliverables, where I recall recent efforts to speed up nightly tasks. If database CPU usage spikes around the same time, it prompts me to evaluate whether the optimization introduced new strain on the system.

Imagine what a front-end team could achieve by combining Jellyfish data with user traffic metrics. Displaying development efforts alongside user engagement metrics would create a direct link between engineering execution and business outcomes.

### Implementing Jellyfish Insights in Grafana

Ready to test the integration for yourself? Here’s how to get started:

**1\. Setup Data Source**

To be able to hit the Jellyfish API live from a dashboard, I used the [Infinity Plugin](https://grafana.com/docs/plugins/yesoreyeram-infinity-datasource/latest/), which provides an easy path for authentication and request composition.

- Install this plugin to your Grafana workspace and create a new data source.
- In this data source under authentication, select API Key Value pair and under Key enter Authorization and under value enter Token: \[your Jellyfish API token\]
- Enter app.jellyfish.co as an allowed host.

**2\. Build Dashboard Visualization**

I’ll use the example of building a table of Deliverables in a dashboard panel.

- Create a new Dashboard, add new Visualization and click into Edit.
- Select your new Infinity Datasource and configure the API request:
  - The URL for this example will be:
  - https://app.jellyfish.co/endpoints/export/v0/delivery/work\_category\_contents?work\_category\_slug=epics&timeframe=${\_\_from:date:MMM-YY}&end=${\_\_to:date:MMM-YY}
  - This is grabbing Deliverables of work category “Epics” over the dashboard’s timeframe.
  - **Note:** The \_\_from and \_\_to parameters and formatting functionality are provided by Grafana.

- Parser: backend
- Under Parsing Options, enter deliverables, which is the key to Deliverable entries in the response.
- On the Transformations tab, you can use the “Filter data by values” transformation to match your team name on the “teams” field and you can use the “Organize fields by name” transformation to select and order which fields you want to see in your table.

## Unlocking New Possibilities with Jellyfish + Grafana

By integrating Jellyfish insights into your workflow, you’ll reduce mental overhead and uncover connections that drive better decision-making. Whether it’s optimizing processes, addressing system issues, or aligning engineering work with business outcomes, Jellyfish and Grafana together provide the tools you need to lead effectively.

[Get started with the Jellyfish API](https://help.jellyfish.co/hc/en-us/articles/29135614810893-Jellyfish-API-Beta) and see how it transforms your approach to engineering management.

### Ready to build an integration with the Jellyfish API? Email [api@jellyfish.co](mailto:api@jellyfish.co) to get started!

## Dive Deeper with Jellyfish Content

[![Jellyfish G2 Summer 2026 Grid](https://jellyfish.co/wp-content/uploads/2026/05/blog-g2-summer26-featured-1024x582.webp)](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-summer-2026/)[**16 Quarters at the Top: Jellyfish Continues to Lead G2’s Software Development Analytics Tools Grid**](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-summer-2026/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/g2-software-development-analytics-tools-grid-summer-2026/)

[![Jellyfish State of Engineering Management](https://jellyfish.co/wp-content/uploads/2026/05/blog-semr26-1024x561.webp)](https://jellyfish.co/blog/ai-adoption-improving-engineering-productivity-and-job-satisfaction-jellyfish-report-finds/)[**AI Adoption Improving Engineering Productivity and Job Satisfaction, Jellyfish Report Finds**](https://jellyfish.co/blog/ai-adoption-improving-engineering-productivity-and-job-satisfaction-jellyfish-report-finds/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/ai-adoption-improving-engineering-productivity-and-job-satisfaction-jellyfish-report-finds/)

[![Pensero Alternatives](https://jellyfish.co/wp-content/uploads/2024/11/blog-12-Best-GetDX-Alternatives-1024x561.webp)](https://jellyfish.co/blog/pensero-alternatives/)[**The Top 8 Alternatives to Pensero for 2026**](https://jellyfish.co/blog/pensero-alternatives/) [Learn more![](https://jellyfish.co/wp-content/themes/jellyfish/assets/images/arrows/arrow-long-purple.svg)](https://jellyfish.co/blog/pensero-alternatives/)

## Ready to Drive Engineering Impact?

Schedule a demo or take an interactive tour. Discover how Jellyfish can enable your teams to work smarter, feel empowered, and deliver better outcomes for the business.

[Request a demo](https://jellyfish.co/request-a-demo) [Product tour](https://jellyfish.co/tour)

Qualified