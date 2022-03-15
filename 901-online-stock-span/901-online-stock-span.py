class StockSpanner:

    def __init__(self):
        
        self.stack = [(-1,-1)]
        self.insert_number = -1

    def next(self, price: int) -> int:
        
        self.insert_number += 1
        
        if self.stack[-1][0] == -1:
            self.stack.append((price,self.insert_number))
            return 1
            
        while self.stack[-1][0]!= -1 and self.stack[-1][0] <= price:
            
            self.stack.pop()
        
        span = self.insert_number - self.stack[-1][1]
        self.stack.append((price,self.insert_number))
        
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)