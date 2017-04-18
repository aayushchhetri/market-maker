import os
from flask import render_template


class Root():
    def __init__(self,title="Market Maker"):
        self.title = title
        if 'VCAP_SERVICES' in os.environ:
            self.host = "market-maker.frankencloud.net"
        else:
            self.host = "localhost:8080"

    def fetch(self):
        return render_template('index.html', title=self.title, host=self.host)
