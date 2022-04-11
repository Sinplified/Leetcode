class Solution:
    
    def getLps(self,p,lps):
        l = 0
        index = 1
        m = len(p)
        
        while index<m:
            if p[index] == p[l]:
                l+=1
                lps[index] = l
                index += 1
            else:
                if l==0:
                    lps[index]=0
                    index += 1
                else:
                    l = lps[l-1]
        
        return lps
    
    def strStr(self, haystack: str, needle: str) -> int:
        
        n = len(haystack)
        m = len(needle)
        
        lps = [0]*m
        lps = self.getLps(needle,lps)
        
        
        index1 = index2 = 0
        
        while index1<n:
            
            if haystack[index1] == needle[index2]:
                index1 += 1
                index2 += 1
                
                if index2 == m:
                    return index1 - m
                
                if index1 == n:
                    return -1
            
            else:
                
                if index2 == 0:
                    index1 += 1
                    
                else:
                    index2 = lps[index2 - 1]
            
        return -1
    