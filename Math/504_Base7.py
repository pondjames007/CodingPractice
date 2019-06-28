# TIPS:
# * Just divide and get Quotient and Remain
class Solution:
    def convertToBase7(self, num: int) -> str:
        res = []
        neg = False
        
        if num == 0: return '0'
        
        if num < 0:
            neg = True
            num = -num
            
        while num > 0:
            res.append(str(num%7))
            num //= 7
        
        ans = ''.join(res[::-1])
        
        if neg:
            ans = '-' + ans
            
        return ans
            