class Node:
    def __init__(self):
        self.links = [None,None]
    
    def containskey(self,ind):
        return self.links[ind] != None
    
    def get(self,ind):
        return self.links[ind]
    
    def put(self,ind,node):
        self.links[ind] = node
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self,num):
        node = self.root
        for i in range(31,-1,-1):
            bit = (num>>i)&1
            
            if not node.links[bit]:
                node.links[bit] = Node()
            
            node = node.links[bit]
    
    def getMax(self,num):
        node = self.root
        maxNum = 0
        
        for i in range(31,-1,-1):
            bit = (num>>i)&1
            if node.links[1-bit]:
                maxNum = maxNum | (1<<i)
                node = node.links[1-bit]
            
            else:
                node = node.links[bit]
        
        return maxNum
            
            

class Solution:
    def maximizeXor(self, arr : List[int], queries: List[List[int]]) -> List[int]:
        arr.sort()
        offlineQueries = []
        m = len(queries)
        for i in range(m):
            offlineQueries.append([queries[i][1],queries[i][0],i])
        
        offlineQueries.sort(key = lambda x: x[0])
        
        ind = 0
        n = len(arr)
        trie = Trie()
        ans = [-1]*m
        
        for i in range(m):
            while (ind<n and arr[ind] <= offlineQueries[i][0]):
                trie.insert(arr[ind])
                ind +=1
            
            queryInd = offlineQueries[i][2]
            
            if ind != 0:
                ans[queryInd] = trie.getMax(offlineQueries[i][1])
            
            else:
                ans[queryInd] = -1
            
        return ans
        
        