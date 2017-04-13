import os
import atexit
import cf_deployment_tracker
from flask import Flask, jsonify, render_template

from library._marketState import State
from library._Cloudant import MarketDB


# Emit Bluemix deployment event #
cf_deployment_tracker.track()

# Setup objects #
conn = MarketDB()
client = conn.fetch_client()
db = conn.fetch_db()
app = Flask(__name__)

# Render Pages #


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
        return "Empty data set"


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
    conn.client.disconnect()
