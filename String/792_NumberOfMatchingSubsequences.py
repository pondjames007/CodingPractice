# TIPS:
# * subsequence: letter order matters
# * bisect: use binary search in a SORTED list
# * bisect.bisect_left(list, x): return the index that can insert x in list, if x is in list, it will return the index at left
# * bisect.insort_left(list, x): insert x into the ordered list
#
# * go through the dictionary and find the index that the next one should be

from collections import defaultdict
import bisect

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        if not words or not S: return 0
        
        pos = defaultdict(list)
        
        for i, c in enumerate(S):
            pos[c].append(i)
        
        count = 0
        for word in words:
            prev = -1
            flag = True
            for c in word:
                pos_index = bisect.bisect(pos[c], prev)
                if pos_index == len(pos[c]): 
                    flag = False
                    break
                prev = pos[c][pos_index]
            if flag == True:
                count += 1
        
        return count
            
        