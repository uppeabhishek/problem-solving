class Graph:
    def __init__(self, n):
        self.parent = [-1] * n
        self.n = n
        self.graph = defaultdict(list)
    
    def getParent(self, node):
        if self.parent[node] == -1:
            return node
        
        return self.getParent(self.parent[node])
    
    def addParent(self, u, parent):
        self.parent[u] = parent
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.addParent(v, u)
        
    def DFS(self):
        result = set()
        for i in range(self.n):
            if i not in result:
                result.add(self.getParent(i))
        
        return result
        
    
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        g = Graph(n)
        
        for u, v in edges:
            g.addEdge(u, v)
        
        return g.DFS()
            
        
        