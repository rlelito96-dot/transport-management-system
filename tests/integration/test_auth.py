def test_register_user(client):
    response = client.post(
        "/auth/register", json={"email": "test@test.com", "password": "secret123"}
    )

    # assert False, response.json()

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == "test@test.com"
    assert "id" in data
