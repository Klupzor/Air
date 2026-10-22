# Architecture

AIR is plain Markdown; nothing in it runs. The repository has four layers with one responsibility each:

| Layer | Responsibility |
|---|---|
| `SPEC.md` | What AIR is: normative principles and rationale. No procedures. |
| `skill/SKILL.md` | Entry point for agents: when AIR applies and which reference to load. |
| `skill/references/` | How AIR is applied, step by step. |
| `skill/templates/` | Starting files materialized into adopting projects. |

## The deployable unit

`skill/` is what gets installed into an AI coding tool. It is copied whole and must work on its own: nothing inside it links outside it, and nothing an agent needs to operate lives only in `SPEC.md`. Installed copies are updated by replacing the whole folder, compared by the `AIR Skill version` line in `SKILL.md`.

## Not shipped

- `examples/minimal-project/` — a small adopted project used as a demonstration and as the fixture for evals.
- `evals/` — scenarios that check whether an agent applies AIR correctly.
- `AGENTS.md`, `PROJECT.md`, `blueprint/` — this repository's own project context.
