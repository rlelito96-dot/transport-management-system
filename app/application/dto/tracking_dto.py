from pydantic import BaseModel


class TrackingDTO(BaseModel):
    order_id: int
    latitude: float
    longitude: float
