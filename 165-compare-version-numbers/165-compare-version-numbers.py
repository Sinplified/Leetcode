class Solution:
    
    def helper(self,version,ind):
        ind1 = ind
        while ind1<len(version) and version[ind1] != '.':
            
            ind1 += 1
        
        curr_v_r = int(version[ind:ind1])
        
        return curr_v_r,ind1
            
    
    def compareVersion(self, version1: str, version2: str) -> int:
        i = 0
        j = 0
        
        curr_v1_r = 0
        curr_v2_r = 0
        
        while i<len(version1) and j<len(version2):
            
            curr_v1_r,i = self.helper(version1,i)
            curr_v2_r,j = self.helper(version2,j)
            
            i+=1
            j+=1
            
            if curr_v2_r < curr_v1_r:
                return 1
            elif curr_v1_r < curr_v2_r:
                return -1
        
        while i<len(version1):
            curr_v1_r,i = self.helper(version1,i)
            i+=1
            if curr_v1_r>0:
                return 1
        
        while j<len(version2):
            
            curr_v2_r,j = self.helper(version2,j)
            j+=1
            
            if curr_v2_r>0:
                return -1
        
        return 0
            