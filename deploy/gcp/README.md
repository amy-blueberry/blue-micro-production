# Bumpp Intelligence — Google Cloud pilot

Dedicated project: `bumpp-intelligence-prod`. Region/zone: `us-east1` / `us-east1-b`.
Requested hostname: `intelligence.bumpp.gg`.

## Deployment design

- Single `e2-small` Compute Engine VM (`intelligence-1`), Debian 12; systemd restarts the app on failure.
- Separate 20 GB persistent data disk (`intelligence-data`), not auto-deleted with the VM. SQLite remains single-server; do not scale multiple writers against copies.
- HTTPS Application Load Balancer and Google-managed certificate. DNS A record: `intelligence` → `136.82.7.249`, DNS only.
- Google-managed IAP sign-in, initial authorized user `devops@houseofblueberry.com`. Additional users require explicit IAM grants. Organization membership alone does not grant app access.
- App validates signed IAP assertions, audience, issuer and identity on every application request. Health endpoint returns only an OK status. Host/origin and CSRF protection remain enforced.
- Network ingress permits only IAP SSH and Google load-balancer/health-check ranges. The VM has no service account. Its public address is for outbound provider requests, not direct app access.
- App runs as non-login `bumpp`, with a read-only system filesystem and writes restricted to its data directory. Runtime credentials are not part of the code archive or Git.
- Daily source-retention cleanup. Research is manually initiated; interrupted jobs remain visible and require explicit retry, avoiding duplicate provider charges.

This is a single-instance pilot, not high availability. There is no autoscaling, automatic application release, or cross-region recovery. Provisioned compute, disks, load balancing and IP addresses incur charges even with no research requests. Provider usage is billed separately.

## Release

Build an allowlisted archive containing `intelligence/` (excluding tests/caches), `deploy/gcp/`, and only these registry files under `docs/production-engine/`: `authority_panel.json`, `agent_watchlist.json`, `intelligence_feeds.json`. Never archive the repository root or `.runtime` wholesale.

Upload code through `gcloud compute scp --tunnel-through-iap`. Run `install.sh` as root with `RELEASE_DIR` set to the uploaded archive directory and `IAP_AUDIENCE` set to `/projects/736625392869/global/backendServices/3928542396117919800`. The uploaded application archive must be named `application.tgz`.

The user explicitly approved migration on November 24, 2026. The existing database and private connection files were copied through IAP SSH after checking that no research job was active. Integrity checks and counts matched: 97 candidates, 4 finding versions, 5 research runs. Saved credentials have mode 0600 and belong to the service user. No private runtime files were committed.

Daily data-disk snapshots are scheduled for 04:00 UTC with seven-day retention. They are crash-consistent disk snapshots, not a tested full disaster-recovery procedure. Restoring a backup must include database integrity checks and the purge command before reopening access, so expired source records are not reintroduced. Backups also contain private connection settings and require restricted project access.

Before subsequent releases, check that no research run is active, preserve a consistent SQLite backup, stage the new code, restart the service, and check health/authentication and retained record counts. Never overwrite an existing database with a seed or older snapshot. Keep a previous code release for rollback; schema changes need a separate migration/rollback plan.

## Operations and verification

Use explicit `--project=bumpp-intelligence-prod --account=devops@houseofblueberry.com` on cloud commands. Do not change existing Bumpp projects.

- `gcloud compute backend-services get-health intelligence --global`: healthy application backend.
- `gcloud compute ssl-certificates describe intelligence --global`: certificate ACTIVE after DNS propagation.
- `gcloud compute ssh intelligence-1 --zone=us-east1-b --tunnel-through-iap`: operator access.
- On VM: `sudo systemctl status bumpp-intelligence`; `curl http://127.0.0.1:8080/healthz`.
- Unsigned requests to app routes must return 401, including a forged identity header.
- Public HTTPS without a session must redirect to Google sign-in. Authorized browser session must load the application.
- Verify persistent DB and service survive restart. Never infer provider connectivity from a saved key; validate with an authorized small research run.

Google guidance: [Enable IAP for Compute Engine](https://docs.cloud.google.com/iap/docs/enabling-compute-howto).

## Launch verification (November 24, 2026)

Server active; backend HEALTHY; persistent disk mounted; application restart verified; missing and forged IAP tokens rejected with 401. 57 Python tests and voice interaction tests passed. Hostname DNS is correct; Google-managed HTTPS certificate was still provisioning at the last check. Browser sign-in and a successful cloud provider research run are not yet verified. Provider credentials being present does not prove API credit or model access.

## Sign-in repair and browser verification

The initial deployment omitted the cryptography dependency needed for ES256 IAP tokens. Added `cryptography==46.0.3` and a deployment-venv regression test that exercises real signatures, wrong audiences, expired tokens, invalid issuers and forged tokens. The installer now runs that test before starting the service. After installing the dependency and restarting, the authenticated Chrome session successfully loaded the live Findings dashboard with 4 briefs and 85 pending leads. HTTPS and browser sign-in are now verified. This does not establish successful provider research calls.

## Cloud pilot request limits

Hosted configuration now sets `BUMPP_RESEARCH_DAILY_CALLS=25` and `BUMPP_SOURCE_DAILY_PAGES=25`. Existing usage counters are preserved. Both allowances reset at midnight UTC. These are request ceilings, not currency budgets. The Findings dashboard shows both remaining counts. Whole batches are checked before queue creation; workers check again before retrieving a page. Failed provider attempts still consume an attempt. Local defaults remain five model calls and ten pages unless configured.
