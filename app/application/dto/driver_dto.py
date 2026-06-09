from pydantic import BaseModel


class DriverDTO(BaseModel):
    name: str
    license_number: str
    company_id: int


class DriverResponseDTO(BaseModel):
    id: int
    name: str
    license_number: str
    company_id: int

    class Config:
        from_attributes = True
