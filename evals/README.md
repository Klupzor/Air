# Evals

Scenarios for checking whether an agent applies AIR correctly. They test the instructions, not the agent: when a scenario fails, the fix usually belongs in `skill/`.

## Running a scenario

1. Prepare the fixture in a scratch directory — usually a fresh copy of `examples/minimal-project/` initialized as a git repository, plus the files the scenario's **Setup** adds.
2. Start a **fresh** agent session with no history from this repository's development. Give it access to `skill/` (installed as a Skill, or as a folder it can read) and nothing else from this repository.
3. Send the scenario's **Prompt**. Where the scenario expects the agent to stop and ask, answer as the **Owner answers** line says.
4. Compare the resulting files, commits, and conversation against **Expected** and **Must not**. Any "must not" item is a failure.

Record the outcome however suits you; the scenarios themselves carry no results.

## Scenarios

| File | Checks |
|---|---|
| [`first-adoption.md`](first-adoption.md) | Adopting a project without AIR from the repository URL |
| [`skill-not-installable.md`](skill-not-installable.md) | Adoption completes when the Skill can't be installed |
| [`second-tool-joins.md`](second-tool-joins.md) | A second tool adds only its own integration; repeating changes nothing |
| [`ambiguous-request.md`](ambiguous-request.md) | Discovery asks instead of guessing |
| [`plumbing-not-feature.md`](plumbing-not-feature.md) | An optional parameter doesn't touch `features/` |
| [`deployment-event.md`](deployment-event.md) | Operational events don't become dated Blueprint entries |
| [`legacy-context-doc.md`](legacy-context-doc.md) | A legacy knowledge file doesn't stay live beside the Blueprint |
| [`task-lifecycle.md`](task-lifecycle.md) | Start commit, owner review, closing commit; no overwrite |
