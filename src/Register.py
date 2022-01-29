import json
import time

class Register:
    def __init__(self, id):
        self.id = id
        self.timer = 0
        self.activated = False
        self.timeCreated = time.time()
        self.timeOfLastUpdate = time.time()
        self.timerStarted = None
        self.itemsNeeded = 20
        self.itemsStocked = 0
        self.timerTime = 0
        self.level = -1
        self.bossGainedTotal = 0.0
        self.resetValues(1)

    def doUpdate(self):
        lastUpdate = self.timeOfLastUpdate
        now = time.time()
        elapsed = now - lastUpdate
        self.tickTimer(elapsed, now)
        self.timeOfLastUpdate = now

        dic = {'register_activated':self.activated,'register_level':self.level,'register_timer':int(self.timer),'register_itemsNeeded':self.itemsNeeded,'register_itemsStocked':self.itemsStocked}

        return json.dumps(dic)

    def tickTimer(self, elapsed, now):
        if self.activated:
            self.timer -= elapsed
            self.checkWinConditions(now)

    def getBossGains(self):
        return self.bossGainedTotal

    def startAction(self):
        if not self.activated:
            self.activated = True
            self.timerStarted = time.time()

    def resetValues(self, newLevel):
        if newLevel != -1 and self.level != -1:
            self.bossGainedTotal += (self.level * 150)
        else:
            self.level = 1

        self.level = newLevel    
        self.itemsNeeded = 15 * self.level
        self.itemsStocked = 0
        self.timerTime = 60
        self.timer = 60

    def scanItem(self):
        if self.activated:
            self.itemsStocked += 1
            self.doUpdate()

    def checkWinConditions(self, now):
        if self.activated:
            timeStillRunning = self.timerStarted + self.timerTime > now
            actionDone = self.itemsStocked >= self.itemsNeeded

            if timeStillRunning and actionDone:
                self.activated = False
                self.resetValues(self.level + 1)

            if not timeStillRunning and actionDone:
                self.activated = False
                self.resetValues(self.level + 1)

            if not timeStillRunning and not actionDone:
                self.activated = False
                self.resetValues(-1)

            if not self.activated:
                self.timerStarted = None