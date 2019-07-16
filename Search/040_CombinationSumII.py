# TIPS:
# Similar to #039 but add one used set to track if it is used
# or check if it is the same as the previous one
# don't check target < 0 and return
# just break it instead so that fewer iterations are made

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        ans = []
        candidates.sort()
        used = set()
        
        for i in range(len(candidates)):
            if candidates[i] in used: continue
            used.add(candidates[i])
            
            self.lookup(candidates, target-candidates[i], i+1, [candidates[i]], ans)
        
        return ans
            
    def lookup(self, candidates, target, index, path, ans):
        
        if target == 0 and path not in ans: ans.append(path)
        
        for i in range(index, len(candidates)):
            if candidates[i] > target: break
            self.lookup(candidates, target-candidates[i], i+1, path+[candidates[i]], ans)