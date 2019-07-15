# TIPS:
# s.find() -> find the index of certain pattern in the string
# s.count() -> count the certain pattern in the string

class Solution:
    def checkRecord(self, s: str) -> bool:
        
        return s.count('A') < 2 and 'LLL' not in s