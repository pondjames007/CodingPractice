# TIPS:
# go through the array and use a stack
# ''.isdigit() -> negative number doesn't count
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op.isdigit() or op[0] == '-': stack.append(int(op))
            elif op == 'C' and stack: stack.pop()
            elif op == 'D': stack.append(stack[-1] * 2)
            elif op == '+': stack.append(stack[-1] + stack[-2])
                
        return sum(stack)