# Architecture

## Overview

A tiny single-process command-line task manager. There is no database, no network service, and no persistence — everything lives in memory for the lifetime of one CLI invocation's underlying process. This example is intentionally minimal: it exists to demonstrate AIR's structure, not sophisticated engineering.

## Components

- `src/models.py` — defines the `Task` entity and its `Status`.
- `src/store.py` — owns in-memory storage and the filtering rule.
- `src/cli.py` — a thin command-line interface over `TaskStore`; contains no business logic of its own.

## Data flow

A CLI command (`add`, `list`, `done`) is parsed by `cli.py`, which calls the corresponding `TaskStore` method and prints the result. There's no flow beyond that — no queues, no async boundaries.

## Key technologies

Python standard library only (`dataclasses`, `enum`, `argparse`). No external dependencies, by design (see `blueprint/decisions.md#d1`).

## External dependencies

None.
