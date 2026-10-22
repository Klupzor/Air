---
name: air
description: Use when a project has adopted the AIR (AI-Readable) framework, or when a human asks to adopt AIR into a project — including a project another AI coding tool already adopted AIR into. Teaches Discovery, Implementation, Context Impact, and Adoption workflows for progressively discovering project context, integrating the current tool with it, and safely changing an AIR-organized project.
---

This frontmatter is metadata for agent tooling that knows how to load skills this way; if your tooling doesn't use it, the rest of this document stands on its own.

# AIR Skill

AIR Skill version: 0.2.1

AIR (AI-Readable) organizes a project's durable knowledge into a small set of canonical locations so an agent can progressively discover what it needs instead of reading everything. This Skill tells you what to do; the operational detail for each phase lives in this Skill's `references/`, loaded only when its trigger below is met. This folder is complete on its own — `SPEC.md` in the AIR repository holds the rationale and is never needed to operate.

## When this Skill applies

- The project has `PROJECT.md`, `AGENTS.md`, or a `blueprint/` directory — AIR is already in use.
- Or: a human asks you to adopt or update AIR in a project — see "Adopting AIR," below.

## Step 0 — Orient

1. Read `PROJECT.md` first. It's the map to everything else — don't read further until you know what it points to.
2. Route by what you find:
   - **No AIR project context, or the current tool isn't integrated yet** → "Adopting AIR."
   - **`current-task.md` exists with `Status: READY`** → "Implementation."
   - **Otherwise** → handle the request; enter "Discovery" if it has material ambiguity.

## Discovery

Enter Discovery when a request has material ambiguity — when a reasonable person could implement it more than one way with genuinely different outcomes. The conversation is where intent, alternatives, and trade-offs get worked out; don't turn an ambiguous request into `current-task.md` early, and don't simulate what a human would answer — ask. If a READY `current-task.md` already exists, never overwrite it: it must be closed first.

**For anything beyond a trivial, unambiguous change, load [`references/discovery.md`](references/discovery.md) and follow it.**

## Implementation

Enter Implementation once `current-task.md` exists with `Status: READY`. Treat it as the complete contract — don't assume access to the Discovery conversation that produced it.

**Load [`references/implementation.md`](references/implementation.md) and follow its steps in order:**

1. Read `current-task.md`
2. Start commit — commit `current-task.md` on the branch the task names
3. Execute — context, code, tests, Context Impact Check
4. Owner review — present the result and iterate
5. Close — the closing commit deletes `current-task.md`

## Context Impact Check

Trigger: after tests pass, before presenting the result for review. Decide whether the implementation changed anything durable:

- **Case A** — no durable change → do nothing.
- **Case B** — a durable fact changed safely → update the affected document(s) alongside the code.
- **Case C** — an architectural or domain-significant change → propose it and get human approval before applying it.

Canonical documents describe what is true now — never a dated log of what happened. **Load [`references/context-impact.md`](references/context-impact.md)** for the full rules, dependency checking, and conflict handling.

## Human Decisions

You may analyze, recommend, propose, and flag missing information. You must not invent a decision that materially affects product, domain, architecture, scope, or behavior — that's the human's call.

## Conflict Handling

If a canonical document and the code disagree, never silently pick a side. If the conflict doesn't bear on the decision at hand, report it and leave both sides alone; if it does, surface it and ask. Format and procedure: [`references/context-impact.md`](references/context-impact.md).

## Adopting AIR in a Project

Enter this when a project has no AIR context yet, when the AI coding tool you're running isn't integrated with it yet, or when a human asks to update AIR. A project's context outlives any single tool; other tools joining later is expected. **Load [`references/adoption.md`](references/adoption.md) and follow it in order** — it covers acquiring AIR, installing this Skill when the tool allows it, and what to do when it doesn't.

## Reference Index

| File | Loaded when |
|---|---|
| [`references/discovery.md`](references/discovery.md) | Entering Discovery — any non-trivial or ambiguous request |
| [`references/implementation.md`](references/implementation.md) | `current-task.md` exists with `Status: READY` |
| [`references/context-impact.md`](references/context-impact.md) | After implementing and testing; whenever editing canonical documents |
| [`references/adoption.md`](references/adoption.md) | Adopting or updating AIR, or integrating a new tool |
| [`templates/current-task.md`](templates/current-task.md) | Creating a task at the end of Discovery |
| [`templates/AGENTS.md`](templates/AGENTS.md), [`templates/PROJECT.md`](templates/PROJECT.md) | Establishing AIR context in a project |
| [`templates/blueprint/`](templates/blueprint/) | Establishing a Blueprint category that doesn't exist yet |
| [`templates/features/README.md`](templates/features/README.md) | Writing or reviewing a feature document (guidance only — not copied into projects) |

Load a reference only when its trigger fires, never all of them up front.
