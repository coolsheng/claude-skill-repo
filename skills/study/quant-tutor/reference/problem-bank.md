# Problem Bank — archetypes, answers, and named traps

Read **only the section for the tier you're currently serving** (plus the review tier when you mix in a ~1-in-6 review problem). Each archetype is a *template*, not a fixed problem — vary the numbers, framing, and surface story every time so the user can't pattern-match on wording. The point of the bank is to guarantee (a) a correct answer you can check against, and (b) a **named cognitive trap** for the explanation. Generate fresh problems in the same spirit when you've exhausted the archetypes.

Difficulty: ●○○ easy · ●●○ medium · ●●● hard.

---

## Tier 1 — EV & linearity of expectation

- **●○○ Fair value of a single roll.** You pay $X to roll one fair d6 and win the face value in dollars. Fair price? → E = 3.5. *Trap:* anchoring on the most likely outcome instead of the mean; there is no "most likely" for a uniform die.
- **●○○ Re-roll once.** Roll a d6; you may keep it or re-roll once and must take the second. Optimal EV? → Re-roll when first ≤ 3; EV = 4.25. *Trap:* treating "re-roll" as free upside — you must compare the roll to the EV of re-rolling (3.5), not to 6.
- **●●○ Sum of dependent indicators.** Shuffle a deck; how many cards land in their own original position (fixed points) on average? → E = 1, by linearity (52 × 1/52), **despite heavy dependence**. *Trap:* believing you must model the dependence; linearity of expectation does **not** require independence.
- **●●○ Coupon collector (short).** Expected rolls of a d6 to see all six faces? → 6(1 + 1/2 + ... + 1/6) = 14.7. *Trap:* guessing ~6 or ~12; the tail (waiting for the last face) dominates.
- **●●● Hat-check / matching.** n people, hats returned at random — expected number who get their own hat, and the variance? → mean 1, variance 1 (a near-Poisson). *Trap:* assuming a large n makes matches more likely; the mean is 1 for all n.
- **●●● Stick-breaking.** Break a unit stick at two uniform random points; expected length of the middle piece? → 1/3 by symmetry/linearity. *Trap:* over-integrating; symmetry says all three expected pieces are equal.

## Tier 2 — Conditional probability & Bayes

- **●○○ Two-child problem.** A family has two children, at least one is a boy. P(both boys)? → 1/3 (not 1/2). *Trap:* dropping the BG/GB asymmetry — conditioning shrinks the sample space unevenly.
- **●●○ Rare-disease false positive.** Prevalence 1/1000, test 99% sensitive, 5% false-positive. You test positive — P(disease)? → ≈ 0.0194 (~2%). *Trap:* **base-rate neglect** — fixating on the 99% and ignoring that healthy-and-false-positive vastly outnumbers sick-and-true-positive.
- **●●○ Boy born on Tuesday.** Two children, at least one is a boy born on a Tuesday. P(two boys)? → 13/27. *Trap:* assuming the day is irrelevant; extra conditioning information reshapes the sample space.
- **●●● Monty Hall (generalized).** 3 doors, then n doors with the host opening all-but-one. Switch? → Switch; win prob (n−1)/n. *Trap:* treating the host's action as uninformative; his choice is **conditioned on knowing**, which leaks information.
- **●●● Sequential Bayes / coin from a bag.** Bag has a fair coin and a two-headed coin; you draw one, flip 3 heads. P(two-headed)? → 8/9. *Trap:* updating only once instead of multiplying the likelihood over each independent flip.

## Tier 3 — Combinatorics

- **●○○ Handshakes.** n people, everyone shakes once. Count? → C(n,2). *Trap:* counting each handshake twice (n(n−1)) and forgetting to halve.
- **●●○ Anagrams with repeats.** Distinct arrangements of "MISSISSIPPI"? → 11!/(4!4!2!) = 34650. *Trap:* forgetting to divide out the indistinguishable repeats.
- **●●○ Stars and bars.** Ways to put 10 identical balls into 4 distinct boxes? → C(13,3) = 286. *Trap:* confusing identical-vs-distinct objects, or distinct-vs-identical boxes.
- **●●● Inclusion–exclusion / derangements.** Permutations of 5 with **no** element fixed? → !5 = 44. *Trap:* subtracting the "at least one fixed" cases without adding back the over-subtracted overlaps.
- **●●● Lattice paths with a block.** Monotone paths corner-to-corner of a grid avoiding one blocked cell? → total minus (paths-through-blocked). *Trap:* double-subtracting or miscounting the sub-rectangles.

