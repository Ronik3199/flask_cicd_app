# Flask CI/CD Monitoring App - our readme file

## Project Overview
In this project, we built a complete CI/CD pipeline for a Python Flask application. The pipeline includes lint checks, unit tests, Docker image building, and deployment. Monitoring is done using Prometheus and Grafana. All services are containerized using Docker and orchestrated via Docker Compose.

## Architecture Overview
The project includes the following components:
- **Flask App**: Exposes API endpoints and metrics
- **GitHub Actions**: CI pipeline for linting, testing, and Docker image builds
- **Docker Compose**: Orchestrates the local environment
- **Prometheus**: Collects metrics from Flask and node-exporter
- **Grafana**: Visualizes the metrics using a dashboard

## API Endpoints
The application exposes the following routes:
- `/` – Home route
- `/status` – Returns the system status
- `/metrics` – Prometheus metrics endpoint
- `/cicd-test` – Endpoint used for live CI/CD demo (commented out by default)

## CI/CD Workflow
### On Pull Request:
- Style checks using `flake8`
- Unit tests from `test_app.py`
- Docker image build

### On Push to Main Branch:
- Docker image is built
- Image is pushed to Docker Hub

## Monitoring & Observability
- Prometheus scrapes metrics from the Flask app and `node-exporter`
- Grafana visualizes metrics using a dashboard imported via JSON
- Access Grafana at `http://localhost:3000`, login with:
  - **Username:** `admin`
  - **Password:** `admin`

## Docker & Compose
To run the full system locally:
```bash
docker-compose up --build
```

Services launched:
- Flask: `http://localhost:5000`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`
- Node Exporter: `http://localhost:9100`

## Deployment
- The app can be deployed to cloud services like Render.
- CI/CD pipeline automates image building and deployment (optional).

## Dashboard JSON
- The Grafana dashboard JSON file is included in the repo under `grafana-dashboard.json`
- You can import it manually from Grafana or use provisioning

## Setup Instructions
1. Clone the repo
2. Ensure Docker and Docker Compose are installed
3. Run `docker-compose up --build`
4. Access services at:
   - Flask: `http://localhost:5000`
   - Prometheus: `http://localhost:9090`
   - Grafana: `http://localhost:3000`

## Team Info:
- **Adi Matok** – 212917926
- **Shay Shalev** – 211783519
- **Roni Lubashevski** – 318917556
- **Mor Moshe** – 323915363

## GitHub Repository
[https://github.com/AdiMatok/flask_cicd_app](https://github.com/AdiMatok/flask_cicd_app)
