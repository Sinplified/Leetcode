class Solution:
    
    def calculateZ(self,Input:str,n:int):
        z =[0]*len(Input)
        left = right = 0
        
        for k in range(len(Input)):
            if k>right:
                left = right = k
                while right<len(Input) and Input[right] == Input[right-left]:
                    right += 1
                
                z[k] = right - left
                right -= 1
            else:
                k1 = k - left
                
                if z[k1] < right-k+1:
                    z[k] = z[k1]
                
                else:
                
                    left = k
                    while right<len(Input) and Input[right] == Input[right - left]:
                        right +=1
                    
                    z[k] = right-left
                    right -= 1
                
                
            
            if z[k] == n:
                return k-n-1
    
        return -1
        
    def matchPattern(self,text:str,pattern:str) -> int :
        
        newString = pattern + '$' + text
        
        return self.calculateZ(newString,len(pattern))
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0 or needle == haystack:
            return 0
        
        return self.matchPattern(haystack,needle)
    
