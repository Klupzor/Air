# Decisions

## What belongs here

- Durable decisions that still constrain future work today — the ones a new contributor (human or agent) would need to know to avoid re-litigating a settled question or accidentally reversing it.
- A lightweight note of the trade-off or rationale, enough to understand *why*, without writing a full design document.

## What does not belong here

- A duplicate of the git log. Most changes don't need an entry here — only the ones with lasting bearing on how future work should be approached.
- Decisions that have since been superseded or reversed and no longer constrain anything. Once a decision stops mattering, remove it rather than letting it accumulate as historical trivia — git history already has the record if anyone needs it.
- Every decision ever made on the project. This file is not a decision log or changelog; it's a short list of the ones that are still load-bearing.

## Suggested structure

A flat, identified list works well:

```markdown
## D1: <short name>

<What was decided, and the one or two sentences of "why" that matter for future work.>
```

If a decision here is later reversed, remove or replace its entry rather than appending a correction — this file should always reflect current durable truth, not a history of how that truth changed.
