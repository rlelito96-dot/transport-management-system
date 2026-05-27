from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependencies.auth import get_current_user
from app.api.dependencies.db import get_db
from app.application.dto.order_dto import (
    OrderDTO,
    OrderResponseDTO,
)
from app.application.use_cases.create_order import (
    CreateOrderUseCase,
)
from app.infrastructure.repositories.order_repo import (
    OrderRepository,
)

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post(
    "",
    response_model=OrderResponseDTO,
    status_code=status.HTTP_201_CREATED,
)
def create_order(
    dto: OrderDTO,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    repo = OrderRepository(db)

    use_case = CreateOrderUseCase(repo)

    return use_case.execute(
        dto=dto,
        created_by=current_user.id,
    )
