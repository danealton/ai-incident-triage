.PHONY: install check lint typecheck test dev

install:
	uv sync

lint:
	uv run ruff check src tests

typecheck:
	uv run mypy src

test:
	uv run pytest

check: lint typecheck test

dev:
	uv run uvicorn triage.main:app --reload
