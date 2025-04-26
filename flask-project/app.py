#! /usr/bin/env python3
#make a flask hello world app

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    businesses = [
        {
            'name': 'Acme Corporation',
            'address': '123 Main Street, Anytown, USA',
            'url': 'https://www.acme.com'
        },
        {
            'name': 'Global Solutions Inc.',
            'address': '456 Business Ave, Metropolis, USA', 
            'url': 'https://www.globalsolutions.com'
        },
        {
            'name': 'Tech Innovations LLC',
            'address': '789 Innovation Drive, Silicon Valley, USA',
            'url': 'https://www.techinnovations.com'
        }
    ]
    return render_template('index.html', businesses=businesses)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)