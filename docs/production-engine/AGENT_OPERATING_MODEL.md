# Bumpp agent operating model

Prepared November 22, 2026. Maps to steps 01–18 of the Miro production playbook.

**Status: proposed architecture and configuration, not deployed services. No recurring automation, source connector, paid render or audience test has been activated.** The current episode-development pause remains in force. Research and workflow design can proceed; script/episode agents remain disabled until the user resumes that work.

## The system we should build

Use a shared operating system with three loops:

1. **Observe and research:** watch approved public sources, identify changes, verify evidence and propose opportunities.
2. **Develop and produce:** run bounded creative/planning/production jobs against approved, versioned inputs.
3. **Measure and improve:** reconcile actual audience response with production cost, then recommend the next test.

A coordinator starts tasks on a schedule or when an event arrives. Eight agent roles below describe responsibilities, not eight independent models thinking continuously. Most polling, arithmetic, deduplication, media inspection, permissions and scheduling should be ordinary code. Use language models where interpretation and drafting help.

The core cycle is: **observe → verify → recommend → human decision → execute approved work → measure → propose the next change**. An observed trend cannot authorize spending or episode publication.

## Agent responsibilities and chart mapping

### Trend Scout — chart steps 01, 02

- **Trigger:** Daily creator watch; weekly company and tool review.
- **Accountable person:** Research lead.
- **Inputs:** Approved public-source watchlist; Dated prior observations.
- **Work:** Fetch permitted public metadata and announcements; Identify new releases and meaningful changes; Deduplicate reposts and repeated announcements.
- **Hand off:** Source-linked change log; Candidate trend cards.
- **Limits:** Cannot infer viewer ages or private retention; Cannot copy scripts or treat popularity as causal evidence.

### Evidence Reviewer — chart steps 01, 02, 03

- **Trigger:** Whenever a new signal is proposed.
- **Accountable person:** Research lead.
- **Inputs:** Candidate signal; Original source and collection details.
- **Work:** Check period, scope, denominators and permissions; Compare like-for-like observations; Find contradictions and separate claims from interpretations.
- **Hand off:** Accepted-for-scope evidence record or unresolved/rejected claim; Research question with supporting and contrary evidence.
- **Limits:** Cannot verify a claim merely because another model agrees; Cannot upgrade evidence after retry exhaustion.

### Audience Analyst — chart steps 16, 17

- **Trigger:** After a fresh authorized analytics export or completed study.
- **Accountable person:** Analyst + research lead.
- **Inputs:** Owner-authorized aggregate analytics; Versioned experiment definitions.
- **Work:** Check freshness, missing data and sample size; Compare exposed cohorts and observation windows; Flag changes in completion, continuation and voluntary return.
- **Hand off:** Dated performance brief; Anomalies with uncertainty and competing explanations.
- **Limits:** Cannot access competitor private analytics; Cannot infer age from comments or make person-level youth profiles.

### Development Assistant — chart steps 02, 04, 05, 06

- **Trigger:** Only after an approved brief and production-development authorization.
- **Accountable person:** Writer + showrunner.
- **Inputs:** Approved brief; Evidence records; Current character and relationship canon.
- **Work:** Draft premise or outline alternatives within the approved scope; Check motivation, continuity and script constraints; Prepare a writer review packet.
- **Hand off:** Drafts marked unapproved; Continuity report and cited hypothesis links.
- **Limits:** Cannot greenlight a story or change canon; Cannot claim simulated viewers validate resonance; Disabled while episode development is paused.

### Production Planner — chart steps 07, 08, 09, 10

- **Trigger:** After exact script version is approved.
- **Accountable person:** Director + producer.
- **Inputs:** Approved script; Asset registry; Route benchmarks.
- **Work:** Extract scene and shot requirements; Retrieve licensed assets and identify missing dependencies; Propose timing, render route and bounded cost estimates.
- **Hand off:** Versioned shot manifest; Asset/voice requests and preview plan.
- **Limits:** Cannot silently change dialogue or approved character identity; Cannot dispatch paid production before preview and budget approval.

