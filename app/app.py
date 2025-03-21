from flask import Flask, render_template, jsonify
import random
import json
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

# Load quotes from a JSON file
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

# Define a counter metric for HTTP requests
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

@app.route('/')
def home():
    # Increment the counter for each request
    REQUEST_COUNT.inc()
    return render_template('index.html')

@app.route('/get_quote')
def get_quote():
    # Increment the counter for each request
    REQUEST_COUNT.inc()
    # Return a random quote as JSON
    quote = random.choice(quotes)
    return jsonify(quote)

if __name__ == '__main__':
    # Start the Prometheus HTTP server on port 5001
    start_http_server(5001)
    # Start the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)