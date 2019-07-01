# TIPS:
# use defaultdict to store position


import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        self.pos[val].add(len(self.nums)-1)
        return len(self.pos[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """

        if self.pos[val]:
            out, ins = self.pos[val].pop(), self.nums[-1]
            self.nums[out] = ins
            if self.pos[ins]:
                self.pos[ins].add(out)
                self.pos[ins].discard(len(self.nums) - 1)
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.nums)
