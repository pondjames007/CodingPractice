# TIPS:
# * Trie data structure: https://zh.wikipedia.org/wiki/Trie
# * No. 208 Implement Trie

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort()
        
        for word in words:
            trie.insert(word)
        
        best = 0
        for word in words:
            if trie.find(word) and len(word) > best:
                best = len(word)
                ans = word
        return ans

class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, word):
        p = self.root
        
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['#'] = True
        
    def find(self, word):
        p = self.root
        
        for c in word:
            if c not in p: return False
            p = p[c]
            if '#' not in p: return False
        return True