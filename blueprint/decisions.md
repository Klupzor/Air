# Decisions

Only decisions that still constrain future work.

## D1: No runtime components

AIR ships no CLI, MCP server, database, index, or orchestrator. Anything that seems to need one is solved first with clearer Markdown and agent judgment.

## D2: The task contract lives in git for exactly one task

`current-task.md` is committed at the start of a task on the branch decided during Discovery, and deleted by the commit that closes it — approved or abandoned. A READY task is never overwritten. This makes a task resumable by any agent from its branch, without leaving task files behind.

## D3: Acquiring AIR is separate from installing it

Adoption requires only access to the Skill (already available, or read from the repository). Installing the Skill into a tool is preferred but never a prerequisite; when a tool can't install it, adoption completes and the human gets minimal manual steps.

## D4: The Skill is a self-contained, versioned folder

`skill/` is installed and updated as a whole, never patched or rewritten per tool. Installed copies compare their version line with the repository's to know when to update. Each tool has one installed copy, updated in place: its app-managed or global location first, and a copy inside a project only with the owner's consent.

## D5: Minimal Skill frontmatter

`SKILL.md` frontmatter carries only `name` and `description`, so compatible tools can load it without AIR depending on any tool's format. The version lives in the body.

## D6: Project context outlives tools

The project's context is shared and canonical; each AI coding tool gets only a thin integration that points at it (`SPEC.md` §19).
