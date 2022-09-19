class Graph:
    
    def __init__(self, size):
        self.graph = defaultdict(set)
        self.size = size
        
    def addEdge(self, u, v):
        self.graph[u].add(v)
    
    def DFSCycleHelper(self, u, visited, recursion_stack):
        
        visited.add(u)
        recursion_stack.add(u)
        
        for v in self.graph[u]:
            if v not in visited:
                if self.DFSCycleHelper(v, visited, recursion_stack):
                    return True
            else:
                if v in recursion_stack:
                    return True
                
        recursion_stack.remove(u)
        return False
    
    def DFSCycle(self):
        visited = set()
        recursion_stack = set()
        
        for i in range(1, self.size + 1):
            if i in self.graph and i not in visited:
                if self.DFSCycleHelper(i, visited, recursion_stack):
                    return True
        
        return False
    
    def topologicalSortHelper(self, u, visited):
        if u in visited:
            return visited[u]
        
        cnt = 1
        
        for v in self.graph[u]:
            cnt = max(cnt, 1 + self.topologicalSortHelper(v, visited))
            
        visited[u] = cnt
        return visited[u]
            
    
    def topologicalSort(self):
        visited = defaultdict(int)
        max_cnt = 0
        
        for i in range(1, self.size + 1):    
            if i in self.graph and i not in visited:
                max_cnt = max(max_cnt, self.topologicalSortHelper(i, visited))
        return max_cnt
                
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        g = Graph(n)
        
        for u, v in relations:
            g.addEdge(u, v)
        
        if g.DFSCycle():
            return -1
    
        return g.topologicalSort()
        
        
        
        