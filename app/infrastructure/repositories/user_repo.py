from sqlalchemy.orm import Session

from app.domain.enums.roles import Role
from app.domain.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, hashed_password: str, role: Role = Role.CLIENT):
        user = User(
            email=email,
            hashed_password=hashed_password,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()
