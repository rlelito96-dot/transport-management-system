from app.domain.models.company import Company


def test_create_order(client, auth_token, db):
    company = Company(name="test", address="Warsaw")

    db.add(company)
    db.commit()
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
