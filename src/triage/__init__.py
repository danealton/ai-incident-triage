"""AI Incident & Bug Triage service."""


def main() -> None:
    import uvicorn

    uvicorn.run("triage.main:app", host="127.0.0.1", port=8000)
