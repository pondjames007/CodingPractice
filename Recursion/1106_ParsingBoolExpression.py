# TIPS:
# 
# Recursion
# 't' -> True
# 'f' -> False
# '!' -> !parse(e, ++s)
# '&' -> True & parse(e, ++s) & parse(e, ++s) until e[s] == ')'
# '|' -> False | parse(e, ++s) | parse(e, ++s) until e[s] == ')'
# T: O(n)
# S: O(n)
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parse(exp):
            ch = exp[self.s]
            self.s += 1 # skip '('

            if ch == 't': return True
            if ch == 'f': return False
            if ch == '!':
                self.s += 1 # skip '('
                ans = not parse(exp)
                self.s += 1 # skip ')'
                return ans

            is_and = ch == '&'
            ans = is_and
            self.s += 1 # skip '('
            while True:
                if is_and: ans &= parse(exp)
                else: ans |= parse(exp)

                if exp[self.s] == ')': 
                    self.s += 1 # move to next
                    break

                self.s += 1 # move to next (skip ',')
            return ans
        
        
        self.s = 0
        
        return parse(expression)
    
    