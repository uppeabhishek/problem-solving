from copy import deepcopy
class Graph:
    def __init__(self, size):
        self.graph = defaultdict(list)
        for i in range(size):
            self.graph[i] = []
        
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, u, visited, recursion_stack):
                
        visited[u] = True
        recursion_stack[u] = True
        
        for v in self.graph[u]:
            if not visited[v]:
                if self.DFSUtil(v, visited, recursion_stack):
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
                if self.DFSUtil(key, visited, recursion_stack):
                    return True
        return False
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = Graph(numCourses)
        for p in prerequisites:
            g.addEdge(p[1], p[0])
        
        return not g.DFSCycle()