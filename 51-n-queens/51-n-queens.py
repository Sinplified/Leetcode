class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        curr = [[None for i in range(n)] for j in range(n)]
        ans = []
        self.Queens(0,curr,ans,n)
        return ans
  
    def filler(self,curr,row,col,to_fill,val):
        n = len(curr) 
        
        r = row+1
        c = col-1
        
        for i in range(n):
            if curr[row][i] == to_fill:
                curr[row][i] = val
        
        for i in range(row,n):
            if curr[i][col] == to_fill:
                curr[i][col] = val
        
        while r<n and c>=0:
            if curr[r][c] == to_fill:
                curr[r][c] = val
            r+=1
            c-=1
        
        row+=1
        col+=1
        while row<n and col<n:
            if curr[row][col] == to_fill:
                curr[row][col] = val
            row+=1
            col+=1

    def Queens(self,row,curr,ans,n):
        if row == n:
            ans1 = []
            for row in curr:
                row1 = ''
                for col in row:
                    if col !='Q':
                        row1 += '.'
                    else:
                        row1 += 'Q'
                ans1.append(row1)
                
            ans.append(ans1)
            
            return
            
        
        for col in range(n):
            if curr[row][col] == None:
                
                self.filler(curr,row,col,None,row)
                curr[row][col] = 'Q'
                
                self.Queens(row+1,curr,ans,n)
                
                curr[row][col] = None
                self.filler(curr,row,col,row,None)
    
