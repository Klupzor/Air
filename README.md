# AIR — AI-Readable Project Framework

AIR stands for **AI-Readable**. Its purpose is to make software projects easier for AI coding agents to understand, navigate, modify, and maintain safely.

## What is AIR

AI coding agents lose reliability when a project's knowledge is scattered — some in stale docs, some only in chat history, some just in someone's head. Left unstructured, agents either re-read everything (slow, expensive, and still incomplete) or guess (fast, and sometimes wrong in ways that matter).

AIR's core idea: a project should expose its durable knowledge in a small number of canonical, predictable locations, so an agent can progressively discover the minimum context necessary for correct and safe reasoning — and so ambiguous requests get resolved with a human in conversation *before* they become implementation commitments, not after.

AIR is a methodology, not a tool. It's a specification, an Agent Skill, a set of reference documents, and a handful of templates — all plain Markdown, nothing that needs to run. See [`SPEC.md`](SPEC.md) for the full, normative definition.

## What's in this repo

| Path | What it is |
|---|---|
| [`SPEC.md`](SPEC.md) | The normative specification of AIR |
| [`skill/SKILL.md`](skill/SKILL.md) | The Agent Skill that teaches a coding agent to follow AIR |
| [`references/`](references/) | Detailed, operational guidance for Discovery, Implementation, Context Impact, and Adoption |
| [`templates/`](templates/) | Starting-point files for adopting AIR in a project |
| [`examples/minimal-project/`](examples/minimal-project/) | A tiny fictional project showing AIR's structure in practice |

## Using AIR in a project

- **New project:** copy the files under `templates/` into the project root and fill the Blueprint in as real knowledge accumulates.
- **Existing project:** don't overwrite what's already there. `references/adoption.md` covers how an agent should inspect existing documentation and propose a mapping onto AIR's canonical categories instead of duplicating it.
- **A second (or third) AI coding tool joins later:** it detects the existing AIR context, preserves it, and adds only its own integration — see `references/adoption.md`.

In every case, once adopted, a project's own files are self-sufficient — following AIR never requires this repository to be present at runtime (`SPEC.md` §17).

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
