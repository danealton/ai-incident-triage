from triage.models import Incident, TriageResult

# Эвристики-заглушки до недели 3 (LLM + RAG): тег -> (ключевые слова, ответственный)
RULES: dict[str, tuple[list[str], str]] = {
    "auth": (["login", "auth", "token", "401", "403"], "oncall-auth"),
    "database": (["sql", "deadlock", "timeout", "postgres", "db"], "oncall-db"),
    "api": (["500", "endpoint", "http", "rest"], "oncall-api"),
}


def triage(incident: Incident) -> TriageResult:
    text = f"{incident.title} {incident.description}".lower()
    tags = [tag for tag, (keys, _) in RULES.items() if any(k in text for k in keys)]
    assignee = next(
        (owner for tag in tags for _, owner in [RULES[tag]] if owner), None
    )
    return TriageResult(
        incident_id=incident.id,
        tags=tags or ["untriaged"],
        assignee=assignee,
        suggested_fix=f"Check recent deploys and logs related to: {', '.join(tags or ['untriaged'])}",
        confidence=0.7 if assignee else 0.2,
    )
