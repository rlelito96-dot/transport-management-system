from app.domain.enums.order_status import OrderStatus


class CreateTrackingUseCase:
    def __init__(self, tracking_repo, order_repo):
        self.tracking_repo = tracking_repo
        self.order_repo = order_repo

    def execute(self, order_id: int, latitude: float, longitude: float):
        order = self.order_repo.get_by_id(order_id)

        if order is None:
            raise ValueError("Order not found")

        if order.status != OrderStatus.IN_TRANSIT:
            raise ValueError("Order is not in transit")

        return self.tracking_repo.create(
            order_id,
            latitude,
            longitude,
        )
