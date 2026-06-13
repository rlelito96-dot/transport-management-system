import logging

from app.core.logging import configure_logging
from app.domain.enums.order_status import OrderStatus
from app.domain.enums.roles import Role
from app.infrastructure.db.session import SessionLocal
from app.infrastructure.repositories.company_repo import CompanyRepository
from app.infrastructure.repositories.driver_repo import DriverRepository
from app.infrastructure.repositories.order_repo import OrderRepository
from app.infrastructure.repositories.user_repo import UserRepository
from app.infrastructure.repositories.vehicle_repo import VehicleRepository

logger = logging.getLogger(__name__)


def run():
    db = SessionLocal()

    company_repo = CompanyRepository(db)
    user_repo = UserRepository(db)
    driver_repo = DriverRepository(db)
    vehicle_repo = VehicleRepository(db)
    order_repo = OrderRepository(db)

    # COMPANY
    company = company_repo.get_by_name("Test Company")

    if not company:
        company = company_repo.create(
            name="Test Company",
            address="Warsaw, Poland",
        )
        logger.info("Company created")
    else:
        logger.info("Company already exists")

    # USER
    user = user_repo.get_by_email("client@test.com")
    if not user:
        user = user_repo.create(
            email="client@test.com",
            hashed_password="hash",
            role=Role.CLIENT,
        )

        # DRIVER
        driver_repo.create(
            name="John",
            license_number="ACB123",
            company_id=company.id,
        )

        # VEHICLE
        vehicle_repo.create(
            plate_number="XYZ123",
            capacity_kg=1200,
            company_id=company.id,
        )

        # ORDER
        order_repo.create(
            pickup_address="Warsaw",
            delivery_address="Berlin",
            cargo_description="Electronics",
            company_id=company.id,
            created_by=user.id,
            status=OrderStatus.PENDING,
        )

    logger.info("Seed data created")


if __name__ == "__main__":
    configure_logging()
    run()
