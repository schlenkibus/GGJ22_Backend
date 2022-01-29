import json
from os import times
import time

class Shelf:
    def __init__(self, id):
        self.id = id
        self.timer = 0
        self.activated = False
        self.timeCreated = time.time()
        self.timeOfLastUpdate = time.time()
        self.timerStarted = None
        self.itemsNeeded = 10
        self.itemsStocked = 0
        self.timerTime = 0
        self.level = 1

    def doUpdate(self):
        lastUpdate = self.timeOfLastUpdate
        now = time.time()
        elapsed = now - lastUpdate
        self.tickTimer(elapsed, now)
        self.timeOfLastUpdate = now

        dic = {'activated':self.activated,'level':self.level,'timer':int(self.timer),'itemsNeeded':self.itemsNeeded,'itemsStocked':self.itemsStocked}

        return json.dumps(dic)

    def tickTimer(self, elapsed, now):
        if self.activated:
            self.timer -= elapsed
            self.checkWinConditions(now)

    def startAction(self):
        if not self.activated:
            self.itemsNeeded = 10 * self.level
            self.itemsStocked = 0
            self.timerTime = 60
            self.activated = True
            self.timer = 60
            self.timerStarted = time.time()

    def stockItem(self):
        if self.activated:
            self.itemsStocked += 1

    def checkWinConditions(self, now):
        if self.activated:
            timeStillRunning = self.timerStarted + self.timerTime > now
            actionDone = self.itemsStocked > self.itemsNeeded

            if timeStillRunning and actionDone:
                self.activated = False
                self.level += 1

            if not timeStillRunning and actionDone:
                self.activated = False
                self.level += 1

            if not timeStillRunning and not actionDone:
                self.activated = False
                self.level = -1 #indicates GameOver

            if not self.activated:
                self.itemsNeeded = 0
                self.itemsStocked = 0
                self.timerStarted = None
                self.timerTime = 0