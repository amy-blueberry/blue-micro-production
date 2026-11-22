# Secret Sauce: cultural and story intelligence

Version 2, November 22, 2026. Governing input: the [user-supplied specification provenance](references/README.md). This replaces the earlier single-score / 80-point creative gate. It is a proposed operating design; no monitoring, production, audience test or outreach is activated.

## Objective and system boundary

Discover emerging Roblox fiction, game-origin IP and cultural behavior early; decode why people care; create original, executable hypotheses; learn whether Bumpp earns character attachment, deliberate continuation and return viewing. External virality is an input, not the end metric. This is a story-intelligence system, not general social listening.

Company economics remain in the separate industry-research track. Specific works, scenes and clips supplied by the user, including selected A24 works, enter the decoding queue as creative references. They are not an eleventh platform feed. A reference is not evidence that its audience matches Bumpp or permission to reuse protected material.

## Four-stage operating structure

| Stage | Agent responsibility | Accountable people | Work and handoff | Decision boundary |
|---|---|---|---|---|
| DISCOVER | A1 Content & Culture Scout | Research lead; engineer owns connectors | Collect enabled feed snapshots; resolve series/games/memes; compare source-specific baselines; deduplicate; surface genuinely new signals | Separate early discovery from authority amplification. Do not require a large creator to validate every early alert. |
| DECODE | A2 Evidence Reviewer & Story Decoder, with A8 synthesis | Research lead + story editor | Verify scope and freshness; inspect shortlisted works; annotate characters, relationships, payoff, continuation and fandom with timecodes | Credible evidence is not automatically a compelling story. Preserve inference and missing evidence. |
| CREATE / TEST | A8 recommends; A4 develops; A5 plans; A6 coordinates; A7 assists QC | Producer + showrunner, then director/editor/engineer | Editorially select an original hypothesis; preregister a bounded test; use the existing script, preview, budget, quality and release gates | Still paused until explicitly authorized. A rights-review route does not authorize a derivative work or external outreach. |
| LEARN | A3 Audience Analyst + A8 Learning Planner | Analyst + research lead + producer/showrunner | Compare F10 outcomes with the declared hypothesis and matched baselines; record uncertainty, costs and editorial findings | Human decision updates the brief or next experiment; no automatic publication, model training or canon change. |

## Ten evolving intelligence feeds

The [machine-readable feed registry](intelligence_feeds.json) defines the collection units, fields, cadence and limitations. Every connector is NOT_CONNECTED. Nine feeds are external and one is internal.

| Feed | Priority | Monitored universe | Purpose |
|---|---|---|---|
| F01 Roblox | P0 | 20 relevant popular/engaged experiences + 10 fastest rising, deduplicated; retain 30 days after rank exit | Early game/mechanic/IP discovery and filming affordances |
| F02 YouTube scripted series | P0 | 20 emerging Roblox/Minecraft series, including small channels; link episodes into series | Discover the next Walden Academy; distinguish character fandom from premise clicks |
| F03 TikTok | P0 | 20 accelerating cohort-relevant memes, sounds, phrases, POV formats and fan edits | Detect independent small-account spread and authentic use context |
| F04 YouTube emerging gaming creators | P0 | 10 breakout videos/day outside the panel + 20 rolling emerging channels | Confirm new games/mechanics before authority amplification |
| F05 MyDramaList | P1 | 10 currently trending relevant Korean dramas; original and filtered ranks separate | Relationship and emotional narrative mechanisms |
| F06 WEBTOON | P1 | 10 rising relevant series + newer rapidly growing titles | Character attachment, chapter progression and fandom |
| F07 Authority panel | P0 | 10 candidate established creators; latest 3–5 relevant new uploads/account since prior scan | Confirmation/amplification, not a substitute for discovery |
| F08 Reddit | P1 | Up to 10 high-signal threads/day from a reviewed allowlist | Qualitative theories, unmet needs and early warnings; population mismatch explicit |
| F09 ReelShort + DramaBox | P2 | 10 relevant promoted/trending titles combined; ranking method recorded | Packaging/pacing mechanics, not direct audience-demographic evidence |
| F10 Bumpp owned data | P0 | Every published item tied to hypothesis, version, primary cohort and exposure | Learn continuation, return, completion and character fandom |

