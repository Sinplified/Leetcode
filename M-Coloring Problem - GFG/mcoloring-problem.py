#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.

def isSafe(graph,v,colour,c,V):
    for i in range(V):
        if graph[v][i] == 1 and colour[i] == c:
            return False
        
    return True

def graphcolourUtil(graph,m,colour,v,V):
    if v==V:
        return True
        
    for c in range(1,m+1):
        
        if isSafe(graph,v,colour,c,V):
            colour[v] = c
            
            if graphcolourUtil(graph,m,colour,v+1,V):
                return True
            
            colour[v] = 0
        
    return False
    

def graphColoring(graph, k, V):
    
    colour = [0]*V
    return graphcolourUtil(graph,k,colour,0,V)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends