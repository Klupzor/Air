# Modules

## What belongs here

- A map from module, package, or directory to the responsibility it owns.
- Ownership boundaries — which part of the codebase is the canonical place to make a given kind of change. This is what resolves "which module actually owns X" when documentation and code disagree (see `SPEC.md` §11, Conflict Handling).

## What does not belong here

- **A line-by-line API reference.** This is the most common way this file turns into a dumping ground: someone starts documenting every function or endpoint here, and the file becomes a second, always-stale copy of the code. If you want to know a function's signature, read the function.
- Business or domain rules — those belong in [`rules.md`](rules.md).
- Architecture-level topology (how whole components or services relate) — that belongs in [`architecture.md`](architecture.md); this file is one level more granular, inside a single component.

## Suggested structure

A simple table is usually enough:

| Module | Owns |
|---|---|
| `path/to/module` | The responsibility it's the canonical home for |

Update this file when ownership genuinely changes — a module starts or stops owning something — not when its internals change but its responsibility doesn't.
