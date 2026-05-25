from src import app as app_module


def test_get_activities_returns_expected_payload(client):
    # Arrange
    expected_activities = set(app_module.activities.keys())

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert expected_activities.issubset(set(payload.keys()))
