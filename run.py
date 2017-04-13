import os
import json
import atexit
import cf_deployment_tracker
from library._marketState import State
from cloudant import Cloudant
from flask import Flask, jsonify, render_template

# Emit Bluemix deployment event #
cf_deployment_tracker.track()

# Connect to  Cloudant DB and create database if not already present #

db_name = 'market-maker'
client = None
db = None

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

# Render Pages #

app = Flask(__name__)


@app.route('/')
def root_page():
    return "Starting from scratch"


@app.route('/marketState', methods=['GET'])
def market_state_page():
    if client:
        new_state = State(db)
        return new_state.fetch()
    else:
        print('No database')
        return jsonify([])


@app.route('/news')
def news_page():
    return "List of news"


@app.route('/marketHistory')
def market_page():
    return "Market History"

# Provide TCP Host#

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 8080))
    app.run(host=host, port=port)


@atexit.register
def shutdown():
    client.disconnect()
