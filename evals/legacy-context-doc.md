# A legacy context document

**Setup:** a copy of `examples/minimal-project/` with `AGENTS.md`, `PROJECT.md`, `blueprint/`, and `features/` removed, plus `docs/PROJECT_CONTEXT.md` containing:

```markdown
# Project context

Tasks have a title and a status: todo, in_progress, or done. New tasks start as todo.
Storage is in memory only; we decided not to add persistence.

## Change log
- 2026-05-02: added status filtering to the list command.
```

**Prompt:**

> Adopt AIR in this project. https://github.com/Klupzor/Air

**Owner answers:** accepts the agent's recommendation.

**Expected:**
- The agent maps the file's knowledge into AIR's categories (the statuses and default to domain/rules, the persistence decision to decisions) and proposes a state for the file: canonical home for a category, or retired.
- If retired, the file gets a "superseded by `blueprint/…`; do not update" banner and nothing links to it as a live source.
- The change-log entry is not carried into the Blueprint.

**Must not:**
- Leave `docs/PROJECT_CONTEXT.md` live and linked from `PROJECT.md` while also creating `blueprint/` files covering the same facts.
- Delete the file without asking.
