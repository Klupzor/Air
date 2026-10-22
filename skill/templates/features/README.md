# Writing feature documents

Guidance for agents. **Not copied into projects** — a project's `features/` holds one file per capability, and nothing else is required.

`features/` describes what the product does — meaningful, user-recognizable capabilities and behavior. Each file describes one capability, in prose, from the outside.

## What belongs there

Behavioral, product-level statements:

> Users can filter tasks by status.

## What does not belong there

Implementation or interface detail:

> The service now accepts an optional `status` parameter.

The test: would a user describe what the product does differently after this change? A new optional parameter, flag, CLI syntax, or endpoint shape usually fails it, so it doesn't touch `features/`. This boundary exists because agents repeatedly edited feature documents for small optional parameters that didn't change what the product does.

Concretely, a feature document must not become:

- **An API or CLI reference.** If it reads like signatures, endpoints, or command syntax, it's describing interface, not capability.
- **A changelog.** "Added X, then changed X to do Y" belongs in commits; a feature document describes current behavior only.

## Referencing rules

If a capability's behavior is governed by a rule in `blueprint/rules.md`, reference the rule rather than restating its wording:

> New tasks default to status `todo` (rule R1 in `blueprint/rules.md`).

## No per-feature template

Feature documents are freeform prose — whatever a person needs to understand the capability. There is deliberately no fixed schema.
