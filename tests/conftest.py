import pytest
from fastapi.testclient import TestClient

from app.api.dependencies.db import get_db
from app.infrastructure.db.session import SessionLocal, engine
from app.main import app


@pytest.fixture()
def db():
    connection = engine.connect()
    transaction = connection.begin()

    session = SessionLocal(bind=connection)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


@pytest.fixture()
def client(db):
    app.dependency_overrides[get_db] = lambda: db

    yield TestClient(app)

    app.dependency_overrides.clear()


@pytest.fixture
def auth_token(client):
    client.post(
        "/auth/register", json={"email": "test@test.com", "password": "password123"}
    )

    login_response = client.post(
        "/auth/login", json={"email": "test@test.com", "password": "password123"}
    )

    token = login_response.json()["access_token"]

    return token
