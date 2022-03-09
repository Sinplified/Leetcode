class qsNode:
    def __init__(self,val,index):
        self.val = val
        self.index = index
        self.prev = None
        self.Next = None
    
class qstack:
    def __init__(self,k):
        self.head = qsNode(-1,-1)
        self.tail = qsNode(-1,-1)
        self.head.Next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.k = k
        
    def tailInsert(self,Node):
        p = self.tail.prev
        p.Next = Node
        Node.prev = p
        Node.Next = self.tail
        self.tail.prev = Node
        self.size += 1
        
    def popTail(self):
        p = self.tail.prev
        p.prev.Next = self.tail
        self.tail.prev = p.prev
        self.size -=1
    
    def Headpop(self):
        n = self.head.Next
        n.Next.prev = self.head
        self.head.Next = n.Next
        self.size -= 1
    
    def Tail(self):
        return self.tail.prev.val
    
    def Head(self):
        return self.head.Next.val
    
    def Insert(self,val,index):
        Node = qsNode(val,index)
        
        if self.size==0:
            self.tailInsert(Node)
            return
        
        if self.head.Next.index == index - self.k:
            self.Headpop()
        
        while self.size>0 and self.Tail()<val:
            self.popTail()
        
        self.tailInsert(Node)
        return
        

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ll = qstack(k)
        ans = [0]*(len(nums)-k+1)
        
        for i in range(len(nums)):
            ll.Insert(nums[i],i)
            if i+1>=k:
                ans[i+1-k] = ll.Head()
        
        return ans
        
        
        
        
        
        
        
        
        