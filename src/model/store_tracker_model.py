from object_models.store import Store
from typing import List

class StoreTrackerModel:
    def __init__(self):
        self.stores : List[Store] = []
    
    def add_store(self, new_store: Store):
        self.stores.append(new_store)
        return 1
    
    def get_all_stores(self):
        print(self.stores)
        return self.stores

    def is_store_present(self, storeName):
        for store in self.stores:
            if store["name"] == storeName:
                return True
        return False
    
    def add_item(self, item, storeName):
        for store in self.stores:
            if store["name"] == storeName:
                store["items"].append(item)
                return store
    
    def get_store(self, storeName):
        for store in self.stores:
            if store["name"] == storeName:
                return store
