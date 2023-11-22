
from model.store_tracker_model import StoreTrackerModel 

class StoreController:

    def __init__(self):
        self.store_tracker_model = StoreTrackerModel()
    

    def get_all_stores(self):
        stores = self.store_tracker_model.get_all_stores()
        return stores

    def add_store(self, store):
        if self.store_tracker_model.add_store(store):
            return 1
        else:
            return 0
    
    def is_store_present(self, name):
        return self.store_tracker_model.is_store_present(name)

    def add_item(self, item, storeName):
        return self.store_tracker_model.add_item(item, storeName)

    def get_store(self, storeName):
        return self.store_tracker_model.get_store(storeName)
