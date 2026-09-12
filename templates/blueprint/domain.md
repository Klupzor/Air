# Domain

## What belongs here

- The vocabulary of the problem space: the terms people on this project actually use, and what they mean.
- The entities the system is built around, and the invariant facts about them (what an entity fundamentally *is*, not what a user can do with it).
- Domain facts that hold regardless of how the system happens to be implemented today.

## What does not belong here

- Product or UI behavior — what a user can do with an entity belongs in [`features/`](../features/), not here.
- Technical structure — how entities are represented in code, storage, or services belongs in [`architecture.md`](architecture.md) or [`modules.md`](modules.md).
- Conditional or procedural rules ("if X then Y") — those belong in [`rules.md`](rules.md). This file defines what things *are*; `rules.md` defines what must *happen*.

## Suggested structure

- **Vocabulary** — a short glossary of domain-specific terms, especially ones that could otherwise be ambiguous.
- **Entities** — the core things the system models, and the facts about each that don't change based on implementation details.

Keep this lightweight. A project with two or three core entities doesn't need this to be long — a few well-chosen definitions that prevent an agent from guessing wrong are worth more than an exhaustive data dictionary.
