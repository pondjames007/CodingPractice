# TIPS:
# * Divide & Conquer
# * look for the operator and get left & right -> recursively do on left and right to get the answer

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if not input: return []
        
        if input.isdigit(): return [int(input)]
        
        res = []
        for i in range(len(input)):
            if input[i] not in {'+', '-', '*'}: continue
            
            left = self.diffWaysToCompute(input[:i])
            right = self.diffWaysToCompute(input[i+1:])
            
            for l in left:
                for r in right:
                    if input[i] == '+': res.append(l+r)
                    elif input[i] == '-': res.append(l-r)
                    elif input[i] == '*': res.append(l*r)
            
        return res