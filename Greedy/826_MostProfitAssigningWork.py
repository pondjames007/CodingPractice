# TIPS:
# zip
# sort both lists
# use 2 pointers to track

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        ans = 0
        best = 0
        t = 0
        
        for w in sorted(worker):
            while t < len(jobs) and w >= jobs[t][0]:
                best = max(jobs[t][1], best)
                
                t = t+1
            ans += best
            
        return ans