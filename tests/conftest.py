from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

from app.api.dependencies.db import get_db
from app.infrastructure.db.session import engine
from app.main import app


@pytest.fixture()
def db():
    connection = engine.connect()
    transaction = connection.begin()

    Session = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=connection,
    )

    session = Session()

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
    email = f"test-{uuid4()}@test.com"
    password = "password123"

    client.post("/auth/register", json={"email": email, "password": password})

    login_response = client.post(
        "/auth/login", json={"email": email, "password": password}
    )

    token = login_response.json()["access_token"]

    return token
