# AIR Specification

Version: 0.1

AIR (AI-Readable) is a project-organization and agent-workflow framework. This document is the normative specification of AIR: what it is, what it requires, and what it deliberately leaves out. It describes AIR independently of any particular AI vendor, coding agent, or tool.

## 1. Purpose

AI coding agents work best when they can reliably answer two questions: *what is durably true about this project*, and *what is the agent currently supposed to do*. Left unstructured, both answers end up scattered across chat history, stale comments, half-updated docs, and the agent's own guesses.

AIR gives a project a small number of canonical, predictable locations for that knowledge, and a workflow for keeping it trustworthy as the project changes. The goal is not to make agents read less for its own sake — it is to let an agent read the **minimum context necessary for correct and safe reasoning**, and to make sure a human decides anything that materially matters.

AIR is a methodology, not a tool. It is expressed entirely as Markdown files that a project keeps in its own repository. Nothing about AIR requires a runtime component, and adopting it does not mean depending on the AIR repository going forward (see §17, Self-Hosting).

## 2. Core Principles

- **Progressive context.** An agent should discover context incrementally, guided by the task at hand, not by reading the whole repository up front.
- **Conversation is temporary discovery space.** Ambiguous requests get explored in conversation before they become commitments. Nothing durable is created from a request until material questions are resolved.
- **One active implementation contract.** A project has at most one `current-task.md`, containing the agreed intent of the work in progress. It is temporary by design.
- **Durable knowledge lives in the Blueprint.** Stable facts about architecture, domain, modules, rules, and decisions belong in a small, fixed set of canonical documents — not scattered, not duplicated.
- **Features describe capability, not implementation.** `features/` records what the product does, in product terms, not how it's coded.
- **No duplicated canonical knowledge.** Every durable fact has exactly one canonical home. Other documents reference it; they do not restate it.
- **Human decisions stay human.** An agent may analyze, recommend, and flag gaps. It must not invent a decision that materially affects product, domain, architecture, scope, or behavior.
- **Conflicts are surfaced, never silently resolved.** When documentation and implementation disagree, the agent reports the conflict and asks, rather than picking a side.
- **A clear separation of concerns governs AIR's own documents:**
  ```text
  SPEC.md        = what AIR is (this document; normative principles)
  references/    = how AIR is applied, in operational detail
  skill/SKILL.md = how an agent activates and follows AIR
  templates/     = how AIR is materialized in a project
  ```
  This document states principles. It intentionally does not walk through step-by-step agent procedures — those live in `references/`, and are triggered by `skill/SKILL.md`. If a rule here starts reading like a procedure, that is a sign it belongs in a reference document instead.

## 3. Project Context Model

A project adopting AIR exposes its knowledge through a small, fixed set of locations:

- **`AGENTS.md`** — a short, always-loaded activation file: AIR is in use, and the essential rules that hold even without the Skill available.
- **`PROJECT.md`** — a one-page map pointing to everything below. It is where an agent orients itself first.
- **`blueprint/`** — durable project knowledge: `architecture.md`, `domain.md`, `modules.md`, `rules.md`, `decisions.md`.
- **`features/`** — one document per meaningful product capability.
- **`current-task.md`** — the single active implementation contract, present only while a task is in flight.

No other canonical categories exist in v0.1. A project does not need a document for every category to have content in it yet — an empty or minimal Blueprint file is normal for a new project (see §15).

## 4. Discovery Phase

Discovery is the conversational process of turning an ambiguous or under-specified request into a resolved, implementable intent. It happens in conversation, with the human, before any implementation contract is written.

```text
User intent
    ↓
Minimum relevant context
    ↓
Understand system
    ↓
Identify ambiguity
    ↓
Ask questions
    ↓
Explore alternatives
    ↓
Propose
    ↓
Human decisions
    ↓
Readiness check
    ↓
Create current-task.md
```

