from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies.db import get_db
from app.application.dto.tracking_dto import TrackingDTO
from app.application.use_cases.create_tracking import CreateTrackingUseCase
from app.infrastructure.repositories.order_repo import OrderRepository
from app.infrastructure.repositories.tracking_repo import TrackingRepository

router = APIRouter(prefix="/tracking", tags=["tracking"])


@router.post("")
def create_tracking(dto: TrackingDTO, db: Session = Depends(get_db)):
    use_case = CreateTrackingUseCase(
        TrackingRepository(db),
        OrderRepository(db),
    )

    return use_case.execute(
        dto.order_id,
        dto.latitude,
        dto.longitude,
    )
