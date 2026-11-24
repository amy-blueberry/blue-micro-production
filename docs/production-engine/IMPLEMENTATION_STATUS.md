# Intelligence implementation status

November 23, 2026. The [local workbench](../../intelligence/README.md) implements a first research/review loop. It does not resume episode production.

| Capability | Status | Boundary |
| --- | --- | --- |
| Synthetic demo and browser review desk | Implemented locally | Six clearly labeled fixtures; not research findings |
| SQLite observations, notes and decision history | Implemented | Single-user local storage; runtime excluded from Git |
| F02 / F04 / F07 YouTube discovery adapter | Implemented; mocked tests | Live collection disabled; actual credentials and account verification outstanding |
| A1 collection / evidence provenance | Partial implementation | Metadata only; manual series grouping and content inspection |
| A2 evidence reviewer | Rules fallback + optional Claude adapter | Model off by default; only permitted notes; no audiovisual understanding claimed |
| Three editorial assessments | Implemented | Separate human ratings with cited notes, no universal score or automatic gate |
| A8 learning planner | Partial implementation | Reviewer decisions and daily/weekly briefs; no automated experimental learning |
| Daily worker | Runnable foreground process | One attempt per UTC day, persistent limits; no installed/hosted scheduler |
| Daily / weekly Markdown briefs | Implemented | Reviewed candidates only; cap five / three; no source-metric ranking |
| F01, F03, F05, F06, F08, F09, F10 | Planned | No collectors or first-party analytics ingestion |
| A3–A7 creative / production / release capabilities | Planned, inactive | No episode generation, assets, publishing or audience tests |
| Shared hosting, accounts, permissions and durable queue | Planned | Local server must not be exposed publicly |

## How this relates to the existing specs

The feed registry, authority panel and agent contracts remain design documents. NOT_CONNECTED / NOT_DEPLOYED accurately describe their live state. Built code is not a live connected feed. Miro shows the target workflow; use this document for implementation status.

The earlier design's velocity and metric-derived trend scoring are **disabled for standard YouTube API data**. The prototype stores and displays dated source counters; it does not compute derived growth metrics. Independent editorial assessments require usable evidence and human judgment. A reviewer checkbox does not itself establish data rights. New ranking capability requires an appropriate source/access basis before implementation. Details and [official policy sources](https://developers.google.com/youtube/terms/developer-policies) are linked in the workbench README.

The proposed 16–19 target and five behavioral cohorts remain strategic hypotheses. Neither synthetic demo results nor AI review constitute audience validation. TEST and DEVELOP_PILOT are recorded recommendations, with execution_authorized=false. Rights, age safety, production budgets and explicit development authorization remain separate gates.

## Activation order

1. Engineer: run the local demo and check configuration with `doctor`.
2. Engineer + research lead: configure private YouTube access, verify panel channel IDs and execute one collection.
3. Research analyst: audit the actual sample for relevance, missing sources and metadata errors; add original inspection notes.
4. Producer: review decisions and issue the first genuine brief. Evaluate usefulness before expanding volume.
5. Engineer + editor: optionally enable Claude, set provider spend controls and compare its drafts against human reviews.
6. Engineer: add authenticated team hosting and reliable cleanup/scheduling before unattended shared operation.

Completion evidence for this release: automated tests and browser walkthrough recorded in the Git commit/release handoff. Live YouTube, paid Claude and audience-effectiveness tests remain outstanding; no keys or internal source documents are published.
