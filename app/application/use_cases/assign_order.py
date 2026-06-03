from app.domain.enums.order_status import OrderStatus


class AssignOrderUseCase:
    def __init__(self, order_repo, driver_repo, vehicle_repo, service):
        self.order_repo = order_repo
        self.driver_repo = driver_repo
        self.vehicle_repo = vehicle_repo
        self.service = service

    def execute(self, order_id, driver_id, vehicle_id):
        order = self.order_repo.get_by_id(order_id)

        driver = self.driver_repo.get_by_id(driver_id)

        vehicle = self.vehicle_repo.get_by_id(vehicle_id)

        self.service.can_assign(order, driver, vehicle)

        order.driver_id = driver.id
        order.vehicle_id = vehicle.id
        order.status = OrderStatus.ASSIGNED

        self.order_repo.db.commit()
        self.order_repo.db.refresh(order)

        return order
