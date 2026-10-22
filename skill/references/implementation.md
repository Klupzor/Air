# Implementation

How a READY `current-task.md` becomes finished, reviewed work. Written for a fresh agent with no access to the Discovery conversation that produced the task — the task file, and the branch it lives on, must be sufficient.

```text
1. Read → 2. Start commit → 3. Execute → 4. Owner review → 5. Close
```

`current-task.md` is in git from the start commit to the closing commit. Between them, any agent — in this session or a later one, in any tool — can resume by checking out the task's branch and reading the file.

## 1. Read `current-task.md`

Read it in full before doing anything else: objective, scope, constraints, acceptance criteria, `Branch`, and especially `Design Details`. If something Implementation needs is missing, that's a gap in the contract — raise it rather than inventing an answer.

## 2. Start commit

Put the task into git before writing any code:

- Use the branch the task's `Branch` section names — create it if it says "new branch", stay put if it says "current branch".
- If `Branch` is missing or unclear, ask the owner which branch to use before committing. Never silently start a task that calls for its own branch on the current one.
- Commit `current-task.md` alone, with a message summarizing the objective.

If the start commit already exists (you're resuming), skip this step.

## 3. Execute

1. **Identify and read only the context this task needs** — follow the task's `Feature` and `Applicable Rules` pointers and `PROJECT.md`; don't read the whole Blueprint by default.
2. **Inspect the relevant code** — what the task touches, what it depends on, and what depends on it. Documents describe intent; code is what runs. If they disagree, see "Conflicts," below.
3. **Implement** within `Scope` and `Constraints`. Follow `Design Details → Decided During Discovery` exactly; use your own judgment for `Left to the Implementer`.
4. **Test** against the `Acceptance Criteria`, adding or updating tests as the codebase's conventions call for.
5. **Context Impact Check** — follow [`context-impact.md`](context-impact.md), and apply what it calls for: nothing (Case A), a document update alongside the code (Case B), or a proposal for the owner (Case C).

## 4. Owner review

Present the result to the owner: what changed, how it was verified, and any canonical-document updates or Case C proposals. Then iterate on their feedback. Committing each round on the task branch is fine. The task isn't done until the owner says so.

## 5. Close

- **Approved** → the final commit deletes `current-task.md` (together with any remaining work). Implementation narrative — what was tried, why an approach was chosen — goes in commit messages, never in canonical documents.
- **Rejected or abandoned** → an abandon commit deletes `current-task.md`, and its message states that the task was abandoned and why. Whether the branch is kept, merged, or discarded is the owner's decision.

Either way the task leaves no file behind: its record is the git history from start commit to closing commit, plus any canonical documents that changed.

## Conflicts

If the code and a canonical document disagree about something material to this task, don't silently pick one — surface it with the CONTEXT CONFLICT format in [`context-impact.md`](context-impact.md) and ask. If the conflict is unrelated to this task, note it and leave both sides alone.
