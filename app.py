from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return f"""
    <h1>🐳 Hello from Docker Container!</h1>
    <h3>Application Info:</h3>
    <ul>
        <li><strong>Container ID:</strong> {os.environ.get('HOSTNAME', 'unknown')}</li>
        <li><strong>Environment:</strong> {os.environ.get('ENV', 'development')}</li>
        <li><strong>Python Version:</strong> {os.environ.get('PYTHON_VERSION', 'unknown')}</li>
        <li><strong>Current Time:</strong> {datetime.datetime.now()}</li>
    </ul>
    <p>🎉 <em>Your Docker setup is working perfectly!</em></p>
    """

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "flask-docker-app",
        "timestamp": datetime.datetime.now().isoformat(),
        "container_id": os.environ.get('HOSTNAME', 'unknown')
    })

@app.route('/api/info')
def info():
    return jsonify({
        "app_name": "Docker Demo App",
        "version": "1.0.0",
        "environment": os.environ.get('ENV', 'development'),
        "python_version": os.environ.get('PYTHON_VERSION', 'unknown'),
        "container_id": os.environ.get('HOSTNAME', 'unknown')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)