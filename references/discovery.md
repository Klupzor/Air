# Discovery

This document is the full elaboration of AIR's Discovery phase (see `SPEC.md` §4 for the conceptual summary). It's the canonical source for what to do at each step, and for when Discovery is actually finished.

Discovery is how an ambiguous or under-specified request becomes a resolved, implementable intent — before anything durable is written down. It happens in conversation, with the human who made the request.

## The flow

```text
User intent
    ↓
Minimum relevant context
    ↓
Understand system
    ↓
Identify ambiguity
    ↓
Ask questions
    ↓
Explore alternatives
    ↓
Propose
    ↓
Human decisions
    ↓
Readiness check
    ↓
Create current-task.md
```

**User intent.** Start from what the human actually asked for, in their own words. Don't paraphrase it into something more specific than they said.

**Minimum relevant context.** Load `PROJECT.md`, and from there only what plausibly bears on this request. Don't read the whole repository as a first move — Discovery stays progressive, the same as every other part of AIR.

**Understand system.** Once you know roughly where the request lands, look at the actual code and the actual canonical documents that cover that area. Facts come from what's really there, not from assumption.

**Identify ambiguity.** Compare the request against what you now know. Where could two reasonable interpretations lead to different outcomes? That's material ambiguity — the kind Discovery exists to resolve. Not every request has any; a small, unambiguous change can skip straight to Implementation (see "What Discovery Is Not," below).

**Ask questions.** Put the ambiguity to the human directly. Do not guess a material requirement and do not simulate what the human would probably say — if it materially affects product, domain, architecture, scope, or behavior, it's their call (see `SPEC.md` §10).

**Explore alternatives.** For anything with a real trade-off, lay out the reasonable options and their consequences, rather than silently picking one.

**Propose.** Bring a concrete recommendation, not just a list of options — the human is deciding, but a well-reasoned proposal makes that decision easier and faster.

**Human decisions.** Get explicit answers to the open questions. If the human's answer surfaces yet another ambiguity, keep iterating — Discovery isn't a single question-and-answer round, it's however many it takes to converge.

**Readiness check.** Before writing anything durable, verify the task actually meets the bar below. If it doesn't, that's a sign Discovery isn't finished, not a sign to write a task file anyway.

**Create current-task.md.** Only now does the implementation contract get written, from `templates/current-task.md`, with `Status: READY`.

## Discovery Readiness checklist

A task is ready for `current-task.md` only when all of the following hold:

- The objective is clear.
- Material ambiguity has been resolved.
- Relevant alternatives were considered where a real trade-off existed.
- Human decisions were made explicitly — not assumed, not simulated.
- Scope is understood: what's in, what's out.
- Constraints are understood.
- Acceptance criteria can be stated concretely.
- Every design detail that could materially diverge between implementers is either decided or explicitly delegated (see the next section).
- No material unresolved question remains.

Do not create a `READY` task prematurely. If any of the above is still open, stay in conversation.

## Deciding what goes in `current-task.md`'s Design Details

`current-task.md` splits `Design Details` into `Decided During Discovery` and `Left to the Implementer`. The bar for putting something in the first group: **two reasonable implementations could produce materially different behavior, architecture, interfaces, or future constraints.** Examples: which system owns a new piece of state, the shape of a public interface another part of the system will depend on, a choice that would be expensive to reverse later.

Discovery should not try to pin down routine function signatures, internal class structure, or naming — that's normal implementation work, and belongs under `Left to the Implementer` (or isn't worth mentioning at all). Trying to decide everything during Discovery defeats its purpose: it turns a conversation meant to resolve real ambiguity into a technical design document nobody asked for.

## What Discovery Is Not

- **Not a ticket queue.** There is no backlog of Discovery sessions to work through — it happens once, for the request in front of you, and ends when that request converges.
- **Not mandatory for trivial or unambiguous changes.** If a request is small and has only one reasonable interpretation, proceed to Implementation directly; forcing every change through a full Discovery pass is exactly the kind of process overhead AIR is trying to avoid.
- **Not a place to simulate the human.** If a question needs a human answer, ask it. An agent's job in Discovery is to surface and clarify, not to decide on the human's behalf.
