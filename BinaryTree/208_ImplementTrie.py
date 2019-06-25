# TIPS:
# * Every level is a HashTable/Dict
# * Every level is a letter
# * Set a label at the end of the word letter node


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['#'] = True # Label the node when it is the last letter of the word to show it is in the dictionary

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # Directly do it
        p = self.root
        for c in word:
            if c not in p:
                return False
            p = p[c]
        
        if '#' in p:
            return True
        else:
            return False
        
        # Another Way to do by using find()
        node = self.find(word)
        return node is not None and '#' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # Directly do it
        p = self.root
        for c in prefix:
            if c not in p:
                return False
            p = p[c]
        return True

        # Another Way to do by using find()
        return self.find(prefix) is not None


    def find(self, prefix: str) -> dict:
        """
        Returns the trie node start of prefix, if there is no word in the trie 
           that starts with the given prefix returns None
        """

        p = self.root
        for c in prefix:
            if c not in p: return None
            p = p[c]
        return p