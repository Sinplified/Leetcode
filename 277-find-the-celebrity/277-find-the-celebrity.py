# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

from queue import Queue

class Solution:
    
    def check_knows(self,e,n):
        for i in range(n):
            if not knows(i,e):
                print(i,e)
                return False
        
        return True
    
    def check_notknows(self,e,n):
        for i in range(n):
            if i!=e and knows(e,i):
                return False
        
        return True
    
    def findCelebrity(self, n: int) -> int:
        q = Queue(maxsize=n)
        for i in range(1,n):
            if knows(0,i):
                q.put(i)
        
        if q.empty():
            return 0 if self.check_knows(0,n) else -1
        
        e = q.get()
        
        while not q.empty():
            if knows(e,q.queue[0]):
                e = q.get()
            else:
                q.get()
        
        if self.check_knows(e,n) and self.check_notknows(e,n):
            return e
        else:
            return -1