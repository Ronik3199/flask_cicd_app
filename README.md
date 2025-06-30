# Flask CI/CD Monitoring App

## Team Members

* Adi Matok - 212917926
* Shay Shalev - 211783519
* Roni Lubashevski - 318917556
* Mor Moshe - 323915363

## GitHub Repository

[https://github.com/100adim/flask\_cicd\_app](https://github.com/100adim/flask_cicd_app)

## CI Badge

[![CI Pipeline](https://github.com/100adim/flask_cicd_app/actions/workflows/ci.yml/badge.svg)](https://github.com/100adim/flask_cicd_app/actions/workflows/ci.yml)

---

## Project Overview

This project implements a complete CI/CD pipeline for a Python Flask application. The pipeline includes lint checks, unit tests, Docker image building, and deployment. Monitoring is done using Prometheus and Grafana. All components are containerized and orchestrated via Docker Compose.

---

## Architecture Overview

The system architecture includes the following components:

* **Flask App**: A backend web service exposing metrics and endpoints
* **Prometheus**: Collects metrics from Flask, Node Exporter, and Grafana
* **Grafana**: Visualizes Prometheus metrics via dashboards
* **Node Exporter**: Provides system-level metrics
* **Docker & Docker Compose**: Used for containerizing and orchestrating the environment
* **GitHub Actions**: Manages CI/CD pipelines for testing and deployment

---

## API Endpoints

The Flask app includes:

* `/` – Home route
* `/status` – Health check endpoint
* `/metrics` – Exposes Prometheus metrics
* `/cicd-test` – Used for live CI/CD demonstration (initially commented out)

---

## CI/CD Workflow

### CI - On Pull Request:

* Lint using `flake8`
* Unit testing with `pytest` (via `test_app.py`)
* Docker image build test

### CD - On Push to `main`:

* Docker image is built and pushed to Docker Hub
* Deployment to host service (e.g. Render)

---

## Branch Protection Rules

The following rules are applied to the `main` branch:

* Pull request required before merging
* One required approval
* Dismiss stale approvals on new commits
* Require approval of most recent commit
* Require status checks (CI workflow) to pass
* Require branch to be up to date
* Require conversation resolution
* Prevent force pushes

---

## Monitoring & Observability

Prometheus scrapes metrics from Flask and Node Exporter. Grafana displays metrics on custom dashboards.

Grafana Access:

* URL: [http://localhost:3000](http://localhost:3000)
* Username: `admin`
* Password: `admin`

To import dashboards:

1. Open Grafana
2. Click "+" -> "Import"
3. Upload JSON from repository folder `grafana_dashboards`
4. Select Prometheus as data source and click Import

---

## Docker Setup

To run the full environment:

```bash
docker-compose up --build
```

Service URLs:

* Flask App: [http://localhost:5000](http://localhost:5000)
* Prometheus: [http://localhost:9090](http://localhost:9090)
* Grafana: [http://localhost:3000](http://localhost:3000)
* Node Exporter: [http://localhost:9100](http://localhost:9100)

---

## Grafana Dashboard JSON Files

Dashboard JSON files are located in the repository folder:

```text
grafana_dashboards/
├── flask_monitoring.json
└── node_exporter_metrics.json
```

These can be imported manually through Grafana's import screen.

---

## Screenshots

### GitHub Actions Workflow

![Workflow Screenshot](https://raw.githubusercontent.com/100adim/flask_cicd_app/main/screenshots/workflow_screenshot.png)

### Grafana Dashboard

![Grafana Screenshot](https://raw.githubusercontent.com/100adim/flask_cicd_app/main/screenshots/grafana_screenshots.png)

---

## Setup Instructions

1. Clone the repository
2. Make sure Docker & Docker Compose are installed
3. Run: `docker-compose up --build`
4. Access services via the URLs above

---

## Live Demo Instructions

* Uncomment the `/cicd-test` endpoint in `app.py`
* Commit and push the change to GitHub
* Show GitHub Actions being triggered
* Access `http://localhost:5000/cicd-test` to verify deployment
* Show metrics updating in Grafana

---

## Deliverables Summary

* GitHub repo with all code, configs, dashboards, and workflows
* `README.md` with explanations, screenshots, and CI badge
* Unit tests located in `test_app.py`
* Word document with team member details and repo link
* Live CI/CD demo as described in the instructions
