#! /usr/bin/env python3
#make a flask hello world app

from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

# Set up log file path
LOG_FILE = 'access_log.txt'

# Create log file if it doesn't exist
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, 'w').close()

def log_access(endpoint):
    """Log endpoint access with timestamp and IP address"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr
    with open(LOG_FILE, 'a') as f:
        f.write(f"{timestamp} - IP: {ip} - Endpoint: {endpoint}\n")

@app.route('/weilan')
def weilan():
    log_access('/weilan')
    return "Hello world from Weilan Liang!"
    
@app.route('/datetime')
def currenttime():
    log_access('/datetime')
    return f"The current time is {datetime.now()}"

@app.route('/log')
def view_log():
    log_access('/log')
    try:
        with open(LOG_FILE, 'r') as f:
            log_contents = f.read()
        return f"<pre>{log_contents}</pre>"
    except Exception as e:
        return f"Error retrieving logs: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)