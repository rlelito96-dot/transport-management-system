# 🚚 Transport Management System (TMS) – Backend API

A backend system for managing transport operations including orders, drivers, vehicles, and shipment tracking.  
Built with a focus on clean architecture, testability, and real-world backend patterns.

---

## 🚀 Quick Start

```bash
cp .env.example .env
docker compose up -d
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

## 📌 Features

- User authentication (JWT-based)
- Order management (create, update status, assign)
- Driver management
- Vehicle management
- Order assignment system (driver + vehicle)
- Shipment tracking system
- Order lifecycle management (PENDING → ASSIGNED → IN_TRANSIT → DELIVERED)
- Unit and integration tests
- Dockerized development environment
- CI/CD pipeline with GitHub Actions

---

## 🧱 Tech Stack

- Python 3.11+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pytest
- Docker & Docker Compose

---

## 🏗 Architecture

The project follows Clean Architecture principles:

- **API Layer** – FastAPI routers
- **Application Layer** – Use Cases (business logic)
- **Domain Layer** – Entities and enums
- **Infrastructure Layer** – Database, repositories

Business logic is implemented in use cases, keeping controllers thin and ensuring separation of concerns and testability.

---

## 🚀 Full Setup

### 1. Clone repository

```bash
git clone https://github.com/your-username/transport-management-system.git
cd tms
```

### 2. Create environment file

```bash
cp .env.example .env
```

### 3. Start database (Docker)

```bash
docker compose up -d
```
### 4. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / WSL
venv/Scripts/activate   # Windows
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run migrations

```bash
alembic upgrade head
```
### 7. Start application

```bash
uvicorn app.main:app --reload
```

##  📖 API Documentation

- **API**: http://localhost:8000
- **Swagger docs**: http://localhost:8000/docs

## 🧪 Running Tests

Run tests locally:

```bash
pytest -v
```

The project contains both unit and integration tests.

## 🔮 Future Improvements

- Async tracking system (Redis + background workers)
- Event-driven architecture
- Caching layer for frequently accessed data
- Role-based access control improvements
