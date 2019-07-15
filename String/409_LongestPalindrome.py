# TIPS:
# keep the most common odd number
# other odd numbers -> minus 1 and add them
# add all even numbers

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = Counter(s)
        
        count = chars.most_common()
        
        flag = True
        ans = 0
        for _, i in count:
            if i%2 == 1:
                if flag:
                    ans += i
                    flag = False
                else:
                    ans += i-1
            
            if i%2 == 0: ans += i
        
        return ans
                