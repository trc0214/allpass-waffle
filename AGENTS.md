# Repository Agent Guidelines

## Canonical source
This GitHub repository is the canonical source for implementation code and Git history. Do not maintain a second editable source tree in cloud storage.

## Branching
- Base branch: `main`.
- Do not develop directly on `main`.
- Use one short-lived branch per task.
- Preferred AI branch format: `ai/<agent>/<task>`.
- Keep pull requests single-purpose and avoid unrelated refactors.

## Environment and secrets
- Never commit `.env`, API keys, tokens, credentials, virtual environments, caches, or local debug output.
- Keep `.env.example` synchronized with required configuration, using placeholders only.

## Setup
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Verification
Run the most relevant available checks for the files changed. If tests exist for touched behavior, run them before merge. Report commands and results in the pull request. If a check cannot be run, record the reason.

## Repository hygiene
- Keep `README.md`, `.gitignore`, dependency manifests, and `.env.example` accurate.
- Tests are source code and should be tracked.
- Do not commit `__pycache__/`, `*.pyc`, `.pytest_cache/`, virtual environments, generated logs, or disposable build artifacts.
- Generated or synchronized artifacts must identify their source and must not become a second editable source of truth.

## Commits
Use Conventional Commits where practical: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`, `build`.

For AI-led checkpoints, include useful metadata when appropriate:
```text
AI-Agent: <agent/model>
Issue: #<number> | N/A
Work-State: In-Progress | Checkpoint | Resolved
Problem: <goal or problem>
Verification: <tests/lint/build or Not run + reason>
```

Commit meaningful checkpoints rather than every trivial edit.

## Issues and pull requests
- An issue represents the problem or goal; a pull request represents the implementation.
- Do not use GitHub closing keywords until acceptance criteria are actually satisfied and the issue should close when merged.
- PR descriptions should state scope, important decisions, verification, risks/limitations, and remaining work.

## Handoff
When another AI or developer continues the task, provide: Goal, Current Branch, Completed, Remaining, Files Changed, Verification, Known Issues/Risks, and Recommended Next Step.
