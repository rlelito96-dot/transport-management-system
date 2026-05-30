from sqlalchemy.orm import Session

from app.domain.models.vehicle import Vehicle


class VehicleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, vehicle_id: int):
        return self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