### Production Coordinator — chart steps 10, 11

- **Trigger:** When approved jobs become ready; on worker/provider events.
- **Accountable person:** Production engineer.
- **Inputs:** Approved job graph; Budget reservations; Provider task state.
- **Work:** Dispatch independent ready jobs within limits; Reconcile external task IDs and charges; Resume work and invalidate stale dependent outputs.
- **Hand off:** Candidate takes with receipts and provenance; Blocked-job or budget exception records.
- **Limits:** Use deterministic queue logic for permissions, retries and budgets; Cannot duplicate paid work on an ambiguous timeout; Cannot override spending caps or publish content.

### Quality Assistant — chart steps 12, 13, 14, 15

- **Trigger:** After a take, cut or master arrives.
- **Accountable person:** Director + editor + producer.
- **Inputs:** Candidate media; Approved references and rubric; Rights records.
- **Work:** Run technical media checks; Flag likely identity, action, timing or continuity defects; Prepare timestamped repair requests and delivery checklist.
- **Hand off:** Review packet with evidence and defect reasons; Technical pass/fail distinct from creative approval.
- **Limits:** Cannot approve emotional quality, rights or release alone; Cannot treat a model score as audience demand.

### Learning Planner — chart steps 03, 17, 18

- **Trigger:** Weekly or after an experiment decision window closes.
- **Accountable person:** Producer + showrunner.
- **Inputs:** Reviewed trend evidence; Audience findings; Full production costs; Prior experiment log.
- **Work:** Compare market signals with actual Bumpp behavior; Propose one testable change and a disconfirming result; Prepare scale/revise/stop options.
- **Hand off:** Weekly decision brief; Proposed experiment and backlog change.
- **Limits:** Cannot auto-change audience strategy, model prompts or spending; Cannot silently train on raw viewer data or auto-publish.

## What the first intelligence loop actually does

### A. Observe the approved watchlist

Start with the user's reference creators and the ten researched companies. Record new uploads, available public metrics, official launch announcements and production-tool disclosures. Keep publication time separate from collection time. Do not expand into broad scraping or copying full episodes/scripts by default.

Proposed starting cadence: one daily creator/market collection and one weekly company/tool synthesis. These are planning defaults, not active scheduled jobs. Production tasks run on events such as an approved script or completed render. Analytics runs wait for fresh data rather than repeatedly querying unchanged reports.

### B. Create evidence records

For every claim record source URL, source date, observation date, entity, metric definition, unit, period, geography, acquisition context if available, access basis and confidence limitations. Classify it as an observation, company claim, estimate, inference or proposal. Keep contradictions.

External pages and transcripts are evidence, not instructions to an agent. An embedded request to change system rules, export data or run a command has no authority. Keep collection connectors read-only and separately permissioned from production tools.

### C. Find comparable changes

Compare videos at similar ages after publication, in the same platform/format and preferably against the creator's own prior distribution. A new release's lifetime views cannot be compared directly with a month-old hit. Save observations prospectively; do not fabricate missing historical 24-hour snapshots.

If permitted snapshots exist, view velocity can be computed as change in the counter divided by elapsed hours. Counter corrections, resets, changed measurement definitions and missing samples invalidate that comparison until reconciled. Counts from different platforms remain separate.

A candidate trend should have supporting examples, observation windows, distinct creators, exceptions and data coverage. Cross-posts are not independent corroboration. Content categories should come from actual permitted inspection or editorial tagging; title text alone is weak evidence of a story mechanism. Small samples become research questions rather than confident genre rankings.

### D. Recommend a testable opportunity

The output is an opportunity card: what changed, the evidence, why it could matter to Bumpp, competing explanations, what might not transfer, and the smallest research test. It should not say “make this because it is viral.”

