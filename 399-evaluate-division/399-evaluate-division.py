class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, a, b, val):
        self.graph[a].append((b, val))
    
    def DFS(self, src, target, result, visited):
                       
        visited.add(src)
        
        if src == target:
            return True
        
        for u in self.graph[src]:
            key, val = u
                        
            if key in self.graph and key not in visited:
                result.append(val)
                if self.DFS(key, target, result, visited):
                    return True
                else:
                    result.pop()
            
        return False

    def getGraph(self):
        return self.graph
    
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        g = Graph()
        
        for i in range(len(equations)):
            a, b = equations[i]
            g.addEdge(a, b, values[i])
            g.addEdge(b, a, 1 / values[i])
        
        result = []
        
        for a, b in queries:            
            if a == b:
                if a in g.getGraph():
                    result.append(1)
                else:
                    result.append(-1)
            else:
                values = []
                visited = set()
                res = g.DFS(a, b, values, visited)

                if res:
                    current = 1
                    for value in values:
                        current = value * current
                    result.append(current)
                else:
                    result.append(-1)      
        
        return result
            
            
            
        
        