from fastapi import FastAPI, HTTPException

from triage.config import settings
from triage.models import Incident, IncidentIn, TriageResult
from triage.service import triage
from triage.store import IncidentStore

app = FastAPI(title=settings.app_name, version="0.1.0")
store = IncidentStore()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/incidents", status_code=201)
def create_incident(payload: IncidentIn) -> TriageResult:
    return triage(store.add(payload))


@app.get("/incidents")
def list_incidents() -> list[Incident]:
    return store.list()


@app.get("/incidents/{incident_id}")
def get_incident(incident_id: str) -> Incident:
    incident = store.get(incident_id)
    if incident is None:
        raise HTTPException(status_code=404, detail="incident not found")
    return incident
