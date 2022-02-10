class TrieNode:
    
    def __init__(self):
        self.children = [None]*26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.counts = 0

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            pos = ord(c)-ord('a')
            if curr.children[pos] == None:
                NewNode = TrieNode()
                curr.children[pos] = NewNode
                self.counts+=1
            curr = curr.children[pos]
        curr.end = True
    
    def count(self):
        return self.counts


class Solution:
    def countDistinct(self, s: str) -> int:
        T = Trie()
        n = len(s)
        
        for i in range(n):
            T.insert(s[i:])
        
        return T.count()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        