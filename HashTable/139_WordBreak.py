# TIPS:
# * Cannot use search to do it -> exceed time
# * Dynamic Programming is the method
# 
# 先把字串s跟f都padding一位
# f[i] =1表示可以在第i位以前的字串可以被分解 ->
#       `f[i] := 1 if we can break s[1..i]`

# f[0] = 1 因為空字串一定可以被分解

# ```
# 	for i = 1 to n // 當字串長度為i的時候是否有解
# 		for j = 0 to i // 找字串長度為i時可以中間break的點
# 			f[i] = 1 if f[j] and s[j+1..i] in wordDict

# 	ans = f[n]
# ```

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        n = len(s)
        s = " " + s # s[1..n]
        f = [False] * (n+1)
        f[0] = True
        
        for i in range(n+1):
            for j in range(i):
                if f[j] == True:
                    new_s = s[j+1:i+1]
                    if new_s in word_dict:
                        f[i] = True
                        break
                        
        return f[n]



# Another method using Recursion to implement Dynamic Programming
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wbreak(s, word_dict, mem):
            # if the substring is in the memory (eg. is in dict), then return
            if s in mem: return mem[s]

            # if the substring is in the dict (first visit), put it in memory and return
            if s in word_dict: 
                mem[s] = True
                return mem[s]

            # Try every break point
            for j in range(1, len(s)+1):
                left = s[:j]
                right = s[j:]

                # find solution for s
                if right in word_dict and wbreak(left, word_dict, mem):
                    mem[s] = True
                    return mem[s]

            # No solution for s, memorize and return
            mem[s] = False
            return mem[s]
        
        
        word_dict = set(wordDict)
        mem_ = {}
        return wbreak(s, word_dict, mem_)