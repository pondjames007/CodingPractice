# TIPS:
# Use bisect to insert newInterval then do merge interval

import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = bisect.insort(intervals, newInterval)
        
        ans = [intervals[0]]
        index = 0
        
        for start, end in intervals[1:]:
            if start <= ans[index][1]:
                if end >= ans[index][1]:
                    ans[index][1] = end
            else:
                ans.append([start, end])
                index += 1
                
        return ans

# Only merge intervals in the range influenced
# Use list(zip(*intervals)) to get start, end list seperately
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        if not newInterval: return intervals
        
        sep_interval = list(zip(*intervals))
        start = bisect.bisect(sep_interval[0], newInterval[0])
        end = bisect.bisect(sep_interval[1], newInterval[1])
        
        if start > 0: start -= 1
        if end < len(intervals): end += 1
        
        adjust = intervals[start:end]
        bisect.insort(adjust, newInterval)
        index = 0
        res = [adjust[0]]
        for a, b in adjust[1:]:
            if a <= res[index][1]:
                if b >= res[index][1]:
                    res[index][1] = b
            else:
                res.append([a, b])
                index += 1
                
        return intervals[:start] + res + intervals[end:]