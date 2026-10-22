# Plumbing is not a feature

**Setup:** `examples/minimal-project/` as is, committed.

**Prompt:**

> Add an optional `limit` parameter to `TaskStore.list` that caps how many tasks it returns. Callers don't use it yet. Make the change and update the docs if needed.

**Expected:**
- `src/store.py` gains the parameter, with a test.
- The agent's Context Impact Check concludes Case A: no canonical document changes.

**Must not:**
- Edit anything under `features/`.
- Add the parameter to `blueprint/` (it's not a rule, decision, or ownership change).
