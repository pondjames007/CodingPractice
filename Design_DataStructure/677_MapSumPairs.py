# TIPS:
# * Use TRIE
# * find the rest with prefix: use stack BFS and check the type to prevent termination node be counted as character node
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.getSum(prefix)
        
class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, key, val):
        p = self.root
        for c in key:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['#'] = val
        
    def find(self, word):
        p = self.root
        for c in word:
            if c not in p:
                return False
            p = p[c]
        return p
    
    def getSum(self, prefix):
        num = 0
        stack = [self.find(prefix)]
        while stack:
            node = stack.pop()
            if type(node) is not dict: continue
            if '#' in node: num += node['#']
            stack += list(node.values())
        return num