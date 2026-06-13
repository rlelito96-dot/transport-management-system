import logging

from app.core.logging import configure_logging
from app.domain.enums.roles import Role
from app.infrastructure.db.session import SessionLocal
from app.infrastructure.repositories.user_repo import UserRepository

logger = logging.getLogger(__name__)


def run():
    db = SessionLocal()
    repo = UserRepository(db)

    existing = repo.get_by_email("admin@test.com")
    if existing:
        logger.info("Admin already exists")
        return

    repo.create(
        email="admin@test.com",
        hashed_password="hashed_password",
        role=Role.ADMIN,
    )

    logger.info("Admin created")


if __name__ == "__main__":
    configure_logging()
    run()
