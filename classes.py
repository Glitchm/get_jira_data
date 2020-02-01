import requests
import conf
from requests import Response
import json

jira_headers = {'Authorization': 'Basic ' + conf.api_token,
              'Content-Type': 'application/json'}


class Jira_info:
    def __init__(self, ext):
        self.ext = ext

    def get_info(self):
        try:
            # Sends the request with the query to look for tickets in alert section that are new
            r: Response = requests.get(conf.api_url + self.ext,
                                       headers=jira_headers)
            info = r.json()
            return info

        except ValueError:
            print(r.text)
            raise