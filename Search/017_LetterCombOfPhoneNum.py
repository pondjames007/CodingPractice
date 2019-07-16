# TIPS:
# make a dictionary to map digit and char
# go through all digits and find out all combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        n_to_c = {}
        char = [*string.ascii_lowercase]
        start = 0
        end = 0
        for i in range(2,10):
            start = end
            if i == 7 or i == 9:
                end += 4
            else:
                end += 3
            n_to_c[i] = char[start:end]
                
        ans = []
        
        self.lookup(n_to_c, digits, [], ans)
        
        return ans
    
        
    def lookup(self, dic, digits, path, ans):
        if not digits: 
            ans.append(''.join(path))
            return
        
        for c in dic[int(digits[0])]:
            self.lookup(dic, digits[1:], path + [c], ans)