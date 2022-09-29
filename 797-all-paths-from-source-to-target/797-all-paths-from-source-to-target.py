from copy import copy
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFS(self, src, dest, visited, current, result):
        
        current.append(src)
                
        if src == dest:
            result.append(copy(current))
            return
        
        for v in self.graph[src]:
            self.DFS(v, dest, visited, current, result)
            current.pop()
    
    def getGraph(self):
        return self.graph
    
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        
        g = Graph()
        
        for i, val in enumerate(graph):
            for v in val:
                g.addEdge(i, v)
                
        result = []
        
        g.DFS(0, n - 1, set(), [], result)
        
        return result