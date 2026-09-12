# Context Impact

This document is the full elaboration of AIR's Context Impact Check (see `SPEC.md` §12 for the conceptual summary, and `references/implementation.md` step 7 for where this fits in the Implementation flow). It also covers dependent-context checking (`SPEC.md` §13) and the detection side of conflict handling (`SPEC.md` §11), since all three are about the same underlying question: *has this change made some canonical document wrong or incomplete?*

## Durable truth vs. transient detail

**A change does not become durable project knowledge merely because it is user-visible or technically observable.** Plenty of changes are both visible and correct without being *durable* in the sense the Blueprint or `features/` cares about — durable means "a future reader needs to know this to reason correctly about the project," not "this technically happened."

The clearest recurring example is the difference between a product capability and implementation plumbing:

- Adding the ability to filter tasks by status → a meaningful product capability → may belong in `features/`.
- Adding an optional `status` parameter to an existing function → implementation/API plumbing → normally does not require changing feature documentation.

This distinction — and its canonical example — is owned by `templates/features/README.md`; this document applies it rather than re-deriving it. It exists because of a repeated, specific failure mode observed in practice: agents kept editing a feature document for a small optional filter parameter that hadn't actually changed what the product does. Use judgment: if an implementation change genuinely changes the product capability or a durable project fact, update the appropriate document. Otherwise, don't — churn is its own cost.

## Case A / B / C

**Case A — No durable change.** The implementation changed, but every canonical document remains accurate. Nothing is updated.

> Example: refactoring `TaskStore.list()` internally to use a dict instead of a list for lookups. Behavior and the documented rule are unchanged — no Blueprint edit.

**Case B — Durable truth changed safely.** An established business, domain, or product fact changed, and the change is a straightforward, non-controversial factual sync — not a reopening of something the human hasn't already effectively settled (through Discovery, or through the task itself). Update the affected canonical document as part of this same commit. This does not require starting a new approval conversation — but it must never be a silent, invisible edit either: it lands in the same reviewable diff as the code change, so anyone reading the commit sees both together.

> Example: the task explicitly added a new default status for new tasks, and `blueprint/rules.md` said tasks default to `todo`. Update the rule in the same commit.

**Case C — Important architectural or domain change.** The implementation changes something with broader durable consequence — architecture, domain ownership, or another significant standing decision. In this case:

1. Identify the affected canonical documents.
2. Propose the specific context change.
3. Obtain human approval before applying it.
4. Only then apply the approved change.

> Example: the task moved payment validation from one module to another. That's an ownership change with consequences beyond this task — propose the `blueprint/modules.md` update and get it confirmed rather than committing it unilaterally.

The line between B and C is judgment, not a formula: a safe factual sync that everyone already agreed to during Discovery is B; anything that would surprise the human if they saw it land without warning is C.

## Dependency checking

Changing one durable concept can make other documents stale even though they weren't directly touched. The guiding question is:

> What durable concept changed, and which canonical documents describe or depend on that concept?

This is a reasoning process, not a lookup. AIR does not maintain a dependency matrix, registry, or graph mapping documents to each other — that would be exactly the kind of indexing infrastructure AIR intentionally avoids (`SPEC.md` §16), and it would go stale in the same way the documents it's tracking would. Instead, scope the check to the likely impact of the change:

```text
Clearly local implementation change
→ lightweight check (often just the one file you already touched)

Business/domain rule change
→ check the relevant domain, rule, and feature documents that rely on it

Architectural or ownership change
→ broader canonical-context review across the Blueprint
```

These are illustrative examples of proportionality, not an exhaustive decision table — use judgment about how far a given change is likely to reach, rather than mechanically classifying every change into one of these three buckets.

## Conflict detection

A conflict is when a canonical document and the actual code disagree about something. Detecting one usually happens naturally during step 4 of Implementation ("inspect relevant code") or during this Context Impact Check itself, when you compare what you just built against what the documents say should be true.

Once detected:

- **Non-blocking** — the conflict has nothing to do with the decision currently being made. Report it (a short note is enough) and leave both sides alone. Don't silently "fix" either the doc or the code as a drive-by.
- **Blocking** — the conflict stands in the way of a decision this task actually needs to make. Surface it using the CONTEXT CONFLICT format defined in `SPEC.md` §11 and ask the human which side should become canonical. Do not guess.

Either way, the rule from `SPEC.md` §11 holds: never silently choose between conflicting project truth and implementation.

## Avoiding documentation churn and duplicate knowledge

- Reference canonical knowledge; don't restate it. If `blueprint/rules.md#r2` already says exactly what the filter does, a feature doc should link to it, not re-explain it in its own words.
- A rewritten sentence that doesn't change meaning isn't a durable change — don't edit a Blueprint file purely to reword something that was already accurate.
- If you find yourself updating the same fact in two places, that's a sign one of them shouldn't exist — collapse to a single canonical home and point the other at it.
- When in doubt between Case A and Case B, prefer Case A. Unnecessary Blueprint edits carry their own cost: they make it harder to trust that a change to a canonical document actually means something changed.
