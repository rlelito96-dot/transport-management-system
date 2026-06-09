from pydantic import BaseModel


class VehicleDTO(BaseModel):
    plate_number: str
    capacity_kg: int
    company_id: int


class VehicleResponseDTO(BaseModel):
    id: int
    plate_number: str
    capacity_kg: int
    company_id: int
    status: str

    class Config:
        from_attributes = True
