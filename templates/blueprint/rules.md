# Rules

## What belongs here

- Canonical, precisely worded business or domain rules — the ones that, if violated, would be a bug even though the code "runs fine."
- Each rule should be identifiable (numbered or named) so other documents — a feature doc, a `current-task.md`'s "Applicable Rules" section — can reference it by name instead of restating it.

## What does not belong here

- Descriptions of product capability or user-facing behavior — that's what the rule enables, and belongs in [`features/`](../features/). A feature doc may reference a rule; it shouldn't reproduce its full wording.
- How the rule is enforced in code (which function checks it, which validator runs it) — that's an implementation detail. The rule is the *fact*; the code is how the fact is currently upheld.

## Suggested structure

A flat, identified list works well:

```markdown
## R1: <short name>

<Precise statement of the rule.>
```

Keep each rule's wording stable once other documents start referencing it — if a rule's *meaning* changes, that's exactly the kind of durable change a Context Impact Check (see `references/context-impact.md`) should catch and propagate.
