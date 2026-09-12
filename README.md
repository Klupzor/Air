# AIR — AI-Readable Project Framework

AIR stands for **AI-Readable**. Its purpose is to make software projects easier for AI coding agents to understand, navigate, modify, and maintain safely.

## What is AIR

AI coding agents lose reliability when a project's knowledge is scattered — some in stale docs, some only in chat history, some just in someone's head. Left unstructured, agents either re-read everything (slow, expensive, and still incomplete) or guess (fast, and sometimes wrong in ways that matter).

AIR's core idea: a project should expose its durable knowledge in a small number of canonical, predictable locations, so an agent can progressively discover the minimum context necessary for correct and safe reasoning — and so ambiguous requests get resolved with a human in conversation *before* they become implementation commitments, not after.

AIR is a methodology, not a tool. It's a specification, an Agent Skill, a set of reference documents, and a handful of templates — all plain Markdown, nothing that needs to run. See [`SPEC.md`](SPEC.md) for the full, normative definition.

## Quick Start

From the project you want to organize, ask your AI coding agent:

> Adopt AIR in this project.

If AIR is not already available to the agent, provide the AIR repository:

> https://github.com/Klupzor/Air

From there, the agent should be able to run the whole adoption workflow on its own:

1. Acquire AIR — read the Skill and the reference documents it needs from the repository (or use the Skill directly, if it's already available).
2. Determine which AI coding tool is currently running.
3. Detect whether the project already has AIR's Project Context.
4. Detect whether the current tool is already integrated with it.
5. Inspect the existing project when establishing or extending that context.
6. Ask you about material ambiguity or conflicts instead of guessing.
7. Establish Project Context if it doesn't exist yet, or reuse it unchanged if it does.
8. Install or register the canonical AIR Skill through the current tool's native mechanism, if the tool allows it.
9. Establish the minimum Tool Integration the current tool still needs.
10. Validate the result.

If the current tool doesn't let an agent install or register a Skill automatically, adoption still isn't blocked: the agent continues the workflow using the repository's contents and tells you the minimal manual steps needed to enable the Skill for that tool. Skill installation and Project Context adoption are separate concerns — the second never depends on the first succeeding.

You shouldn't need to reorganize anything by hand. The full acquisition-and-adoption procedure the agent follows is defined in [`references/adoption.md`](references/adoption.md).

Installing the Skill is a convenience the current tool may support, not a prerequisite — AIR adoption means organizing the project around its canonical Project Context, with the Skill as the preferred operational mechanism when it's available. Once adopted, a project's own files are self-sufficient — following AIR never requires this repository to be present at runtime (`SPEC.md` §17).

## What's in this repo

| Path | What it is |
|---|---|
| [`SPEC.md`](SPEC.md) | The normative specification of AIR |
| [`skill/SKILL.md`](skill/SKILL.md) | The Agent Skill that teaches a coding agent to follow AIR |
| [`references/`](references/) | Detailed, operational guidance for Discovery, Implementation, Context Impact, and Adoption |
| [`templates/`](templates/) | Fallback starting-point files for manual adoption, or for inspecting AIR's structure directly |
| [`examples/minimal-project/`](examples/minimal-project/) | A tiny fictional project showing AIR's structure in practice |

## Manual setup (fallback)

Templates remain useful — as a fallback when the current tool can't run the adoption workflow automatically, and as a reference when a human wants to see AIR's starting structure directly, without an agent involved.

- **Can't automate adoption:** copy the files under [`templates/`](templates/) into the project root yourself, then use them the same way an agent would — `PROJECT.md` and `AGENTS.md` at the root, `blueprint/` filled in as real knowledge accumulates, `features/` describing what the product does.
- **Existing project, doing it by hand:** don't overwrite what's already there — map your existing documentation onto AIR's canonical categories the same way [`references/adoption.md`](references/adoption.md) has an agent do it, rather than duplicating it.
- **Just want to see the shape of it:** [`examples/minimal-project/`](examples/minimal-project/) shows a filled-in, worked example; `templates/` shows the empty starting point.

This is a fallback path, not the recommended one — prefer asking an agent to adopt AIR, per the Quick Start above.

## Core ideas at a glance

| Idea | Summary | Details |
|---|---|---|
| Discovery | Ambiguity gets resolved in conversation before anything durable is written | [`SPEC.md` §4](SPEC.md#4-discovery-phase) |
| `current-task.md` | The single, temporary implementation contract — created once Discovery converges, deleted once committed | [`SPEC.md` §6](SPEC.md#6-current-taskmd) |
| Blueprint | Durable project knowledge: architecture, domain, modules, rules, decisions | [`SPEC.md` §7](SPEC.md#7-blueprint) |
| Features | What the product does, in product terms — not an API reference | [`SPEC.md` §8](SPEC.md#8-features) |
| Context Impact | After implementing, decide whether durable knowledge actually changed | [`SPEC.md` §12](SPEC.md#12-context-impact) |
| Tool Integration | Project context is canonical and shared; a tool's integration is only an adapter around it, never a duplicate | [`SPEC.md` §19](SPEC.md#19-project-context-and-tool-integration) |

AIR is conceptually independent of any specific AI coding agent (`SPEC.md` §18).

## License

[MIT](LICENSE)
