# Adoption

This document is the full elaboration of AIR's Adoption phase (see `SPEC.md` §15 for the conceptual summary of adopting AIR's structure, and `SPEC.md` §19 for the conceptual summary of keeping tool integration separate from project context). It is the canonical source for how AIR itself is acquired before adoption can begin, for the adoption procedure in both new and existing projects, and for how adoption behaves when more than one AI coding tool works on the same project over time — for example Claude Code, Codex, Cursor, or OpenCode, at different points in a project's life.

## Acquiring AIR

Acquiring AIR means obtaining enough access to it — the Skill, and whatever reference documents adoption requires — to execute adoption. It does not mean installing the Skill: installation is a separate, optional step, decided only once the current tool is known, and it never gates whether acquisition succeeded.

**Acquisition** — either case is sufficient on its own to proceed with adoption:

- **Case A — the AIR Skill is already available to the current tool.** Use it as-is; don't fetch or re-read another copy of AIR just because it exists elsewhere.
- **Case B — the AIR repository URL is provided (`https://github.com/Klupzor/Air`).** Treat it as the canonical source: read the Skill and whichever reference documents this adoption needs from it. Do not copy the entire AIR repository into the project merely because the agent needs to read it — see "Repository, Project Context, and Tool Integration," below, for why.

**Skill installation** — evaluated only after the current tool has been identified (Tool-aware initialization step 1, below), and never a precondition for the acquisition above:

- **Case C — the current tool supports installing or registering a Skill natively.** Prefer installing or registering the canonical AIR Skill through that mechanism over reimplementing AIR's workflow as a second, tool-specific Skill. After installation, use the canonical Skill and continue adoption normally.
- **Case D — the current tool does not allow the agent to install or register a Skill automatically.** This is not an AIR adoption failure. Continue the adoption workflow using whatever AIR content was acquired in Case A or B, establish the project's Tool Integration to the extent a non-Skill mechanism allows (see "Installing a tool integration," below), and tell the human what couldn't be automated. Give the minimal manual installation or registration steps the tool actually requires — don't invent a command or filename that hasn't been established reliably for that tool.

**Automatic Skill installation is preferred, but it is never a prerequisite for AIR adoption.** What adoption actually depends on is acquisition (Case A or B); installation (Case C or D) is an optional capability of whichever tool turns out to be running, and adoption proceeds the same way regardless of which of the two applies.

This is a one-time bootstrap, not an ongoing dependency: acquisition happens once, at adoption time. It does not conflict with `SPEC.md` §17's Self-Hosting guarantee — §17 is about the *adopted project* remaining operable without the AIR repository afterward, not a claim that the repository is never needed to adopt AIR in the first place.

## Repository, Project Context, and Tool Integration

Acquiring and adopting AIR moves through three distinct things, not two — conflating any of them is a mistake this document exists to prevent:

```text
AIR Repository
    ↓  (Acquisition — Case A or B, above)
AIR Skill / references
    ↓  (Adoption)
Project Context
    +
Tool Integration
```

- **AIR Repository** — the source and distribution mechanism for the methodology itself. It is where a Skill or reference document is acquired *from*; it never becomes a second project context, and adoption never copies it wholesale into the adopting project.
- **Project Context** — the durable knowledge defined in `SPEC.md` §3 (`PROJECT.md`, the Blueprint, `features/`, `current-task.md` when active). It belongs to the adopting project and is shared across every tool that works on it.
- **Tool Integration** — specific to one tool working on one project. Installing the canonical AIR Skill through a tool's native mechanism is one way of establishing that tool's integration; it is never a copy of `SPEC.md`, the Blueprint, or any other project knowledge into a tool-specific file.

`SPEC.md` §19 is the canonical statement of the rule keeping the second and third of these separate; this section only adds the first term — the repository — which sits upstream of both and is neither.

Skill installation and Project Context adoption are separate concerns: a tool can be missing its Skill while Project Context is already established and correct (Case D, above, or a second tool joining, below), and Project Context can need establishing while a Skill is already installed and available (a brand-new project, with a tool whose Skill was already installed globally beforehand). Neither one being done implies anything about the other.

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

Step 1 identifies the current tool before anything about Skill installation is decided; steps 4 and 5 then settle acquisition and installation from "Acquiring AIR," above — as two separate questions, only the first of which adoption actually depends on:

```text
Is AIR already available, or can it be acquired from the repository? (Case A/B, "Acquiring AIR")
  no  → explain to the human what access is required, and stop
  yes → adoption can proceed — Skill installation is decided next, but nothing above depended on it

Does the current tool (identified in step 1) support installing/registering a Skill natively? (step 4)
  yes → install/register the canonical AIR Skill (Case C, "Acquiring AIR")
  no  → continue adoption anyway; give the minimal manual instructions required (Case D, "Acquiring AIR")

  → Continue AIR Adoption (Establishing project context / Adding a tool integration, below)
```

This runs once per tool, per project, alongside the five steps above — never as a maintained record of which tools have the Skill (see "Not a tool registry," below).

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

