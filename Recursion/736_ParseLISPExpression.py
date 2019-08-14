# TIPS:
# 
# a valid expr:
#   ( ->
#       add  -> ' ' + expr1 + ' ' + expr2                               -> )
#       mult -> the same as add                                         -> )
#       let  -> ' ' + s1 + ' ' + e1 + ... + sn + ' ' + en + ' ' + expr  -> )
#   number 3 | -12 -> )
#   symbol x | a1  -> )

from collections import deque
class Solution:
    def evaluate(self, expression: str) -> int:
        self.scopes = deque()
        self.pos = 0

        return self.eval(expression)

    def eval(self, s):
        self.scopes.appendleft({})
        value = 0 # The return value of current expr

        if s[self.pos] == '(': self.pos += 1

        # command, variable or number
        token = self.getToken(s)

        if token == 'add':
            self.pos += 1
            v1 = self.eval(s)
            self.pos += 1
            v2 = self.eval(s)
            value = v1 + v2
        elif token == 'mult':
            self.pos += 1
            v1 = self.eval(s)
            self.pos += 1
            v2 = self.eval(s)
            value = v1 * v2
        elif token == 'let':
            var = ''
            # expecting " var1 exp1 var2 exp2 ... last_expr"
            while s[self.pos] != ')':
                self.pos += 1

                # Must be last_expr
                if s[self.pos] == '(':
                    self.pos += 1
                    value = self.eval(s)
                    break
                
                # Get a token, could be 'x' or '-12' for last_expr
                var = self.getToken(s)

                # End of let, var is last_expr
                if s[self.pos] == ')':
                    if var[0].isalpha():
                        value = self.getValue(var)
                    else:
                        value = int(var)
                    break

                # x -12 -> set x to -12 and store in the current scope and take it as the current return value
                self.pos += 1
                vlaue = self.scopes[0][var] = self.eval(s)
        
        elif token[0].isalpha(): 
            value = self.getValue(token) # symbol
        else:
            value = int(token) # number
        
        if self.pos < len(s):
            if s[self.pos] == ')': self.pos += 1
            self.scopes.popleft()
        return value

    # Get a token from current position
    # "let x" -> "let"
    # "-12 (add x y)" -> '-12'
    def getToken(self, s):
        token = ''
        while self.pos < len(s):
            if s[self.pos] == ')' or s[self.pos] == ' ': break

            token += s[self.pos]
            self.pos += 1
            
        return token

    def getValue(self, symbol):
        for scope in self.scopes:
            if symbol in scope: return scope[symbol]
        return 0