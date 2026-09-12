# Implementation

This document is the full elaboration of AIR's Implementation phase (see `SPEC.md` §5 for the conceptual summary). It's written for a fresh agent that has no access to the Discovery conversation that produced `current-task.md` — that file must be sufficient on its own.

Implementation begins once `current-task.md` exists with `Status: READY`, and proceeds through these steps in order:

## 1. Read `current-task.md`

This is the contract. Read it in full before doing anything else — objective, scope, constraints, acceptance criteria, and especially `Design Details`.

## 2. Identify required context

From the task's `Feature` and `Applicable Rules` pointers, and from `PROJECT.md`, work out which Blueprint documents and feature docs are actually relevant. Don't assume you need to read everything — identify what this specific task touches.

## 3. Read only relevant project context

Load the documents identified in step 2. This is progressive context applied to Implementation the same way it applies to Discovery: read what's needed for correct and safe reasoning about this task, not the whole Blueprint by default.

## 4. Inspect relevant code

Read the actual code the task will touch, and anything it depends on or that depends on it. Canonical documents describe intent; the code is what's actually running — check both, especially if anything in the documents seems inconsistent with what the code does (see "Handling conflicts," below).

## 5. Implement

Build the change. Respect `Scope` and `Constraints` from the task. For anything in `Design Details → Decided During Discovery`, follow it exactly — it was resolved for a reason, and reopening it here would defeat the purpose of having decided it up front. For anything under `Left to the Implementer`, use your own judgment; that's precisely what was delegated to you.

## 6. Test

Verify the change against the task's `Acceptance Criteria`. Add or update tests as the codebase's existing conventions call for.

## 7. Context Impact Check

Once the implementation works, determine whether it changed anything durable. This is a distinct step from testing — passing tests tells you the code is correct; a Context Impact Check tells you whether the project's canonical knowledge is still accurate. Follow `references/context-impact.md` in full for this step; it is not repeated here.

## 8. Update canonical context when appropriate

Apply whatever the Context Impact Check called for — a Case A no-op, a Case B update alongside this commit, or a Case C proposal that needs human approval before it's applied. Again, the detail lives in `references/context-impact.md`.

## 9. Commit

Commit the implementation, any test changes, and any canonical-document updates together. Implementation narrative and reasoning — what was tried, why an approach was chosen — belongs in the commit message, not in any canonical document (`SPEC.md` §14).

Immediately after the commit, **delete `current-task.md`**:

```text
Discovery
    ↓
current-task.md (Status: READY)
    ↓
Implementation
    ↓
Context Impact Check
    ↓
Commit
    ↓
Delete current-task.md
```

The task's permanent record is now the commit itself, plus whatever canonical documents were updated in step 8 — not a retained or archived task file (`SPEC.md` §6).

## Handling conflicts encountered along the way

If, at any step, the code and the canonical documents disagree about something material to this task, do not silently pick one. Surface it using the CONTEXT CONFLICT format defined in `SPEC.md` §11, and ask. If the conflict is unrelated to this task, note it and move on without touching either side — see `references/context-impact.md` for the full distinction between blocking and non-blocking conflicts.

## Operating without the Discovery conversation

This entire procedure assumes you were not present for Discovery and have no memory of it. That's intentional — it's the test of whether `current-task.md` did its job. If something needed for Implementation seems to be missing from the task file, that's a gap in the task contract, not something to guess at: raise it rather than inventing an answer.
