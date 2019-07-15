# TIPS:
# check twice: one time treat '*' as '(' and use ')' to pair it, if all ')' can be paired then go to second time.
# the second time: treat '*' as ')' and do the same thing again to '(', if both trials succeed -> it is True

class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s: return True
        
        
        stack = []
        for c in s:
            if c == '(' or c == '*': stack.append(c)
            
            if c == ')':
                if not stack: return False
                else: stack.pop()
        
        if not stack: return True
        
        stack = []
        for c in s[::-1]:
            if c == ')' or c == '*': stack.append(c)
            
            if c == '(':
                if not stack: return False
                else: stack.pop()
        
        return True