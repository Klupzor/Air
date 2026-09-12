---
name: air
description: Use when a project has adopted the AIR (AI-Readable) framework, or when a human asks to adopt AIR into a project — including a project another AI coding tool already adopted AIR into. Teaches Discovery, Implementation, Context Impact, and Adoption workflows for progressively discovering project context, integrating the current tool with it, and safely changing an AIR-organized project.
---

This frontmatter is metadata for agent tooling that knows how to load skills this way; if your tooling doesn't use it, the rest of this document stands on its own.

# AIR Skill

AIR (AI-Readable) organizes a project's durable knowledge into a small set of canonical locations so an agent can progressively discover what it needs instead of reading everything. This Skill tells you what to do; the reasoning behind each rule lives in `SPEC.md`, and the operational detail for each phase lives in `references/`, loaded only when its trigger below is met.

## When this Skill applies

- The project has `PROJECT.md`, `AGENTS.md`, or a `blueprint/` directory — AIR is already in use.
- Or: a human asks you to adopt AIR into a project — whether or not it already has AIR's context, and whether or not the current tool has been integrated with it yet — see "Adopting AIR," below.

## Overview

AIR has three phases:

1. **Discovery** — resolve ambiguity and get human decisions, in conversation, before writing anything durable.
2. **Implementation** — carry out a converged, `READY` task, from `current-task.md` alone.
3. **Context Impact Check** — after implementing, decide whether any canonical document is now stale, and update it if so.

This file stays short on purpose. Each phase below has one paragraph of guidance and a pointer to the reference document that actually explains it — load that reference when the phase's trigger applies, not before.

## Step 0 — Orient

1. Read `PROJECT.md` first. It's the map to everything else — don't read further until you know what it points to.
2. Check whether AIR's project context exists, whether the current tool has its own integration yet, and whether `current-task.md` exists.
   - **No AIR project context at all** → go to "Adopting AIR," below.
   - **Project context exists, but the current tool has no integration yet** → go to "Adopting AIR," below (only the missing integration needs adding).
   - **Project context exists, the current tool is already integrated, and `current-task.md` doesn't exist** → go to "Discovery."
   - **`current-task.md` exists with `Status: READY`** → go to "Implementation."

## Discovery

Enter Discovery when a request has material ambiguity — when a reasonable person could implement it more than one way with genuinely different outcomes. Do not immediately turn an ambiguous request into `current-task.md`; the conversation is where intent, alternatives, and trade-offs get worked out. Do not simulate what a human would answer, and do not guess a material requirement — ask.

**Before proceeding on anything beyond a trivial, unambiguous change, load [`references/discovery.md`](../references/discovery.md) and follow it.** It defines the full flow, the readiness checklist, and how to decide what belongs in `current-task.md`'s `Design Details`.

## Implementation

Enter Implementation once `current-task.md` exists with `Status: READY`. Treat the task file as the complete contract — you should not need, and should not assume access to, the Discovery conversation that produced it.

**Load [`references/implementation.md`](../references/implementation.md) and follow its steps in order:**

1. Read `current-task.md`
2. Identify required context
3. Read only relevant project context
4. Inspect relevant code
5. Implement
6. Test
7. Context Impact Check
8. Update canonical context when appropriate
9. Commit — then delete `current-task.md`

## Context Impact Check

Trigger: after tests pass, before committing (step 7 above). Determine whether the implementation changed anything durable:

- **Case A** — no durable change → do nothing.
- **Case B** — a durable fact changed safely → update the affected document(s) in the same commit.
- **Case C** — an architectural or domain-significant change → propose it and get human approval before applying it.

**Load [`references/context-impact.md`](../references/context-impact.md)** for the full definitions, the dependency-checking guidance, and the conflict-detection procedure.

After the commit lands, `current-task.md` is deleted — it is never archived or retained (`SPEC.md` §6).

## Human Decisions

You may analyze, recommend, propose, and flag missing information. You must not invent a decision that materially affects product, domain, architecture, scope, or behavior — that's the human's call, most often surfaced during Discovery. Full boundary: `SPEC.md` §10.

## Conflict Handling

If a canonical document and the actual code disagree, never silently pick a side. If the conflict doesn't bear on the decision at hand, report it and leave both sides alone. If it does, surface it using the CONTEXT CONFLICT format in `SPEC.md` §11 and ask. Procedure: `references/context-impact.md`.

## Adopting AIR in a Project

Enter this whenever AIR's project context doesn't exist yet, or when it does but the AI coding tool you're currently running hasn't been integrated with it yet — a project's context is meant to outlive any single tool, so other tools joining later is expected, not exceptional.

AIR itself may already be available to you, or a human may hand you the AIR repository (`https://github.com/Klupzor/Air`) to read it from instead — acquiring AIR is step zero of adopting it, and is covered by "Acquiring AIR" in the reference document below, not restated here.

**Load [`references/adoption.md`](../references/adoption.md) and follow it in order:**

1. Identify the AI coding tool currently running.
2. Detect whether AIR's project context already exists.
3. Detect whether the current tool is already integrated.
4. Identify what native Skill or instruction mechanism the current tool provides.
5. Determine the minimum tool-specific integration required, and add or update only that — leaving project context and every other tool's integration untouched.

If step 2 finds no project context at all, establish it first — from `templates/` for a new project, or by mapping existing project knowledge onto AIR's canonical categories for an existing one — before adding the current tool's integration. Prefer installing or registering the canonical Skill through the current tool's native mechanism, when it has one, rather than reimplementing the workflow in a tool-specific format; if the tool doesn't allow automatic installation, that isn't an adoption failure — continue the rest of the workflow and give the human only the minimal manual instructions needed to enable the Skill for that tool.

Project context and tool integration are never the same thing; the rule governing how they relate is in `SPEC.md` §19.

## Reference Index

| File | Loaded when |
|---|---|
| [`references/discovery.md`](../references/discovery.md) | Entering Discovery — any non-trivial or ambiguous request |
| [`references/implementation.md`](../references/implementation.md) | `current-task.md` exists with `Status: READY` |
| [`references/context-impact.md`](../references/context-impact.md) | After implementing and testing, before committing |
| [`references/adoption.md`](../references/adoption.md) | Project doesn't have AIR yet, or the current tool isn't integrated with it yet |
| [`templates/current-task.md`](../templates/current-task.md) | Creating a task at the end of Discovery |
| [`templates/AGENTS.md`](../templates/AGENTS.md) | Adopting AIR into a new project |
| [`templates/PROJECT.md`](../templates/PROJECT.md) | Adopting AIR into a new project |
| [`templates/blueprint/`](../templates/blueprint/) | Adopting AIR, or creating a Blueprint category that doesn't exist yet |
| [`templates/features/README.md`](../templates/features/README.md) | Writing or reviewing a feature document |

Never load all four `references/` files up front "just in case" — each loads only when its own trigger fires. That's progressive context applied to AIR's own documentation, not just the project's.
