class TrieNode:
    
    def __init__(self,data = None):
        self.data = data
        self.children = [None]*26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            
            if curr.children[ord(c)-ord('a')] == None:
                NewNode = TrieNode(c)
                curr.children[ord(c) - ord('a')] = NewNode
                
            curr = curr.children[ord(c)-ord('a')]
        
        curr.end = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        
        for c in word:
            
            if curr.children[ord(c)-ord('a')] != None:
                curr = curr.children[ord(c)-ord('a')]
            else:
                return False
        
        if curr.end:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        
        for c in prefix:
            if curr.children[ord(c)-ord('a')] != None:
                curr = curr.children[ord(c) - ord('a')]
            
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)