Status: recorded
Created: 2026-07-14
Updated: 2026-07-14
Relates-To: .10x/tickets/done/2026-07-14-index-and-brief-oscilar.md

# Oscilar Site Index and Analytics Engineer Recruiter Brief

## What was observed

### Namespace state and superseded apply path

The deterministic target was `site-oscilar-com-v1`, in region `gcp-us-central1`.

A fresh local-only plan of `https://oscilar.com/` completed with:

- `dry_run: true`
- `turbopuffer_api_calls: false`
- `api_calls_occurred: false`
- `credentials_required: false`
- namespace and namespace candidate: `site-oscilar-com-v1`
- sitemap-first crawl with same-site host `oscilar.com`
- 260 pages scraped and 5,730 chunks generated
- 347 requests; zero failed requests, zero blocked requests, zero robots-disallowed requests
- no page/chunk limit reached
- 413 chunks/rows to embed and upsert, 5,317 unchanged chunks
- 1,446 stale rows; no stale deletion requested
- 2 pages added, 40 changed, 80 removed, and 218 unchanged relative to local applied state
- English policy detected localized duplication and excluded `/es/**` and `/pt/**`: 638 localized URLs total (319 Spanish and 319 Portuguese)
- no duplicated docs-version family detected
- artifact hash `8a29787ad75579426a3c0dd76af7997c07af202a67d80d16be946a8d2f7a5e82`
- plan ID `plan_8a29787ad7557942`
- plan artifacts under `artifacts/site-crawls/oscilar-com-plan-20260714/`
- local state at `.turbo-search/state/oscilar-com/site-oscilar-com-v1/state.duckdb`

The plan reported `first_apply: false`. Read-only DuckDB inspection confirmed prior applied state: 6,763 active rows and one apply run, performed on 2026-07-13 from `plan_cf309400646eac2c`, with 6,763 rows upserted and zero rows deleted.

This contradicted the original premise that v1 would be a new namespace. Execution paused before preflight or live apply. The user then explicitly ratified option C: use the existing v1, do not preflight or apply, and do not create v2. Consequently:

- no apply preflight ran;
- no live Turbopuffer write ran;
- no stale-row deletion ran;
- no namespace was created, replaced, or deleted;
- the fresh plan remains unapplied inspection context.

### Plan artifact inspection

Inspected `summary.json`, `plan.json`, `manifest.json`, the 5,730-line `chunks.jsonl`, and representative generated Markdown pages for the homepage, platform, about, careers, Coast customer story, and 2025 year-in-review. The 260-page English corpus covered the intended business surface: product/platform, onboarding, fraud, credit, AML/compliance, industries, integrations, customers, company/careers, blog, webinars, and other public resources. Repeated footer and responsive-layout text exists in extracted pages, but no page family dominated the corpus enough to require a scope decision.

### Live retrieval validation

Seven narrow retrievals completed against the existing 6,763-row v1. Every result reported:

- `command: retrieve`
- `dry_run: false`
- `turbopuffer_api_calls: true`
- `api_calls_occurred: true`
- region `gcp-us-central1`
- namespace `site-oscilar-com-v1`
- page ranking, profile `none`, pool 20, aggregation `max`
- cited hits (5-10 per query)

The questions covered business/use cases/value, product/technical differentiators, data and analytics work, company/history/culture, careers, quantified customer outcomes, and founders.

## Cited recruiter-call brief

### Fast answer: what the business does

