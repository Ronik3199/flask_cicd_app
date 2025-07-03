<<<<<<< HEAD
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
=======
# Flask CI/CD Monitoring App 

## Project Overview

In this project, we built a complete CI/CD process for a Python Flask application. The process includes lint checks, unit tests, Docker image build, pushing the image to Docker Hub, and deploying to a Render environment. We also added monitoring using Prometheus and Grafana to view metrics from the app and the system.

## Architecture Overview

The app includes a Flask service with several endpoints. The CI file runs via GitHub Actions on every Pull Request and performs style checks and unit tests. After that, a Docker image is built and pushed to Docker Hub. Using Docker Compose, we run a local environment with Flask, Prometheus, Grafana, and node-exporter.

## API Endpoints

The application includes the following routes:
- `/hello` returns a welcome message
- `/metrics` shows Prometheus metrics
- `/cicd-test` – this endpoint is commented out and used for demonstrating CI/CD during the presentation

## CI/CD Workflow

When a Pull Request is opened, GitHub Actions runs:
- Style checks (flake8)
- Unit tests from the file `test_app.py`
- Docker image build

When code is pushed to the `main` branch:
- Docker image is built
- Pushed to Docker Hub
- The project is deployed via Render (or optionally with Docker Compose)

## Monitoring & Observability

Prometheus scrapes metrics from the Flask service and from node-exporter.  
Grafana is configured with a dashboard imported from a JSON file. You can access Grafana at `http://localhost:3000` with user `admin` and password `admin`, and import the dashboard from the JSON file.

## Docker & Compose

To run everything locally, all services are defined in the docker-compose file.  
Use the following command to run the system: docker-compose up --build


The following services will be launched:
- Flask on port 5000
- Prometheus on port 9090
- Grafana on port 3000
- Node Exporter on port 9100

## Docker Hub

The Docker image is pushed to Docker Hub at:  
https://hub.docker.com/r/mormoshe7/flask-cicd-app

## Deployment

The application was deployed to Render and is available at:  
https://flask-cicd-app-6gzn.onrender.com

## Setup Instructions

To run the system:
1. Clone the repo
2. Make sure all dependencies are installed
3. Run `docker-compose`
4. Access the services in the browser:
   - Flask: http://localhost:5000  
   - Prometheus: http://localhost:9090  
   - Grafana: http://localhost:3000

## Team Info

Adi Matok – 212917926  
Shay Shalev – 211783519  
Roni Lubashevski – 318917556  
Mor Moshe – 323915363

GitHub Repo:  
https://github.com/Ronik3199/flask_cicd_app




>>>>>>> 7d693a82924c567a74d8690d228ccbdc44a8f313
