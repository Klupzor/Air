# Adoption

This document is the full elaboration of AIR's Adoption phase (see `SPEC.md` §15 for the conceptual summary of adopting AIR's structure, and `SPEC.md` §19 for the conceptual summary of keeping tool integration separate from project context). It is the canonical source for the adoption procedure in both new and existing projects, and for how adoption behaves when more than one AI coding tool works on the same project over time — for example Claude Code, Codex, Cursor, or OpenCode, at different points in a project's life.

## Tool-aware initialization

Before touching anything, every adoption call answers these, in order:

1. Identify the AI coding tool currently operating on the project.
2. Detect whether AIR's Project Context already exists.
3. Detect whether the current tool is already integrated with AIR.
4. Identify what native Skill or instruction mechanism the current tool provides.
5. Determine the minimum tool-specific integration required for the current tool to correctly discover and apply AIR.

If step 2 finds no Project Context, adoption establishes both:

```text
AIR Project Context
+
Current Tool Integration
```

If step 2 finds Project Context already exists, but step 3 finds the current tool isn't integrated, adoption establishes only:

```text
Current Tool Integration
```

The existing Project Context is preserved either way — see "Preservation rule," below. Only after these five are answered should the project be modified.

## Establishing project context

Reached when step 2 above finds nothing yet.

### New project

Copy `templates/AGENTS.md`, `templates/PROJECT.md`, `templates/blueprint/*`, and `templates/features/README.md` into the project as-is. Leave the Blueprint files minimal or empty until there's real content for them — don't fabricate project knowledge to fill them in. This establishes Project Context only; the current tool's own integration is added next (see "Installing a tool integration," below).

### Existing project

Do not overwrite or duplicate what's already there.

1. Inspect the project for existing sources of project knowledge (READMEs, design docs, wikis, ADRs, code comments).
2. Determine which existing documents already cover architecture, domain, rules, decisions, or features — even partially, even under different names.
3. Propose a mapping onto AIR's canonical categories. An existing document that already serves as a canonical home can stay where it is — AIR doesn't require the project to physically match the template structure if an equivalent canonical location already exists.
4. Ask the human before any reorganization that could destroy, obscure, or merge existing information. For example:

   ```text
   Existing architecture documentation appears to live in:
   docs/architecture.md

   I propose using that as the canonical architecture source rather than creating a duplicate blueprint/architecture.md.

   Approve?
   ```

5. Preserve information — move or link rather than delete, unless the human explicitly approves removal.
6. Avoid creating a duplicate document once a canonical one has been identified or agreed on.

## Adding a tool integration to an existing project

Reached when step 2 finds Project Context but step 3 finds the current tool isn't integrated yet.

- Reuse the existing Project Context as-is — don't re-derive or re-verify it as if adopting from scratch.
- Detect existing integrations by inspecting the repository for whatever artifacts are conventionally used (a Skill file or registration, a known instruction filename). A tool integration file should identify itself as such — for example, a one-line comment naming the tool and noting it's an AIR integration — so a *different* tool's agent can recognize it later without needing to know that tool's specific conventions in advance.
- Determine what the current tool specifically needs, from step 4 of Tool-aware initialization.
- Add or update only the missing piece.
- Never copy durable knowledge into a tool-specific file (see "Project context vs. tool integration," below).
- Never rewrite a large existing document merely to make it compatible with another tool.
- Never replace an existing integration unless the current tool's own requirements genuinely changed (for example, its Skill format was updated) — not as a stylistic cleanup of another tool's file.
- Preserve every other tool's integration unchanged.

## Installing a tool integration

When the current tool supports a native Skill mechanism and the AIR Skill isn't already available to it, install or register the canonical AIR Skill through that mechanism. Prefer reusing the one canonical Skill over writing a second, tool-specific reimplementation of the Discovery/Implementation/Context-Impact workflow — multiple paraphrased copies of the same workflow are exactly the kind of duplication AIR avoids elsewhere, and it applies here too.

If the tool instead provides a project instruction file, configure that entry point. If both exist, prefer the Skill for the operational workflow and keep the instruction entry point concise.

Either way, a tool-specific integration file contains only the minimum instructions necessary for that tool to discover and activate AIR — it points at the project's canonical context (`PROJECT.md`, the Blueprint, `references/`) rather than reproducing any of it. The exact installation or registration mechanism is tool-dependent and is deliberately not specified further here (`SPEC.md` §18, §19).

## Project context vs. tool integration

A tool-specific instruction file may say, for example:

```text
Load PROJECT.md first.
Use the AIR Blueprint for durable project knowledge.
Follow the AIR Discovery workflow.
```

It should not contain a copied version of `architecture.md`, `domain.md`, `rules.md`, or `features/*`. The integration points an agent at the canonical context; it does not restate it.

One genuine edge case: some tools read `AGENTS.md` itself as their instruction entry point by convention. In that case, `AGENTS.md` already serves as that tool's integration, and nothing more needs to be added — this is fine, because `AGENTS.md`'s own content is already just pointers and essential rules, not restated Blueprint knowledge. A tool that needs something else — a dedicated Skill registration, or a differently named instruction file — gets a separate, minimal artifact that points back to `AGENTS.md` and `PROJECT.md` rather than restating them.

Adapting AIR to the tool is expected. Adapting the project's AIR context to the tool should generally not happen. `SPEC.md` §19 states the maxim this follows from: "Adapt the agent to the project, not the project context to every agent."

## Idempotency

```text
First agent:
Project → AIR Adoption → Project Context + Tool A Integration

Second agent:
Existing AIR Project → Detect existing context → Preserve existing context → Add Tool B Integration only

Third agent:
Existing AIR Project → Detect existing context → Detect Tool A + Tool B → Add Tool C Integration only
```

Running "Adopt AIR in this project" repeatedly, with the same tool or a different one, must never progressively create duplicate context, duplicate documentation, or competing versions of AIR knowledge.

## Preservation rule

If an existing project contains `PROJECT.md`, `blueprint/`, `features/`, treat those as the project's canonical context. Do not create `CLAUDE_CONTEXT.md`, `OPENCODE_CONTEXT.md`, `CODEX_CONTEXT.md`, or any equivalent duplicated knowledge store.

## Worked example: a second tool joins

**Claude Code** opens a project with no AIR yet. The human asks it to adopt AIR. Claude Code establishes Project Context and its own integration.

**OpenCode** later opens the same project. The human asks it to adopt AIR. Following Tool-aware initialization above, OpenCode detects Project Context already exists, detects that another tool may already be integrated, detects that its own integration is missing, and adds only that.

Explicitly, OpenCode must not:

- recreate the Blueprint;
- rewrite `PROJECT.md`;
- duplicate feature documentation;
- create a second project context;
- create `CLAUDE_CONTEXT.md`, `OPENCODE_CONTEXT.md`, or an equivalent;
- remove or rewrite Claude Code's integration merely for stylistic consistency.

Running the same adoption request again, from either tool, changes nothing further — that's the idempotency guarantee made concrete.

## Not a tool registry

Tool-aware initialization is a fresh inspection performed every time adoption runs — like Implementation's "read `PROJECT.md`'s pointers fresh each time" (`references/implementation.md` step 2) — not a maintained ledger of which tools are integrated. A maintained ledger would be exactly the dependency matrix or registry `SPEC.md` §16 already excludes, and it would go stale the same way a stored dependency graph would. Detecting an integration means looking for it, each time, not consulting a record of it.
