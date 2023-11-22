class Store:
    def __init__(self, name, items:[]):
        self.name = name
        self.items = items

    def getName(self):
        return self.name
    
    def getItems(self):
        return self.items
    
    def setName(self, name):
        self.name = name
    
    def setItem(self, item):
        self.items = item