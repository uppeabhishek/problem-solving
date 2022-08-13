class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.dict = defaultdict(list)

    def addEdge(self, u, v):
        self.dict[u].append(v)
        self.dict[v].append(u)
    
    def dfs_helper(self, u, visited):
        
        visited.add(u)
        
        for v in self.dict[u]:
            if v not in visited:
                self.dfs_helper(v, visited)
            
    
    def dfs(self):
        
        visited = set()
        
        cnt = 0
        
        for i in range(self.edges):
            if i not in visited:
                cnt += 1
                self.dfs_helper(i, visited)
        
        return cnt
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = Graph(n)
        for edge in edges:
            g.addEdge(edge[0], edge[1])
        
        return g.dfs()
        
        
        
        
        