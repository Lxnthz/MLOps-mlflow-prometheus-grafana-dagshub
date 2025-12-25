from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, Response, request, jsonify
import time
import random
import psutil
import requests
import threading
import logging

app = Flask(__name__)

# METRICS API
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')  # Total requests
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP Request Latency')  # Latency
THROUGHPUT = Counter('http_requests_throughput', 'Total number of requests per second')  # Throughput
ERROR_COUNT = Counter('http_requests_error_total', 'Total number of failed requests')  # Errors
SUCCESS_COUNT = Counter('http_requests_success_total', 'Total number of successful requests')  # Successes
REQUEST_SIZE = Histogram('http_request_size_bytes', 'Size of HTTP request payload (bytes)')  # Request size
RESPONSE_SIZE = Histogram('http_response_size_bytes', 'Size of HTTP response payload (bytes)')  # Response size

# SYSTEM METRICS
CPU_USAGE = Gauge('system_cpu_usage', 'CPU Usage Percentage')
RAM_USAGE = Gauge('system_ram_usage', 'RAM Usage Percentage')
DISK_USAGE = Gauge('system_disk_usage', 'Disk Usage Percentage')
NET_BYTES_SENT = Gauge('system_net_bytes_sent', 'Total Bytes Sent')
NET_BYTES_RECV = Gauge('system_net_bytes_recv', 'Total Bytes Received')
MEMORY_AVAILABLE = Gauge('system_memory_available', 'Available Memory in Bytes')
DISK_READ_BYTES = Gauge('system_disk_read_bytes', 'Bytes Read from Disk')
DISK_WRITE_BYTES = Gauge('system_disk_write_bytes', 'Bytes Written to Disk')
MLFLOW_HEALTH = Gauge('mlflow_server_health', 'Health of the MLflow Model Server')

logging.basicConfig(level=logging.INFO)

# Endpoint for Prometheus
@app.route('/metrics', methods=['GET'])
def metrics():
    # Update system metrics every time /metrics is accessed
    CPU_USAGE.set(psutil.cpu_percent(interval=None))
    RAM_USAGE.set(psutil.virtual_memory().percent)
    DISK_USAGE.set(psutil.disk_usage('/').percent)
    net_io = psutil.net_io_counters()
    NET_BYTES_SENT.set(net_io.bytes_sent)
    NET_BYTES_RECV.set(net_io.bytes_recv)
    MEMORY_AVAILABLE.set(psutil.virtual_memory().available)
    disk_io = psutil.disk_io_counters()
    DISK_READ_BYTES.set(disk_io.read_bytes)
    DISK_WRITE_BYTES.set(disk_io.write_bytes)

    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# Endpoint for model predictions
@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    REQUEST_COUNT.inc()
    data = request.get_json()
    logging.info(f"Received request: {data}")

    # Record request size
    if data:
        REQUEST_SIZE.observe(len(str(data).encode('utf-8')))

    # Define the MLflow model server URL
    api_url = "http://127.0.0.1:5001/invocations"

    try:
        # Prepare the input data for the model
        input_data = {
            "instances": [data["input"]]  # Use "instances" as the key
        }

        # Send the request to the MLflow model server
        response = requests.post(api_url, json=input_data)
        response.raise_for_status()  # Raise an error for HTTP failures
        duration = time.time() - start_time

        REQUEST_LATENCY.observe(duration)
        SUCCESS_COUNT.inc()
        logging.info(f"Prediction successful: {response.json()}")

        # Record response size
        RESPONSE_SIZE.observe(len(response.content))

        # Return the prediction result
        return jsonify(response.json())

    except Exception as e:
        ERROR_COUNT.inc()
        logging.error(f"Prediction failed: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Add a /ping endpoint
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "OK"}), 200

def check_mlflow_health():
    while True:
        try:
            response = requests.get("http://127.0.0.1:5001/ping")
            MLFLOW_HEALTH.set(1 if response.status_code == 200 else 0)
        except:
            MLFLOW_HEALTH.set(0)
        time.sleep(10)

if __name__ == '__main__':
    # Start the health check thread
    threading.Thread(target=check_mlflow_health, daemon=True).start()

    # Start the Flask server
    app.run(host='0.0.0.0', port=8000)