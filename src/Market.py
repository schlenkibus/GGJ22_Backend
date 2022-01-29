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

    def getID(self):
        return str(self.id)

    def queueShelfes(self):
        self.shelf.startAction()

    def stockShelfItem(self):
        self.shelf.stockItem()

    def doUpdate(self):
        shelfInfo = self.shelf.doUpdate()
        return shelfInfo    