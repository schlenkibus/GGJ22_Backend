import uuid
from Shelf import Shelf
from Floor import Floor
from Register import Register

class Market:
    def __init__(self):
        self.id = uuid.uuid4()
        self.level = 1
        self.money = 0
        self.shelfes = [Shelf(0), Shelf(1), Shelf(2)]
        self.floors = [Floor(0), Floor(1), Floor(2)]
        self.registers = [Register(0), Register(1)]

    def getID(self):
        return str(self.id)

    