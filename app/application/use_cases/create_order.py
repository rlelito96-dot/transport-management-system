from app.application.dto.order_dto import (
    OrderCreateDTO,
)
from app.infrastructure.repositories.order_repo import (
    OrderRepository,
)


class CreateOrderUseCase:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    def execute(
        self,
        dto: OrderCreateDTO,
        created_by: int,
    ):
        return self.order_repo.create(
            pickup_address=dto.pickup_address,
            delivery_address=dto.delivery_address,
            cargo_description=dto.cargo_description,
            company_id=dto.company_id,
            created_by=created_by,
        )
