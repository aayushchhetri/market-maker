from flask import jsonify


class News:
    def __init__(self, db):
        self.conn = db

    def fetch(self):
        return jsonify(self.conn['47784ea3b2c643acfe345225871c640f'])