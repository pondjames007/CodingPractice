# TIPS:
# * Use TRIE : SUPER SLOW
# * 

# TRIE implementation (not good)
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            p = self.root
            for c in word:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        l_word = list(word)
        for i in range(len(l_word)):
            org_l = l_word[i]
            for l in range(ord('a'), ord('z')+1):
                if chr(l) != org_l:
                    l_word[i] = chr(l)
                    word = "".join(l_word)
                    node = self.find(word)

                    if node is not None and '#' in node:
                        return True
            l_word[i] = org_l
        return False
    
    def find(self, prefix: str) -> dict:
        p = self.root
        for c in prefix:
            if c not in p: return None
            p = p[c]
        return p

# Fuzzy Match/Search
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_ = {}

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            for i in range(len(word)):
                c = word[i]
                word = word[:i] + '*' + word[i+1:]
                if word not in self.dict_:
                    self.dict_[word] = set()
                
                self.dict_[word].add(c)
                word = word[:i] + c + word[i+1:]

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for i in range(len(word)):
            c = word[i]
            word = word[:i] + '*' + word[i+1:]
            if word in self.dict_:
                char_set = self.dict_[word]
                if c not in char_set or len(char_set) > 1:
                    return True
            
            word = word[:i] + c + word[i+1:]
        
        return False