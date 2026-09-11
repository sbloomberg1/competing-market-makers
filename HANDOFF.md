# Competition onboarding manifest: competing_market_makers

**Private research prerelease [v0.1.1](https://github.com/sbloomberg1/competing-market-makers/releases/tag/v0.1.1) — not activated on Apex.** Signed images and the full evaluation have been verified in GitHub Actions. This manifest is filled with measured results and explicit outstanding decisions. The release assets contain the final spec and handoff; the immutable source tag contains the earlier release-source spec. No onboarding issue has been sent.

## 1. Goal statement and alignment plan

A maker earns trading surplus while competing against other adaptive makers with equal capital, public information and simulated timing. Winning a bracket is useful only alongside evidence of profitability and robustness to different fields.

Alignment checks:

- Compare the champion against fixed reference fields, all seat assignments and previously strong opponents; inspect head-to-head reliability for close policies.
- Inspect signed conditional edge, terminal marked profit, fees, volume, inventory and each condition stratum. Investigate sustained disagreement between ranking and terminal marked profit.
- Run the out-of-band stress audit and inspect top artifacts after each reveal. Review every round's top three entries and rerun the sizing/rank audit whenever a materially stronger policy appears. No inference of live-market deployability follows from this simulation alone.

The ranking score uses trade-time conditional expected surplus; terminal marked profit is unranked. This removes later price-path and Bernoulli noise while retaining adverse selection and information costs. The claim is marked at terminal probability; no random binary payout is added. This is a design choice requiring economic review with Apex.

## 2. Deliverables

| Item | Location | Status |
|---|---|---|
| Repository and release tag | [https://github.com/sbloomberg1/competing-market-makers](https://github.com/sbloomberg1/competing-market-makers); template Git history preserved | [v0.1.1](https://github.com/sbloomberg1/competing-market-makers/releases/tag/v0.1.1); private |
| Competition spec | `spec.yaml` | Final registry digests and exact signing identity; preflight and triage checked |
| Player image | `spec.yaml`, `evidence/release/player-verification.json` | Published privately, signed by digest, pulled and evaluated |
| Referee image | `spec.yaml`, `evidence/release/referee-verification.json` | Published privately, signed by digest, pulled and evaluated |
| Layer 2 screen | None proposed | Rationale in §5.15; Apex review required |
| Round generation | Platform seed plus referee-owned configuration | No separate `generate_round` needed |
| Overfit control | `benchmarks/overfit.py`; solo study in the primary Paying for Information repository | Implemented; memorizes public training seed 0 |
| Signing workflow | `.github/workflows/release.yml` | [Executed successfully](https://github.com/sbloomberg1/competing-market-makers/actions/runs/34649873981); both signatures verified |
| Input schema and fixtures | `referee/config.py`, `input.schema.json`, `fixtures/` | Generated and validated |
| Positive reference | `player/submission.py` | Full-container scores: 0.461856, 0.150063, 0.368899, -0.581848 |
| Adversarial set | `adversarial/`, `evidence/adversarial-results.json` | Ten fixtures exercised through containers |
| Records and reader | `/data/history/episodes.jsonl.gz`, `scripts/read_records.py` | 8,192 full-run episodes reconstructed; 27.92 MB compressed |
| Miner README | `README.md` | Complete for candidate rules |
| End-to-end evidence | `evidence/docker-full/`, `evidence/REPORT.md` | Local and GitHub released-image runs complete; stage pending |

Pins: `PROVENANCE.json` lists template/builder commits, every player/referee Python source hash, and the shared market-engine hash. Python base: `python:3.12-slim@sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9b536e184ea`, built for linux/amd64. No pip dependencies in either runtime image. Model revisions and dataset hashes: n/a, no external model/data; scenarios are generated procedurally. Development dependencies are exact versions in `requirements-dev.txt`. The final `spec.yaml` uses the pushed registry digests and verified signing identity. `evidence/release/verification.json` binds them to the tagged source commit and retains the verification results.

### Verified private release

The [release workflow](https://github.com/sbloomberg1/competing-market-makers/actions/runs/34649873981) built both linux/amd64 images from source commit `f309263f71a17eab85126978d26c5e64b91e4a45`, signed each digest with keyless Cosign, verified the signatures, pulled both images and ran the full configured evaluation. GitHub runtime: **62.92 seconds** in the referee; **66.08 seconds** for the full loop. All 8,192 replay records reconcile. Every scored and accounting field matches the local full-size result exactly; elapsed time is excluded from that comparison. This was a GitHub-hosted Docker run, not an Apex stage round.

| Image | Signed digest |
|---|---|
| Player | `sha256:dc473c1d5fad004ff9c747b71d20cfd79695ca4aeba779e85b376b77479a6f4f` |
| Referee | `sha256:c14baa6990a34b4da67a03fd272626dfc2992e43b89dda95d0886f64e94c9cae` |

Identity: `https://github.com/sbloomberg1/competing-market-makers/.github/workflows/release.yml@refs/tags/v0.1.1`. Issuer: `https://token.actions.githubusercontent.com`. Repository and both container packages were verified private on 11 September 2026. Apex reviewer and private-package access must be arranged before onboarding.

Use the [final spec release asset](https://github.com/sbloomberg1/competing-market-makers/releases/download/v0.1.1/spec.yaml) with [input.schema.json](https://github.com/sbloomberg1/competing-market-makers/releases/download/v0.1.1/input.schema.json), or the matching files on main. The `v0.1.1` source tag is immutable and contains the pre-build release-source spec; it is not the final deployment manifest. The release review archive contains this completed handoff, final spec, tests, research evidence, signature outputs and the full released-image replay. Source commit and runtime-file hashes are recorded in `PROVENANCE.json`.

## 3. Proposed operations

| Parameter | Proposal and reason |
|---|---|
| process_type | cpu; simulator and batched policies need no GPU |
| kind | duel; adaptive opponents are the central research question |
| duel | 4 players, 3 games per match, swap_sides=false; tie-priority seats rotate internally; platform advancement contract pending |
| round_length_in_days | 1; frequent adaptation without changing the evaluation distribution |
| submission_reveal_days | 2; permit iteration while delaying direct copying |
| lower_is_better | false |
| baseline_raw_score / baseline_score | 0 / 0; no arbitrary positive score offset |
| resources per sandbox | 1 CPU, 512 MiB, 0 GPUs; full local run completed at these limits |
| evaluate.timeout_s / referee.timeout_s | 1200 / 1200; derived budget and headroom below |
| per-request deadline | 100 ms for the whole batch of up to 256; below toolkit's usual per-move norm, justified by batching and measured runtime; sophisticated policy headroom needs stage review |
| submission fee | Propose approximately USD 1; Macrocosmos decides |
| incentive weight | Propose 0.02 for the experimental follow-on; Macrocosmos decides |

Declared floor is zero. The positive reference is a test artifact, not a declared nonzero floor. The builder's simultaneous “positive published baseline” and “baseline copy cannot lead” requirements need a bootstrap policy decision; see §5.4. Do not silently substitute a hidden score offset or contradictory floor.

## 4. Round variation and sizing

Every episode belongs to one of eight equally sized strata: usual volatility (55 or 170 ticks, with ±10 jitter), public-noise bound (180 or 650, with ±25 jitter), and information fee multiplier (1 or 6). Retail arrival count varies from three to five per episode. A private per-episode RNG is derived from the platform master seed and episode index with SHA-256. Initial fair value, path, jump signs, signal errors, retail directions/markups and the jittered parameters change with the seed. A fixed eight-stratum mixture keeps difficulty approximately stationary. Choosing only new price paths without changing condition parameters is not the entire rotation mechanism.

The usual live ranges exclude the stress audit's doubled volatility, public noise and information prices. The audit has no input-schema switch available to a submission. Published historical seeds are practice data, never live seeds. No external round generator is required, provided Apex keeps a sufficiently unpredictable master seed private to the referee.

Measured N: **8,192** episodes, 24 ticks each, batch 256. Twenty master seeds, with live condition generation. Reference mean **0.460887635**; sample σ_round **0.003884241**. A 1% margin at that mean is 0.004608876; one quarter is 0.001152219.

**Solo quarter-margin rule: not applicable to duel advancement; the raw scores would fail it.** The adaptive reference wins 20/20 ordinary fields, 20/20 seat permutations across five seeds and 5/5 stress fields. Its largest within-seed range over seats is 0.000789. However, identical adaptive policies produce different inventory/fill paths and nonzero score spreads, with a largest spread of about 0.0086 in five seeds. Close-policy advancement is therefore not qualified. The three-game setting is a proposal, not a demonstrated cure. A field of four losing static makers still has a relative winner.

The primary competition supplies the shared generator’s overfit control. This duel’s own evidence emphasizes opponent interaction and seat allocation. Before activation, Apex must agree how ties, statistically close results, repeat games, invalid entries and four-player advancement work. Do not introduce combat-specific `killed_opponent` or `self_death` metadata to force market outcomes through an unrelated aggregator.

Full-size reference evaluation: **36.60 seconds** in the referee; **38.25 seconds** including local harness lifecycle. One local full-size run and 20 trusted-policy simulations are supplied; these are not twenty separate stage rounds.

Timeout budget:

- 32 batches × 24 ticks × 1 phase × 4 players = **3,072 action calls**.
- At 0.1 seconds each: **307.2 seconds**. A player that actually exceeds a deadline forfeits and receives no further calls; this budget covers one that stays just inside every deadline.
- Readiness and reset allowance: **68 seconds** (four players, sequentially).
- CPU scoring, JSON processing and record-write reserve: **240 seconds**, approximately 6.1 times the entire measured referee runtime. This is a conservative planning allowance, not a measured maximum on Apex storage/hardware; verify it with a dense-response run on stage.
- Planning worst case: **68 + 307.2 + 240 = 615.2 seconds**.
- Proposed timeout: **1,200 seconds**, headroom **1.95×**. Fits the skill's 20-minute ceiling. Remaining margin: 584.8 seconds.

The cardinality and per-response size are bounded. Host outages and blocked filesystem I/O are operational failures outside this planning bound. No score uses wall time. Records are best effort and a record-write failure does not change arithmetic, as tested.

## 5. Threat-model questionnaire — private review

1. **Miner-visible surface.** Round input schema: `episodes`, `batch_size`, `deadline_ms`, all platform-controlled. Reset wrapper passes constant match ID `market`, player index 0 and seed 0, plus mode, horizon, price scale, batch size and deadline. Observations contain ID/time, public signal/age/noise, usual volatility, signal/tier/cost schedule, account limits/cash/inventory, own previous fills and previous quotes. Purchased signals are the intentionally bought information. No future prices, terminal probability, master/per-task seed or event tape enters the player. The referee-only seed env is not copied into the player container.
2. **Seed leverage.** The public engine plus the true master seed would regenerate all scenarios. Privacy and entropy of the platform seed are therefore essential. SHA-256 does not increase the entropy of a weak seed. Apex must confirm the live seed is private and impractical to enumerate (prefer at least 128 unpredictable bits), and that neither logs nor job metadata expose it before/during a run. Do not reuse the published test seeds in production.
3. **Degenerate submissions.** Constant narrow quotes, random legal quotes, all-zero/wrong-shaped responses, empty results and no trading were exercised. Malformed/failing entries receive −1000 and cannot win; constant/random makers lose signed edge; no-trade receives zero and loses to the positive reference field. No ad hoc gate excludes a legitimate simple profitable strategy. An idle valid policy can beat a wholly losing field; a tournament win alone is not a profitability or liquidity qualification.
4. **Baseline resubmission.** An exact copy earns the same positive raw score as the reference. It cannot beat an identical rescored incumbent by 1%, but it could become the first leader against the declared zero floor. That is an unresolved contradiction in the builder's written requirements, not something this code conceals. Apex should specify reference seeding/eligibility or an explicit initial qualification policy. Do not mark this check passed without that decision.
5. **Metric gaming.** Probes covered narrow constant quotes, random prices, never trading, excessive information spending, late failure after profitable ticks, message abuse and inventory/cash accounting. Signed episode values are summed before the solo floor; negative tasks cannot be dropped. Marked profit is compared with conditional edge to expose directional-risk divergence. This was a bounded engineering probe, not a completed independent day-long red-team review. Economic strategies, cross-episode learning, simulator specialization and coordinated entries remain review areas.
6. **Malicious responses.** `transport.py` accepts one bounded UTF-8 JSON object, rejects duplicate keys, nonfinite JSON constants and excessive nesting, and imposes a total response deadline. `validate_action` checks exact batch length, action structure, key set, integer types excluding booleans, price order and ranges. A bad response forfeits the entire evaluation/game for that player. Invalid raw payloads are not reflected in metadata.
7. **Profitable failure.** Missing, unhealthy, exception, timeout and late-invalid fixtures forfeit the entire player result. A forfeit receives −1000, below any valid bounded signed score, and is removed from winner selection. Unexpected referee bugs are not converted into successful scored results; they propagate for platform attribution. There is no retry that chooses a more favorable market path. Remaining valid duel players continue with the failed player inactive, which can still affect their field and is part of the coordinated-entry risk.
8. **Aggregation integrity.** N is platform-controlled and fixed; denominator never shrinks. The solo floor applies once after summing all signed episode edges. No per-episode clipping or arbitrary positive offset. Quote inventory/capital/size bounds limit a valid tick to at most eight fills per maker; edge magnitude is at most eight currency units per tick before fees. A 24-tick episode is bounded well above −1000 even under the stress fee schedule. Early forfeits never retain partial eligibility. Per-stratum diagnostics reveal concentration.
9. **Adversarial loop results.** All ten fixtures were evaluated as real mounted submissions in isolated containers at 256 episodes. See table below and machine-readable results; these fixtures are shared between the competitions. Full-size reference runs separately demonstrate scale.
10. **Defense hygiene.** Detailed threat rationale is confined to this private manifest. Miner documentation states ordinary market and response rules, not attack explanations. Production error strings are generic; result metadata contains scoring/account diagnostics. Test fixtures and this manifest should be reviewed before choosing public repository visibility. This is a source review, not a claim of an external information-flow audit.
11. **Copy plus epsilon.** A duel does not inherit the solo 1% threshold. Tiny mutations of an equivalent policy can win from sampling/tie allocation. Close-result handling and related-entry controls are unresolved; local evidence does not establish a defense against this.
12. **Cross-round leakage.** A prior task record reveals that task, not the private seeds. Seeds and condition jitter change; the overfit control collapses on unseen worlds. Parameter distributions are intentionally learnable. The record archive must be released after evaluation; exposing it live would reveal current truth. A miner can retain its own public/paid observations as part of legitimate policy state.
13. **Error-message hygiene.** Normal terminal reasons are `completed` or `forfeit`; transport/action failures use generic unavailability/invalid-action text. No secret seed, URL, source exception or hidden state is echoed to a player by the scorer. Player-generated logs live in that player's sandbox and are not trusted scoring inputs.
14. **Referee state.** New episode state is allocated per evaluation. No cross-game cache or submission-controlled pathname. Conditions derive deterministically from the seed and index. All scored terms use integer prices, quantities, costs and simulated ticks. Elapsed seconds are an unranked diagnostic; deadlines alone depend on a clock. Native and container accounting are deterministic for a fixed input and policy.
15. **Code execution.** Python permits filtering, dynamic inventory rules, search and learned approximations; ONNX/TorchScript alone would exclude useful methods. The spec adds `socket` and `subprocess` to generic AST screening. No Layer 2 image is proposed because there is no untrusted model parser or data deserializer beyond the constrained JSON interface. Generic screening is not a security boundary; container separation, no egress and CPU/memory/PID limits remain required. Apex decides whether another screen is needed.
16. **Player-image hygiene.** Only `launch.py` and unchanged vendored gym_v1 enter the player image. Submission code is mounted at runtime. Engine, conditions, future paths, seed and scorer are absent. No Docker socket or referee filesystem is mounted in a player. The local duel harness uses a separate internal network for each player, with the referee attached to all; it prevents player-to-player traffic. Apex must confirm equivalent network isolation on stage.
17. **Diagnostics payload.** Result metadata contains signed edge, marked profit, information expenditure, volume, purchase counts, stratum aggregates, active flags and elapsed time. Post-evaluation records intentionally include per-tick fair values to make fill-edge arithmetic reconstructible. They therefore correlate with that completed task’s hidden truth, by design. This conflicts with a literal reading of “no diagnostics correlate with hidden ground truth”; the safe distinction is completed-task disclosure versus future/live leakage. No seed is disclosed. Do not stream these records during play.
18. **Evaluation records.** Versioned gzip JSONL in `/data/history/episodes.jsonl.gz`, one record per episode plus a summary. Each episode includes realized conditions, buy/quote observations, chosen actions, account fills, charged fees, eligibility, terminal state and arithmetic. Summary includes phase/tick of faults and fixed-denominator aggregation. Malformed raw payloads are omitted; their failure location is recorded. Neither master nor per-task RNG seeds are present. Records hold only one batch in memory and write failures leave scores unchanged. `read_records.py` reconstructed all 8,192 full-run episodes, 27.92 MB compressed. Confirm Apex archives `history/` and that this volume fits its artifact policy. As with any task transcript, realized conditions are present, not RNG state or seeds.

| Submission | Candidate player's score | Outcome |
|---|---:|---|
| constant.py | -1.943348 | completed |
| empty.py | -1000.000000 | forfeit |
| exception.py | -1000.000000 | forfeit |
| late_failure.py | -1000.000000 | forfeit |
| nan.py | -1000.000000 | forfeit |
| no_trade.py | 0.000000 | completed |
| oversized.py | -1000.000000 | forfeit |
| random.py | -7.512841 | completed |
| timeout.py | -1000.000000 | forfeit |
| zero.py | -1000.000000 | forfeit |

## 6. GPU justification

Not applicable: both images are CPU-only. No GPU access is requested.

## 7. Admission sequence and outstanding decisions

1. Private repositories and signed `v0.1.1` review releases are published under `sbloomberg1`. Both released-image evaluations and replay checks passed. The final spec is pinned to actual registry digests; toolkit preflight and onboarding triage were rerun.
2. Arrange Apex reviewer and package-pull access. No Apex onboarding issue or message has been sent. `ONBOARDING_ISSUE.md` is a concrete draft for that request.
3. Apex reviews score/goal alignment, the baseline-copy/bootstrap contradiction, private seed entropy, network isolation, record archiving/size and the 100 ms batch budget. The duel additionally needs four-player advancement, signed-score/forfeit handling, close-match rules and coordinated-entry review.
4. Resolve those decisions; run fresh-seed and stage-hardware checks, including dense record writes and deadline behavior. The supplied results support a concrete design review, not a claim that security/admission review has already occurred.
5. With authorization, submit the onboarding draft plus this manifest and released artifacts. Macrocosmos reviews, copies the final spec to its private registry, runs the baseline on stage and determines fee, incentive weight and activation timing. Runtime or scoring updates require a new immutable version and signatures.
