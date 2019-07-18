# TIPS:
# don't need to use hashtable
# sometimes we know the data range: like 26 chars
# then we can just use array to store it
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s: return []
        
        ans = []
        p_ = [0]*26
        s_ = [0]*26
        
        for c in p:
            p_[ord(c) - ord('a')] += 1
        l = len(p)
        for i in range(len(s)):
            if i >= l:
                s_[ord(s[i-l]) - ord('a')] -= 1
                
            s_[ord(s[i]) - ord('a')] += 1
            
            if s_ == p_: ans.append(i+1-l)
        
        return ans
        