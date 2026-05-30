from enum import Enum


class Role(str, Enum):
    ADMIN = "ADMIN"
    DISPATCHER = "DISPATCHER"
    CLIENT = "CLIENT"
