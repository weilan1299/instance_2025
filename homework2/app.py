#! /usr/bin/env python3
#make a flask hello world app

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/weilan')
def weilan():
    return "Hello world from Weilan Liang!"
    
@app.route('/datetime')
def currenttime():
    return f"The current time is {datetime.now()}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)