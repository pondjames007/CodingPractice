# TIPS:
# * DFS recursion
# * Almost the same way as #200
# * you don't need to use 'seen' to store whether it is used or not
#   you can use M[i][i] and change it to 0 or whatever to label it is used (not suggested)
# * enumerate all student, then use DFS to go through all his friend, then kick them out

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def lookup(i, M):
            for j in range(len(M[i])):
                if M[i][j] == 1 and j not in seen:
                    seen.add(j)
                    lookup(j, M)
            return
        
        if not M: return 0
        
        seen = set()
        ans = 0
        for i in range(len(M)):
            if i not in seen:
                lookup(i, M)
                ans += 1
                
        return ans
                