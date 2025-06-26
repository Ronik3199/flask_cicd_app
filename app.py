from flask import Flask
from prometheus_client import Counter, Summary, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'request_count', 'Total number of requests', ['endpoint']
)
REQUEST_LATENCY = Summary('request_latency_seconds', 'Request latency')


@app.route("/")
@REQUEST_LATENCY.time()
def home():
    REQUEST_COUNT.labels(endpoint='/').inc()
    return "Welcome to the Flask CI/CD App!"


@app.route("/status")
@REQUEST_LATENCY.time()
def status():
    REQUEST_COUNT.labels(endpoint='/status').inc()
    return {"status": "OK"}, 200


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
