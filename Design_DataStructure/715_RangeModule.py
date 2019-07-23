# TIPS:

# Vector
# store the range as a pair in the vector
# every time add/remove will go through the vector and do add/merge/remove the interval -> O(n)
# also we want the pairs be sorted (by left key)
# so that when query it can use binary search and become more efficient -> O(logn)
class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        new_ranges = []
        inserted = False
        
        for l, r in self.ranges:
            # Correct place to insert the new range
            if l > right and not inserted:
                new_ranges.append([left,right])
                inserted = True
            
            if r < left or l > right:
                new_ranges.append([l,r])
            else:
                left = min(left, l)
                right = max(right, r)
        
        if not inserted: new_ranges.append([left,right])
        
        self.ranges = new_ranges

    def queryRange(self, left: int, right: int) -> bool:
        n = len(self.ranges)
        l = 0
        r = n-1
        
        while l <= r:
            m = (l+r)//2
            if self.ranges[m][1] < left:
                l = m+1
            elif self.ranges[m][0] > right:
                r = m-1
            else:
                return self.ranges[m][0] <= left and self.ranges[m][1] >= right
        
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_ranges = []

        for l, r in self.ranges:
            if r <= left or l >= right:
                new_ranges.append([l,r])
            else:
                if l < left:
                    new_ranges.append([l,left])
                if r > right:
                    new_ranges.append([right, r])
                    
        self.ranges = new_ranges


# Ordered Map
# map[left] = right
# find overlapping ranges efficiently, then do merge/update
# Add/Delete: O(m*logn)
# Query: O(logn)
# m = # of overlapping ranges
# 
# l, r = getOverlappingRanges(ranges, left, right)
# l, r := iterators to the [first, last+1] overlapping ranges 

