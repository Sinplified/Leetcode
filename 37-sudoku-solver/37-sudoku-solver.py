class Solution:
    
    def isValid(self,board,row,col,c):
        for i in range(9):
            if board[i][col] == c:
                return False
            
            if board[row][i] == c:
                return False
            
            if board[3*(row//3)+i//3][3*(col//3)+i%3] == c:
                return False
            
        return True
    
    def solve(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in range(49,58,1):
                        if self.isValid(board,i,j,chr(c)):
                            board[i][j] = chr(c)
                            
                            if self.solve(board):
                                return True
                            
                            else:
                                board[i][j] = '.'
                    
                    return False
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)