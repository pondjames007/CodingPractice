# TIPS:
# * BFS / bidirection BFS
# * "brute force-ish" change a-z on every bit
from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList: return 0
        
        l = len(beginWord)
        steps = {beginWord: 1}
        q = deque([beginWord])
        
        while len(q) > 0:
            word = q.popleft()
            step = steps[word]
            
            for i in range(l):
                c = word[i]
                
                for t in string.ascii_lowercase:
                    if t == c: continue
                    new_word = word[:i] + t + word[i+1:]
                    
                    if new_word == endWord: return step + 1
                    if new_word not in wordList: continue
                        
                    wordList.remove(new_word)
                    steps[new_word] = step + 1
                    q.append(new_word)
                    
        return 0

# bidirection BFS
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        
        if endWord not in wordList: return 0
        
        l = len(beginWord)
        steps = {beginWord: 1, endWord: 1}
        q = deque([beginWord])
        p = deque([endWord])
        
        while q and p:
            if len(p) > len(q):
                p, q = q, p
                
            word = q.popleft()
            step = steps[word]
            
            for i in range(l):
                c = word[i]
                
                for t in string.ascii_lowercase:
                    if t == c: continue
                        
                    new_word = word[:i] + t + word[i+1:]
                    
                    if new_word == p[-1]: return step + steps[new_word]
                    if new_word not in wordList: continue
                        
                    wordList.remove(new_word)
                    steps[new_word] = step + 1
                    q.append(new_word)
                    
        return 0