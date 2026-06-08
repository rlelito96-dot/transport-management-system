from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.base import Base


class Tracking(Base):
    __tablename__ = "tracking"

    id: Mapped[int] = mapped_column(primary_key=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))

    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)

    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", back_populates="tracking")
