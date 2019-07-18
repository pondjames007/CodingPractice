# TIPS:
# Just use Counter
# or count it then put in heap
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        res = [x[0] for x in count.most_common(k)]
        
        return res