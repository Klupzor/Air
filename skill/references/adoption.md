# Adoption

How a project starts using AIR, how each AI coding tool that works on it gets integrated, and how AIR is updated later. One request — "Adopt AIR in this project" — covers all three, and is safe to repeat.

Three things are involved and must not be confused:

- **The AIR repository** (`https://github.com/Klupzor/Air`) — where AIR is acquired from. Never copied into a project.
- **Project Context** — the project's own durable knowledge: `AGENTS.md`, `PROJECT.md`, `blueprint/`, `features/`, and `current-task.md` while a task is active. Shared by every tool.
- **Tool Integration** — whatever one tool needs to find and apply AIR: this Skill installed in the tool, or an instruction file pointing at the Project Context. It adapts the tool to the project and never holds project knowledge.

## Acquiring AIR

Adopting AIR requires access to this Skill — `SKILL.md` with its `references/` and `templates/`. Acquisition is getting that access; installation is making it permanent in a tool. Only acquisition is required.

Acquisition:

- **A — The Skill is already available** to the current tool. Use it; fetch nothing.
- **B — The human provides the AIR repository URL.** Read the repository's `skill/` folder. Don't copy the repository, or its `SPEC.md`, into the project.

Installation, decided once the current tool is identified:

- **C — Install once per tool, in this order.** Always install the repository's `skill/` folder whole; never rewrite it into a tool-specific version of the workflow.
  1. **Already installed for this tool, anywhere** — app-managed, global, or inside a project: that copy is the one. Update it in place (E); never add a second copy somewhere else.
  2. **Not installed** — install it in the tool's app-managed or global location, so every project uses the same copy (for Claude Code, its global skills).
  3. **The tool or app won't let you install it there** — ask the human whether to install it inside this repository instead. Install it in the repository only if they say yes.
- **D — The Skill ends up not installed** (no location was possible, or the human declined the repository). Adoption continues: use the Skill content you acquired, configure an instruction entry point if the tool has one, and finish by giving the human the minimal steps to install the Skill themselves — only steps you can establish reliably for that tool; never invent a command or path.
- **E — An installed Skill is outdated.** Compare its `AIR Skill version` line with the repository's; a missing line counts as outdated. If the repository's is newer, replace the whole installed folder where it is; never patch or merge it, and never touch Project Context while doing so. If you can't write where it's installed (an app-managed copy, for example), tell the human it's outdated and that it should be replaced with the repository's `skill/` folder — don't work around it by installing a copy elsewhere. If the repository is unreachable, keep using the installed copy.

**Installing the Skill is preferred, never a prerequisite** — adoption succeeds the same way whether C or D applies.

## Tool-aware initialization

Every adoption request answers these in order, before modifying anything:

0. Acquire AIR (A or B above).
1. Identify the AI coding tool you're running in.
2. Detect whether Project Context already exists.
3. Detect whether the current tool is already integrated — including a Skill available to you from any location (app-managed, global, or in the project), not just files in the repository — and whether that Skill is outdated (E).
4. Identify the tool's native mechanisms: Skill installation, an instruction file, both, or neither.
5. Determine the minimum change — what's missing, nothing more.

Then work in this order: establish Project Context if it's missing ("Establishing project context"); then the current tool's integration ("Adding a tool integration"), installing the Skill per C or D; then validate — `PROJECT.md` points at real content, and the tool will find AIR in a new session. If nothing is missing, adoption changes nothing beyond the health-check report.

## Establishing project context

### New project

Copy `AGENTS.md`, `PROJECT.md`, and the `blueprint/` files from this Skill's `templates/`. The blueprint templates are seeds: replace their guidance with real content as it becomes known, and leave a file short rather than invent knowledge. Create `features/` with one file per capability the product already has — but don't copy `templates/features/README.md`; it's guidance for agents, not a project file.

### Existing project

Don't overwrite or duplicate what's already there.

