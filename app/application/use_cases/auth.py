from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.infrastructure.repositories.user_repo import UserRepository


class RegisterUserUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, email: str, password: str):
        existing_user = self.repo.get_by_email(email)

        if existing_user:
            raise ValueError("User already exists")

        hashed_password = hash_password(password)

        user = self.repo.create(
            email=email,
            hashed_password=hashed_password,
            role="CLIENT",
        )

        return user


class LoginUserUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, email: str, password: str):
        user = self.repo.get_by_email(email)

        if not user:
            raise ValueError("Invalid credentials")

        if not verify_password(password, user.hashed_password):
            raise ValueError("Invalid credentials")

        access_token = create_access_token(data={"sub": str(user.id)})

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }
