import pytest

from app.infrastructure.db.session import SessionLocal, engine


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