1. Inspect the project for existing knowledge: READMEs, design docs, wikis, ADRs, older agent context files.
2. Work out which of them already cover architecture, domain, rules, decisions, or features — even partly, even under other names.
3. Propose a mapping onto AIR's categories. An existing document can stay where it is and become the canonical home; the project doesn't have to match the template layout.
4. Ask the human before any reorganization that could destroy, obscure, or merge information. For example:

   ```text
   Existing architecture documentation appears to live in:
   docs/architecture.md

   I propose using that as the canonical architecture source rather than creating a duplicate blueprint/architecture.md.

   Approve?
   ```

5. Preserve information: move or link rather than delete, unless the human approves removal.
6. Finish with every legacy knowledge document in exactly one state: **canonical** (`PROJECT.md` points to it as the home for a category) or **retired** (a banner at the top — "Superseded by `blueprint/…`; do not update" — and nothing points to it as a live source). A legacy file left live beside the Blueprint becomes a second, drifting copy, whatever it's called.

## Adding a tool integration

Reached when Project Context exists but the current tool isn't integrated.

- Reuse the Project Context as it is; don't re-derive it.
- Look for existing integrations — Skill folders, instruction files — and leave every other tool's integration untouched. Replace one only when that tool's own requirements genuinely changed, never as a cleanup.
- Add only what the current tool lacks: the Skill (C), an instruction entry point, or both — in which case the Skill carries the workflow and the entry point stays short.
- An instruction entry point only points at the Project Context, for example:

  ```text
  Load PROJECT.md first.
  Use the AIR Blueprint for durable project knowledge.
  Follow the AIR Discovery workflow.
  ```

  It never contains copies of Blueprint or feature content. Mark it as an AIR integration in a one-line comment, so another tool's agent recognizes it.
- If the tool already reads `AGENTS.md` as its instruction file, that file is its integration — add nothing.

Adapting AIR to the tool is expected; adapting the project's context to the tool is not.

## Idempotency and preservation

```text
First tool:   project → acquire AIR → establish Project Context → Tool A integration
Second tool:  existing project → detect context → detect Tool A → acquire/use AIR → Tool B integration only
Third tool:   existing project → detect context → detect Tools A + B → acquire/use AIR → Tool C integration only
```

Repeating adoption, from any tool, never recreates Project Context, never duplicates documentation, never reinstalls a Skill that's current, and never creates a parallel knowledge store — not `CLAUDE_CONTEXT.md`, `OPENCODE_CONTEXT.md`, or anything playing the same role under another name.

## Health check

When adoption runs in a project that already has AIR, report — don't fix — drift you notice:

- Blueprint files past roughly 200 lines, or containing dated entries and history narration.
- Template guidance copied in as project content, such as the features guidance file.
- A live legacy knowledge store beside the Blueprint.
- A READY `current-task.md` with no start commit, or on a branch other than the one it names.
- A copy of the AIR Skill inside the project when the tool also has an app-managed or global copy.

The owner decides what to do about each; any fix is an ordinary task for later.

## Worked example

1. In a project without AIR, a human tells Claude Code: "Adopt AIR in this project. https://github.com/Klupzor/Air". Claude Code reads `skill/` from the repository (B), finds no Project Context, asks how to map the existing `docs/` (Existing project), establishes the context, installs the Skill in Claude Code's global skills (C), and validates.
2. Later the human opens the project in OpenCode with the same request. OpenCode finds the context and Claude Code's integration, and adds only its own integration — installing the Skill in OpenCode's global location if it can, or asking before installing it in the repository (C), or giving the human the steps (D). It doesn't touch the Blueprint, `PROJECT.md`, `features/`, or Claude Code's integration.
3. Repeating the request in either tool changes nothing beyond the health-check report.
4. After a new AIR version is released, "Update AIR in this project" in either tool replaces that tool's installed Skill folder where it is — or, for an app-managed copy it can't write, tells the human to replace it (E). The Project Context is untouched.

## Not a tool registry

Integrations and Skill versions are detected by looking, every time adoption runs. AIR keeps no record of which tools are integrated; such a record would drift like any other duplicate.
