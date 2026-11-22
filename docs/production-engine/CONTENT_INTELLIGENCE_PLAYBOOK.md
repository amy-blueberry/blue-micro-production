# Content and culture intelligence for Bumpp

Revised November 22, 2026 from the user's Miro feedback. This is an operating specification, not a completed scan, audience finding, active scheduler or authorization to create episodes.

## What changed

The creative unit of analysis is the **work, scene, story mechanism or cultural moment**, not the company. Accept user-supplied films, series, clips, scenes, screenshots and creative notes. A24 and other production houses are possible sources of selected works; their names do not establish a coherent style or prove appeal to Bumpp's audience. No specific A24 title has been supplied or reviewed in this revision.

Company economics and production technology remain useful in a separate business-intelligence track. They do not determine which stories to tell. Keep the existing company research, but remove company rankings from the creative recommendation logic.

## Two inputs into the creative loop

### 1. Curated reference content

**Owner:** Research lead with writer/creative lead. **Trigger:** A reference arrives or an approved reference publishes new content.

1. Register the exact title, episode, scene/time range or file pointer, who selected it, and what they want to learn. Preserve access/reuse limits separately from the fact that a reference is publicly viewable.
2. Record what was actually inspected: full audiovisual work, bounded clip, transcript, trailer, screenshots, or metadata only. Do not describe transcript-only analysis as a viewing audit.
3. Identify character wants, relationship imbalance, stakes, escalation, reversals, withheld information and payoff. For inspected audiovisual material, also examine staging, performance, shot choices, sound and pacing.
4. Attach timestamps or bounded descriptions supporting each observation. Separate observations from interpretations of why it works.
5. Produce a mechanism card: what to learn, what could translate to Roblox-native storytelling, what should not transfer, and what audience evidence is missing.
6. Link the card to a research hypothesis. The eventual writer adapts a general mechanism to original characters and situations; reference inclusion does not authorize copying dialogue, plots, music, character designs or footage.

Do not adopt mature themes or imagery because the studio is admired. A reference can inform craft while its content is unsuitable for the chosen age scope.

### 2. Daily audience-culture radar

**Owner:** Research lead. **Worker:** A1 Content & Culture Scout. **Cadence:** Daily after deployment; currently inactive.

1. Load the current version of the target-audience hypothesis and approved sources/topics. Gen Alpha and young Gen Z are broad brief terms, not a single measured cohort. Keep the supplied 16–19 design target distinct from measured reference-show audiences and other candidate cohorts.
2. Collect permitted public or licensed observations of current interests, fandoms, memes, formats, gaming culture, relationship conversations and viral moments. Accept user-supplied examples as inputs too. API, export, licensed feed or permitted manual inspection are implementation routes; no unrestricted scrape or private-access bypass is implied.
3. Store source, publication time, observation time, platform, available counters and denominator/window. Deduplicate reposts. Compare like formats at similar ages after publication; maintain missing values as missing.
4. Distinguish emerging, accelerating, established, saturated and fading signals using available dated observations. A single observation cannot establish acceleration or trend decay.
5. Explain relevance to the target cohort using scoped research or authorized aggregate data when available. Otherwise mark relevance as a hypothesis. Do not infer age, gender or location from profiles, avatars or comment language.
6. Identify the underlying interest or social tension. A meme's surface wording is not a story engine. Record alternative explanations, paid-distribution uncertainty and counterexamples.
7. Route meaningful changes to the evidence reviewer. Save a no-material-change result when appropriate. Daily cadence does not justify inventing a fresh trend.

## Daily review and handoff

A1 produces reference mechanism cards and culture-signal cards. A2 checks source credibility, inspection coverage, comparability, freshness and relevance claims. The research lead accepts evidence only for its supported scope.

A8 Learning Planner reviews accepted evidence **daily**, and when material new evidence or a completed experiment arrives. It combines the reference craft, current culture signal, actual Bumpp findings where available, competition and production feasibility into an opportunity brief. Past findings remain dated; new production cost or audience data is not assumed to arrive every day.

Each opportunity brief includes:

