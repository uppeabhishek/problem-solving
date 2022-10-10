class Graph:
    def __init__(self, n):
        self.graph = defaultdict(set)
        self.n = n
    
    def addEdge(self, u, v):
        self.graph[u].add(v)
    
    def getGraph(self):
        return self.graph
        
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        g = Graph(n)
        
        for u, v in trust:
            g.addEdge(u, v)
        
        graph = g.getGraph()
        
        # out degree
        out_degree = [0] * n
        for i in range(1, n + 1):
            out_degree[i - 1] = len(graph[i])
        
        index = -1        
        for i, ele in enumerate(out_degree):
            if ele == 0:
                if index == -1:
                    index = i + 1
                else:
                    return -1
        
        if index == -1:
            return -1
        
        
        for i in range(1, n + 1):
            if i != index:
                if index not in graph[i]:
                    return -1
        
        return index
        