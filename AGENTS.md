# AGENTS.md

Instructions for AI coding agents working in this repository.

## Project

**AI Incident & Bug Triage** — FastAPI backend. Capstone project for the
Edge of Tomorrow course (5 weeks). Week 1 scope: HTTP API skeleton,
pydantic models, in-memory store, rule-based triage stub.

## Environment

- Python managed by `uv` (`uv sync`, `uv run <cmd>`). Do not use pip directly.
- Config: `.env` (copied from `.env.example`), `TRIAGE_`-prefixed vars in `src/triage/config.py`.

## Commands

- `make check` — lint + typecheck + tests. **Must pass before every commit.**
- `make lint` / `make typecheck` / `make test` / `make dev` — individual steps.
- Prefer `rtk`-wrapped commands to save tokens: `rtk pytest`, `rtk mypy`, `rtk git`, `rtk gh`.

## Behaviour rules

Adapted from the course guidelines (`GEMINI.md`):

1. **Think Before Coding** — state assumptions, ask when unclear, present tradeoffs instead of silently picking an interpretation.
2. **Simplicity First** — minimum code that solves the problem; no speculative features or abstractions.
3. **Surgical Changes** — every changed line traces to the request; match existing style.
4. **Goal-Driven Execution** — turn tasks into verifiable goals, loop until `make check` is green.

Practices:

- Use `rg`/grep for searching the project; use scripts for data/file processing.
- Batch related tool calls.
- Use sub-agents for code writing, review and planning when available.

## Git workflow

- **Work via Pull Requests only.** Never push to `main` directly:
  `git checkout -b <branch>` → commit → `gh pr create`.
- One meaningful commit per work block; commit messages in Russian.
- Never commit secrets. `.env` and `*.key`/`*.pem` are gitignored — keep it that way.

## Safety

- Destructive commands (`rm -rf`, `git push --force`, `DROP TABLE`, `git reset --hard`)
  require explicit user confirmation — the global Claude Code settings enforce an `ask` prompt.

## Memory

If `memo-mcp` is available: `search_memory` before complex/architectural tasks,
`append_memory` after milestones. Project tag: `ai-incident-triage`.
