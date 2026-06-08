from app.domain.enums.order_status import OrderStatus
from app.domain.enums.roles import Role
from app.domain.models.company import Company
from app.domain.models.order import Order
from app.domain.models.user import User


def test_create_tracking(client, db):
    company = Company(
        name="test",
        address="Warsaw",
    )

    db.add(company)
    db.flush()
    db.refresh(company)

    user = User(email="test@test.com", hashed_password="hash", role=Role.CLIENT)

    db.add(user)
    db.flush()
    db.refresh(user)

    order = Order(
        pickup_address="A",
        delivery_address="B",
        cargo_description="test",
        company_id=company.id,
        status=OrderStatus.IN_TRANSIT,
        created_by=user.id,
    )

    db.add(order)
    db.flush()
    db.refresh(order)

    response = client.post(
        "/tracking",
        json={
            "order_id": order.id,
            "latitude": 52.23,
            "longitude": 21.01,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["order_id"] == order.id
    assert data["latitude"] == 52.23
