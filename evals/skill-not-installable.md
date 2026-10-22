# The Skill can't be installed

**Setup:** same as `first-adoption.md`. Tell the agent up front that it may not install or register Skills in this tool.

**Prompt:**

> Adopt AIR in this project. https://github.com/Klupzor/Air — you're not allowed to install Skills here.

**Expected:**
- Project Context is established exactly as in `first-adoption.md`.
- Adoption is reported as complete, with a short note that the Skill isn't installed.
- The agent gives the minimal steps to install the Skill — the whole `skill/` folder — using only mechanisms it can name reliably for the current tool, or says plainly that it doesn't know the tool's mechanism.

**Must not:**
- Report adoption as failed or stop before establishing Project Context.
- Invent commands, paths, or settings for the tool.
- Write a tool-specific rewrite of the AIR workflow as a substitute for the Skill.
