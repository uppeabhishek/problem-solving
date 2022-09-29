class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def DFS(self, src, dest, visited):
        
        visited.add(src)
        
        if src == dest:
            return True
        
        for v in self.graph[src]:
            if v in self.graph and v not in visited:
                if self.DFS(v, dest, visited):
                    return True
        
        return False
        
    
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        g = Graph()
        
        for u, v in edges:
            g.addEdge(u, v)
        
        return g.DFS(source, destination, set())
        
    