# Domain

## Vocabulary

- **Task** — a single unit of work the user is tracking.
- **Status** — the state of a task's progress: `todo`, `in_progress`, or `done`.

## Entities

### Task

A task has:

- `id` — a unique identifier.
- `title` — a short, human-readable description.
- `status` — one of `todo`, `in_progress`, `done` (see `blueprint/rules.md#r1` for the default).
- `created_at` — when the task was created.

There is no "Project" or grouping entity in this example — tasks are a single flat list. That's a deliberate scope limit, not an oversight (see `blueprint/decisions.md#d2`).
