from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies.db import get_db
from app.application.dto.vehicle_dto import (
    VehicleDTO,
    VehicleResponseDTO,
)
from app.application.use_cases.create_vehicle import (
    CreateVehicleUseCase,
)
from app.infrastructure.repositories.vehicle_repo import VehicleRepository

router = APIRouter(
    prefix="/vehicles",
    tags=["vehicles"],
)


@router.post("", response_model=VehicleResponseDTO)
def create_vehicle(dto: VehicleDTO, db: Session = Depends(get_db)):
    use_case = CreateVehicleUseCase(VehicleRepository(db))

    return use_case.execute(dto)
