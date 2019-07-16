# TIPS:
# Similar to #040 and #039
# since it cannot duplicate the candidates, no need to check previous or ans
# candidates are 1-9, no need to make a list

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        self.lookup(k, n, 1, [], ans)
        
        return ans    
    
    def lookup(self, k, n, idx, path, ans):
        if k < 0: return
        if k == 0 and n == 0: ans.append(path)

        for i in range(idx, 10):
            if i > n: break
            
            self.lookup(k-1, n-i, i+1, path+[i], ans)