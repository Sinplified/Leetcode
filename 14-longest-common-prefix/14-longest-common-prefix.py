class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        s0 = 0
        sn = len(strs[0])
        
        for i in range(1,len(strs)):
            
            sn = min(sn,len(strs[i]))
            for j in range(sn):
                if (strs[0][j]!=strs[i][j]):
                    sn = j
                    break
            
            if sn==0:
                return ''
        
        return strs[0][0:sn]