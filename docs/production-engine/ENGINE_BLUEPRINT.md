# Bumpp production engine: evidence and proposed architecture

Prepared November 22, 2026. Status: architecture and build plan; no production system, episode, asset or viewer test has been executed by this document. This design does not select a show or convert the supplied audience hypotheses into validated research.

## The proposed product

Build an operating system for making repeatable series: a persistent story/asset library, a shot-production queue, a review surface and an editing/export pipeline. Models and rendering tools perform bounded jobs inside it. Humans own story decisions, performance direction and final approval.

The optimization goal is **more approved finished minutes at an agreed quality, with lower total cost and shorter delivery time**. Generation volume alone is not a success metric. Story effectiveness is a separate audience outcome; a visually flawless episode can still be uninteresting.

Two feedback loops must remain separate:

- **Production loop:** plan → create → inspect → repair the failed component → accept. Learns about cost, continuity, technical quality and delivery.
- **Audience loop:** appropriate exposure → actual viewer response → research interpretation → revise the brief. Learns about comprehension, character attachment and voluntary return. A model's simulated reaction does not supply audience evidence.

## 1. What the researched companies actually disclose

| Case | Public evidence | What we can learn |
|---|---|---|
| Kunlun / DramaWave | SkyProduction connects scripts, assets, storyboards, video, post and QC; it includes agent functions, shot replacement and team controls. | An integrated production workspace, rather than one model call, is a credible architecture. |
| COL / FlareFlow parent | Its filing describes script breakdown, reusable character/scene assets, storyboards, generation, project collaboration and external-model integration. | Asset reuse and project state are central infrastructure. Parent capability is not proof that every title follows one workflow. |
| Zero Takes / DramaBox | Supplier says DramaBox supplied scripts; its human team created consistent characters and directed, generated and edited scenes for released series. | Writing, commissioning and generation may be separate teams. “AI-produced” still includes editorial labor. |

