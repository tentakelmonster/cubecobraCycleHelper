import json
from pathlib import Path

JSON_PATH = Path.cwd() / "resources" / "cycles.json"

class CycleData(object):
    """ Reads the cycle data from the JSON """
    def __init__(self):
        self.cycleData = self.getCycleDataFromJson()

    @staticmethod
    def getCycleDataFromJson():
        with open(JSON_PATH, 'r') as jsonFile:
            data = json.load(jsonFile)
        return data

    def getCycleData(self):
        return self.cycleData
