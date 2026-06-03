from app.domain.enums.order_status import OrderStatus
from app.domain.enums.roles import Role
from app.domain.enums.vehicle_status import VehicleStatus
from app.domain.models.company import Company
from app.domain.models.driver import Driver
from app.domain.models.order import Order
from app.domain.models.user import User
from app.domain.models.vehicle import Vehicle


def test_create_order(client, auth_token, db):
    company = Company(name="test", address="Warsaw")

    db.add(company)
    db.flush()
    db.refresh(company)

    response = client.post(
        "/orders",
        json={
            "pickup_address": "Warsaw",
            "delivery_address": "Berlin",
            "cargo_description": "Electronics",
            "company_id": company.id,
        },
        headers={"Authorization": f"Bearer {auth_token}"},
    )

    assert response.status_code == 201
    data = response.json()
    assert data["pickup_address"] == "Warsaw"


def test_assign_order(
    client,
    auth_token,
    db,
):
    company = Company(name="test", address="Warsaw")

    db.add(company)
    db.flush()
    db.refresh(company)

    user = User(email="test@test.com", hashed_password="hash", role=Role.CLIENT)

    db.add(user)
    db.flush()
    db.refresh(user)

    driver = Driver(name="X", license_number="abc123", company_id=company.id)

    vehicle = Vehicle(
        plate_number="456",
        capacity_kg=240,
        status=VehicleStatus.ACTIVE,
        company_id=company.id,
    )

    order = Order(
        pickup_address="Warsaw",
        delivery_address="Berlin",
        cargo_description="X",
        status=OrderStatus.PENDING,
        company_id=company.id,
        created_by=user.id,
    )

    db.add_all([driver, vehicle, order])
    db.flush()
    db.refresh(driver)
    db.refresh(vehicle)
    db.refresh(order)

    response = client.post(
        f"/orders/{order.id}/assign",
        params={
            "driver_id": driver.id,
            "vehicle_id": vehicle.id,
        },
        headers={"Authorization": f"Bearer {auth_token}"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == OrderStatus.ASSIGNED
    assert data["delivery_address"] == "Berlin"
    assert data["cargo_description"] == "X"
    assert data["company_id"] == company.id
