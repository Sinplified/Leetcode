class Solution:
    
    def __init__(self):
        self.BASE = 10**6
    
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle)==0 or needle==haystack:
            return 0
        
        return self.Rabin_karp(haystack,needle)
        
    def Rabin_karp(self,source:str,target:str)-> int :
        
        m = len(target)
        power = 1
        
        for i in range(m):
            power = (power*31)%(self.BASE)
        
        targetCode = 0
        for i in range(m):
            targetCode = (targetCode*31 + ord(target[i]) - 96)%(self.BASE)
        
        hashcode = 0
        
        
        for i in range(len(source)):
            
            hashcode = (hashcode*31 + ord(source[i])-96)%(self.BASE)
            
            if i<m-1:
                continue
            
            if i>=m:
                hashcode = (hashcode - (ord(source[i-m])-96)*power)%(self.BASE)
        
            if hashcode<0 :
                hashcode += BASE

            if hashcode == targetCode:
                if source[i-m+1: i+1] == target:
                    return i-m+1
        
        return -1
        