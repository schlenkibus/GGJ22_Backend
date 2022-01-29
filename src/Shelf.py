import json
import time

class Shelf:
    def __init__(self, id):
        self.id = id
        self.timer = 600
        self.activated = True
        self.timeCreated = time.time()
        self.timeOfLastUpdate = time.time()

    def doUpdate(self):
        lastUpdate = self.timeOfLastUpdate
        now = time.time()
        elapsed = now - lastUpdate
        self.tickTimer(elapsed)
        self.timeOfLastUpdate = now
        return json.dumps([int(self.timer), self.activated])

    def tickTimer(self, elapsed):
        if self.activated:
            self.timer -= elapsed
            self.checkWinConditions()

    def checkWinConditions(self):
        #todo
        return