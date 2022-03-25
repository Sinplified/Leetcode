class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        prev = roman_dict[s[0]]
        ans = 0
        for i in range(1,len(s)):
            curr = roman_dict[s[i]]
            if curr>prev:
                ans -= prev
            
            else:
                ans+=prev
            
            prev = curr
        
        ans += prev
        return ans