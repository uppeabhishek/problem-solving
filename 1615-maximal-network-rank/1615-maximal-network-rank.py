class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
            
    def getGraph(self):
        return self.graph
    
    
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        g = Graph(n)
        
        for u, v in roads:
            g.addEdge(u, v)
        
        graph = g.getGraph()
        
        sets = []
                
        for i in range(n):
            new_set = set()
            for j in graph[i]:
                a, b = i, j
                if a > b:
                    a, b = b, a
                new_set.add((a, b))
            sets.append(new_set)
                    
        max_len = 0
        
        for i in range(n):            
            for j in range(i + 1, n):
                max_len = max(max_len, len(sets[i].union(sets[j])))
        
        return max_len
                
                
        