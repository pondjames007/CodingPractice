# TIPS:
# record freq of each number
# record numbers for each freq
# track maximum freq
 
from collections import Counter, defaultdict

class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.freq_ele = defaultdict(list)
        self.max_f = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        self.max_f = max(self.max_f, self.freq[x])
        self.freq_ele[self.freq[x]].append(x)

    def pop(self) -> int:
        x = self.freq_ele[self.max_f].pop()
        if not self.freq_ele[self.max_f]: self.max_f -= 1
        self.freq[x] -= 1
        
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()