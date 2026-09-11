# Evaluation evidence — competing-market-makers

Competition prerelease 0.1.1, engine 0.1.0; measured locally and on GitHub on 11 September 2026. This is a research qualification report, not a stage or production approval.

| Check | Result |
|---|---|
| Full configured evaluation | 8,192 episodes, 36.60 seconds in referee |
| Isolated containers | Five containers; one CPU / 512 MiB each; linux/amd64; internal referee-to-player links |
| Reference raw score(s) | 0.461856, 0.150063, 0.368899, -0.581848 |
| Tests | 26 passed |
| Replay accounting | 8,192 episodes reconstructed exactly |
| Full replay size | 27.92 MB compressed |
| Master seeds | 20 |
| Reference mean | 0.460887635 |
| Sample standard deviation | 0.003884241 |
| Quarter of a 1% margin | 0.001152219 |
| Release / stage approval | Signed private prerelease complete / stage pending |

The adaptive reference wins all 20 ordinary fields against wide, tight and static policies. It also wins all 20 seat permutations in the five-seed seat audit, and all five stress fields. The greatest within-seed score range for the adaptive policy across seats is 0.000789.

This is a duel, so the solo 1% takeover rule does not directly apply. Its raw-score SD would fail the solo quarter-margin test. Close-policy tournament reliability therefore remains unqualified. Identical policies do not reliably produce exact draws: account paths diverge after tie allocation, and their within-game score spread reached roughly 0.0086 in the five tested seeds. A losing field of four static makers still produces a relative winner. These are explicit limits of the current tournament proposal; review repeat counts, statistical draws, duplicate entries and profitability checks with Apex before activation.

## Files and reproduction

- `summary.json`: machine-readable qualification summary.
- `docker-full/run.json`: images, resource limits, timing and full result. Image IDs/build digests are local evidence, not signed registry releases.
- `record-verification.json` and `docker-full/history/episodes.jsonl.gz`: accounting verification and records.
- `tests.txt`, `preflight.txt`, `adversarial-results.json`: test and fixture outcomes.
- `../scripts/experiment.py`: trusted-reference experiment runner. Untrusted submissions belong in `docker_match.py`.
- `../scripts/read_records.py`: replay and score arithmetic verifier.

The numerical reference experiments run trusted strategies in the host process; isolated full-size container runs separately confirm the runtime. Only the recorded configurations and reference policies were timed. The worst-case budget is derived in HANDOFF.md; it has not been validated on Apex stage hardware.

## Signed released-image verification

[GitHub release workflow](https://github.com/sbloomberg1/competing-market-makers/actions/runs/34649873981) passed all tests and evaluated the actual signed registry images for 8,192 episodes. Runtime: 62.92s in the referee, 66.08s including the harness lifecycle. Scores and all accounting diagnostics exactly match the local full-size result, excluding elapsed time. All records reconcile. This is a second host and real published images, not an Apex stage run.

`release/verification.json` links source, signed image digests and replay hash. Adjacent files contain both build metadata files, full Cosign verification output, the run/result and record verification. The private release asset `review-package.tar.gz` preserves the full replay under `released-evaluation/history/`. The historical `docker-full` results remain labeled as local images.
