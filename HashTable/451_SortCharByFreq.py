# TIPS:
# * collections.Counter
# * How to do it without Counter?
# * sorted(list, key= func, reverse= False) -> sort in defaut ASCENDING ORDER
# * list.sort(key= , reverse= ) 

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        cnt_list = cnt.most_common()
        
        ans = ''
        for l, n in cnt_list:
            ans += l*n
            
        return ans
        
# SECOND ANSWER: NO colleciton.Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = {}
        for c in s:
            if c not in cnt:
                cnt[c] = 1
            else:
                cnt[c] += 1
        char_list = sorted(list(cnt.items()), key= lambda x: x[1], reverse=True)
        
        ans = ''
        for l, n in char_list:
            ans += l*n
            
        return ans
        