Sources: [Kunlun Q3 2026, p.9](https://static.cninfo.com.cn/finalpage/2026-10-30/1225644210.PDF); [COL H1 2026, pp.18–19](https://static.cninfo.com.cn/finalpage/2026-08-26/1225504423.PDF); [Zero Takes supplier account](https://zerotakes.com/).

These disclosures do not reveal complete private prompts, training datasets, failure rates, staffing per title or independently audited production costs. The architecture below is our proposal, informed by these cases. It is not a claim to have reproduced a competitor's proprietary stack.

## 2. How generated-video shows are made

A practical reconstruction is:

1. Approve a script and identify what each scene must accomplish.
2. Define character identity, wardrobe, locations, visual style and voice/performance references.
3. Break scenes into camera shots with explicit action, duration and continuity requirements.
4. Build an inexpensive storyboard and timed rough edit, often called an animatic.
5. Approve the dramatic timing before spending on finished footage.
6. Produce suitable reference frames and generate short video takes against them. Choose a voice-first or picture-first workflow based on the shot; dialogue timing often benefits from approved audio first.
7. Review identity, performance, motion, props and continuity. Regenerate or repair only the failed material.
8. Assemble selected takes; shape reactions, pauses, music, effects and captions in the edit.
9. Perform episode-level review and delivery checks. Localize only against an approved version.

The exact method varies by model and production. Generated audio, lip sync, motion transfer and reference conditioning are capabilities to evaluate, not interchangeable guarantees. A model that produces a beautiful single clip may be unsuitable for a recurring cast or a long dialogue exchange.

The important unit of work is usually the **shot**, while the unit of creative approval remains the **scene and episode**. Independent shots can run concurrently after shared dependencies are approved. Shots with shared action, prop state or camera continuity require coordination.

## 3. Bumpp should compare two production routes

### Route A: repeatable game-engine / 3D production

Reusable characters, rigs, sets, props, actions, expressions, cameras and lighting are staged in a controllable scene. AI can assist development, breakdown, planning and selected assets, while rendering/capture supplies the image.

This is the leading hypothesis for a recurring Roblox-native cast because it offers explicit control of identity and spatial continuity. It is not yet a measured cost advantage. Animation effort, performance quality and capture/export constraints can still make it expensive.

Roblox Studio supports rig animation. That does not establish a complete supported unattended video-export pipeline. Blender supports background rendering and can be evaluated with appropriately owned or licensed assets; access to a Roblox asset does not automatically grant export/reuse rights.

Sources: [Roblox Animation Editor](https://create.roblox.com/docs/animation/editor); [Blender command-line rendering](https://docs.blender.org/manual/en/latest/advanced/command_line/render.html).

### Route B: reference-conditioned generative video

Approved references and shot instructions produce candidate footage through a video API. Humans choose performances and manage drift, repairs and editing. This route may be valuable for visual styles or shots that would be costly to stage manually, but that value must survive revision costs.

Example candidate adapter: [Runway's official API](https://docs.dev.runwayml.com/api/) supports image-to-video tasks. This identifies an available capability, not the best model for Bumpp or a vendor used by every researched studio. Select a provider/version through a controlled benchmark and current contract review.

### Routing decision

Do not force every shot through generative video. For each shot, compare accepted quality, full cost, turnaround, revision control, rights and dependence on adjacent shots. Start with one primary route and a limited exception route. Supporting many models before the workload is understood adds engineering and review overhead.

Keep one consistent visual language within a series unless a deliberate creative treatment warrants a change. Route-level cost savings that produce visible style discontinuity may be a false economy.

## 4. Production line, outputs and acceptance gates

| Stage | Required input | Deliverable | Human owner / gate | Automation opportunity |
|---|---|---|---|---|
| Audience brief | Research and chosen target hypothesis | Approved audience/format assumptions and open questions | Research lead + creative lead | Retrieve evidence and flag unsupported claims |
| Series memory | Approved development materials | Versioned characters, relationships, secrets, rules and chronology | Showrunner | Check contradictions; retrieve relevant canon |
| Script | Approved premise and constraints | Scene script with motivations and consequences | Writer/showrunner | Draft alternatives and structural checks |
| Breakdown | Approved script version | Scenes, shots, assets, dialogue, duration estimates, dependencies | Director/producer | Structured extraction and missing-asset checks |
| Look / asset preparation | Breakdown + asset library | Approved identity, wardrobe, set, prop and performance references | Art/animation lead | Retrieve/reuse assets and make candidate variations |
| Timing preview | Dialogue + boards/blocking | Animatic and proposed edit | Director/editor | Assemble a rough sequence; flag overlong beats |
| Shot creation | Approved references and timing | Candidate takes with provenance and cost | Director chooses acceptable performance | Queue rendering/generation; run technical checks |
| Correction | Specific rejection reason | Revised take or changed staging | Same shot owner | Target only the failed component; bounded retries |
| Episode edit | Accepted shots and audio | Coherent cut with music, effects and captions | Editor/showrunner | Assembly, proxy creation and technical preparation |
| QC / delivery | Approved cut and rights records | Delivery master and manifest | Producer/editor; final human approval | Format, sync, missing-media and caption checks |
| Feedback | Real research or release observations | Scoped findings tied to versions | Analyst + creative lead | Aggregate measurements; surface anomalies |

Approval records bind to exact versions. Changing dialogue can invalidate timing, performance, lip sync and captions. A harmless metadata correction need not invalidate the finished video. The dependency system must distinguish these cases.

## 5. The engine's six components

### A. Series and asset memory

Store reusable creative decisions, not just prompts. Each character needs approved visual/rig references, wardrobe variants, voice permissions and behavioral constraints. Each scene needs geography, prop state and lighting/time context. Relationship and information ledgers record who knows what at a given point in the story.

Start with retrieval of explicit, human-approved records. Do not begin by fine-tuning on scraped Roblox creator scripts or assuming the supplied audience bible is a proven training dataset. Revisit fine-tuning only after a defined task, suitable licensed data and a benchmark demonstrate a benefit.

### B. Production planner

Convert approved scripts into structured jobs. A job states purpose, visible action, characters, setting, duration, dialogue/audio dependency, camera, continuity-in/out and prohibited deviations. Validate the output against a schema and require review for ambiguous story intent.

The planner estimates work and identifies reusable assets. It cannot authorize new creative direction merely because an expensive shot is difficult. Escalate a budget/staging tradeoff to the director.

### C. Work queue and provider adapters

Schedule independent jobs concurrently within per-provider and per-project limits. Put API credentials in a secret store. Persist external task IDs and receipts before retrying. A timeout may mean a paid job is still running, so reconcile its state before submitting another chargeable job.

An adapter exposes submit, status, retrieve and cancel when the provider supports them. Cancellation is best effort; already-started jobs can still incur charges. Preserve provider/model version, settings, references and output hashes. A seed does not guarantee bit-identical regeneration across versions.

For a first build, a database-backed queue may suffice. A durable workflow system such as Temporal is a candidate when waiting, retries and recovery become complex. Its workflow durability does not make external billing exactly-once; the application still needs idempotency and reconciliation. [Temporal documentation](https://docs.temporal.io/durable-execution).

### D. Review workspace

Show the current candidate next to its approved references, prior accepted take and continuity notes. Let reviewers accept, reject with a reason, or request a specific change. Suggested rejection codes: identity, wardrobe, prop, action, geography, performance, timing, audio, technical or rights.

Machine checks can detect missing files, bad duration, silence or obvious discrepancies. Vision/audio models can flag likely issues for review. They should not certify emotional authenticity, audience resonance or release readiness by themselves.

### E. Edit and delivery assembly

Build a timeline from accepted take IDs and approved audio. Generate a rough assembly automatically; the editor shapes the actual performance and rhythm. Preserve handles for trimming and support replacement of one shot without rebuilding every unrelated asset.

FFmpeg can handle media assembly and conversion tasks; it is not an autonomous dramatic editor. An editor's preferred nonlinear editor remains the finishing surface. [FFmpeg FAQ](https://www.ffmpeg.org/faq.html).

Speech tools can provide timing information for synchronization and captions. ElevenLabs offers a speech API with timestamps; audition its output and verify voice rights before selecting it. Timing output does not guarantee natural performance or accurate facial animation. [Official speech-timing documentation](https://elevenlabs.io/docs/api-reference/text-to-speech/stream-with-timestamps/).

### F. Production and audience analytics

Join costs, attempt history, labor and acceptance to the finished edit. Keep research/behavior metrics separate but linked through show, episode, version and discovery-creative identifiers. A creative correction should not erase the previous result or cost.

## 6. Minimum records and workflow contract

| Record | Minimum fields |
|---|---|
| Series version | ID, canon version, audience-hypothesis reference, style rules, rights record |
| Asset version | ID, type, owner/license, permitted uses, reference/rig location, hash, approval |
| Scene plan | ID, script version, purpose, characters, location, chronology, continuity states |
| Shot job | ID, scene ID, route, input versions, camera/action, timing, dependencies, cost/retry limits |
| Generation attempt | Job ID, attempt number, provider/model version, external task ID, settings, timestamps, outputs, billed cost |
| Review | Take ID, reviewer, rubric version, decision, reason codes, requested correction, timestamp |
| Edit version | Timeline, accepted take IDs, audio/caption versions, delivery settings, approvals |
| Experiment | Hypothesis, population, consent/research handling, design, versions, metrics, uncertainty, decision |

Suggested job progression:

`DRAFT → PLANNED → REFERENCES_APPROVED → PREVIEW_APPROVED → QUEUED → RUNNING → QC → HUMAN_REVIEW → ACCEPTED`

Separate states: `BLOCKED`, `REWORK`, `FAILED`, `CANCELED`, `SUPERSEDED`. These are not forms of acceptance. A job may be technically complete without its take being artistically approved. Episode release is a separate gate after edit review, not a consequence of all jobs finishing.

Production loop specification:

```text
Select a ready job whose approved dependencies match its recorded versions.
Reserve capacity and budget; persist the dispatch intent.
Submit or reconcile an existing external task; persist its identifier.
Retrieve the result and its cost; run technical checks.
Send the candidate and references to the assigned reviewer.
If accepted, freeze the take/version and unblock dependents.
If rejected, record the reason and choose a targeted correction.
If retries or spending reach the cap, mark BLOCKED and route to the director.
Never pass a rejected take because a retry limit was reached.
Only create the episode master from accepted material and approved edit decisions.
```

Automatic provider retries handle transient service errors. Creative retries spend money seeking a better take and need separate counts and limits. Human response time is part of delivery time; monitor review queues alongside generation queues.

## 7. What actually improves efficiency

1. **Approve cheap work before expensive work.** Validate character intent and timing in boards or a rough edit before finished generation.
2. **Reuse approved assets.** Recurring sets, rigs, wardrobe, motions, camera setups and voices reduce repeated work and inconsistency.
3. **Constrain the first format.** A manageable cast, location set and staging vocabulary improve predictability. These are production constraints to negotiate creatively, not a reason to flatten the drama.
4. **Batch compatible work.** Group shots sharing a set or asset setup while preserving their narrative continuity requirements.
5. **Run independent work concurrently.** Do not render dependent shots against unresolved character or audio versions.
6. **Repair the smallest failed component.** Re-record one line, regenerate one shot or adjust one camera rather than rebuilding an episode.
7. **Cap unproductive retries.** Change staging, route or creative approach when repeated attempts fail.
8. **Measure the bottleneck.** More generation capacity is wasteful if director review or editing is already saturated.
9. **Improve within a route before adding vendors.** Review prompt/shot specifications, asset quality and acceptance reasons before assuming a new model solves every problem.
10. **Keep human responsibility clear.** Agents can propose and check; one person must own the intended scene and final choice.

## 8. Cost and throughput scorecard

Use these metrics for comparable workloads at a specified quality standard:

- Cost per approved finished minute = all allocated labor, model/render charges, assets, audio, post and rework / minutes accepted in the final edit.
- First-pass acceptance = shots accepted on the first creative attempt / shots reviewed.
- Attempts per accepted shot, with blocked/abandoned jobs reported separately.
- Rework labor and charges / total labor and charges.
- Human hours per approved minute, separated into direction, animation, edit and review.
- End-to-end elapsed time, including queue waits and review—not just API runtime.
- Asset reuse, continuity defects after assembly and delivery defects.
- Audience comprehension, character attachment and voluntary return in separately scoped real tests.

Illustrative arithmetic, not an industry benchmark: a 60-second test with 12 shots at three attempts per shot requires 36 generation attempts. Moving to 1.5 attempts per shot would require 18. This halves attempt count under equal-shot assumptions; it does not automatically halve total cost because labor, audio, editing and other costs remain. Do not assume independent retry probabilities or unlimited improvement.

A rough capacity model is the minimum of planning, shot production, review and editing capacity. Expand whichever stage is actually limiting approved output. Set numeric cost/time goals after the benchmark; no daily episode quota or percentage cost reduction is supported yet.

## 9. People and responsibility

The initial team needs these responsibilities, which may be combined where skills and capacity allow:

- **Showrunner / writer:** story, dialogue, character motivation and canon.
- **Director / editor:** performance, timing, shot acceptance and the finished cut.
- **Technical artist / animator:** rigs, sets, staging, reusable motions and visual continuity.
- **Production automation engineer:** jobs, storage, integrations, recovery, cost accounting and review tools.
- **Producer / research lead:** scope, schedule, rights records, age suitability and actual audience validation.

This is a role map, not an established staffing ratio or a claim that five full-time hires are mandatory. Review capacity should not be an invisible spare-time task. A human should approve final creative and rights decisions even if agents perform the preceding checks.

## 10. Build sequence and acceptance gates

**Milestone 1 — specification and baseline.** Agree the target visual quality, output format, rights constraints and production metrics. Audit existing assets and select a narrow, rights-cleared benchmark workload. No claim of audience fit follows from this selection.

**Milestone 2 — production control.** Implement asset/version records, one-shot jobs, approvals, cost logging and a manual route. Demonstrate restart recovery and traceability before adding generative spending.

**Milestone 3 — two-route comparison.** Once the benchmark workload is authorized, compare engine rendering/capture and generated video on matched shot requirements. Include dialogue, reaction, two-character continuity and prop interaction; these expose different failure modes. Record every failure and human hour. This document does not execute the test or greenlight an episode.

**Milestone 4 — accepted-shot assembly.** Assemble a test cut only from accepted assets. Change one upstream input and demonstrate that the system invalidates affected work while retaining unrelated accepted material.

**Milestone 5 — controlled scale.** Increase concurrency after proving budget caps, duplicate-job prevention, review throughput and consistent quality. Validate actual audience response separately before commissioning a series slate.

The first useful engine is a reliable path from an approved specification to a reviewed take and a traceable edit. It should earn the right to scale through measured performance rather than a promise of unlimited automated shows.

## Agent automation layer

The [agent operating model](AGENT_OPERATING_MODEL.md) maps eight logical responsibilities to the 18-step Miro playbook. It defines research, production and learning loops, data permissions, version-bound approvals and rollout gates. The accompanying configurations are inactive specifications; no continuous monitoring has been deployed.

## Intelligence input contract, version 2

Production now receives an editorially approved packet from DISCOVER → DECODE → CREATE/TEST → LEARN. The [content intelligence playbook](CONTENT_INTELLIGENCE_PLAYBOOK.md) specifies ten evolving feeds, one primary behavioral cohort, separate viral/story/execution assessments and a preregistered outcome. A single viral score cannot authorize a show. F10 instrumentation is required before publication, and the existing script, preview, spend, rights, quality and release gates remain.
