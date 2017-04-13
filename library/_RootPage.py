from flask import render_template


class Root():
    def __init__(self,title="Market Maker"):
        self.title = title

    def fetch(self):
        return render_template('index.html', title=self.title)