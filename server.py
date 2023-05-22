#!/usr/bin/env python
from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

# Define a counter metric
counter_metric = Counter('microsample_calls_total', 'Total calls to microsampl api (counter)')

__info = {
    'name': 'Erik Lonroth',
    'skill': 100,
    'title': 'wizard'
}

info = __info

application = Flask(__name__)

@application.route('/')
def index():
    counter_metric.inc()
    return "Online"

# Show info
@application.route('/api/info', methods=['GET'])
def get_info():
    # Increase counter to 
    counter_metric.inc()
    return jsonify(info)

# Provide dummy metrics for prometheus
@application.route('/metrics')
def metrics():
    
    # Generate the latest metrics in Prometheus format
    prometheus_metrics = generate_latest()

    return Response(prometheus_metrics, mimetype=CONTENT_TYPE_LATEST)
    


def main():
    application.run()

if __name__ == '__main__':
    application.run()
