from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "V1.0.0"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
