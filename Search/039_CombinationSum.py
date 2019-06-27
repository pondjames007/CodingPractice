# TIPS:
# * DFS

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        
        return ans
    
    def dfs(self, candidates, target, index, path, ans):
        if target < 0:
            return
        if target == 0:
            ans.append(path)
        
        for i in range(index, len(candidates)):
            self.dfs(candidates, target-candidates[i], i, path + [candidates[i]], ans)
                
                
        
        