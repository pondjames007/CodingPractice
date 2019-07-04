# TIPS:
# Use 2 hash tables to store key to val and val to keys
# Can also use LinkedList to store val to keys (not good in Python)

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valueMap = {}
        self.keyMap = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.keyMap: self.keyMap[key] = 1
        else: self.keyMap[key] += 1
        
        if self.keyMap[key] not in self.valueMap:
            self.valueMap[self.keyMap[key]] = {key}
        else:
            self.valueMap[self.keyMap[key]].add(key)
            
        if self.keyMap[key]-1 in self.valueMap:
            if len(self.valueMap[self.keyMap[key]-1]) == 1:
                self.valueMap.pop(self.keyMap[key]-1)
            else: 
                self.valueMap[self.keyMap[key]-1].discard(key)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.keyMap:
            if len(self.valueMap[self.keyMap[key]]) == 1: 
                self.valueMap.pop(self.keyMap[key])
            else: 
                self.valueMap[self.keyMap[key]].discard(key)
            
            if self.keyMap[key] == 1:
                self.keyMap.pop(key)
            else:
                self.keyMap[key] -= 1

                if self.keyMap[key] not in self.valueMap:
                    self.valueMap[self.keyMap[key]] = {key}
                else:
                    self.valueMap[self.keyMap[key]].add(key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if not self.valueMap: return ""
        
        maximum = max(self.valueMap.keys())
        
        return list(self.valueMap[maximum])[-1]

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if not self.valueMap: return ""
        
        minimum = min(self.valueMap.keys())
        
        return list(self.valueMap[minimum])[0]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()