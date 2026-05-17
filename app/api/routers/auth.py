from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies.db import get_db
from app.application.dto.user_dto import (
    UserCreateDTO,
    UserLoginDTO,
    UserResponseDTO,
)
from app.application.use_cases.auth import LoginUserUseCase, RegisterUserUseCase
from app.infrastructure.repositories.user_repo import UserRepository

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponseDTO)
def register_user(
    user_data: UserCreateDTO,
    db: Session = Depends(get_db),
):
    repo = UserRepository(db)
    use_case = RegisterUserUseCase(repo)

    try:
        user = use_case.execute(
            email=user_data.email,
            password=user_data.password,
        )

        return user

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error


@router.post("/login")
def login_user(
    user_data: UserLoginDTO,
    db: Session = Depends(get_db),
):
    repo = UserRepository(db)
    use_case = LoginUserUseCase(repo)

    try:
        user = use_case.execute(
            email=user_data.email,
            password=user_data.password,
        )

        return user

    except ValueError as error:
        raise HTTPException(
            status_code=401,
            detail=str(error),
        ) from error
