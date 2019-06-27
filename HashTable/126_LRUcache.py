# TIPS:
# * collections.OrderedDict
# * Maybe LinkedList to store the order
# * How to implement without using OrderedDict?

from collections import OrderedDict
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value

