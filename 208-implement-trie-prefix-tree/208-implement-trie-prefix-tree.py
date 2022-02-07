class TrieNode:
    
    def __init__(self):
        self.children = [None]*26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            pos = ord(c)-ord('a')
            if curr.children[pos] == None:
                NewNode = TrieNode()
                curr.children[pos] = NewNode
                
            curr = curr.children[pos]
        
        curr.end = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        
        for c in word:
            pos = ord(c)-ord('a')
            
            if curr.children[pos] != None:
                curr = curr.children[pos]
            else:
                return False
        
        if curr.end:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        
        for c in prefix:
            
            pos = ord(c)-ord('a')
            
            if curr.children[pos] != None:
                curr = curr.children[pos]
            
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)