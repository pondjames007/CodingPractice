# TIPS:
#
# Just go through the moves and check the position
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        
        for c in moves:
            if c == 'U': pos[1] += 1
            elif c == 'D': pos[1] -= 1
            elif c == 'L': pos[0] -= 1
            elif c == 'R': pos[0] += 1
        
        return pos == [0, 0]

# Use collections.Counter can be faster
import collections
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        
        s = collections.Counter(moves)
        pos[0] += s['U'] - s['D']
        pos[1] += s['R'] - s['L']
        
        return pos == [0, 0]