from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_from_activity():
    activity = "Chess Club"
    participant = "michael@mergington.edu"

    response = client.delete(
        f"/activities/{activity}/participants/{participant}"
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": f"Unregistered {participant} from {activity}"
    }
    assert participant not in client.get("/activities").json()[activity]["participants"]


def test_unregister_missing_participant_returns_404():
    response = client.delete(
        "/activities/Chess Club/participants/nonexistent@mergington.edu"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
