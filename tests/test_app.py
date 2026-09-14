from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    activities_after_signup = client.get("/activities").json()
    unregister_response = client.delete(f"/activities/{activity_name}/signup?email={email}")
    updated_activities = client.get("/activities").json()

    # Assert
    assert signup_response.status_code == 200
    assert email in activities_after_signup[activity_name]["participants"]
    assert unregister_response.status_code == 200
    assert email not in updated_activities[activity_name]["participants"]
