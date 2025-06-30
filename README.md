# Flask CI/CD Monitoring App

## Team Members

* Adi Matok - 212917926
* Shay Shalev - 211783519
* Roni Lubashevski - 318917556
* Mor Moshe - 323915363

## GitHub Repository

[https://github.com/100adim/flask\_cicd\_app](https://github.com/100adim/flask_cicd_app)

---

## Project Overview

This project implements a complete CI/CD pipeline for a Python Flask application. The pipeline includes lint checks, unit tests, Docker image building, and deployment. Monitoring is done using Prometheus and Grafana. All components are containerized and orchestrated via Docker Compose.

---

## Architecture Overview

The project consists of the following components:

* **Flask App**: Provides API endpoints and exposes Prometheus metrics
* **GitHub Actions**: Handles CI pipeline for linting, testing, and Docker image builds
* **Docker Compose**: Orchestrates local multi-container setup
* **Prometheus**: Scrapes metrics from the Flask app and node-exporter
* **Grafana**: Visualizes metrics through custom dashboards
* **Node Exporter**: Exposes host-level metrics

---

## API Endpoints

The Flask application exposes the following endpoints:

* `/` - Home route
* `/status` - Returns system status
* `/metrics` - Prometheus metrics endpoint
* `/cicd-test` - Used for live CI/CD demo (initially commented out)

---

## CI/CD Workflow

### On Pull Request:

* Lint checks using `flake8`
* Unit tests using `pytest`
* Docker image build test

### On Push to Main Branch:

* Docker image is built
* Docker image is pushed to Docker Hub
* Optional deployment to cloud (e.g. Render)

---

## GitHub Branch Protection Rules

The repository is configured with branch protection rules for the `main` branch to ensure code quality and secure deployment. The following rules are enforced:

* Pull request required before merging
* At least one approval is required
* Dismiss stale pull request approvals when new commits are pushed
* Require approval of the most recent reviewable push
* Require status checks to pass (linked to CI workflow)
* Require branches to be up to date before merging
* Require conversation resolution before merging
* Prevent force pushes to the branch
* CI job added as a required status check

---

## Monitoring & Observability

* Prometheus scrapes metrics from Flask and Node Exporter
* Grafana visualizes metrics using dashboards imported via JSON

Access Grafana locally:

* URL: [http://localhost:3000](http://localhost:3000)
* Username: `admin`
* Password: `admin`

Manual dashboard import:

1. Open Grafana
2. Click "+" -> "Import"
3. Upload one of the JSON files from `grafana_dashboards/`
4. Select "Prometheus" as data source and click "Import"

---

## Docker & Docker Compose

Run the system locally with:

```bash
docker-compose up --build
```

Access services locally:

* Flask: [http://localhost:5000](http://localhost:5000)
* Prometheus: [http://localhost:9090](http://localhost:9090)
* Grafana: [http://localhost:3000](http://localhost:3000)
* Node Exporter: [http://localhost:9100](http://localhost:9100)

---

## Dashboard JSON Files

Grafana dashboards are included in:

```
grafana_dashboards/
├── flask_monitoring.json
└── node_exporter_metrics.json
```

These can be imported manually in Grafana.

---

## Screenshots

### Grafana Dashboard

![Grafana Dashboard](screenshots/grafana_dashboard.png)

### Request Count Panel

![Request Count Total](screenshots/request_count_total.png)

### GitHub Actions Workflow

![GitHub Actions](screenshots/github-actions.png)

---

## Setup Instructions

1. Clone the repository
2. Ensure Docker and Docker Compose are installed
3. Run `docker-compose up --build`
4. Access the services via the ports listed above

---

## Live CI/CD Demonstration Checklist

* Uncomment `/cicd-test` endpoint
* Commit and push change to GitHub
* Show GitHub Actions running
* Access `http://localhost:5000/cicd-test` to verify deployment
* View updated metrics in Grafana dashboard
