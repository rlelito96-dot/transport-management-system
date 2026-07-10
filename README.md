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
```

## 🌐 Production Deployment

Production environment is deployed on AWS ECS Fargate behind an Application Load Balancer.

The application is automatically deployed through GitHub Actions after changes are merged into `main`.

---

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
- Automated CI/CD pipeline with GitHub Actions and AWS ECS deployment

---

## 🧱 Tech Stack

- Python 3.11+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pytest
- Docker & Docker Compose
- AWS (ECS, ECR, RDS, ALB, CloudWatch)
- GitHub Actions CI/CD

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
cd transport-management-system
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

##  📖 API Documentation

- **API**: http://localhost:8000
- **Swagger docs**: http://localhost:8000/docs
- **Redoc**: http://localhost:8000/redoc

## 🧪 Running Tests

Run tests locally:

```bash
pytest -v
```

---

## ☁️ AWS Deployment Architecture

The application is deployed on AWS using containerized infrastructure.

```text
User
  |
  v
Application Load Balancer (ALB)
  |
  v
ECS Fargate Service
  |
  v
FastAPI Docker Container
  |
  v
RDS PostgreSQL
```

AWS services used:

- **Amazon ECS Fargate** – runs the backend container
- **Amazon ECR** – stores Docker images
- **Application Load Balancer** – routes HTTP traffic to ECS
- **Amazon RDS PostgreSQL** – managed database
- **Amazon CloudWatch** – logs and monitoring

---

## 🔄 CI/CD Pipeline

Deployment is automated with GitHub Actions.

```text
Pipeline flow:

Pull Request
    |
    v
Run tests (pytest)

Merge to main
    |
    v
Build Docker image
    |
    v
Push image to Amazon ECR
    |
    v
Update ECS service
    |
    v
New application deployment
```

The pipeline automatically deploys changes merged into the `main` branch.


## 📊 Monitoring

Implemented monitoring using Amazon CloudWatch:

- ECS container logs available through CloudWatch Logs
- Application Load Balancer metrics
- Response time alarm monitoring

Example monitored metric:

- TargetResponseTime > 2 seconds

CloudWatch alarms help detect application performance issues.

---

## 🔮 Future Improvements

- Async tracking system (Redis + background workers)
- Event-driven architecture
- Caching layer for frequently accessed data
- Role-based access control improvements