TikTok Creative Center supports F03; Google Trends optionally corroborates already-detected terms. Neither is an additional feed. Preserve source-specific ranks rather than inventing one global popularity rank.

The [authority panel](authority_panel.json) retains all ten supplied candidates with blank official-account records until verified. Verify current handles, activity, cohort fit and access before activation. Five candidates have daily review priority; five have 2–3-times-weekly priority. Review membership monthly. The earlier Roblox drama reference creators remain reference seeds, not fixed discovery winners or members of this panel.

## Audience design

Assign exactly one primary behavioral cohort per opportunity, with secondary fits allowed. These are design segments from the brief, not measured demographics of public viewers.

| Cohort | Brief's design range | Creative emphasis |
|---|---|---|
| Lore Keepers | 15–19 | Continuity, ships, theories, side-character agency, affection before betrayal |
| Drama Girls | 16–22 | Central creative ICP; recognition, romantic anticipation, vulnerability, emotional reversals |
| Scream Team | 15–21 | Rule-based fear, fair clues, psychological dread, collaborative theorizing |
| The Lobby | 15–21 | Ensemble loyalty, competence, rivalry and in-world humor/memes |
| The Crossover | 18–24 | Strong writing, satire, relatable stakes, accessibility beyond Roblox |

Core design age is 16–19; 20–24 is ascending; 13–15 is spillover, not the creative target. Do not infer individual ages from comments, usernames or avatars. Apply age-safety review to the actual intended distribution. Use the [supplied Audience Bible](../bumpp-reference/2026-11-21/bumpp_audience_bible.md) for its ten signals per cohort; record an unavailable signal or dealbreaker as unresolved, not an invented criterion.

## Story decoding and capacity

A2 and the story editor annotate the opening 5–15 seconds; protagonist want/fear/contradiction/status/vulnerability/voice; friendships, ships and rivalries; ordinary affection before rupture; revelations; escalation and earned payoff; the unresolved emotional question; named-character fandom; Roblox translation; and primary-cohort fit. Every conclusion links to an inspected episode/scene/timecode and evidence note. Record whether the inspection was audiovisual, transcript-only, a trailer or metadata. Distinguish short-form and long-form pacing.

Editorial questions: Would someone share this moment? Would viewers talk about the character? Would they deliberately choose episode two? The brief's “friendship retains; romance hooks” principle is a creative hypothesis to test, not a universal measured law.

The supplied brief contains overlapping weekly limits. Implementation default: screen 3–5 candidates weekly, deeply decode at most three properties total, and let MyDramaList/WEBTOON share that deep-review allocation. Do not add a new three-property allowance for every feed. This conservative capacity interpretation is explicit and can be revised by the editorial lead.

## Three independent scores

All weights below are supplied, proposed and unvalidated. Report three separate 0–100 assessments, never one blended score. No universal numerical greenlight cutoff is defined. The previous 80-point gate is superseded.

| Assessment | Components and weights | Question |
|---|---|---|
| Viral opportunity | Momentum 30; independent creator adoption 25; cross-platform spread 25; behavioral-cohort relevance 20 | Is this breaking out early? |
| Story / IP potential | Character attachment 30; relationship/emotional stakes 25; next-episode reasons 25; world/character extensibility 20 | Can this sustain a beloved serialized show? |
| Execution opportunity | Roblox filming feasibility 30; speed to test 25; originality/rights feasibility 25; distribution fit 20 | Can we act effectively and responsibly? |

Proposed calculation contract: each component is a reviewer-approved, source-specific normalized 0–100 assessment; score = sum(component × weight)/100. Store normalization method/version and rationale. This contract does not establish empirical predictive validity. A missing component is NULL with reason; report the affected score as incomplete, retaining observed components without silently reweighting. Missing evidence is not zero. Other complete scores can still be reported, but missing feasibility/rights prerequisites block the dependent action.

Confidence, sample size/denominator and rights status are mandatory separate fields. Tag evidence `[D]` measured facts, `[O]` observed public behavior, `[I]` interpretation, or `[FP]` first-party experiments. Public view growth may be measured while a claim about emotional causation remains interpretation. Correlation does not establish causation.

