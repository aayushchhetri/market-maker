from flask import jsonify


class History:
    def __init__(self, db):
        self.conn = db

    def fetch(self):
        return jsonify(self.conn['ca50ee7a3cda1a8b36ffb5fae9c13dea'])