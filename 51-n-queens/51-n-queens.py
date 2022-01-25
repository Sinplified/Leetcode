class Solution:
    
    def solve(self,col,board,ans,leftrow,upperDiagonal,lowerDiagonal,n):
        if col==n:
            ans.append([''.join(row) for row in board])
            return
        
        for row in range(n):
            if ((leftrow[row]==0) and (lowerDiagonal[row+col]==0) and 
                (upperDiagonal[n-1+col-row]==0)):
                board[row][col] = 'Q'
                leftrow[row] = 1
                lowerDiagonal[row+col] = 1
                upperDiagonal[n-1+col-row] = 1
                self.solve(col+1,board,ans,leftrow,upperDiagonal,lowerDiagonal,n)
                board[row][col] = '.'
                leftrow[row] = 0
                lowerDiagonal[row+col] = 0
                upperDiagonal[n-1+col-row] = 0
                
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for i in range(n)] for j in range(n)]
        
        leftrow = [0]*n
        upperDiagonal = [0]*((2*n)-1)
        
        lowerDiagonal = [0]*((2*n)-1)
        self.solve(0,board,ans,leftrow,upperDiagonal,lowerDiagonal,n)
        
        return ans