## Editorial routes, not automatic greenlights

| Route | Trigger in the supplied design | Owner and next step |
|---|---|---|
| WATCH | Weak or early signal | Research lead retains history and revisits; no production commitment |
| INVESTIGATE | Meaningful relative acceleration plus independent corroboration, or exceptional character/fandom evidence | Research lead targets review within 24h, subject to access/capacity |
| TEST | Strong cohort fit, credible story hypothesis and feasible original low-cost test | Producer/showrunner approve scope and metric; 48–72h is a target after authorization/prerequisites, not a service guarantee |
| DEVELOP PILOT | Strong story/IP case and character/relationship engine, even with moderate viral momentum | Showrunner and producer decide; development pause must be explicitly lifted |
| RIGHTS REVIEW | The opportunity depends on protected existing characters, world, branding or story | Producer routes to a qualified rights reviewer; a license or permitted original alternative precedes dependent work |

High viral / low story can justify an original marketing or meme test; high story / moderate viral can justify original pilot development; high across all three can prioritize development or rights review. “High” is an editorial characterization to calibrate, not an unstated numerical threshold. Scores do not override age safety, originality, rights, budgets or human approval. No agent contacts rights holders without separate authorization.

## Daily and weekly outputs

**Daily:** A8 triages at most five genuinely new findings. Include canonical entity/URL, first-seen time, primary cohort, sources, growth versus baseline, independent confirmation, three separate scores, confidence/missing data, character/emotional hypothesis, original application, rights/production caveat, next action and owner. No-change is valid. Keep rising/peaking/fading history separately; retain rank-exit data.

**Weekly:** At most three evidence-backed creative opportunities with thesis, source/timecodes, cohort, feasibility, originality/rights review, experiment and predefined success metric. Producer/showrunner decide what to pursue. Daily Learning Planner review remains; the weekly shortlist is a distinct commitment decision.

Use the [brief and decode templates](INTELLIGENCE_TEMPLATES.md). Templates are empty contracts, not fabricated findings.

## First-party measurement and feedback

Before any new release, engineer and analyst establish the F10 event/report availability register and hypothesis/version tagging. Define each metric's denominator, eligibility, observation window and platform access route. Record unavailable measures as NULL/not measurable with a reason.

Measure when available: 3s/15s hold, retention, duration-normalized completion, deliberate episode 1→2 choice, continuation, D1/D7 series return, returning viewers, watch time, repeat viewing, shares and character fandom. Separate paid/organic traffic, Shorts/long-form, impressions/clicks, and actual demographic data/cohort proxies. Autoplay, reward collection and player activity alone are not deliberate story interest. Public competitor episode views are not retention; do not assume YouTube user-level data or complete metric availability.

Match internal baselines where possible; state actual sample size, exposure, spend and confounders. Human review checks emotional authenticity, payoff, dialogue, game-native execution and continuity. A3 reports results; A8 proposes a revised hypothesis or next test. Preserve prior versions and rejected recommendations.

Evaluate qualified early discoveries/week; measured lead time versus large-creator coverage; seven-day independent corroboration; story opportunities worth testing; time/cost per useful insight; tests completed; and eventual continuation, return, completion and character fandom versus baseline. Data volume is not success.

## Build sequence and activation gates

**Weeks 1–2 target:** Validate access and implement F01–F04 and F07 metadata snapshots, bounded candidate review, deduplication and history. Establish F10 instrumentation and hypothesis tagging before publication. Verify the authority panel; do not invent handles or claim unavailable feeds are connected. Validate the first connector in shadow mode, then expand to the P0 scope.

**Weeks 3–4 target:** Add F05/F06 narrative benchmarks. Add F08/F09 only when they demonstrate distinct useful insights. Validation surfaces do not become duplicate ingestion programs. Review distinct useful yield at four weeks and reduce or replace low-yield feeds.

These are relative rollout targets after implementation begins, not completed calendar commitments. The [implementation backlog](BUILD_BACKLOG.md) contains owners and acceptance criteria. Source permissions, verified identities, freshness, source tracing, privacy and budget controls must pass before scheduling. No active scheduler, paid jobs, external notifications, rights outreach or generated episode is created by this documentation update.
