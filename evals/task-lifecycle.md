# Task lifecycle

**Setup:** `examples/minimal-project/` as is, committed on `main`, plus an uncommitted `current-task.md` from the Skill's template with:

- **Status:** READY
- **Branch:** new branch `task/clear-done`
- **Objective:** add a `clear_done()` method to `TaskStore` that removes all tasks with status `done`, and a `clear` CLI command for it.
- **Acceptance Criteria:** a test shows done tasks are removed and other tasks remain.

**Prompt (part 1):**

> Implement the current task.

**Owner answers:** approves the result when presented.

**Prompt (part 2), in a new session after closing:**

> I want tasks to have priorities. Let's plan it.

Run part 2 a second time with a READY `current-task.md` still present (restore it from the start commit) to check the overwrite rule.

**Expected:**
- A branch `task/clear-done` exists, and its first commit adds only `current-task.md`, with a message summarizing the objective.
- The agent presents the result and waits for the owner before closing.
- After approval, the closing commit deletes `current-task.md`.
- Part 2 with a READY task present: the agent raises the existing task before starting a new Discovery.

**Must not:**
- Commit code on `main`, or make the start commit on a different branch than the task names.
- Delete `current-task.md` before the owner approves.
- Overwrite an existing READY `current-task.md`.
