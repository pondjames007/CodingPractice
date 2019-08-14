# TIPS:
#
# Sol 1: Recursion
# Case 0: '()' -> 1
# Case 1: The Whole String is Balanced:
#   '(A)' -> 2 * score('A')
# Case 2: Substring is balanced:
#   '(A)(B)(C)' -> score('(A)') + score('(B)(C)')
# T: O(n) ~ O(n^2) 
# S: O(n)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        return self.score(S, 0, len(S)-1)

    def score(self, S, l, r):
        if r-l == 1: return 1 # case 0: '()'
        b = 0
        for i in range(l, r):
            if S[i] == '(': b += 1
            if S[i] == ')': b -= 1
            
            if b == 0: # balanced
                # score('(A)(B)(C)') = score('(A)') + score('(B)(C)')
                return self.score(S, l, i) + self.score(S, i+1, r)
        
        # score('(A)') = 2 * score('A')
        return 2 * score(S, l+1, r-1)

# Sol 2: Counting
# All Scores are come from '()'
# Scan the string from left to right
# record the number of open '(' as d
# 
# When saw '()', add 2^(d-1) to the answer
# 
# 'Convert' the original string into a set of full balanced strings.
# T: O(n)
# S: O(1)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = 0
        d = 0
        for i in range(len(S)):
            d += 1 if S[i] == '(' else -1
            if S[i] == '(' and S[i+1] == ')':
                ans += 1 << (d-1)
        return ans