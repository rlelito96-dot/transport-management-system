from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.enums.order_status import OrderStatus
from app.infrastructure.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    pickup_address: Mapped[str] = mapped_column(String(255))
    delivery_address: Mapped[str] = mapped_column(String(255))
    cargo_description: Mapped[str] = mapped_column(String(500))

    status: Mapped[OrderStatus] = mapped_column(
        String(50),
        default=OrderStatus.PENDING.value,
    )

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"))
    driver_id: Mapped[int | None] = mapped_column(
        ForeignKey("drivers.id"), nullable=True
    )
    vehicle_id: Mapped[int | None] = mapped_column(
        ForeignKey("vehicles.id"), nullable=True
    )

    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"))

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    company = relationship("Company", back_populates="orders")
    driver = relationship("Driver", back_populates="orders")
    vehicle = relationship("Vehicle", back_populates="orders")
