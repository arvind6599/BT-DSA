
# stores the labels of each node to easily traverse all verteices
l=[]

def maze(MazeMatrix,start,finish):
    #MazeMatrix is a binary matrix (2D list of lists)
    #start & finish are tuples containing the starting and finishing point indices e.g. (1,1) & (5,5)
    import networkx as nx 
    #import matplotlib.pyplot as plt
    #import statements, function body
    
    def MazeMatrix2Graph(MazeMatrix):
        #MazeMatrix is a binary matrix (2D list of lists)

        #function body

        MazeGraph=nx.Graph()
        m=len(MazeMatrix)
        n=len(MazeMatrix[0])
        M=MazeMatrix
        
        #Makes the graaph and also initializes the visited value as False
        
        for i in range(m):
            for j in range(n):
                if(MazeMatrix[i][j]==1):
                    MazeGraph.add_node((i,j))
                    l.append((i,j))
                    if(i!=0 and M[i-1][j]==1):
                        MazeGraph.add_edge((i,j),(i-1,j))
                        l.append((i-1,j))
                    if(j!=0 and M[i][j-1]==1):
                        MazeGraph.add_edge((i,j),(i,j-1))
                        l.append((i,j-1))
                    if(i<m-1 and M[i+1][j]==1):
                        MazeGraph.add_edge((i,j),(i+1,j))
                        l.append((i+1,j))
                    if(j<n-1 and M[i][j+1]==1):
                        MazeGraph.add_edge((i,j),(i,j+1))
                        l.append((i,j+1))
        
        #nx.draw(MazeGraph,with_labels=True)
        #plt.show()
     
        return MazeGraph #a networkx graph whose nodes represent the '1's in the input matrix. node labels are tuples.
    
    def MazeAnswerBFS(MazeGraph,start,finish):
        #MazeGraph is a networkx graph 
        #start and finish are tuples containing the starting and finishing point indices

        
        
        #function body 
        
        v={}
        queue = [] 
        shortest_path=[]
        
        #initializing all visited values to False
        for i in l:
            v[i]=False

        queue.append(start)
        v[start]=True
  
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            
            for i in list(MazeGraph.neighbors(s)): 
                if v[i]==False:
                    MazeGraph.nodes[i]['parent']=s
                    queue.append(i) 
                    v[i]=True
                
                if i == finish:
                    shortest_path.append(finish)
                    while(i!=start):
                        shortest_path.append(MazeGraph.nodes[i]['parent'])
                        i=MazeGraph.nodes[i]['parent']
                    
                    shortest_path.reverse()

                    return shortest_path
                    
                    
                
         #list of tuples containing indices of the points in the answer
    
    def MazeComponentsDFS(MazeGraph):
        #MazeGraph is a networkx graph
        
        #function body 
        v={} #dictonary for visited status
        for i in l:
            v[i]=False
        
        def dfs(i,c,v):
            
            for x in MazeGraph.neighbors(i) :
                if v[x] == False :
                  v[x] = True
                  c.append(x)
                  dfs(x,c,v)
            return c
        
        
        
        components=[]
        for u in l:
            if v[u] == False :
                c=[u]
                v[u] = True
                dfs(u,c,v)
                components.append(c)
         
        return components #list of lists, each containing tuples of the indices of points in that component
    
    #function body
    G=MazeMatrix2Graph(MazeMatrix)
    a=MazeAnswerBFS(G,start,finish)
    b=MazeComponentsDFS(G)



    print(a)
    print('\n')
    print(b)
    #a is the output of MazeAnswerBFS and b is the output of MazeComponentsDFS

if __name__ == '__main__':
    #DO NOT MODIFY THE FOLLOWING
    hw3bmaze=    [[1,0,1,1,0,1],
                  [1,1,0,0,0,0],
                  [0,1,0,1,1,1],
                  [0,1,1,1,0,1],
                  [1,0,0,1,1,1],
                  [1,1,0,0,0,1],
                  [0,0,1,1,0,1]]
    
    hw3bstart=(0,0)
    hw3bfinish=(6,5)
    print(maze(hw3bmaze,hw3bstart,hw3bfinish))
    
#output for this example should be:
#[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5)]
#[[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5), (3, 5), (2, 5), (2, 4), (2, 3)], [(0, 2), (0, 3)], [(0, 5)], [(4, 0), (5, 0), (5, 1)], [(6, 2), (6, 3)]]
