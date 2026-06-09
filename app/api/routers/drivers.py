from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies.db import get_db
from app.application.dto.driver_dto import (
    DriverDTO,
    DriverResponseDTO,
)
from app.application.use_cases.create_driver import (
    CreateDriverUseCase,
)
from app.infrastructure.repositories.driver_repo import (
    DriverRepository,
)

router = APIRouter(
    prefix="/drivers",
    tags=["drivers"],
)


@router.post("", response_model=DriverResponseDTO)
def create_driver(dto: DriverDTO, db: Session = Depends(get_db)):
    use_case = CreateDriverUseCase(DriverRepository(db))

    return use_case.execute(dto)
