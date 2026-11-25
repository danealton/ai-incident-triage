import uuid

from triage.models import Incident, IncidentIn


class IncidentStore:
    """In-memory хранилище инцидентов. БД подключим позже по программе курса."""

    def __init__(self) -> None:
        self._items: dict[str, Incident] = {}

    def add(self, data: IncidentIn) -> Incident:
        incident = Incident(id=uuid.uuid4().hex, **data.model_dump())
        self._items[incident.id] = incident
        return incident

    def list(self) -> list[Incident]:
        return list(self._items.values())

    def get(self, incident_id: str) -> Incident | None:
        return self._items.get(incident_id)
