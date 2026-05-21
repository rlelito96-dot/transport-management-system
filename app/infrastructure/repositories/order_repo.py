from sqlalchemy.orm import Session

from app.domain.models.order import Order


class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        pickup_address: str,
        delivery_address: str,
        cargo_description: str,
        company_id: int,
        created_by: int,
    ):
        order = Order(
            pickup_address=pickup_address,
            delivery_address=delivery_address,
            cargo_description=cargo_description,
            company_id=company_id,
            created_by=created_by,
        )

        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)

        return order

    def get_all(self):
        return self.db.query(Order).all()

    def get_by_id(self, order_id: int):
        return self.db.query(Order).filter(Order.id == order_id).first()
