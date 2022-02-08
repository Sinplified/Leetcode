class TrieNode:
    
    def __init__(self):
        self.children = [None]*26
        self.end = 0
        self.wordcount = 0

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
            curr.wordcount += 1
        
        curr.end += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        
        for c in word:
            pos = ord(c)-ord('a')
            
            if curr.children[pos] != None:
                curr = curr.children[pos]
            else:
                return 0
        
        return curr.end

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        
        for c in prefix:
            
            pos = ord(c)-ord('a')
            
            if curr.children[pos] != None:
                curr = curr.children[pos]
            
            else:
                return 0
        return curr.wordcount

    def erase(self, word: str) -> None:
        
        curr = self.root
        for c in word:
            pos = ord(c) - ord('a')
            
            if curr.children[pos].wordcount == 1:
                curr.children[pos] = None
                return
            
            curr = curr.children[pos]
            curr.wordcount -= 1
        
        curr.end -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)