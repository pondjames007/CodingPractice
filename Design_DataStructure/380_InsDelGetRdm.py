# TIPS:
# Use SET -> slow
# Use array and dict to do it
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        length = len(self.data)
        self.data.add(val)
        if length == len(self.data): return False
        else: return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        length = len(self.data)
        self.data.discard(val)
        if length == len(self.data): return False
        else: return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return random.sample(self.data, 1)[0]

# Use an array and a dict to store the elements
# don't use del to kill element in the dictionary
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums)-1
            return True
        else: return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos: return False
        idx = self.pos[val]
        self.pos[self.nums[-1]] = idx
        self.nums[idx] = self.nums[-1]
        self.nums.pop()
        self.pos.pop(val)
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)