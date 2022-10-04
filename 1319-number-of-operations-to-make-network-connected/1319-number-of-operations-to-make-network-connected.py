class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSHelper(self, u, visited):
        visited.add(u)
        
        for v in self.graph[u]: 
            if v not in visited:
                self.DFSHelper(v, visited)
            
    def DFS(self):
        visited = set()
        self.separateConnections = 0
        
        for i in range(self.n):
            if i not in visited:
                self.separateConnections += 1
                self.DFSHelper(i, visited)
                
        return self.separateConnections - 1
        
    def getGraph(self):
        return self.graph
    
class Solution:
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n - 1:
            return -1
        
        g = Graph(n)
        
        for i, j in connections:
            g.addEdge(i, j)
            g.addEdge(j, i)

        return g.DFS()