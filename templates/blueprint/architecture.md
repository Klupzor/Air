# Architecture

## What belongs here

- The system's major components/services and how they're structured.
- How components communicate (APIs, message queues, shared storage, in-process calls).
- Deployment topology (single process, distributed services, client/server, etc.).
- Technology choices that are structurally significant — i.e. changing them would mean changing the shape of the system, not just swapping a library.

## What does not belong here

- Business or domain rules — those belong in [`rules.md`](rules.md).
- Vocabulary and entity definitions — those belong in [`domain.md`](domain.md).
- An exhaustive list of every module, file, or API endpoint — that belongs in [`modules.md`](modules.md); this file describes the shape of the system, not its inventory.
- The history or rationale of *why* the architecture ended up this way — that belongs in [`decisions.md`](decisions.md); this file may link to a decision, but shouldn't reproduce its reasoning.

## Suggested structure

A short document is normal, especially early on. Headings that tend to be useful:

- **Overview** — one paragraph on the system's overall shape.
- **Components** — the major pieces and their responsibilities, at a level above individual modules.
- **Data flow** — how a request or piece of data moves through the system.
- **Key technologies** — languages, frameworks, or infrastructure that shape the architecture.
- **External dependencies** — other systems this one talks to.

Keep this file accurate rather than exhaustive. If a detail would only matter to someone reading a specific module's code, it likely belongs in `modules.md` or the code itself, not here.