## Tier 4 — Distributions

- **●○○ Name the distribution.** "Number of heads in 20 flips" / "flips until first head" / "calls per hour" → Binomial / Geometric / Poisson. *Trap:* defaulting to normal because it's familiar.
- **●●○ Geometric memorylessness.** Rolling a d6 until the first 6; given no 6 in 3 rolls, expected additional rolls? → still 6. *Trap:* gambler's-fallacy expectation that a 6 is "due."
- **●●○ Poisson from binomial.** 1000 trials, p = 0.002; P(exactly 3 successes)? → Poisson(λ=2), ≈ 0.180. *Trap:* grinding the exact binomial instead of recognizing the rare-event Poisson limit.
- **●●● Sum/variance reasoning.** Variance of the sum of n i.i.d. Bernoulli(p)? → np(1−p); and why E[X²] ≠ E[X]². *Trap:* adding standard deviations instead of variances.
- **●●● Order statistics.** Expected max of n Uniform(0,1) draws? → n/(n+1). *Trap:* assuming the max sits at 1 or at the mean 0.5.

## Tier 5 — Optimal stopping & sequential decisions

- **●●○ Die-rolling stop.** Roll a d6 repeatedly, take the value when you stop, but each roll costs nothing and you keep the last; optimal threshold for k rolls allowed? → backward induction from EV 3.5 (stop above the continuation value). *Trap:* using a fixed threshold instead of one that **rises as rolls remain**.
- **●●○ Re-roll two dice.** Roll 2 dice, may re-roll any subset once to maximize sum EV. Which to keep? → keep any die ≥ 4 (above 3.5). *Trap:* keeping the higher of the two rather than comparing each to the re-roll EV.
- **●●● Secretary problem.** n candidates in random order, observe-then-commit. Strategy and win prob? → reject first n/e (~37%), then take the next record; win prob → 1/e. *Trap:* believing more looking is always better; over-sampling burns your best candidate.
- **●●● House-selling / threshold.** Offers arrive i.i.d. with a holding cost c per period; accept rule? → accept above a reservation value set by the indifference equation. *Trap:* ignoring the cost of waiting, or treating the threshold as the mean offer.

## Tier 6 — Betting & Kelly

- **●○○ Equal-EV ≠ equal.** Two bets, same +EV, different variance. Which to size bigger? → the lower-variance one (Kelly scales with edge/odds). *Trap:* treating EV as the whole story and ignoring variance/ruin.
- **●●○ Kelly fraction.** Even-money bet, win prob 0.6. Optimal fraction of bankroll? → f* = 2p−1 = 0.2. *Trap:* betting full edge or "all-in on +EV," which maximizes ruin, not growth.
- **●●○ General Kelly.** Net odds b-to-1, win prob p. Fraction? → f* = (bp − (1−p))/b. *Trap:* forgetting the loss term, or sizing on EV instead of log-growth.
- **●●● Half-Kelly trade-off.** Why do pros bet half-Kelly? → ~3/4 of the growth for ~1/2 the variance; growth is flat near the optimum but variance isn't. *Trap:* assuming full Kelly is "correct" — it ignores estimation error in p, which is never known exactly.
- **●●● Repeated bets / geometric mean.** Win +50%/lose −40% on a fair coin, each round. Long-run? → geometric mean < 1 → you go broke despite +EV arithmetic mean. *Trap:* using the arithmetic mean for a multiplicative process (the volatility tax).

## Tier 7 — Market-making & adverse selection

- **●●○ Set a market.** A fair die is rolled; you must quote a two-way price on the outcome. Where, and how wide? → center 3.5, width covers your adverse-selection risk + inventory. *Trap:* quoting a zero-width market at fair value — you get picked off by anyone with an edge.
- **●●○ Updating on the trade.** You quote 4.0/4.5 on an unknown value; a counterparty **lifts your offer**. What do you now believe? → the true value is likely > 4.5; **fade your estimate upward** before requoting. *Trap:* treating the fill as neutral — *if they wanted it, they probably know something.*
- **●●● Winner's curse.** Sealed-bid auction for an item of common but uncertain value; you win. What does winning tell you? → you likely over-estimated — winning is conditional on being the most optimistic bidder, so **shade your bid down**. *Trap:* bidding your unconditional estimate and ignoring that winning is bad news about your estimate.
- **●●● Inventory & skew.** You're long after a series of buys; how do you adjust quotes? → skew both sides down to attract sells and discourage buys, balancing inventory risk vs spread capture. *Trap:* quoting symmetrically around fair value while carrying directional inventory risk.

