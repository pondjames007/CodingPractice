# TIPS:
# * Use BISECT to insert
# * Use 2 HEAPS (1 Min -> get median+1 element and 1 Max -> get median-1 element) to get median

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.length = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)
        self.length += 1
    def findMedian(self) -> float:
        if self.length%2 == 0:
            return (self.nums[self.length//2] + self.nums[self.length//2 - 1])/2
        else:
            return float(self.nums[self.length//2])

# Use 2 HEAPS to find median
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.median = 0

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            heappush(self.min_heap, num)
            self.median = num
        else:
            if len(self.min_heap) == len(self.max_heap):
                tmp = heappop(self.min_heap)
                if num >= tmp:
                    self.median = tmp
                    heappush(self.min_heap,num)
                    
                else:
                    heappush(self.max_heap,-num)
                    tmp2 = -heappop(self.max_heap)
                    self.median = tmp2
                    heappush(self.min_heap,tmp2)
                heappush(self.min_heap,tmp)
            else:
                tmp = heappop(self.min_heap)
                if num <= tmp:
                    heappush(self.max_heap,-num)
                    tmp2 = -heappop(self.max_heap)
                    self.median = (tmp + tmp2) / 2.0
                    heappush(self.max_heap,-tmp2)
                    heappush(self.min_heap,tmp)
                else:
                    heappush(self.min_heap,num)
                    tmp2 = heappop(self.min_heap)
                    self.median = (tmp + tmp2) / 2.0
                    heappush(self.min_heap,tmp2)
                    heappush(self.max_heap,-tmp) 
                    
    def findMedian(self) -> float:
        return self.median