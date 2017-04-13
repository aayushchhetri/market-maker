from flask import jsonify


class State:
    def __init__(self, db):
        self.conn = db
        self.conn['37d2890837d8dd6ec1006cbb8e450e5b'].fetch()

    def fetch(self):
        return jsonify(self.conn['37d2890837d8dd6ec1006cbb8e450e5b'])
