from sqlalchemy.orm import Session

from app.domain.models.tracking import Tracking


class TrackingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, order_id: int, latitude: float, longitude: float):
        tracking = Tracking(
            order_id=order_id,
            latitude=latitude,
            longitude=longitude,
        )

        self.db.add(tracking)
        self.db.commit()
        self.db.refresh(tracking)

        return tracking

    def get_by_order(self, order_id: int):
        return self.db.query(Tracking).filter(Tracking.order_id == order_id).all()
