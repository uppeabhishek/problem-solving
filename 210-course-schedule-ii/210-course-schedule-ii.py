class Graph:
    def __init__(self, size):
        self.graph = defaultdict(list)
        for i in range(size):
            self.graph[i] = []
        
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSCycleUtil(self, u, visited, recursion_stack):
        visited[u] = True
        recursion_stack[u] = True
        
        for v in self.graph[u]:
            if not visited[v]:
                if self.DFSCycleUtil(v, visited, recursion_stack):
                    return True
            elif recursion_stack[v]:
                return True
        
        recursion_stack[u] = False
        return False

    def DFSCycle(self):
        visited = [False] * len(self.graph)
        recursion_stack = [False] * len(self.graph)
                
        for key in self.graph:
            if not visited[key]:
                if self.DFSCycleUtil(key, visited, recursion_stack):
                    return True
        return False
    
    def DFSUtil(self, u, visited, result):
        visited.add(u)
        for v in self.graph[u]:
            if v not in visited:
                self.DFSUtil(v, visited, result)
        
        result.append(u)
        
    def DFS(self):
        result = []
        visited = set()
        for key in self.graph:
            if key not in visited:
                self.DFSUtil(key, visited, result)
        
        return result
        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = Graph(numCourses)
        
        for p in prerequisites:
            g.addEdge(p[0], p[1])
            
        if g.DFSCycle():
            return []
        
        return g.DFS()
            