Discovery is interactive: the agent asks the human rather than guessing on their behalf, and inspects real code when it needs facts rather than assuming them. It remains progressive — Discovery does not require reading the entire repository, only what's relevant to the ambiguity at hand. The full workflow, the readiness checklist, and how to decide what belongs in `current-task.md`'s design details are defined in [`references/discovery.md`](references/discovery.md).

## 5. Implementation Phase

Implementation begins once `current-task.md` exists with `Status: READY`. It is typically carried out by a fresh agent with no access to the Discovery conversation that produced the task — `current-task.md` alone must be sufficient. Implementation covers reading the task, reading only the project context it requires, inspecting relevant code, implementing, testing, running a Context Impact Check, updating canonical context where warranted, and committing. The full ordered procedure is defined in [`references/implementation.md`](references/implementation.md).

## 6. `current-task.md`

`current-task.md` is the implementation contract produced at the end of Discovery. It captures agreed intent, not conversation history — a fresh agent must be able to continue the work from this file alone.

It is not a task-management system, not a task history, and not a step-by-step coding recipe. There is only ever one active task, and it lives at the project root, not under `tasks/`.

**Lifecycle:**

```text
Discovery
    ↓
current-task.md (Status: READY)
    ↓
Implementation
    ↓
Context Impact Check
    ↓
Commit
    ↓
Delete current-task.md
```

The file does not exist before Discovery converges, and it is deleted once its task is committed. The permanent record of what happened is git history, plus whatever canonical context was updated along the way — never an archived or retained `current-task.md`. This lifecycle is stated identically in [`skill/SKILL.md`](skill/SKILL.md), [`references/implementation.md`](references/implementation.md), and [`templates/current-task.md`](templates/current-task.md); it does not vary between them.

The template defines these sections: `Status`, `Objective`, `Feature`, `Decisions`, `Scope`, `Constraints`, `Acceptance Criteria`, `Design Details`, `Applicable Rules`, `Expected Context Impact`. `Decisions` captures the product/scope/domain-level calls made during Discovery (the *what and why*). `Design Details` is narrower and more technical: it separates choices that were `Decided During Discovery` from those intentionally `Left to the Implementer`, so that two competent agents implementing the same task don't accidentally diverge on something that matters. A design choice only needs to be decided during Discovery when two reasonable implementations could produce materially different behavior, architecture, interfaces, or future constraints — routine function signatures and internal structure are left to the implementer. Field-level guidance lives in [`templates/current-task.md`](templates/current-task.md).

## 7. Blueprint

The Blueprint is a project's durable knowledge, split into five categories, each with a single responsibility:

| File | Owns |
|---|---|
| `blueprint/architecture.md` | System structure: components, how they communicate, deployment topology |
| `blueprint/domain.md` | Vocabulary, entities, and invariant domain facts |
| `blueprint/modules.md` | Which module/directory owns which responsibility |
| `blueprint/rules.md` | Canonical business/domain rules, precisely worded |
| `blueprint/decisions.md` | Durable decisions that still constrain future work, with lightweight rationale |

None of these should become a dumping ground for everything an agent happens to learn. Each template in [`templates/blueprint/`](templates/blueprint/) states explicitly what belongs and what doesn't.

## 8. Features

`features/` describes what the product does, in terms a user or product owner would recognize — not an API reference or an implementation diary. "Users can filter tasks by status" belongs here. "The service now accepts an optional status parameter" generally does not, unless that implementation detail is itself durable knowledge someone would need to know later.

This is the same boundary as Context Impact's product-capability-vs-plumbing distinction (§12), and shares one canonical example between [`templates/features/README.md`](templates/features/README.md) and [`references/context-impact.md`](references/context-impact.md) rather than restating it twice with different wording.

## 9. Progressive Context

The goal is not "minimize tokens at all costs." The goal is: read the minimum context necessary for correct and safe reasoning. In practice this means starting from `PROJECT.md`, following its pointers only as needed for the task at hand, and expanding scope in proportion to the ambiguity or risk actually present — not as a blanket policy of reading less.

