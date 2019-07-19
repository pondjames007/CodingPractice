# TIPS:
# straight forward check.
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            s = str(i)
            if '0' in s: continue
                
            check = [i%int(d) == 0 for d in s]
            if all(check): ans.append(i)
                
        return ans