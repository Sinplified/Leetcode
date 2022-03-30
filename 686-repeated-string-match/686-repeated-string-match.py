import math

class Solution:
    
    def __init__(self):
        self.BASE = 10**6
        
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
            
            
    
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        if(A==B):
            return 1
        
        count = math.ceil(len(B)/len(A))
        source = A*count
        
        if source==B:
            return count
        if(self.Rabin_karp(source,B)!=-1):
            return count
        if(self.Rabin_karp(source+A,B)!=-1):
            return count+1
        
        return -1