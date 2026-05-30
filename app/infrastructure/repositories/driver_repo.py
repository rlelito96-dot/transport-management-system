from sqlalchemy.orm import Session

from app.domain.models.driver import Driver


class DriverRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, driver_id: int):
        return self.db.query(Driver).filter(Driver.id == driver_id).first()

    def create(self, name: str, license_number: str, company_id: int):
        driver = Driver(name=name, license_number=license_number, company_id=company_id)
        self.db.add(driver)
        self.db.commit()
        self.db.refresh(driver)
        return driver

    def list(self):
        return self.db.query(Driver).all()

    def get_by_company(self, company_id: int):
        return self.db.query(Driver).filter(Driver.company_id == company_id).all()
