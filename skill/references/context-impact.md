# Context Impact

How to keep a project's canonical documents — the Blueprint, `features/`, `PROJECT.md`, `AGENTS.md` — accurate as the code changes, without letting them grow into logs or duplicates. Run it after implementing and testing (Implementation step 3), and apply its writing rules any time you edit a canonical document. Every question here is the same one: *has this change made a canonical document wrong or incomplete?*

## Durable truth

**A change does not become durable project knowledge merely because it is user-visible or technically observable.** Durable means "a future reader needs to know this to reason correctly about the project," not "this happened."

**Canonical documents describe what is true now — never what happened.** No dated entries, no "applied so far," "previously," "no longer," or "since <date>" narration, no tombstones for resolved questions or superseded decisions. When something changes, rewrite the affected statement so it is simply true; when something stops mattering, remove it. The event itself — when it happened, what was tried, why — goes in the commit message. Operational events (deployed, applied, connected, migrated) are not durable knowledge; record only a resulting fact, and only if it changes how future work must be done.

**Features describe capability, not interface.** Before touching `features/`, ask: *would a user describe what the product does differently after this change?* If not — a new optional parameter, flag, CLI syntax, endpoint shape, internal option — leave `features/` alone. The canonical example lives in [`../templates/features/README.md`](../templates/features/README.md).

## Case A / B / C

**Case A — No durable change.** Every canonical document is still accurate. Update nothing.

> Example: `TaskStore.list()` now uses a dict internally. Behavior and documented rules are unchanged.

**Case B — Durable truth changed safely.** An established fact changed, as already agreed in Discovery or by the task itself. Update the affected document in the same change set as the code, so the owner reviews both together — no separate approval conversation, but never an invisible edit either.

> Example: the task changed the default status of new tasks; update that rule in `blueprint/rules.md`.

**Case C — Architectural or domain change.** Architecture, ownership, or another standing decision changed. Identify the affected documents, propose the specific change, get the owner's approval, and only then apply it.

> Example: payment validation moved to another module — propose the `blueprint/modules.md` update rather than committing it unilaterally.

B versus C is judgment: anything that would surprise the owner if it landed without warning is C. When unsure between A and B, prefer A.

## Dependency checking

Changing one concept can make other documents stale. Ask:

> What durable concept changed, and which canonical documents describe or depend on that concept?

Answer by reasoning, not by consulting a map — AIR deliberately keeps no dependency registry. Scale the check to the change: a local change needs a glance at the file you touched; a business rule change needs the related domain, rule, and feature documents; an architectural or ownership change needs a broader review of the Blueprint.

## Writing rules

- **One home per fact.** Before stating anything, search for where it already lives. If it has a home, reference it; if you find the same fact in two places, collapse it to one.
- **Facts owned by another repository** are referenced, not restated — a service's deployment status belongs to that service's repository.
- **Never describe another document's contents or structure** ("X says…", "this is stated identically in Y"). Such claims rot silently. Quote only text you have just read, verbatim.
- **Don't reword accurate text.** A rewritten sentence that means the same thing is churn, not an update.
- **Size is a signal.** A Blueprint file growing past roughly 200 lines is likely becoming a dumping ground — propose a prune or split to the owner, as you would a Case C change. This is a smell, not a limit.

## Conflicts

A conflict is a canonical document and the code disagreeing. You'll usually notice one while inspecting code or during this check.

- **Non-blocking** — unrelated to the decision at hand. Report it briefly and leave both sides alone; no drive-by fixes.
- **Blocking** — it stands in the way of a decision this task needs. Surface it and ask the owner which side becomes canonical:

```text
CONTEXT CONFLICT

Documentation says:
Module A owns payment validation.

Code currently does:
Module B owns payment validation.

This affects the requested consolidation because consolidation requires choosing one ownership model.

Which behavior should become canonical?
```

Never silently choose between documented truth and implementation.
