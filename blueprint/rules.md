# Rules

Authoring rules for AIR's own documents. AIR projects get the general versions of R1 and R2 through `skill/references/context-impact.md`; the rest are specific to this repository.

## R1: One canonical home, cited elsewhere

Each concept is stated in full once, in the home listed in `blueprint/modules.md`. Other files cite that home; a short operational summary is allowed only where an agent needs it to act (as in `skill/SKILL.md`). Before adding a sentence, search for whether its rule already has a home.

## R2: No claims about other documents

Never write statements about what another document says or how it is structured ("stated identically in…", "shared rather than restated"). Quote only text you have just read, verbatim.

## R3: Append SPEC sections, never renumber

Other files cite `SPEC.md` by section number and anchor. New sections are appended; existing numbers never change.

## R4: Vendor names only as illustrations

Real tool names may appear as examples. No requirement, step, or filename in AIR may depend on a specific tool.

## R5: `skill/` is self-contained

Nothing inside `skill/` links outside it, and anything an agent needs in order to operate lives inside it. `SPEC.md` may be cited for rationale only.

## R6: Version bump on any `skill/` change

Any change under `skill/` updates the `AIR Skill version` line in `skill/SKILL.md` and the `Version` line in `SPEC.md` to the same new number. Installed copies rely on it to detect that they are outdated.
