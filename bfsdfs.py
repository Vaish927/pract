graph = {
  'p' : ['q','r','s'],
  'q' : ['p', 'r'],
  'r' : ['p','q','t'],
  's' : ['p'],
  't' : ['r']
}



visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = "->") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        

def dfs(visited, graph, node):  #function for dfs 
    visited.add(node)
    print (node,end="->")
    """ if node not in visited:
        print (node,end="->")
        visited.add(node) """
    for neighbour in graph[node]:
          if neighbour not in visited:
            dfs(visited, graph, neighbour)


ch=1
while(ch==1):
    print("\n1.BFS\n2.DFS")
    ip=int(input("Enter Your Choice:"))
    
    if(ip==1):
    
        print("Following is the Depth-First Search")
        bfs(visited, graph, 'p')
    
    
    elif(ip==2):
        print("\nFollowing is the Breadth-First Search")
        visit=set()
        dfs(visit, graph, 'p')    # function calling
        
    else:
        print("\nPlease Enter Valid Choice!")
        
    ch=int(input("Want To continue?(0/1)"))


    """
    
# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Function to perform DFS traversal on the graph on a graph
def DFS(graph, v, discovered):
 
    discovered[v] = True            # mark the current node as discovered
    print(v, end=' ')               # print the current node
 
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:       # if `u` is not yet discovered
            DFS(graph, u, discovered)
 
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
 
    # total number of nodes in the graph (labelled from 0 to 12)
    n = 13
 
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n
 
    # Perform DFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)
    """