Oscilar sells an AI-native, unified risk decisioning platform to financial institutions and other digital businesses. It brings onboarding/KYC-KYB, fraud, credit underwriting, AML/compliance, and case management onto one real-time decision layer instead of requiring separate point solutions. Its stated value is faster and more accurate decisions, less manual review and engineering dependence, lower customer friction, and auditable regulatory control. [Risk Decisioning guide](https://oscilar.com/blog/riskdecisioning) · [About Oscilar](https://oscilar.com/about-us)

### Product and differentiation

- **Unified data and decisions:** Oscilar says it combines first-party, behavioral, device, bureau, and third-party data in a real-time entity view so onboarding, fraud, credit, and compliance teams share context. [Risk Decisioning guide](https://oscilar.com/blog/riskdecisioning)
- **Rules, models, and experimentation:** The platform combines rules with supervised ML and anomaly detection, plus no/low-code natural-language policy creation, backtesting, A/B testing, KPI monitoring, and controlled rollout. [Decision engine guide](https://oscilar.com/blog/decisioning-engine) · [Credit decisioning platform guide](https://oscilar.com/blog/credit-decisioning-platform)
- **Agentic operations:** Its agents perform work such as document analysis, AML L1 triage, case summaries, rule recommendations, and test generation while keeping human approval, explanation, and auditability in the loop. [Agentic AI overview](https://oscilar.com/blog/agentic-ai-oscilar) · [2025 year in review](https://oscilar.com/blog/2025)
- **Integration and speed:** Oscilar describes a vendor-agnostic real-time data ecosystem and pre-wired integrations. Its 2025 recap claims tens of billions of real-time decisions, 30+ new data sources, and sub-200ms P99 response times at scale. These are company-authored claims, not independently verified here. [2025 year in review](https://oscilar.com/blog/2025)
- **Concrete customer value:** Coast reports a 75% reduction in manual-review time, from two hours per person per day to under 30 minutes, with easier extraction and analysis for strategy evaluation and false-positive tuning. [Coast case study](https://oscilar.com/customers/coast)

### Why the analytics engineer role is strategically important

This is not just dashboard production. Risk products and GTM operations both depend on trustworthy entity definitions, timely pipelines, observable quality, consistent KPIs, and analysis that can become operational decisions. The product itself emphasizes real-time analytics, experimentation, monitoring, explainability, and data integrations; the GTM analytics engineer is the analogous internal data foundation for how the company sells, plans, and scales. [Decision engine guide](https://oscilar.com/blog/decisioning-engine) · [Real-time transaction monitoring](https://oscilar.com/blog/real-time-transaction-monitoring) · [2025 year in review](https://oscilar.com/blog/2025)

The official public role page, directly fetched outside the Turbopuffer corpus during execution, describes a **foundational GTM Ops & Strategy analytics engineer** partnering across Ops, Finance, Sales, Marketing, BDR, and Customer Success. The work includes canonical dbt models; SQL and Python; ETL; QA, SLAs, and data integrity; dashboards, self-service, and internal tools; Airflow and GitHub; build-versus-buy judgment; and AI/LLM/agent-assisted workflows with human validation. It calls for a full-stack startup mindset. This page was **never included in the Buoy crawl or Turbopuffer index**: [Oscilar Analytics Engineer role on Ashby](https://jobs.ashbyhq.com/oscilar/4705d263-1deb-49c3-ab8c-57f271b2e478).

### Company and culture signals

Oscilar says it was founded in 2021 by Neha Narkhede, co-creator of Apache Kafka and co-founder of Confluent, and former Facebook engineering executive Sachin Kulkarni. The founding story connects real-time/event-streaming experience to fraud detection and risk decisioning. [Founding interview](https://oscilar.com/blog/founding-oscilar) · [FairPlay partnership background](https://oscilar.com/blog/fairplay-oscilar-partnership-accouncement)

Its careers page emphasizes ambitious technical work, mission, fast execution, extreme ownership, collaboration, continuous learning, and a remote-first culture. Treat these as recruiting claims to test with concrete examples in the call. [Careers](https://oscilar.com/careers)

### 30-second positioning pitch

> I’m interested because this role sits at the intersection of analytics engineering and company operations: building canonical dbt models and reliable pipelines, then turning them into self-service decisions for Finance and GTM teams. Oscilar’s product depends on real-time, explainable, high-integrity decisions, so I like that the internal analytics mandate also emphasizes data quality, SLAs, practical tooling, and human-validated AI workflows. I’d bring a builder mindset—strong SQL and data modeling, pragmatic Python and orchestration, close stakeholder partnership, and a bias toward creating trusted systems rather than one-off reports.

This is a template, not a claim about the candidate's actual background; personalize it with one relevant project and one cross-functional outcome.

### Likely recruiter topics to prepare

1. Why Oscilar, fintech/risk, and an AI-native startup now.
2. Why a foundational, broad GTM analytics role rather than a narrowly scoped BI role.
3. A concise example of turning ambiguous stakeholder needs into canonical models and trusted metrics.
4. Hands-on depth with dbt/SQL, Python/ETL, orchestration, Git/version control, dashboards, tests, data-quality monitoring, and SLAs.
5. Working across Finance, Sales, Marketing, BDR, CS, and Ops when definitions or priorities conflict.
6. A build-versus-buy decision and a case where a lightweight internal tool was better than another dashboard.
7. Responsible use of AI/LLMs or agents: where automation helped, what humans validated, and how quality was measured.
8. Startup ownership, pace, ambiguity, remote collaboration, and logistics such as location, timing, compensation, and interview process.

### High-value questions to ask

- What are the first two or three canonical models or business definitions this person must establish, and which decisions are currently blocked by their absence?
- What would strong performance look like after 90 and 180 days?
- What is the current source/warehouse/BI stack, and how mature are dbt, orchestration, tests, lineage, and SLAs today?
- Where do metric definitions currently break down across Finance, Sales, Marketing, BDR, and Customer Success, and who owns resolution?
- How is work divided among this role, GTM Ops, Finance, data/platform engineering, and business systems?
- Which AI-assisted workflows are already in production internally, and what human-validation and quality controls are expected?
- Is the first priority executive reporting, pipeline/revenue analytics, customer lifecycle analytics, planning, data reliability, or internal tooling?
- What recent example best demonstrates the company's stated values of extreme ownership and fast execution without sacrificing data quality?

## Procedure

Commands ran from `/Users/crlough/Code/personal/turbo-search`. Secret values were never printed or persisted.

```bash
uv run buoy plan "https://oscilar.com/" \
  --namespace site-oscilar-com-v1 \
  --out-dir artifacts/site-crawls/oscilar-com-plan-20260714 \
  --json
```

Plan artifacts were inspected with bounded Python/JSON summaries, line counts, file listings, and targeted reads. Prior state was inspected read-only with DuckDB.

Each live retrieval used the repository `.env` only inside a subshell:

```bash
(
  set -a
  . ./.env
  set +a
  uv run buoy retrieve "<narrow question>" \
    --live --namespace site-oscilar-com-v1 --top-k <8-or-10> --json
)
```

No `buoy apply` command of any kind was run after the user superseded the original apply path.

## What this supports

- The existing `site-oscilar-com-v1` namespace is live and retrievable.
- The recruiter brief is grounded in live-retrieved Oscilar pages, with the official role posting separately labeled outside the index.
- The original new-namespace premise was false; pausing prevented an unauthorized update to an existing namespace.
- The current public English site differs materially from the prior applied state, so retrieval freshness is limited.

## Limits

- Live retrieval reflects the existing 6,763-row index applied on 2026-07-13, not today's unapplied 5,730-chunk plan. It may omit 413 new/changed chunks and retain 1,446 rows that are stale relative to today's crawl.
- The fresh plan was inspected but not applied. Its generated artifacts are gitignored operational context, not durable committed source material.
- Company, scale, performance, awards, and customer-outcome statements are Oscilar-authored marketing or case-study claims unless explicitly stated otherwise; no independent verification was performed.
- The official public Ashby role page was directly fetched outside the Turbopuffer corpus; it was never included in the Buoy crawl or Turbopuffer index.
- The sources do not establish the exact internal warehouse/BI stack, reporting line, team size, compensation, interview sequence, or current pain-point priority. Those remain recruiter questions, not inferred facts.
