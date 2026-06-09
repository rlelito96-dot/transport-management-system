from sqlalchemy.orm import Session

from app.domain.models.vehicle import Vehicle


class VehicleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, vehicle_id: int):
        return self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

    def create(self, plate_number: str, capacity_kg: int, company_id: int):
        vehicle = Vehicle(
            plate_number=plate_number,
            capacity_kg=capacity_kg,
            company_id=company_id,
        )

        self.db.add(vehicle)
        self.db.commit()
        self.db.refresh(vehicle)

        return vehicle
