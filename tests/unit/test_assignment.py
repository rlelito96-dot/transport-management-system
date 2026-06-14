import pytest

from app.domain.enums.order_status import OrderStatus
from app.domain.enums.vehicle_status import VehicleStatus
from app.domain.services.assignment_service import AssignmentService


def test_can_assign_success(order, driver, vehicle):
    service = AssignmentService()

    result = service.can_assign(order, driver, vehicle)

    assert result is True


def test_cannot_assign_if_order_not_pending(order, driver, vehicle):
    service = AssignmentService()

    order.status = OrderStatus.ASSIGNED

    with pytest.raises(ValueError, match="Order already assigned"):
        service.can_assign(order, driver, vehicle)


def test_cannot_assign_if_driver_missing(order, vehicle):
    service = AssignmentService()

    with pytest.raises(ValueError, match="Driver not found"):
        service.can_assign(order, None, vehicle)


def test_cannot_assign_if_vehicle_missing(order, driver):
    service = AssignmentService()

    with pytest.raises(ValueError, match="Vehicle not found"):
        service.can_assign(order, driver, None)


def test_cannot_assign_if_vehicle_not_available(order, driver, vehicle):
    service = AssignmentService()

    vehicle.status = VehicleStatus.IN_SERVICE

    with pytest.raises(ValueError, match="Vehicle not available"):
        service.can_assign(order, driver, vehicle)
