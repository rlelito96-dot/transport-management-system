from app.domain.enums.roles import Role
from app.domain.models.company import Company
from app.domain.models.order import Order
from app.domain.models.user import User
from app.infrastructure.repositories.order_repo import (
    OrderRepository,
)


def test_create_order(db):
    repo = OrderRepository(db)

    company = Company(
        name="Test",
        address="X",
    )

    user = User(
        email="test@test.com",
        hashed_password="x",
        role=Role.CLIENT,
    )

    db.add_all([company, user])
    db.flush()
    db.refresh(company)
    db.refresh(user)

    order = repo.create(
        pickup_address="Warsaw",
        delivery_address="Berlin",
        cargo_description="Electronics",
        company_id=company.id,
        created_by=user.id,
    )

    assert isinstance(order, Order)
    assert order.id is not None
    assert order.delivery_address == "Berlin"
