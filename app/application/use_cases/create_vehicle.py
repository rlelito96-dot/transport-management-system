from app.application.dto.vehicle_dto import VehicleDTO
from app.infrastructure.repositories.vehicle_repo import VehicleRepository


class CreateVehicleUseCase:
    def __init__(self, repo: VehicleRepository):
        self.repo = repo

    def execute(self, dto: VehicleDTO):
        return self.repo.create(
            plate_number=dto.plate_number,
            capacity_kg=dto.capacity_kg,
            company_id=dto.company_id,
        )
