# Private release v0.1.1

The [private research prerelease](https://github.com/sbloomberg1/competing-market-makers/releases/tag/v0.1.1) contains signed player/referee images, the final deployment spec, and the completed review package. It is not an Apex activation. No onboarding issue has been sent.

The [release workflow](https://github.com/sbloomberg1/competing-market-makers/actions/runs/34649873981) built source commit `f309263f71a17eab85126978d26c5e64b91e4a45`, signed and verified both registry digests, then pulled those images and ran the full 8,192-episode evaluation. All replay arithmetic passed. `evidence/release/verification.json` records the image digests, signing identity, source commit, replay hash and timings. Repository and package visibility were checked as private on 11 September 2026.

## Which spec to use

Use the release's `spec.yaml` and `input.schema.json` assets or the identical files on main. The immutable `v0.1.1` source tag contains the release-source spec before the images existed. The workflow generated the final spec from the pushed image digests; a later documentation commit copied it to main without changing any runtime source. `review-package.tar.gz` contains the completed handoff, final spec, source files, experiment evidence, signature verification outputs and full released-image replay.

The earlier `v0.1.0` workflow stopped at the signing-tool installer before publishing images. Version 0.1.1 corrected the pinned installer/tool version pairing. No score rule changed; engine evidence retains version 0.1.0 in provenance. The repository keeps both immutable source tags for auditability.

## Verify the images

With private GHCR access, run Cosign against each digest in `spec.yaml`, using certificate identity `https://github.com/sbloomberg1/competing-market-makers/.github/workflows/release.yml@refs/tags/v0.1.1` and issuer `https://token.actions.githubusercontent.com`. The release workflow contains the exact commands and checks the transparency-log proof. Do not substitute local image IDs for registry digests.

## Next release

1. Resolve the relevant design changes, bump the competition version, update the tag identity and source hashes, and run tests, preflight and full-size evaluations. Preserve template history and `template-upstream`.
2. Push a new immutable version tag. The workflow builds, pushes, signs and verifies both images, runs them, verifies all records and emits `signed-release-spec`.
3. Download that artifact, copy its final spec to main, rerun toolkit preflight and onboarding triage, retain verification outputs, and attach a completed review package to the matching release. Runtime files must still match the tagged source hashes.
4. Arrange reviewer and private-image pull access. With authorization to contact Macrocosmos, submit the completed onboarding draft and final release assets. Macrocosmos determines security review, staging, operational settings and activation.

All future runtime/scoring changes need a new immutable competition version and signed images. Release completion does not resolve the admission questions in `HANDOFF.md`.
