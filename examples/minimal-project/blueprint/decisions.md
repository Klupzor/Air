# Decisions

## D1: In-memory storage only, no persistence

The example uses an in-memory store with no database or file persistence, to keep the demonstration free of external dependencies. Revisit this if the example ever needs to show a persistence-related workflow.

## D2: Flat task list, no per-project grouping

Tasks are not grouped under a "Project" entity (see `blueprint/domain.md`). This keeps the example's domain to a single concept, which is enough to demonstrate AIR's structure without adding scope the example doesn't need.
