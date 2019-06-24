# TIPS:
# * String.isalpha() -> check if it is a letter

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for s in S:
            if s.isalpha():
                res = [x + y for x in res for y in [s.lower(), s.upper()]]
            else:
                res = [x + s for x in res]
        
        return res