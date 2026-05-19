from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.base import Base


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(255), unique=True)
    address: Mapped[str] = mapped_column(String(255))

    vehicles = relationship("Vehicle", back_populates="company")
    drivers = relationship("Driver", back_populates="company")
    orders = relationship("Order", back_populates="company")
