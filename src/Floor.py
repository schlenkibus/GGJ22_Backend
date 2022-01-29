import json
import time

class Floor:
    def __init__(self, id):
        self.id = id
        self.timeCreated = time.time()
        self.timer = 0
        self.activated = False

    def doUpdater(self):
        return json.dumps([self.timer, self.activated])