---

## Track L — Logic & deduction puzzles

Answers here are usually a **strategy or a minimum count**, not a probability. Check the *method*. Difficulty roughly L1 ●○○ → L3 ●●●.

- **●○○ Burning ropes.** Two ropes, each burns in 60 min but unevenly. Measure 45 min? → light rope A both ends + rope B one end; when A is gone (30 min) light B's other end; B gone at 45. *Trap:* assuming "half-burned = half the time" — uneven ropes break that.
- **●○○ Two-egg drop.** 100-floor building, 2 eggs, find the highest safe floor with fewest worst-case drops? → 14 (drop from 14, 27, 39, …, decreasing gaps). *Trap:* binary search — it can waste your second egg and blow the worst case.
- **●●○ Poisoned wine / weighings.** 1000 bottles, 1 poisoned, result shows in 24h. Min test subjects? → 10 (binary-encode bottle index across 10 testers). *Trap:* testing sequentially or in halves instead of encoding in bits.
- **●●○ 12 balls, one odd.** One ball is heavier-or-lighter (unknown which); find it and which, in 3 weighings? → yes, with the standard 4v4 split scheme. *Trap:* fixed groupings that don't use the *outcome* of weighing 1 to choose weighing 2.
- **●●● 100 prisoners & switches / lightbulb.** Prisoners visit a room with one switch; declare when all have visited. Strategy? → one designated counter toggles/counts; others flip once. *Trap:* trying to coordinate symmetrically instead of electing a single counter.
- **●●● Blue eyes / common knowledge.** n blue-eyed islanders leave on night n. Why does the visitor's "I see blue eyes" matter if everyone already sees one? → it makes the fact *common knowledge*, bootstrapping the induction. *Trap:* conflating "everyone knows" with "everyone knows that everyone knows."
- **●●● 100 prisoners & boxes.** Each opens 50 of 100 boxes to find their number; all must succeed. Best strategy & rough odds? → follow the permutation cycles; survival ≈ 31%. *Trap:* assuming independent 1/2 each → (1/2)^100; the cycle strategy couples the outcomes.

## Track G — Game theory

Light prerequisite: Tier 1 (EV). Answers are a **strategy, equilibrium, or number**. Difficulty G1 ●○○ → G3 ●●●.

- **●○○ Dominant strategy / prisoner's dilemma.** Payoff matrix given; what do rational players do? → both defect (dominant), despite cooperate-cooperate being better. *Trap:* picking the socially optimal cell instead of the individually dominant one.
- **●●○ Guess ⅔ of the average (Keynesian beauty contest).** Everyone picks 0–100; closest to ⅔ of the mean wins. Rational pick? → iterate the deletion of dominated strategies → 0; in practice shade by how rational the field is. *Trap:* one level of thinking ("⅔ of 50 = 33") instead of iterating to equilibrium.
- **●●○ Second-price (Vickrey) auction.** Optimal bid? → your true value (truthful is dominant). *Trap:* shading down as you would in a first-price auction — second-price removes the incentive.
- **●●● First-price auction / winner's curse.** Common-value item, you win the sealed bid. How to bid? → shade **below** your estimate; winning means you were the most optimistic, so condition on that. *Trap:* bidding your unconditional estimate (links to Tier 7 winner's curse).
- **●●● Pirate game.** 5 ranked pirates split 100 coins; each proposes in turn, majority-or-tie passes, else proposer dies. Top pirate's optimal proposal? → 98/0/1/0/1 by backward induction. *Trap:* forward "fairness" reasoning instead of solving from the 2-pirate endgame backward.
- **●●● Colonel Blotto.** Allocate limited troops across fronts vs an opponent; pure strategy? → none — the equilibrium is mixed/randomized. *Trap:* seeking one optimal deterministic allocation in a game that has none.

---

## Using a problem after the user answers

1. State **right/wrong** plainly first.
2. **The clean line** — the shortest correct reasoning to the number.
3. **The trap** — name the cognitive error above (base-rate neglect, gambler's fallacy, winner's curse, volatility tax, …). This is the highest-value part; make it stick.
4. **One sentence** generalizing to a real trading / decision-making instinct.
