from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependencies.auth import get_current_user
from app.api.dependencies.db import get_db
from app.application.dto.order_dto import (
    OrderDTO,
    OrderResponseDTO,
)
from app.application.use_cases.assign_order import AssignOrderUseCase
from app.application.use_cases.create_order import (
    CreateOrderUseCase,
)
from app.application.use_cases.update_order_status import (
    UpdateOrderStatusUseCase,
)
from app.domain.enums.order_status import OrderStatus
from app.domain.services.assignment_service import AssignmentService
from app.infrastructure.repositories.driver_repo import (
    DriverRepository,
)
from app.infrastructure.repositories.order_repo import (
    OrderRepository,
)
from app.infrastructure.repositories.vehicle_repo import (
    VehicleRepository,
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


@router.post("/{order_id}/assign")
def assign_order(
    order_id: int,
    driver_id: int,
    vehicle_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    use_case = AssignOrderUseCase(
        OrderRepository(db),
        DriverRepository(db),
        VehicleRepository(db),
        AssignmentService(),
    )

    return use_case.execute(order_id, driver_id, vehicle_id)


@router.post("/{order_id}/start")
def start_delivery(
    order_id: int,
    db: Session = Depends(get_db),
):
    use_case = UpdateOrderStatusUseCase(OrderRepository(db))

    return use_case.execute(
        order_id,
        OrderStatus.IN_TRANSIT,
    )


@router.post("/{order_id}/complete")
def complete_delivery(
    order_id: int,
    db: Session = Depends(get_db),
):
    use_case = UpdateOrderStatusUseCase(OrderRepository(db))

    return use_case.execute(
        order_id,
        OrderStatus.DELIVERED,
    )
