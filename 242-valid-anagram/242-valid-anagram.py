class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26
        
        for c in s:
            ind = ord(c) - ord('a')
            freq[ind] += 1
        
        for c in t:
            ind = ord(c) - ord('a')
            freq[ind] -= 1
        
        
        for i in freq:
            if i != 0:
                return False
        
        return True