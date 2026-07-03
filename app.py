from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>🚀 Jenkins CI/CD Pipeline Validation</h1>
    <h2>Deployment Successful!</h2>

    <p><b>Status:</b> Running Successfully ✅</p>
    <p><b>Server:</b> {socket.gethostname()}</p>
    <p><b>Deployment Time:</b> {datetime.now()}</p>

    <hr>

    <h3>If you can see this page, your pipeline is working!</h3>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
