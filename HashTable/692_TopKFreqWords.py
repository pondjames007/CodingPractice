# TIPS:
# underscore built in functions
# use hash table with heapq

from collections import Counter
import heapq

class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word



class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)   
        
        freqs = []
        heapq.heapify(freqs)
        for word, count in counts.items():
            heapq.heappush(freqs, (Element(count, word), word))
            if len(freqs) > k:
                heapq.heappop(freqs)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs)[1])
        return res[::-1]
       
# reverse the count to make it to be smallest
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)   
        
        freqs = []
        heapq.heapify(freqs)
        
        for w, c in counts.items():
            heapq.heappush(freqs, (-c, w))
            
        res = [x[1] for x in heapq.nsmallest(k, freqs)]
        
        return res