class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s,i,i)
            len2 = self.expandAroundCenter(s,i,i+1)
            Len = max(len1,len2)
            
            if Len>end-start:
                start = i - (Len-1)//2
                end = i + (Len//2)
            
        return s[start:end+1]
    
    def expandAroundCenter(self,s,left,right):
        L,R = left,right
        while L>=0 and R<len(s) and s[L]==s[R]:
            L-=1
            R+=1
        
        return R-L-1