from app.core.security import hash_password
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
