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
Commits record repository history; Issues and pull requests record lifecycle state, verification, and handoff context. Do not add custom work-state metadata to commit messages.

## Issues and pull requests
- An issue represents the problem or goal; a pull request represents the implementation.
- Standard Bug/Implementation Issue Forms require `Drafted By` for the actual human or AI agent/model that produced the initial Issue content. Preserve it as immutable provenance; do not overwrite it during handoff, revision, or implementation.
- If an Issue is created through Blank issue, GitHub CLI, API, or automation without the standard Issue Form, put `Drafted By: <human-or-agent/model>` at the top of the Issue body before creation. Do not create an Issue without initial attribution.
- If another AI materially changes Issue-defining content such as scope, acceptance criteria, reproduction, impact, or dependencies, add one concise Issue comment beginning with `AI-Contributor: <agent/model>` and `Role: Planning`, `Role: Revision`, or `Role: Synthesis`. Routine wording edits do not require attribution.
- GitHub account identity records the operator account and must not be used to infer the actual AI contributor when explicit attribution exists.
- Do not use GitHub closing keywords until acceptance criteria are actually satisfied and the issue should close when merged.
- PR descriptions should state scope, important decisions, verification, risks/limitations, and remaining work.

## Handoff
When another AI or developer continues the task, provide: Goal, Current Branch, Completed, Remaining, Files Changed, Verification, Known Issues/Risks, and Recommended Next Step.
