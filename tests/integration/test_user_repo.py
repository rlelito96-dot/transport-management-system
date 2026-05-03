from app.infrastructure.repositories.user_repo import UserRepository


def test_create_user(db):
    repo = UserRepository(db)

    user = repo.create(email="test@test.com", hashed_password="hashed", role="CLIENT")

    assert user.id is not None
    assert user.email == "test@test.com"


def test_db_is_clean(db):
    repo = UserRepository(db)

    user = repo.get_by_email("test@test.com")

    assert user is None
