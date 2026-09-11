# Draft: [onboarding] competing_market_makers v0.1.1

**Ready to request design and stage review once access is arranged. Open admission decisions are listed below; this draft has not been sent.**

## What is the competition?

Four submitted Python market makers choose quotes simultaneously against shared informed and retail flow. Each player receives mean signed conditional fill edge; the greatest eligible score wins each game. Success means an adaptive, profitable maker that remains competitive across different fields and seat assignments. Close-policy handling and four-player bracket semantics require review before activation.

This is a separate follow-on competition in a paired market-simulation project. We used the builder skill at commit `5a0be85a5975f0948a2d4878597a820c636656e2` and retained the hello-world example's repository history.

## HANDOFF.md

Attach [HANDOFF.md](https://github.com/sbloomberg1/competing-market-makers/releases/download/v0.1.1/HANDOFF.md) and the [complete review package](https://github.com/sbloomberg1/competing-market-makers/releases/download/v0.1.1/review-package.tar.gz). The private questionnaire is complete with explicit limitations and outstanding decisions. Use these finalized assets rather than the pre-build handoff at the source tag.

## Evaluation time budget vs. timeouts

Proposed worst-case planning budget: 68s startup/reset + 3,072 action calls × 0.1s + 240s scoring/record-write reserve = 615.2s. Referee and evaluation timeouts are both 1,200s; approximately 1.95× headroom. Local full-size reference run: 36.60s in the referee; signed released-image run on GitHub: 62.92s (66.08s full loop). Both used one CPU / 512 MiB. Stage hardware and dense-record write allowance still require verification; no unflagged over-budget claim is made.

## Release fields

| Form field | Value |
|---|---|
| Competition id | `competing_market_makers` |
| Spec version | `0.1.1` private prerelease |
| Competition repo URL | https://github.com/sbloomberg1/competing-market-makers (private) |
| Released git tag | [`v0.1.1`](https://github.com/sbloomberg1/competing-market-makers/releases/tag/v0.1.1) |
| Player image ref | `ghcr.io/sbloomberg1/competing-market-makers-player` |
| Player image digest | `sha256:dc473c1d5fad004ff9c747b71d20cfd79695ca4aeba779e85b376b77479a6f4f` |
| Referee image ref | `ghcr.io/sbloomberg1/competing-market-makers-referee` |
| Referee image digest | `sha256:c14baa6990a34b4da67a03fd272626dfc2992e43b89dda95d0886f64e94c9cae` |
| Target environment | Stage first |
| spec.yaml | [Final release asset](https://github.com/sbloomberg1/competing-market-makers/releases/download/v0.1.1/spec.yaml), with [input schema](https://github.com/sbloomberg1/competing-market-makers/releases/download/v0.1.1/input.schema.json) |

Signing identity: `https://github.com/sbloomberg1/competing-market-makers/.github/workflows/release.yml@refs/tags/v0.1.1`; issuer: `https://token.actions.githubusercontent.com`. [Successful workflow](https://github.com/sbloomberg1/competing-market-makers/actions/runs/34649873981); exact verification output and replay evidence are included in the release package.

## Pre-submission checks

- [x] `apex-dev preflight --spec ./spec.yaml --input fixtures/input.json` passes structural and input validation.
- [x] Custom local container harness produced a valid `result.json` and replay archive. The pinned toolkit's `apex-dev run` itself does not execute the match.
- [x] Both images keyless-signed and signatures verified on the released tag.
- [x] Both images pushed, pulled by registry digest and evaluated by the authenticated release workflow. Apex pull access still needs to be arranged.
- [x] Final spec passes toolkit onboarding triage as well as preflight.
- [ ] Apex admission decisions in `HANDOFF.md` resolved, with stage validation scheduled.

Local tests: 26 passed. Full replay accounting: 8,192 episodes verified. Ten adversarial submission fixtures exercised through the complete player/referee loop. The adaptive reference wins 20/20 strong-field matches; close-policy reliability remains unqualified.

## Decisions requested from Apex

- Confirm baseline bootstrap/eligibility: a published positive reference can otherwise lead against a declared zero floor.
- Confirm referee-only, high-entropy seeds; network isolation; post-evaluation `history/` archiving and record-size allowance.
- Review trade-time conditional edge as the ranking score and terminal marked profit as a diagnostic.
- Review the 100 ms deadline for the whole batch, CPU allowance and the stage timeout budget.
- Confirm four-player advancement, three-game repetition, signed scores, −1000 forfeit sentinel, draws/near-ties and coordinated-entry handling.
