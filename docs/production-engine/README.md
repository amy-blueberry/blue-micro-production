# Bumpp operating structure

Current version: Secret Sauce intelligence v2, November 22, 2026. Architecture and configuration only; connectors, schedules and production are inactive.

## Visual entry points

1. [Intelligence structure: four stages, ten feeds, scores and routes](https://miro.com/app/board/uXjVELeVptk=/?moveToWidget=3458764691253050156).
2. [Detailed agent workflow: eight roles, handoffs, approvals and exceptions](https://miro.com/app/board/uXjVELeVptk=/?moveToWidget=3458764691250487231).
3. [Production playbook: 18 steps, owners and tools](https://miro.com/app/board/uXjVELeVptk=/?moveToWidget=3458764691247743232).

All three are sections of the same Miro board. Links focus the appropriate section and do not grant board access.

## Specification hierarchy

- [Supplied source specification](references/README.md): source provenance; the original internal attachment is not distributed here.
- [Content intelligence playbook](CONTENT_INTELLIGENCE_PLAYBOOK.md): DISCOVER → DECODE → CREATE/TEST → LEARN; audience design, limits and decision rules.
- [Feed registry](intelligence_feeds.json): nine dynamic external feeds and one internal learning feed.
- [Authority panel](authority_panel.json): ten supplied candidates, pending account/activity/cohort verification.
- [Reference watchlist](agent_watchlist.json): existing seed references and separate company-research context; not the discovery universe.
- [Agent operating model](AGENT_OPERATING_MODEL.md) and [contracts](agent_contracts.json): responsibilities, triggers, version-bound approvals and three independent score sets.
- [Templates](INTELLIGENCE_TEMPLATES.md): daily findings, story decodes, weekly opportunities and learning records.
- [Production blueprint](ENGINE_BLUEPRINT.md) and [backlog](BUILD_BACKLOG.md): implementation order, production mechanics, owners and acceptance checks.

## Material version changes

Replaced the single 80-point virality gate with separate viral opportunity, story/IP potential and execution opportunity assessments. There is no combined score or universal numerical cutoff. Added dynamic feed universes, a separate amplification panel, five daily findings / three weekly opportunities, explicit behavioral cohort assignment, and F10 instrumentation before publication. Existing production authorization, safety, rights, budget and quality gates remain.

No current creator metrics, live trends, actual audience outcomes or verified API access are implied by this update. The conservative review-cap interpretation is documented in the playbook. Existing Miro comments are retained.
