from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.models.company import Company


class CompanyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, company_id: int) -> Company | None:
        self.db.get(Company, company_id)

    def get_by_name(self, name: str) -> Company | None:
        return self.db.scalar(select(Company).where(Company.name == name))

    def create(self, name: str, address: str) -> Company:
        company = Company(
            name=name,
            address=address,
        )

        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)

        return company
