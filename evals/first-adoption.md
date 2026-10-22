# First adoption from the repository URL

**Setup:** a copy of `examples/minimal-project/` with `AGENTS.md`, `PROJECT.md`, `blueprint/`, and `features/` removed. The AIR Skill is not installed.

**Prompt:**

> Adopt AIR in this project.
> https://github.com/Klupzor/Air

**Owner answers:** approves any proposed mapping.

**Expected:**
- The agent reads the Skill from the repository's `skill/` folder.
- It creates `AGENTS.md`, `PROJECT.md`, and `blueprint/` from the Skill's templates, with content drawn from the actual code (the `Task` entity, the three statuses, the three modules).
- `features/` holds one file per capability (creating tasks, listing and filtering them, marking them done) and no copy of the features guidance README.
- It installs the Skill through the tool's mechanism, or gives minimal manual steps if it can't.

**Must not:**
- Copy `SPEC.md`, `references/`, or the whole repository into the project.
- Invent knowledge the code doesn't support (persistence, users, projects).
- Leave template guidance ("What belongs here") in Blueprint files.