Illustrative scenario, not a finding: multiple comparable releases show unusual interest in a relationship-reversal mechanism. The reviewer checks publication ages and creator baselines, flags possible promotional effects and proposes comparing audience interpretations of that mechanism with an alternative. Only after a human decision can authorized development proceed. No creator's story is copied.

### E. Learn from a decision and its outcome

Store accepted and rejected recommendations. Connect any later test to its exact brief, content, discovery creative, audience scope and observation window. A later outcome can change confidence in a hypothesis, but must not overwrite the earlier record.

“Learning” initially means better evidence, approved memories and tested workflow changes. It does not require automatic model fine-tuning. Changes to audience strategy, prompts, scoring rules, model versions or budgets need evaluation and a recorded human release decision.

## Data access: what is public, private or not yet connected

| Source | Useful inputs | Access and interpretation limit |
|---|---|---|
| Public YouTube material | Published metadata and permitted public statistics | Public performance is not private retention or payer behavior; use approved endpoints and current quotas. |
| Our YouTube channel | Authorized performance/retention reports where available | Analytics/Reporting calls require OAuth authorization; another creator's private reports are not available merely because its videos are public. |
| Roblox experience | Defined playback/funnel/return events and aggregate reports | Instrument a published experience appropriately; built-in custom-event charts aggregate daily and may take up to 24 hours. Do not imply a verified real-time export API. |
| TikTok | Authorized account exports, permitted public inspection or licensed data | Research Tools require eligibility and approval; do not assume a commercial studio qualifies. |
| Company intelligence | Filings, official releases, supplier case studies and trade interviews | Keep parent/app/title scopes separate; promotional claims remain attributed. |
| Production systems | Task status, attempts, cost receipts, labor and human review reasons | Requires instrumented jobs. Record failures and waits as well as successful output. |
| Audience studies | Consented, appropriately recruited aggregate findings | AI personas and inferred demographics from comments are not participant evidence. |

Primary access sources checked November 22, 2026:

