# TIPS:
# make a dictionary
# do DFS to go through all subordinates

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if not employees: return 0
        e_dict = {}
        
        for e in employees:
            e_dict[e.id] = (e.importance, e.subordinates)
            
        stack = [id]
        ans = 0
        
        while stack:
            person = stack.pop()
            ans += e_dict[person][0]
            if not e_dict[person][1]: continue
            stack += e_dict[person][1]
        
        return ans