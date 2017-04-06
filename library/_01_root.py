from flask import Flask


app = Flask(__name__)


@app.route('/')
def rootPage():
    return "Starting from scratch"

@app.route('/countries')
def countryPage():
    return "List of countries"

@app.route('/news')
def newsPage():
    return "List of news"

@app.route('/market')
def marketPage():
    return "Market History"