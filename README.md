# AI Incident & Bug Triage

Сквозной проект курса **Edge of Tomorrow** (трек 1 — SaaS Backend), недели 1–5.
Ментор — [@larchanka](https://github.com/larchanka). Ревью идёт по спецификациям, код не показываем.

Сервис принимает багрепорты/алерты, сопоставляет их с логами, документацией
и кодовой базой и предлагает первичное решение, теги и ответственного инженера.
На неделе 1 — каркас: HTTP API, структуры данных, in-memory хранилище,
правиловые эвристики триажа. LLM и RAG подключаются на неделях 3–4.

## Требования

- Python 3.15+, [uv](https://docs.astral.sh/uv/)
- `make`

## Быстрый старт

```bash
uv sync                 # зависимости + .venv
cp .env.example .env    # конфиг
make check              # ruff + mypy + pytest — должно быть зелёным
make dev                # uvicorn --reload на :8000
```

## API

| Метод | Путь | Описание |
| --- | --- | --- |
| GET | `/health` | healthcheck |
| POST | `/incidents` | принять репорт, вернуть результат триажа |
| GET | `/incidents` | список инцидентов |
| GET | `/incidents/{id}` | инцидент по id |

Пример:

```bash
curl -X POST localhost:8000/incidents \
  -H 'content-type: application/json' \
  -d '{"title": "Login fails", "description": "401 on token refresh"}'
```

## Харнесс и процесс

- Coding-агент: **Claude Code** + `rtk` (см. `AGENTS.md`)
- Работа — **только через Pull Request**, прямых пушей в `main` нет
- Проверочная команда: `make check`
