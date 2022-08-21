class Graph:
    
    def __init__(self):
        self.graph = defaultdict(set)
    
    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)
    
    def getGraph(self):
        return self.graph
    
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0
        
        g = Graph()
        
        routes_list = [set(route) for route in routes]
        
        n = len(routes_list)
        
        for i in range(n):
            for j in range(i + 1, n):
                if len(routes_list[i].intersection(routes_list[j])):
                    g.addEdge(i, j)
        
        
        targets = set()
        
        queue = deque([])
        
        visited = set()

        
        for i in range(n):
            if target in routes_list[i]:
                targets.add(i)
            if source in routes_list[i]:
                queue.append((i, 1))
                visited.add(i)
        
        graph = g.getGraph()
        
        
        while len(queue):
            current, depth = queue.popleft()
            
            if current in targets:
                return depth
            
            for ele in graph[current]:
                if ele not in visited:
                    queue.append((ele, depth + 1))
                    visited.add(ele)
        
        return -1
            
        
        