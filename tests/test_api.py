from fastapi.testclient import TestClient

from triage.main import app

client = TestClient(app)


def test_health() -> None:
    assert client.get("/health").json() == {"status": "ok"}


def test_create_incident_returns_triage() -> None:
    resp = client.post(
        "/incidents",
        json={"title": "Login fails", "description": "401 on token refresh"},
    )
    assert resp.status_code == 201
    body = resp.json()
    assert "auth" in body["tags"]
    assert body["assignee"] == "oncall-auth"
    assert body["incident_id"]


def test_list_and_get_incident() -> None:
    created = client.post(
        "/incidents", json={"title": "DB timeout", "description": "deadlock in postgres"}
    ).json()
    assert any(i["id"] == created["incident_id"] for i in client.get("/incidents").json())
    assert client.get(f"/incidents/{created['incident_id']}").status_code == 200


def test_get_unknown_incident_404() -> None:
    assert client.get("/incidents/nope").status_code == 404


def test_create_incident_validation_error() -> None:
    assert client.post("/incidents", json={"title": ""}).status_code == 422
