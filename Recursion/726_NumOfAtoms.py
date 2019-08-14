# TIPS:
# reverse the formula and write every conditions

from functools import reduce
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        table = defaultdict(int)
        num = ''
        ele = ''
        
        # handle parentheses
        num_stack = []
        p = 0

        # handle element = 1
        prev = ''
        one = True 

        for c in formula[::-1]:
            if c.isdigit():
                num = c + num
                one = False
            else:
                if num:
                    num_stack.append(int(num))
                    num = ''
                if not prev.isdigit() and not prev.islower(): one = True

            if c == ')': 
                p += 1

            if c == '(': 
                p -= 1
                num_stack.pop()

            if c.islower():
                ele = c + ele

            if c.isupper():
                ele = c + ele
                if one: num_stack.append(1)
                table[ele] += reduce(lambda x,y: x*y, num_stack[-p-1:])
                num_stack.pop()
                ele = ''
                one = False
            
            prev = c
                
        ans = ''
        table = sorted(list(table.items()))
        for a, b in table:
            if b == 1: b = ''
            ans += a + str(b)
            
        return ans