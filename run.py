import os
import atexit
import cf_deployment_tracker
from flask import Flask

from library._marketState import State
from library._RootPage import Root
from library._Cloudant import MarketDB


# Emit Bluemix deployment event #
cf_deployment_tracker.track()

# Setup objects #
conn = MarketDB()
client = conn.fetch_client()
db = conn.fetch_db()
app = Flask(__name__)
app.template_folder = 'library/templates'

# Render Pages #


@app.route('/')
def root_page():
        page = Root()
        return page.fetch()


@app.route('/marketState', methods=['GET'])
def market_state_page():
    if client:
        page = State(db)
        return page.fetch()
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