Whether the Skill gets installed at all, and what to do if it can't, is decided in "Acquiring AIR," above (Cases C and D). This section covers what's left once that decision is made: shaping the tool integration itself.

If the current tool has no native Skill mechanism, or the Skill wasn't installed (Case D), it likely offers a project instruction file instead — configure that entry point. If both a Skill and an instruction file exist, prefer the Skill for the operational workflow and keep the instruction entry point concise.

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
Project → acquire AIR → establish Project Context → establish Tool A Integration

Second agent:
Existing AIR Project → detect Project Context → detect Tool A → acquire/use AIR → establish Tool B Integration only

Third agent:
Existing AIR Project → detect Project Context → detect Tool A + Tool B → acquire/use AIR → establish Tool C Integration only
```

"Acquire/use AIR" folds in the same Case A–D logic from "Acquiring AIR," above, every time it runs: if the Skill is already globally available to the second or third agent, it isn't reinstalled; if it isn't available but the agent can install it, it may; if it can't, adoption continues regardless and the minimal manual instructions are given for that tool.

Running "Adopt AIR in this project" repeatedly, with the same tool or a different one, must never progressively create duplicate context, duplicate documentation, or competing versions of AIR knowledge — and now, by the same logic, must never reinstall a Skill that's already in place either.

## Preservation rule

If an existing project contains `PROJECT.md`, `blueprint/`, `features/`, treat those as the project's canonical context. Do not create `CLAUDE_CONTEXT.md`, `OPENCODE_CONTEXT.md`, `CODEX_CONTEXT.md`, or any equivalent duplicated knowledge store.

## Worked example: first contact via the repository URL

This is the first of two worked examples — the second, "a second tool joins" below, covers what happens when a later tool finds AIR already adopted.

A human, in a project with no AIR and no AIR Skill available yet, says:

> Adopt AIR in this project.
> https://github.com/Klupzor/Air

The agent runs the full flow end to end:

1. Identifies the AI coding tool it's currently running as.
2. Reads/acquires AIR from the provided repository (Case B, "Acquiring AIR") — the Skill and whichever reference documents this adoption needs.
3. Determines that no AIR Project Context exists yet in this project.
4. Determines that, therefore, the current tool has no integration either.
5. Determines whether it can install or register the AIR Skill through this tool's native mechanism.
6. If yes: installs/registers the canonical Skill (Case C) and continues using it.
7. If no: continues adoption anyway, using the repository contents already read in step 2 (Case D) — this is not a failure.
8. Inspects the project as needed to establish Project Context, mapping existing documentation onto AIR's canonical categories if the project isn't brand-new (see "Establishing project context," above).
9. Asks the human about any material decision or conflict it finds, instead of guessing.
10. Establishes Project Context (or reuses it, if part of it turns out to already exist).
11. Establishes the minimum Tool Integration this tool needs — the Skill registration from step 6, or the manual-instructions path from step 7, plus any instruction-file entry point the tool requires.
12. Validates the result: `PROJECT.md` exists and points at real content, the current tool can discover AIR on a future session, and — if step 7 was taken — the human has the exact minimal instructions needed to finish enabling the Skill.

Steps 5–7 (Skill installation) and steps 8–10 (Project Context) are independent outcomes of the same adoption call: this scenario succeeds whether or not the Skill gets installed automatically, because Skill installation and Project Context adoption are separate concerns.

## Worked example: a second tool joins

**Claude Code** opens a project with no AIR yet. The human asks it to adopt AIR. Claude Code establishes Project Context and its own integration.

**OpenCode** later opens the same project. The human asks it to adopt AIR. Following Tool-aware initialization above, OpenCode detects Project Context already exists, detects that another tool may already be integrated, detects that its own integration is missing, and adds only that. If the AIR Skill isn't already available to OpenCode, it acquires or installs it per "Acquiring AIR," above, first — that acquisition is a separate step from anything it does to Project Context.

Explicitly, OpenCode must not:

- recreate the Blueprint;
- rewrite `PROJECT.md`;
- duplicate feature documentation;
- create a second project context;
- create `CLAUDE_CONTEXT.md`, `OPENCODE_CONTEXT.md`, or an equivalent;
- remove or rewrite Claude Code's integration merely for stylistic consistency.

Running the same adoption request again, from either tool, changes nothing further — that's the idempotency guarantee made concrete.

## Not a tool registry

Tool-aware initialization is a fresh inspection performed every time adoption runs — like Implementation's "read `PROJECT.md`'s pointers fresh each time" (`references/implementation.md` step 2) — not a maintained ledger of which tools are integrated. A maintained ledger would be exactly the dependency matrix or registry `SPEC.md` §16 already excludes, and it would go stale the same way a stored dependency graph would. Detecting an integration means looking for it, each time, not consulting a record of it. The same is true of Skill availability: whether the current tool already has the AIR Skill (Case A, "Acquiring AIR") is checked fresh each time too, not assumed from a previous adoption run or tracked in a registry.
