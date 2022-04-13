class Solution:
    
    def say(self,s):
        
        ans = []
        curr_freq = 1
        
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                ans.append(str(curr_freq) + s[i-1])
                curr_freq = 1
            
            else:
                curr_freq += 1
        
        ans.append(str(curr_freq)+s[-1])
        return ''.join(ans)
        
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return '1'
        
        what_to_say = self.countAndSay(n-1)
        
        return self.say(what_to_say)
        