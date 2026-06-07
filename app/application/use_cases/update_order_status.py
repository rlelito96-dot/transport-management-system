from app.domain.enums.order_status import OrderStatus


class UpdateOrderStatusUseCase:
    def __init__(self, order_repo):
        self.order_repo = order_repo

    def execute(self, order_id: int, new_status: OrderStatus):
        order = self.order_repo.get_by_id(order_id)

        if order is None:
            raise ValueError("Order not found")

        order.status = new_status

        self.order_repo.db.commit()
        self.order_repo.db.refresh(order)

        return order
