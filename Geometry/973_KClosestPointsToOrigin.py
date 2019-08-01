# TIPS:
# use heap to help us sort

import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        
        for point in points:
            a, b = point
            dist = [math.sqrt(a**2 + b**2), point]
            heapq.heappush(heap, dist)
        
        
        ans = [heapq.heappop(heap)[1] for _ in range(K)]
        
        return ans
        
            