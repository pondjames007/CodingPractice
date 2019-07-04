# TIPS:
# BISECT OP

import bisect

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        
        if index == len(letters): return letters[0]
        
        return letters[index]