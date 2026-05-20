from pydantic import BaseModel, Field


class OrderDTO(BaseModel):
    pickup_address: str = Field(min_length=5)
    delivery_address: str = Field(min_length=5)
    cargo_description: str = Field(min_length=3)

    company_id: int


class OrderResponseDTO(BaseModel):
    id: int

    pickup_address: str
    delivery_address: str
    cargo_description: str

    status: str

    company_id: int

    class Config:
        from_attributes = True
