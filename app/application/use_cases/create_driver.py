from app.application.dto.driver_dto import DriverDTO
from app.infrastructure_repositories.driver_repo import DriverRepository


class CreateDriverUseCase:
    def __init__(self, repo: DriverRepository):
        self.repo = repo

    def execute(self, dto: DriverDTO):
        return self.repo.create(
            name=dto.name,
            license_number=dto.license_number,
            company_id=dto.company_id,
        )