- [YouTube video resource and methods](https://developers.google.com/youtube/data/reference/rest/v3/videos).
- [YouTube Analytics/Reporting authorization](https://developers.google.com/youtube/reporting/guides/authorization).
- [Roblox custom events](https://create.roblox.com/docs/production/analytics/custom-events).
- [TikTok Research Tools FAQ](https://developers.tiktok.com/docs/en/research-api-faq).

For Roblox, start with explicitly defined events such as playback start, reported completion, next-episode choice and return. They are proposed product events, not preexisting metrics. Validate event emission, deduplication and eligibility. Playback progress does not establish visual attention; forced autoplay and reward collection should not be treated as intentional story interest. Confirm the permitted export/collection path before building the analyst connector.

## The shared memory and control layer

### Store these records separately

- **Source observations:** facts and reported metrics, timestamps, source rights and evidence type.
- **Hypotheses:** supporting/disconfirming evidence, population scope and current confidence.
- **Series canon:** only approved creative facts and versions.
- **Production state:** asset IDs, shot versions, job attempts, external task IDs, approvals and costs.
- **Experiments:** question, comparison, outcome definitions, observation window, actual sample and uncertainty.
- **Decisions:** owner, approved action, permitted spend, applicable version, expiry/review date and rationale.

Use a relational database for these records and object storage for permitted media/references. Miro shows the workflow and decision summaries; it should not be the sole execution-state database. GitHub holds code, schemas, public research and approved summaries. Credentials, private channel data, identifiable participant material and unapproved internal documents stay out of this public repository.

### Coordinator behavior

A durable workflow runner, such as Temporal, is a candidate for long-running jobs and recovery. This is an implementation option, not a dependency already installed. Its durability does not remove the need to reconcile external paid jobs. [Temporal durable execution](https://docs.temporal.io/durable-execution).

1. Receive a timer or event; check freshness, access and prerequisites.
2. Create an idempotent job with a task-specific context packet, input hashes and resource limits.
3. Run the appropriate collection, analysis or production worker.
4. Validate the structured result and save provenance, costs and errors.
5. Route evidence/creative decisions to the appropriate reviewer.
6. Continue only if the exact input version has the required approval.
7. On failure, retry only the recoverable operation within its cap; otherwise mark blocked/unresolved.
8. Notify the decision owner only for a meaningful finding, a completed decision packet or an actionable failure. A future notification channel must be explicitly authorized; none is connected here.

Two types of retry require separate budgets: transient network/service recovery and creative attempts to improve a take. After an ambiguous provider timeout, check whether the external job already exists before buying another run. Pending jobs reserve budget; final receipts reconcile it. Changed approved inputs invalidate affected downstream work, not the entire project indiscriminately.

## Standard output contracts

**Trend card:** claim; source links; source/publication/observation dates; compared entities; data windows; units; baseline; coverage; confidence limits; counterevidence; proposed next question.

**Audience brief:** eligible population; exposure and content versions; metric definitions; sample/denominator; observation period; data latency; comparison method; uncertainty; alternatives; recommended test.

**Production request:** show/episode/scene/shot IDs; exact approved input versions; references; route/model settings; dependency IDs; human approver; reserved budget; attempt cap; output destination.

**Review packet:** artifact and reference IDs; automated check results; suspected defects with timestamps; repair proposal; cost so far; required human action. Technical pass and creative approval are separate fields.

**Decision brief:** evidence summary; options; recommended action; disconfirming observation; cost/scope implications; approver; expiration; downstream jobs that would be authorized.

The [agent contracts](agent_contracts.json) and [watchlist](agent_watchlist.json) are machine-readable starting specifications. Both explicitly remain inactive. They do not make API connections or install a scheduler.

## First build: the intelligence loop

### Milestone 1: observations and traceability

Engineer connects one permitted public-source route, stores dated snapshots and exposes a review inbox. Research lead approves the watchlist and a tagging rubric. Acceptance: a real observation can be traced to its source; missing/stale data cannot appear as zero or as a new trend; rerunning the collection does not duplicate records.

### Milestone 2: evidence review and decision briefs

Implement Trend Scout, Evidence Reviewer and Learning Planner in research-only mode. Evaluate a human-labeled set containing genuine changes, repeated articles, scope mismatches, unavailable data and unsupported claims. Measure source accuracy, useful-signal yield, reviewer correction rate, cost and review time. Do not call the system reliable because it produced fluent reports.

### Milestone 3: our own audience analytics

Add an owner-authorized report or approved aggregate export. Validate data availability, definitions and lag. Compare against human calculations. Acceptance: no cross-platform metric mixing, no confident claims from undersized cohorts, and no private material in public outputs.

### Milestone 4: approved production assistance

After episode development resumes, connect the development/planning roles to the existing approval process. Start with one approved input and a bounded task. Then integrate the production queue and quality assistant, testing duplicate prevention, cap enforcement, stale-version handling and required human acceptance.

### Milestone 5: controlled continuous operation

Deploy the coordinator and register approved schedules, source permissions, run limits and recipients. Track successful runs, missed runs, source freshness, cost, agent corrections and human review backlog. Conduct shadow-mode review before enabling automatic low-risk downstream actions. Trigger external production only from explicit, version-bound approvals.

## What people see each day

A concise decision inbox should contain only:

- New credible market signals, with sources and uncertainty.
- Changes in our own audience response, when fresh authorized data exists.
- Production exceptions such as repeated failures or a budget limit.
- Specific approvals needed, each with a recommended action and its consequence.

A weekly brief compares trends, experiments, costs and decisions, then proposes the next research or production adjustment. The useful outcome is better decisions and less repetitive work, not a larger volume of automated reports.

## Current readiness

Completed in this package: agent responsibilities, step mapping, inactive contracts, source watchlist, data-access research and rollout gates.

Not completed: live source authorization, analytics ingestion, a running scheduler, deployed workers, generated episodes, real viewer tests or measured savings. The next concrete implementation is the public-source intelligence loop; the private-analytics and production stages depend on their respective permissions, instrumentation and approvals.
