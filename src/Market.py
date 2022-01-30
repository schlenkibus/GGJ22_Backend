import json
import time
import uuid
from Shelf import Shelf
from Floor import Floor
from Register import Register

class Market:
    def __init__(self):
        self.timeZero = time.time()
        self.id = uuid.uuid4()
        self.shelf = Shelf(0)
        self.floor = Floor(0)
        self.register = Register(0)
        self.playerMoney = 0.0
        self.bossMoney = 0.0
        self.playerMoneyPerSec = 50.0 / 3600
        self.playerPosX = 0
        self.playerPosY = 0

    def getID(self):
        return str(self.id)

    def queueShelfes(self):
        self.shelf.startAction()

    def stockShelfItem(self):
        self.shelf.stockItem()

    def orderRegister(self):
        self.register.startAction()

    def scanItem(self):
        self.register.scanItem()

    def updatePlayerPos(self, x, y):
        self.playerPosX = x
        self.playerPosY = y

    def getPlayerPos(self):
        return {'x': self.playerPosX, 'y': self.playerPosY}

    def doUpdate(self):
        registerInfo = json.loads(self.register.doUpdate())
        shelfInfo = json.loads(self.shelf.doUpdate())
        passed = time.time() - self.timeZero
        self.playerMoney = passed * self.playerMoneyPerSec
        self.bossMoney = self.shelf.getBossGains() + self.register.getBossGains()
        shelfInfo['playerMoney'] = self.playerMoney
        shelfInfo['bossMoney'] = self.bossMoney
        return json.dumps(shelfInfo)[:-1] + ', ' + json.dumps(registerInfo)[1::]