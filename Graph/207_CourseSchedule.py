# TIPS:
# Store a mapping of PRE: [courses] (courses)
# Store a number of list (remain) for every class that how many classes should take first before taking it
# Store a list of courses that can be taken right now (remain == 0)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        
        courses = [[] for _ in range(numCourses)]
        pre_remain = [0 for _ in range(numCourses)]
        
        for c, pre in prerequisites:
            courses[pre].append(c)
            pre_remain[c] += 1
            
        can_take = [i for i in range(numCourses) if pre_remain[i] == 0]
        
        if not can_take: return False
        
        for i in can_take:
            for j in courses[i]:
                pre_remain[j] -= 1
                if pre_remain[j] == 0:
                    can_take.append(j)
        return len(can_take) == numCourses