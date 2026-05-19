from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.base import Base


class Driver(Base):
    __tablename__ = "drivers"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(255))
    license_number: Mapped[str] = mapped_column(String(100), unique=True)

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"))

    company = relationship("Company", back_populates="drivers")
    orders = relationship("Order", back_populates="driver")
