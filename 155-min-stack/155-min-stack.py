class MinStack:

    def __init__(self):
        
        self.primary_stack = []
        self.secondary_stack = []

    def push(self, val: int) -> None:
        
        self.primary_stack.append(val)
        if len(self.secondary_stack)==0 or val <= self.secondary_stack[-1]:
            self.secondary_stack.append(val)

    def pop(self) -> None:
        
        if self.primary_stack[-1] == self.secondary_stack[-1]:
            self.secondary_stack.pop()
            
        self.primary_stack.pop()

    def top(self) -> int:
        
        return self.primary_stack[-1]

    def getMin(self) -> int:
        return self.secondary_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()