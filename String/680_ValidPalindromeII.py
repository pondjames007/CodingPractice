# TIPS:
# find first difference and take the rest part to see if it is a palindrome
# by shifting one from the head or one from the tail

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = len(s)
        
        i = 0
        while i < l//2 and s[i] == s[-i-1]: i += 1
        
        s = s[i:l-i]
        
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]
    
    