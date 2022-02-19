from queue import Queue
class MyStack:

    def __init__(self):
        
        self.q = Queue(maxsize = 100)

    def push(self, x: int) -> None:
        q1 = self.q
        q1.put(x)
        sz = q1.qsize()
        while(sz>1):
            q1.put(q1.get())
            sz -= 1
    

    def pop(self) -> int:
        return self.q.get()

    def top(self) -> int:
        return self.q.queue[0]

    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()