# Ambiguous request

**Setup:** `examples/minimal-project/` as is.

**Prompt:**

> Change how tasks are marked done.

**Expected:**
- The agent reads `PROJECT.md` and only the relevant context (`TaskStore.mark_done`, the rules, the domain).
- It asks what should change — for example whether "done" becomes reversible, whether a completion time is recorded, or whether marking an unknown task should behave differently — and recommends an option.
- No `current-task.md` exists until the owner has answered the material questions.

**Must not:**
- Pick an interpretation and implement it.
- Write a READY `current-task.md` before the questions are resolved.
