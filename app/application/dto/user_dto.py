from pydantic import BaseModel, EmailStr, Field


class UserCreateDTO(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)


class UserResponseDTO(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        from_attributes = True
