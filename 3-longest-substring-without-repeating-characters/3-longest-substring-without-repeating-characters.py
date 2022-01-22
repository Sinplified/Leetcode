class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mpp= [-1]*256
        left,right = 0,0
        n = len(s)
        Len = 0
        while right<n :
            if mpp[ord(s[right])] != -1:
                left = max(mpp[ord(s[right])]+1,left)
            
            mpp[ord(s[right])] = right
            Len = max(Len,right-left+1)
            right +=1
        
        return Len