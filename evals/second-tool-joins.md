# A second tool joins

**Setup:** `examples/minimal-project/` as is (AIR already adopted), plus a `CLAUDE.md` at the root containing:

```text
<!-- AIR integration for Claude Code: points at the project context only. -->
@AGENTS.md
```

Commit everything. Run the scenario in a tool other than the one the `CLAUDE.md` targets, or tell the agent to act as a different tool.

**Prompt:**

> Adopt AIR in this project.

Then, after it finishes, send the same prompt again.

**Expected:**
- First run: the agent detects the existing Project Context and the existing integration, and adds only what the current tool lacks (or nothing, if the tool already reads `AGENTS.md`).
- Second run: no file changes.

**Must not:**
- Modify `AGENTS.md`, `PROJECT.md`, `blueprint/`, `features/`, or `CLAUDE.md`.
- Create a parallel context file (`*_CONTEXT.md` or similar).
- Copy Blueprint or feature content into the new integration.
