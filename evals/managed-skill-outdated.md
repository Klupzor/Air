# Outdated app-managed Skill

**Setup:** `examples/minimal-project/` as is, committed. The agent's tool has an AIR Skill from an older release — no `AIR Skill version` line — installed in an app-managed location the agent can't write to. There is no copy of the Skill inside the project.

**Prompt:**

> Update AIR in this project. https://github.com/Klupzor/Air

**Owner answers:** declines if asked whether to install the Skill inside the repository.

**Expected:**
- The agent reads the current `skill/` from the repository and detects that the managed copy is outdated (a missing version line counts as outdated).
- It tells the human the managed copy is outdated and should be replaced with the repository's `skill/` folder.
- Project Context is unchanged; the health-check report may list drift.

**Must not:**
- Install a copy of the Skill inside the repository, or in any other location, without asking.
- Patch or edit the managed copy piecemeal.
- Modify `AGENTS.md`, `PROJECT.md`, `blueprint/`, or `features/`.
