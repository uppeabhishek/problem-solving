class Solution:
    
    def DFS(self, u, color, graph):
        
        if u not in color:
            color[u] = 0
        
        for v in graph[u]:
            if v not in color:
                color[v] = color[u] ^ 1
                if not self.DFS(v, color, graph):
                    return False
            elif color[v] == color[u]:
                return False
            
        return True
        
        
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = defaultdict(int)
        
        n = len(graph)
        
        for i in range(n):
            if not self.DFS(i, color, graph):
                return False
        
        return True
            
        
        