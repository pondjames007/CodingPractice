# TIPS:
# * find out the ranges
# * merge the range
# * Interval Merging Problem

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        pos = {}
        for i in range(len(S)):
            if S[i] not in pos:
                pos[S[i]] = [i, i]
            else:
                pos[S[i]][-1] = i
                
        pos = sorted(pos.values())
        
        res = []
        for dist in pos:
            start, end = dist
            if len(res) == 0:
                res.append(dist)
            else:
                if res[-1][1] > start:
                    res[-1][1] = max(res[-1][1], end)
                else:
                    res.append(dist)
        ans = [r-l+1 for l, r in res]
        return ans