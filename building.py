import PyInstaller
import sys
import os
import json


class Building:
    def __init__(self):
        self.build_info = None
        self.sys = sys.argv

    def do(self):
        if os.path.isfile("building_info.json"):
            with open("building_info.json", "r") as info:
                self.build_info = json.loads(info.read())
        else:
            with open("building_info.json", "x") as info:
                info.write(json.dumps({"app": {"name": "",
                                               "version": "",
                                               "url": "",
                                               "info": ""}}))
                raise Exception("Information document not filled in!")
