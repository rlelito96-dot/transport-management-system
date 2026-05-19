from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.enums.vehicle_status import VehicleStatus
from app.infrastructure.db.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(primary_key=True)

    plate_number: Mapped[str] = mapped_column(String(50), unique=True)
    capacity_kg: Mapped[int] = mapped_column()

    status: Mapped[VehicleStatus] = mapped_column(
        String(50),
        default=VehicleStatus.ACTIVE.value,
    )

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"))

    company = relationship("Company", back_populates="vehicles")
    orders = relationship("Order", back_populates="vehicle")
