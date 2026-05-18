def test_register_user(client):
    response = client.post(
        "/auth/register", json={"email": "test@test.com", "password": "secret123"}
    )

    # assert False, response.json()

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == "test@test.com"
    assert "id" in data


def test_login_user(client):
    client.post(
        "/auth/register", json={"email": "test@test.com", "password": "secret123"}
    )

    response = client.post(
        "/auth/login",
        json={"email": "test@test.com", "password": "secret123"},
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_get_current_user(client):
    client.post(
        "/auth/register",
        json={
            "email": "test@test.com",
            "password": "secret123",
        },
    )

    login_response = client.post(
        "/auth/login",
        json={
            "email": "test@test.com",
            "password": "secret123",
        },
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == "test@test.com"
