# Sequential Worker–Judge playbook

This run is complete. To refresh it, preserve a versioned copy before changing its state. Do not reclassify a historical rank as a current leaderboard.

1. Confirm the selection benchmark, quarter, geography and revenue definition. Keep one queue entry per selected app/operator. Map parent relationships to avoid double counting.
2. Work on the first `PENDING` entity only. Search company/app, legal operator, parent, HQ, investors, dated traction, titles, monetization and distribution. Prefer filings, terms, storefronts and first-party disclosures, supplemented by attributable reporting and explicitly labeled estimates.
3. Draft the six sections and structured metrics using an existing `evidence/*.json` as the schema. Each metric needs `name`, numeric `value`, `unit`, `period`, `scope`, `source_url` and `qualifies`. Preserve source qualifiers such as approximately, over, cumulative, combined platforms, or parent-level funding in the narrative and unit/scope fields. Do not manufacture an absolute revenue number from a rank.
4. Judge ownership/HQ identification, at least two dated qualifying metrics, absence of prohibited placeholders, and specific strategy. The ownership and strategy checks require substantive analyst review; they are not automatically proven by populated text.
5. Save the draft with `python3 record_profile.py /absolute/path/to/draft.json`. The helper enforces the first-pending queue order, stores the Markdown/evidence/judgment, hashes the profile and updates counts. It does not browse or verify source truth automatically.
6. If the result needs follow-up and attempts are below two, increment that entity's `attempts` in `queue.json`, perform one targeted search addressing the exact gap, record the findings, revise and re-judge before advancing. `attempts` counts additional research rounds, not individual page opens. Never conceal a failed gate by changing its meaning.
7. On pass, advance immediately. After two unsuccessful follow-ups, mark DONE with `EXCEPTION_AFTER_TWO_RETRIES` and expose the remaining gaps; DONE alone does not mean verified. If interrupted, leave the active draft and queue available for resumption.
8. Once pending is zero, regenerate the comparison, metrics, source index and quality report. Check exact profile count, dates/units, source links, profile hashes and local navigation. Bundle only the active research folder, excluding caches and unrelated private source materials.

The included snapshots are finished research, not an unattended live data feed. Refreshes need renewed web research and explicit analyst judgments.
