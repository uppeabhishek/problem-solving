class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSHelper(self, u, safe):        
        
        if u in safe:
            return safe[u]
        
        safe[u] = False
        
        for v in self.graph[u]:
            if not self.DFSHelper(v, safe):
                return False
        
        safe[u] = True
        return safe[u]
        
        
    
    def DFS(self):
        
        visited = set()
        safe = defaultdict(bool)

        result = []
        
        for i in range(self.n): 
            if self.DFSHelper(i, safe):
                result.append(i)
        
        return result
    
    def getGraph(self):
        return self.graph
    
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
            
        g = Graph(n)
        
        for i in range(n):
            for j in graph[i]:
                g.addEdge(i, j)
            
        return g.DFS()
        
            
        
        
        