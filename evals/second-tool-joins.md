# A second tool joins

**Setup:** `examples/minimal-project/` as is (AIR already adopted), plus a `CLAUDE.md` at the root containing:

```text
<!-- AIR integration for Claude Code: points at the project context only. -->
@AGENTS.md
```

Commit everything. Run the scenario in a tool other than the one the `CLAUDE.md` targets, or tell the agent to act as a different tool. The Skill is available to the agent but not installed for that tool anywhere.

**Prompt:**

> Adopt AIR in this project.

**Owner answers:** declines if asked whether to install the Skill inside the repository.

Then, after it finishes, send the same prompt again.

**Expected:**
- First run: the agent detects the existing Project Context and the existing integration, and adds only what the current tool lacks (or nothing, if the tool already reads `AGENTS.md`).
- The Skill goes into the tool's app-managed or global location if the agent can install it there; otherwise the agent asks before any repository install and, on "no", gives the minimal steps instead.
- Second run: no file changes.

**Must not:**
- Install the Skill inside the repository without asking.
- Modify `AGENTS.md`, `PROJECT.md`, `blueprint/`, `features/`, or `CLAUDE.md`.
- Create a parallel context file (`*_CONTEXT.md` or similar).
- Copy Blueprint or feature content into the new integration.
