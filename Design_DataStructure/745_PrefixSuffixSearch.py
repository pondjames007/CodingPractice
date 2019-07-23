# TIPS:

# Hash Table
# Good Speed
# Space Comlexity is High
# Store every prefixes and siffixes combination as key with idx as value
# key = {prefix}_{suffix}
class WordFilter:

    def __init__(self, words: List[str]):
        self.filters = {}
        
        for idx, word in enumerate(words):
            n = len(word)
            prefixes = ['']*(n+1)
            suffixes = ['']*(n+1)
            for i in range(n):
                prefixes[i+1] = prefixes[i] + word[i]
                suffixes[i+1] = word[n-i-1] + suffixes[i]
                
            for pre in prefixes:
                for suf in suffixes:
                    self.filters[pre + '_' + suf] = idx

    def f(self, prefix: str, suffix: str) -> int:
        key = prefix + '_' + suffix
        if key in self.filters: return self.filters[key]
        return -1
        

# Trie
# Speed is not that good (maybe it is because we constantly construct new nodes)
# Theoretically Time Complexity and Space Complexity are lower than using Hash Table
# At this time the query will become:
# key = {siffix}_{prefix}
# For every word, we insert {suffix}_{word} into trie
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        for idx, w in enumerate(words):
            key = "{" + w
            self.trie.insert(key, idx)
            for j in range(len(w)):
                key = w[len(w)-j-1] + key
                self.trie.insert(key, idx)

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.startWith(suffix + '{' + prefix)

class Trie:
    def __init__(self):
        self.root = [{}, 0]
        
    def insert(self, word, idx):
        p = self.root
        for c in word:
            if c not in p[0]:
                p[0][c] = [{}, idx]
            p = p[0][c]
            p[1] = idx
        p[0]['#'] = True
    
    def find(self, word):
        p = self.root
        for c in word:
            if c not in p[0]: return None
            p = p[0][c]
        return p
    
    def startWith(self, prefix):
        p = self.find(prefix)
        if p: return p[1]
        return -1
    