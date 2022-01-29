#User function Template for python3

class Solution:
    def allPaths(self,m,n,i,j,path,ans):
        if i==n-1 and j==n-1:
            ans.append(''.join(path))
            return
        
        m[i][j] = 0
        
        if i+1<n and m[i+1][j]!= 0:
            path.append('D')
            self.allPaths(m,n,i+1,j,path,ans)
            path.pop()
            
        if j-1>=0 and m[i][j-1]!= 0:
            path.append('L')
            self.allPaths(m,n,i,j-1,path,ans)
            path.pop()
        
        if j+1<n and m[i][j+1]!= 0:
            path.append('R')
            self.allPaths(m,n,i,j+1,path,ans)
            path.pop()
        
        if i-1>=0 and m[i-1][j]!= 0:
            path.append('U')
            self.allPaths(m,n,i-1,j,path,ans)
            path.pop()
        
        m[i][j] = 1
    
    def findPath(self, m, n):
        if m[0][0] == 0:
            return []
        
        ans = []
        self.allPaths(m,n,0,0,[],ans)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends