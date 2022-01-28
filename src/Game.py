from Market import Market

class Game:
    def __init__(self, app):
        self.app = app
        self.markets = []

    def createMarket(self):
        market = Market()
        self.markets.append(market)
        return market.getID()

    def getUpdateForMarket(self, id):
        for market in self.markets:
            if market.id == id:
                return market.doAndSendUpdate()
        return ""

    def findMarket(self, id):
        for market in self.markets:
            if market.getID() == id:
                return market
        return None

    def getMarkets(self):
        ret = []
        for market in self.markets:
            ret.append(market.getID())
        return ret