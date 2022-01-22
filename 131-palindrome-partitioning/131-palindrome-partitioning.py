class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        Len = len(s)
        dp = [[False for i in range(Len)] for j in range(Len)]
        result = []
        currentList = []
        self.dfs(result,s,0,currentList,dp)
        return result
    
    def dfs(self,result,s,start,currentList,dp):
        if start>= len(s):
            result.append(currentList[:])
        
        for ind in range(start,len(s)):
            if (s[start]==s[ind]) and (ind-start<=2 or dp[start+1][ind-1]):
                dp[start][ind] = True
                currentList.append(s[start:ind+1])
                self.dfs(result,s,ind+1,currentList,dp)
                currentList.pop()