## 10. Human Decision Boundaries

The AI may:

- analyze the request and the existing project;
- recommend an approach;
- identify trade-offs between alternatives;
- propose a solution;
- identify missing information or unresolved questions.

The AI must **not**:

- invent a decision that materially affects product behavior, domain meaning, architecture, scope, or user-facing behavior;
- simulate or assume what a human would have decided;
- proceed to a `READY` `current-task.md` while a material question remains open.

When a decision meets this bar, the agent stops and asks. This boundary applies everywhere in AIR, most visibly during Discovery (§4), but also whenever Context Impact (§12) surfaces a Case C change.

## 11. Conflict Handling

Documentation and implementation will sometimes disagree. The rule is: **never silently choose between conflicting project truth and implementation.**

- If the conflict is unrelated to the decision currently being made, report it and leave both sides alone.
- If the conflict blocks the decision currently being made, surface it, explain the competing interpretations, and ask the human to decide.

The canonical format for surfacing a blocking conflict:

```text
CONTEXT CONFLICT

Documentation says:
Module A owns payment validation.

Code currently does:
Module B owns payment validation.

This affects the requested consolidation because consolidation requires choosing one ownership model.

Which behavior should become canonical?
```

This is the one place this format is written out in full; every other AIR document refers back to "the CONTEXT CONFLICT format in SPEC §11" rather than reproducing it. The detection procedure and the blocking-vs-non-blocking distinction are defined in [`references/context-impact.md`](references/context-impact.md).

## 12. Context Impact

After implementation, an agent determines whether durable project knowledge has changed:

- **Case A — No durable change.** Implementation changed, but the Blueprint remains accurate. Nothing is updated.
- **Case B — Durable truth changed safely.** An established business/domain/product fact changed. The affected canonical document is updated as part of the normal, reviewable commit — this does not require a new approval conversation, but it is never a silent, invisible edit either.
- **Case C — Important architectural or domain change.** Architecture, domain ownership, or another significant durable decision changed. The agent identifies the affected documents, proposes the change, obtains human approval, and only then applies it.

