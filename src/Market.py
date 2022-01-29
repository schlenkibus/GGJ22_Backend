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

    def getID(self):
        return str(self.id)

    def queueShelfes(self):
        self.shelf.startAction()

    def stockShelfItem(self):
        self.shelf.stockItem()

    def doUpdate(self):
        shelfInfo = json.loads(self.shelf.doUpdate())
        passed = time.time() - self.timeZero
        self.playerMoney = passed * self.playerMoneyPerSec
        self.bossMoney = self.shelf.getBossGains()
        shelfInfo['playerMoney'] = self.playerMoney
        shelfInfo['bossMoney'] = self.bossMoney
        return shelfInfo