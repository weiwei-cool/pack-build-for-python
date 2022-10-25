import sys
import os
import json
import requests


class Main:
    def __init__(self, name):
        self.name = name
        self.url = "flystudiokey.xyz"
        if not os.path.isdir("./bin"):
            os.mkdir("./bin")
            self.first_run()

    def file_write(self):
        pass

    def first_run(self):
        res = json.loads(requests.get(url=f"https://ann.{self.url}/get-app-ann").text)
        d_url = res["data"][0]["d_url"]
        file = requests.get(d_url["7zip"])