Full definitions, worked examples, and the durable-truth boundary (including why a change being user-visible doesn't by itself make it durable) are in [`references/context-impact.md`](references/context-impact.md).

## 13. Dependent-Context Checking

Changing one concept can make other documentation stale even though that document wasn't directly touched. The guiding question is:

> Which other canonical documents describe or depend on the concept being changed?

This is not "always read every document," and AIR does not maintain a dependency matrix, registry, or graph to answer it — the check is proportional to the likely impact of the change, reasoned about by the agent each time. A clearly local implementation change warrants a lightweight check; an architectural or ownership change warrants a broader review. See [`references/context-impact.md`](references/context-impact.md) for guidance, not a rulebook.

## 14. Git and History

Git is the project's history mechanism. AIR's own documents are deliberately not history:

- `current-task.md` is not a log of what was tried — it's deleted once its work is committed (§6).
- `blueprint/decisions.md` holds durable decisions with ongoing bearing, not a duplicate of every commit's rationale.
- Implementation narrative, alternatives considered, and the reasoning behind a change belong in commit messages, not in canonical documents.

If a document starts accumulating historical narrative, that content should move to git history or be removed.

## 15. Adoption of AIR in New and Existing Projects

**New projects** can start directly with the structure in §3: an empty or minimal Blueprint, `AGENTS.md` and `PROJECT.md` from `templates/`, and no `current-task.md` until the first Discovery converges.

**Existing projects** already have architecture notes, domain knowledge, or decision records somewhere — possibly not in AIR's canonical locations. AIR must not overwrite or duplicate that knowledge. Adoption in an existing project means inspecting what already exists, proposing a mapping onto AIR's canonical categories (which may mean pointing at an existing document rather than creating a new one), and asking the human before any reorganization that could destroy or obscure existing information. The operational checklist and example phrasing for this are in [`references/adoption.md`](references/adoption.md).

A project's context can also outlive any single tool: adopting AIR again later, with the same tool or a different one, must reuse the Project Context that already exists rather than recreate it. §19 defines the rule that keeps a tool's own integration separate from that shared context.

Either way, adoption is complete once the project's own files are sufficient for an agent to follow AIR without needing anything else (§17, Self-Hosting, below).

## 16. What AIR Intentionally Does Not Provide

AIR v0.1 is deliberately tool-light. It does not include, and should not be extended in v0.1 to include:

- an MCP server or any custom daemon;
- a database, vector database, or project index;
- a context-management service or agent orchestrator;
- a CLI or other external runtime infrastructure;
- a dependency matrix, registry, or graph for tracking which documents depend on which;
- a task database or task history mechanism (`current-task.md` is singular and temporary; git is history);
- mandatory metadata systems, schemas, or complex configuration beyond plain Markdown.

If a project's needs seem to call for one of these, that is a signal to solve it with clearer Markdown and better agent judgment first, not to add infrastructure. AIR is a specification, a Skill, reference docs, templates, and an example — nothing that must run.

## 17. Self-Hosting

A project that has adopted AIR must remain understandable and operable even if the AIR repository disappears, the Skill becomes unavailable, or the original author is unreachable. Everything an agent needs to follow AIR in that project — `AGENTS.md`, `PROJECT.md`, the Blueprint, `features/`, and (when active) `current-task.md` — lives in the project's own files. The AIR repository is the source and distribution mechanism for the methodology; it is not a runtime dependency of any project that uses it.

## 18. Vendor Neutrality

AIR is conceptually independent of any specific AI coding agent, including Claude Code, Codex, Cursor, and OpenCode. This specification and the files under `references/` and `templates/` contain no agent-specific assumptions. `skill/SKILL.md` uses a minimal, generic frontmatter format for practical loadability by compatible tooling, but the framework it describes does not depend on that format, and installation notes for specific agents (where a project chooses to document them) are not part of the core specification. When more than one such tool works on a project over its lifetime, §19 defines how each tool's integration stays separate from the project's shared context.

## 19. Project Context and Tool Integration

A project's lifetime often spans more than one AI coding tool — for example Claude Code, Codex, Cursor, or OpenCode (§18), introduced at different points. AIR treats two things adoption produces as fundamentally different, and they must never be conflated:

- **Project Context** — the durable knowledge defined in §3: `AGENTS.md`, `PROJECT.md`, the Blueprint, `features/`, and `current-task.md` when active. It is canonical and shared across every tool that works on the project.
- **Tool Integration** — whatever instructions, Skill registration, or configuration a specific AI coding tool needs to discover and correctly apply AIR. It is specific to that tool and exists only to adapt the tool to the project's context.

> The project's AIR context is canonical and shared. Tool integrations are adapters around that context.

A Tool Integration points an agent at the Project Context; it never duplicates that context into a tool-specific document. When Project Context already exists and a new tool is introduced, adoption means reusing that context, adding only the integration the new tool is missing, and leaving every other tool's existing integration untouched unless the current tool genuinely requires it to change. Adoption is idempotent: running it again — for the same tool or a different one — never recreates Project Context that already exists, and never leaves behind more than one competing version of it.

The exact mechanism for registering a Skill or configuring an instruction entry point is inherently tool-dependent, so this specification defines only the requirement, not the mechanism:

> An AIR-compatible agent must be able to discover and apply the AIR workflow without requiring the project's durable context to be duplicated for that agent.

Tool-specific mechanisms belong in operational guidance ([`references/adoption.md`](references/adoption.md)), not in this document, consistent with §2's separation of concerns. The objective throughout:

> Adapt the agent to the project, not the project context to every agent.
