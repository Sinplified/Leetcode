from queue import Queue

class Solution:
    
    def Enqueue(self,Q,element,grid):
        i = element[0]
        j = element[1]
        t = element[2]
        m = len(grid)
        n = len(grid[0])
        
        if i-1>=0 and grid[i-1][j] == 1:
            Q.put((i-1,j,t+1))
            grid[i-1][j] = 2
            
        if j-1>=0 and grid[i][j-1]==1:
            Q.put((i,j-1,t+1))
            grid[i][j-1] = 2
        
        if i+1<m and grid[i+1][j] == 1:
            Q.put((i+1,j,t+1))
            grid[i+1][j] = 2
        
        if j+1<n and grid[i][j+1] == 1:
            Q.put((i,j+1,t+1))
            grid[i][j+1] = 2
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Q = Queue(maxsize = 100)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    Q.put((i,j,0))
        
        minutes = 0
        while not Q.empty():
            element = Q.get()
            self.Enqueue(Q,element,grid)
            minutes = element[-1]
    
        for row in grid:
            for ele in row:
                if ele == 1:
                    return -1

        return minutes