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




