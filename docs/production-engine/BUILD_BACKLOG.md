# Production-engine implementation backlog

November 22, 2026. Proposed work; no tickets below are implemented. Parent specification: [Engine blueprint](ENGINE_BLUEPRINT.md).

## Intelligence implementation comes first

Relative targets after implementation begins; all work remains proposed. Production tasks in the existing table depend on explicit development authorization.

| Stage | Deliverable | Owner | Acceptance |
|---|---|---|---|
| Before scheduling | Source access, canonical IDs and candidate account verification | Engineer + research lead | No unverified handles, unsupported access path or missing permissions represented as connected |
| Weeks 1–2 | F01–F04 + F07 dynamic discovery snapshots | Engineer + research lead | Correct bounded universes; new/small creators included; panel excluded from emerging-creator feed; timestamped baselines and deduplication |
| Weeks 1–2 | History and signal triage | Engineer + analyst | Missing not zero; 1/3/7-day comparisons require real snapshots; game rank-exit history retained 30 days; independent adoption distinguished from reposts |
| Before new publication | F10 metrics and creative-hypothesis tagging | Engineer + analyst + producer | Metric availability/denominators verified; deliberate continuation distinct from autoplay; paid/organic and formats separate |
| Weeks 1–2 | A2 decode and A8 brief workflow | Story editor + research lead | 3–5 candidate screens and at most 3 full decodes/week; timecoded evidence; at most 5 new daily findings and 3 weekly opportunities |
| Weeks 1–2 | Separate scorecards and editorial routes | Producer + showrunner | Three weight sets sum to 100 each; incomplete scores stay incomplete; no combined rank or hard viral gate; rights review cannot initiate outreach |
| Weeks 3–4 | F05/F06 narrative benchmarks | Research lead + story editor | Relevant dynamic universes and shared deep-review capacity; published likes are not labeled retention |
| Weeks 3–4 | Conditional F08/F09 | Research lead | Only enable after distinct useful yield is demonstrated; Reddit is scoped qualitative evidence; promotion/ranking methods explicit |
| Four-week review | Feed yield and panel governance | Producer + research lead | Measure useful insight cost, actual early lead time and corroboration; reduce low-yield feeds; review authority panel monthly |

## Production backlog after authorization

| Order | Deliverable | Owner | Acceptance criterion |
|---:|---|---|---|
| 1 | Quality and rights brief | Producer + director | Agreed delivery format, artistic criteria, permitted assets/voices and unresolved audience assumptions |
| 2 | Versioned asset registry | Engineer + technical artist | Every selected reference has identity, hash/version, permission record and approval |
| 3 | Canon and continuity records | Showrunner | Scene knowledge/relationships and prop/location states can be retrieved without inferring missing facts |
| 4 | Script-to-shot planning schema | Engineer + director | Approved inputs produce reviewable shot plans; ambiguous intent cannot silently auto-approve |
| 5 | Durable job queue | Engineer | Interrupted workers recover; jobs wait for dependencies and respect concurrency limits |
| 6 | Budget reservation and reconciliation | Engineer + producer | Duplicate submission is prevented/reconciled; caps include reserved in-flight cost and actual charges |
| 7 | Human review workspace | Engineer + director | Reviewer sees candidate, references, cost and history; rejection requires a specific reason |
| 8 | Primary rendering/capture route | Technical artist + engineer | Approved, rights-cleared scene can produce a repeatable take; unsupported unattended export remains explicit |
| 9 | Generative-video adapter | Engineer + director | Submit/status/retrieve and failure paths work; model/settings/version/cost are persisted |
| 10 | Voice and timing integration | Editor + engineer | Approved voice permissions and audio versions connect to timeline/captions without silent drift |
| 11 | Technical QC and bounded correction | Engineer + editor | Technical failures block acceptance; retry exhaustion blocks rather than approves |
| 12 | Accepted-take assembly | Editor + engineer | Assembly references only approved versions; director can revise timing and select takes |
| 13 | Change-impact handling | Engineer + director | Dialogue/asset changes invalidate affected outputs; unrelated approvals remain intact |
| 14 | Production scorecard | Producer + engineer | Rework, labor, waits and all attempts are included in approved-minute economics |
| 15 | Benchmark review and scale decision | Producer + director + research lead | Route selection rests on matched workload evidence; creative/audience limitations remain visible |

## Appropriate integration checks when implementation begins

- A provider times out after accepting a paid task: recover its ID/status without blindly buying a duplicate.
- A character reference changes after shot approval: dependent work becomes stale; unrelated shots stay usable.
- Automated QC passes but the director rejects performance: the take remains rejected.
- A budget cap is reached with tasks in flight: stop new dispatches, reconcile existing commitments and preserve receipts.
- A retry cap is exhausted: produce an actionable blocked record, never an automatic approval.
- A canceled job still returns a chargeable result: record cost and keep the output out of the approved edit.
- A voice permission or asset license is withdrawn/invalidated: affected delivery is blocked pending human resolution.
- One candidate succeeds after several failures: all failed-attempt cost and labor remain in the scorecard.

These are proposed meaningful tests for a future implementation, not tests that have already run. Do not build integrations with unverified platform access or publish generated assets from this backlog alone.
