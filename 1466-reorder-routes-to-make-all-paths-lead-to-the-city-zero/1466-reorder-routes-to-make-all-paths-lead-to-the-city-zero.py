class Graph:
    
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.original_graph = defaultdict(set)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.original_graph[u].add(v)
        
    def DFSHelper(self, u, visited):        
        visited.add(u)
        
        for v in self.graph[u]:
            if v not in visited:
                if u not in self.original_graph[v]:
                    self.cnt += 1
                self.DFSHelper(v, visited)
            
    def DFS(self):
        visited = set()
        self.cnt = 0
        self.DFSHelper(0, visited)
        return self.cnt
        
    
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        g = Graph(n)
        
        for i, j in connections:
            g.addEdge(i, j)
        
        return g.DFS()
        