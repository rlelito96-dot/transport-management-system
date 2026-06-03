from app.domain.enums.order_status import OrderStatus
from app.domain.enums.vehicle_status import VehicleStatus


class AssignmentService:
    def can_assign(self, order, driver, vehicle):
        if order.status != OrderStatus.PENDING:
            raise ValueError("Order already assigned")

        if driver is None:
            raise ValueError("Driver not found")

        if vehicle is None:
            raise ValueError("Vehicle not found")

        if vehicle.status != VehicleStatus.ACTIVE:
            raise ValueError("Vehicle not available")

        return True
