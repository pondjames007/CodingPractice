# TIPS:
# * all(): return True if all elements in a list are all True
# * all([]) will return True

import collections

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        ctr_lp = {k: v for k, v in collections.Counter(licensePlate).items() if k.isalpha()}
        ans = ''
        for word in words:
            ctr_wd = collections.Counter(word)
            res = []

            for ctr in ctr_lp:
                if ctr in ctr_wd and ctr_lp[ctr] <= ctr_wd[ctr]:
                    res.append(True)
                else:
                    res.append(False)

            if all(res):
                if len(ans) == 0 or len(word) < len(ans):
                    ans = word
        
        return ans
                