- A precise target-audience hypothesis and project goal.
- The reference mechanism and current signal, each linked to evidence.
- Why the audience might care: identity, emotional stake or relationship tension.
- A comparison with actual inspected competing content and how Bumpp could stand out.
- A proposed reason viewers would continue or voluntarily share; counterevidence and uncertainty.
- The smallest research test, its outcome definitions and a result that would weaken the idea.
- The creative opportunity scorecard below, reviewer rationale and unresolved dependencies.
- A recommended action: research, revise, park, reject, or request development authorization.

This is hypothesis development, not permission to draft a pilot while episode work is paused.

## Two independent gates

**Evidence gate:** Is the source accurate and applicable to the claim? Research lead owns this check. A true announcement or large view count can pass a factual check without establishing creative appeal.

**Creative greenlight gate:** Is the opportunity compelling to the intended audience, aligned with our goals, differentiated, feasible and strong enough to merit development? Producer and showrunner own this decision. A high score cannot bypass rights, age safety, evidence gaps, budget limits or the development pause.

### Proposed virality-potential rubric

This is a provisional editorial prioritization score, **not a probability of virality**, a prediction model, a reported audience result or an established industry benchmark. No opportunities have been scored here. The user requested high potential before greenlight; the numerical definition below is a proposed implementation default to calibrate against actual results.

| Dimension | Reviewer question | Required support |
| --- | --- | --- |
| Audience appeal | Does the tension matter to our specified audience? | Scoped audience evidence or clearly labeled hypothesis and planned validation |
| Hook clarity | Can a viewer quickly understand the situation and why it matters? | Inspected reference mechanics; later, actual hook/comprehension testing |
| Emotional continuation | Is there a believable unresolved relationship or consequence? | Mechanism analysis and counterexamples; later, observed continuation |
| Shareability | Is there a voluntary reason to discuss, quote or share it? | Relevant observed behavior or a testable hypothesis, without reward/coercion proxies |
| Competitive distinction | Is there a concrete reason this stands out among comparable content? | Named, inspected comparators and a specific difference |

Each dimension is rated 0–4 by a human reviewer: 0 contradicts the case; 1 weak; 2 mixed; 3 strong editorial case; 4 exceptional editorial case. **Missing information is null, not zero.** Every rating includes evidence, rationale and a separate confidence label. A strong hypothesis is still untested; the score never upgrades its evidence status.

If all five dimensions are scored, total = sum of ratings × 5, on a 0–100 scale. Proposed “high” = at least 80/100, with audience appeal and competitive distinction each at least 3/4. Any missing dimension means NOT_SCORED and cannot satisfy the high-score gate. Goals, rights, age safety, feasibility and explicit development authorization are additional pass/fail requirements.

Before using this cutoff to allocate production spend, test reviewer agreement on a labeled reference set and compare prospective ratings with later outcomes. Record rubric versions and score changes; do not tune the cutoff after seeing a result and present it as a prediction. High potential can justify a bounded research test while production remains blocked.

## Minimal record contracts

**Reference card:** reference_id; title; source/file pointer; selected segment; selection rationale; inspection mode/coverage; access basis; timestamped observations; story/craft mechanism; adaptation hypothesis; do-not-transfer notes; audience relevance status; reviewer; version.

**Culture card:** signal_id; source links; published_at; collected_at; platform; topic; available metrics and windows; baseline; candidate cohort; relevance evidence; counterevidence; trend stage; next freshness review; creative implication; reviewer.

**Opportunity card:** opportunity_id; audience hypothesis version; goal; reference_ids; signal_ids; evidence gate result; inspected competitors; differentiation; five dimension ratings with evidence/rationale/confidence; provisional total; test proposal; safety/rights/feasibility status; decision owner; next action; approved version.

## Implementation acceptance

Start with one permitted content source, user-reference intake and the daily research loop in shadow mode. Engineer owns ingestion/state; research lead owns tagging/evidence; producer/showrunner own opportunities and decisions.

Accept the first implementation only when a reference can be traced to its exact inspected segment, a social signal retains its actual time window, cohort assumptions are explicit, repeated scans do not duplicate evidence, missing data cannot become a high score, and a company ranking cannot substitute for a creative case. Evaluate useful-signal yield, reviewer correction rate, latency, cost and time saved before expanding sources.

Daily scraping/collection and review are specified here but not activated by editing the chart. The [agent contracts](agent_contracts.json) and [watchlist](agent_watchlist.json) retain inactive status.
