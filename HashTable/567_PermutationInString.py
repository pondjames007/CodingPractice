# TIPS:
# Similar to #438

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_ = [0]*26
        s2_ = [0]*26
        
        for c in s1:
            s1_[ord(c) - ord('a')] += 1
        
        l = len(s1)
        for i in range(len(s2)):
            if i >= l: 
                s2_[ord(s2[i-l]) - ord('a')] -= 1
            s2_[ord(s2[i]) - ord('a')] += 1
            
            if s1_ == s2_: return True
        
        return False