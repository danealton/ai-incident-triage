from enum import StrEnum

from pydantic import BaseModel, Field


class Severity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class IncidentIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1)
    source: str = "manual"
    severity: Severity = Severity.MEDIUM


class Incident(IncidentIn):
    id: str


class TriageResult(BaseModel):
    incident_id: str
    tags: list[str]
    assignee: str | None
    suggested_fix: str
    confidence: float = Field(ge=0, le=1)
