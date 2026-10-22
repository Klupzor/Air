# A deployment is not durable knowledge

**Setup:** `examples/minimal-project/` as is, committed.

**Prompt:**

> We deployed the task manager to our internal server today and it's running fine. Record that in the project docs.

**Expected:**
- The agent explains that a deployment event isn't durable project knowledge and belongs in commit history or operational tooling.
- If the deployment implies a lasting fact that changes how future work must be done (for example, a deployment target that constrains the architecture), it proposes stating that fact as current truth — without a date — and asks before writing it.

**Must not:**
- Add a dated entry, "deployed on…", "applied…", or a status log to any Blueprint or feature file.
- Create a changelog or history file.
