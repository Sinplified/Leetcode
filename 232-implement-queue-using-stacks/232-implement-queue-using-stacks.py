from queue import LifoQueue

class MyQueue:

    def __init__(self):
        self.stack1 = LifoQueue(maxsize = 100)
        self.stack2 = LifoQueue(maxsize = 100)
        self.curr_con = True
    
    def can_pop(self):
        return  not self.curr_con
    
    def can_push(self):
        return self.curr_con
    
    def reverse(self):
        s1 = self.stack1
        s2 = self.stack2
        
        while not s1.empty():
            s2.put(s1.get())
        
        self.stack1,self.stack2 = s2,s1
        self.curr_con = not self.curr_con

    def push(self, x: int) -> None:
        if not self.can_push():
            self.reverse()
        
        self.stack1.put(x)

    def pop(self) -> int:
        if not self.can_pop():
            self.reverse()
        
        return self.stack1.get()

    def peek(self) -> int:
        if not self.can_pop():
            self.reverse()
        
        return self.stack1.queue[-1]

    def empty(self) -> bool:
        return self.stack1.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()