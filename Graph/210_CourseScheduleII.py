# TIPS:
# Similar to #207

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites: return [i for i in range(numCourses)]
        
        courses = [[] for _ in range(numCourses)]
        remain = [0 for _ in range(numCourses)]
        
        for c, pre in prerequisites:
            courses[pre].append(c)
            remain[c] += 1
            
        can_take = [i for i in range(numCourses) if remain[i] == 0]
        
        if not can_take: return []
        
        ans = []
        
        for c in can_take:
            ans.append(c)
            for p in courses[c]:
                remain[p] -= 1
                if remain[p] == 0:
                    can_take.append(p)
                
        return ans if len(ans) == numCourses else []