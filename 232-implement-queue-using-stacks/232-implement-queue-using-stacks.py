from queue import LifoQueue

class MyQueue:

    def __init__(self):
        self.input = LifoQueue(maxsize = 100)
        self.output = LifoQueue(maxsize = 100)
        

    def push(self, x: int) -> None:
        self.input.put(x)

    def pop(self) -> int:
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())
        
        x = self.output.get()
        return x

    def peek(self) -> int:
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())
        
        return self.output.queue[-1]

    def empty(self) -> bool:
        return self.input.empty() and self.output.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()