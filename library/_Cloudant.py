import os
import json
from cloudant import Cloudant


class MarketDB:
    def __init__(self,new_name='market-maker'):
        self.db_name = new_name
        self.client = None
        self.db = None
        # Connect to  Cloudant DB and create database if not already present #

        if 'VCAP_SERVICES' in os.environ:
            vcap = json.loads(os.getenv('VCAP_SERVICES'))
            print('Found VCAP_SERVICES')
            if 'cloudantNoSQLDB' in vcap:
                creds = vcap['cloudantNoSQLDB'][0]['credentials']
                user = creds['username']
                password = creds['password']
                url = 'https://' + creds['host']
                self.client = Cloudant(user, password, url=url, connect=True)
                self.db = self.client.create_database(self.db_name, throw_on_exists=False)
        elif os.path.isfile('vcap-local.json'):
            with open('vcap-local.json') as f:
                vcap = json.load(f)
                print('Found local VCAP_SERVICES')
                creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
                user = creds['username']
                password = creds['password']
                url = 'https://' + creds['host']
                self.client = Cloudant(user, password, url=url, connect=True)
                self.db = self.client.create_database(self.db_name, throw_on_exists=False)

    def fetch_client(self):
        return self.client

    def fetch_db(self):
        return self.db
