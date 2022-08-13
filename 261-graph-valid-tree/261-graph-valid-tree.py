class Graph:
    
    def __init__(self, edges):
        self.edges = edges
        self.dict = defaultdict(list)
    
    def addEdge(self, u, v):
        self.dict[u].append(v)
        self.dict[v].append(u)

        
    def dfsHelper(self, u, visited, parent):
                
        visited[u] = True
        
        for v in self.dict[u]:
            if not visited[v]:
                if self.dfsHelper(v, visited, u):
                    return True
            else:
                if v != parent:
                    return True
        
        return False
    
    def dfs(self):
        visited = [False] * self.edges
        recursion_stack = [False] * self.edges
        
        for u in range(self.edges):
            if visited[u] == False:
                res = self.dfsHelper(u, visited, -1)
                
                if res:
                    return False
                
                for v in visited:
                    if not v:
                        return False
                
        return True
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = Graph(n)
        
        for u, v in edges:
            g.addEdge(u, v)
            
        return g.dfs()
        
