#User function Template for python3
from typing import List
class Solution:
    
    def solve(self,i:int,s:str,f:List[str],ans:List[str]):
        
        if i == len(s) :
            if len(f) != 0:
                ans.append(''.join(f))
            return
        
        f.append(s[i])
        self.solve(i+1,s,f,ans)
        
        f.pop()
        self.solve(i+1,s,f,ans)
    
	def AllPossibleStrings(self, s):
		# Code here
		f = []
		
		ans = []
		self.solve(0,s,f,ans)
		ans.sort()
		
		return ans
		
		
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends