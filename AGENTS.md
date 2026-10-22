# Agent Instructions

This project uses [AIR](https://github.com/Klupzor/Air) (AI-Readable) — and it *is* AIR, so its own rules apply to how it is written. If the AIR Skill is available to you, load it and follow it. The rules below are the essentials that hold even if the Skill isn't available.

- Start at [`PROJECT.md`](PROJECT.md). Use progressive context: read only what the current task requires.
- For anything beyond a trivial, unambiguous change, resolve material ambiguity in conversation (Discovery) before writing or acting on an implementation contract.
- `current-task.md`, if present, is the single active implementation contract. It is written once Discovery has converged, committed at the start of the task on the branch it names, and deleted by the commit that closes the task. Never overwrite it with a new task.
- `blueprint/` holds this repository's durable design knowledge. Don't duplicate canonical knowledge across documents — reference it instead. Follow the authoring rules in [`blueprint/rules.md`](blueprint/rules.md) for every change to AIR's own documents.
- Any change under `skill/` bumps the version (rule R6).
- Never invent a decision that materially affects AIR's principles, workflow, or structure. Ask the owner.
- If documentation and reality disagree, surface the conflict and ask — never silently pick a side.
- After a meaningful change, run a Context Impact Check. Canonical documents state what is true now — never a dated log of what happened; that belongs in commit messages.
