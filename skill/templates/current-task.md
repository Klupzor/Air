<!--
The single active implementation contract for the project. It exists
only between Discovery converging and the commit that closes the task:
the implementer's start commit adds it on the branch named below, and
the closing commit (approved or abandoned) deletes it. Never overwrite
a READY task with a new one — close it first. The record of the task is
git history; this file is never archived. Full lifecycle: the AIR
Skill's references/implementation.md.
-->

# Current Task

## Status

READY

<!--
READY is the only status this file ever holds. Before Discovery
converges the file doesn't exist; partial convergence happens in
conversation.
-->

## Branch

<!--
Decided with the human during Discovery: "new branch <name>" for a
change large enough to review or discard on its own, otherwise "current
branch". The implementer makes the start commit here and asks if this
section is missing or unclear.
-->

## Objective

<!-- One or two sentences: what this task accomplishes and why. -->

## Feature

<!-- Which product capability (see features/) this task belongs to, if any. -->

## Decisions

<!--
Product, scope, domain, or behavior-level decisions made by the human
during Discovery — the *what and why*. Do not restate canonical
knowledge that already lives in blueprint/ or features/; reference it
instead.
-->

## Scope

<!-- What is explicitly in scope, and what is explicitly out of scope. -->

## Constraints

<!-- Technical, product, or timeline constraints that shape the implementation. -->

## Acceptance Criteria

<!-- Concrete, checkable conditions that define "done." -->

## Design Details

<!--
This section exists so two competent implementers don't accidentally
diverge on something that matters. It is not a technical design
document, and Discovery should not try to specify every function
signature or class structure here.

Only list a design detail under "Decided During Discovery" when two
reasonable implementations could produce materially different
behavior, architecture, interfaces, or future constraints. Anything
else — routine signatures, internal structure, naming — belongs under
"Left to the Implementer," or doesn't need to be mentioned at all.
-->

### Decided During Discovery

<!-- Design choices that materially affect the implementation and were resolved with the human. -->

### Left to the Implementer

<!-- Implementation details explicitly delegated — no human decision was needed. -->

## Applicable Rules

<!-- Pointers to the specific blueprint/rules.md entries this task must respect. Do not restate the rule text. -->

## Expected Context Impact

<!--
A best-effort note on which canonical documents this task is likely to
affect (see the AIR Skill's references/context-impact.md). This is a starting guess
for the implementer, not a binding commitment — the actual Context
Impact Check happens after implementation.
-->
