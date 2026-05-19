from enum import Enum


class VehicleStatus(str, Enum):
    ACTIVE = "ACTIVE"
    IN_SERVICE = "IN_SERVICE"
    BROKEN = "BROKEN"
    RETIRED = "RETIRED"
