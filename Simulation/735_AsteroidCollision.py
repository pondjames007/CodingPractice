# TIPS:
#
# Use Stack
# Collision condition: a[i](>0) -> and <- a[i+1](<0)
# if the right one survives, it will keep going to collide with next one in the stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        
        for ast in asteroids[1:]:
            while True:
                if ast < 0 and stack and stack[-1] > 0:
                    if abs(ast) > abs(stack[-1]): 
                        stack.pop()
                    elif abs(ast) == abs(stack[-1]):
                        stack.pop()
                        break
                    else: break

                else:
                    stack.append(ast)
                    break
                
        return stack