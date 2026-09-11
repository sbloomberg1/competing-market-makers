# Competing Market Makers — design candidate 0.1.1

Status: research and implementation candidate; not approved or released.

## Success

Produce an adaptive market maker that earns edge under competition from other submitted makers with equal capital, information access and simulated timing. Inspect profitability against a fixed reference field, inventory exposure and sensitivity to opponents as well as tournament victory.

## Proposed game

Four submitted policies share one binary-claim market. They observe the same public news and the previous book, plus their own fills and inventory. They replace quotes simultaneously; a private latent probability then moves, an informed taker consumes stale quotes, and retail routes by price. Ties use rotating seat priority. No player observes another player's current action before choosing its own. Information purchases are disabled in this competition's first version.

The shared engine follows the Paying for Information design's bounded martingale, capital rules, price-sensitive retail and accounting. Each Apex game aggregates independent episodes and balanced tie-priority rotations. The greatest mean signed edge wins the game. Invalid players forfeit the entire game; all-invalid or exactly tied games can return no winner. A platform bracket determines the round, subject to Apex confirming its four-player advancement and tiebreak contract. We will not invent combat outcomes to force financial results through a combat-specific aggregator.

## Evidence required

Repeat reference fields across at least 20 seeds and seat assignments; quantify champion reliability and matchup dependence. Check negative-edge winners, identical-policy ties and all-player failures. Benchmark resource use with four isolated player containers. Assess coordinated-entry and opponent-selection exposure privately before admission. Eight-player games are a future option, not part of this initial spec.

## Initial operating proposal

CPU only, 1 CPU / 512 MiB per sandbox; one-day rounds; two-day reveal delay; four players per match and balanced internal seat rotations. Final tournament settings, fee and emission weight require platform review. Maintain this as a separate competition and release from Paying for Information.
