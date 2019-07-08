# TIPS:
# check start and end

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        
        intervals.sort()
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
        