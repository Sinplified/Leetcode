from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        stack = LifoQueue(maxsize = 10000)
        
        closing_bracket = [')',']','}']
        
        for bracket in s:
            if bracket in closing_bracket:
                if stack.empty():
                    return False
                
                top = stack.queue[-1]
                
                if((top == '(' and bracket == ')') or
                  (top == "[" and bracket == "]") or (top == "{" and bracket == '}')):
                    stack.get()
                else:
                    return False
                
            
            else:
                stack.put(bracket)
        
        
        return stack.empty()