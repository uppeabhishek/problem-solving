class Graph:
    def __init__(self, n):
        self.graph = defaultdict(set)
        self.n = n
        
    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)
    
    def BFS(self):
        pass
    
    def getGraph(self):
        return self.graph
    
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]
        
        if n == 2:
            return [0, 1]
        
        g = Graph(n)
        
        for edge in edges:
            g.addEdge(edge[0], edge[1])
        
        graph = g.getGraph()
        
        leaves = []
        
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        allNodes = n
                
        while allNodes > 2:
            
            nextLeaves = []
            
            while len(leaves):
                
                leaf = leaves.pop()
                
                neighbor = graph[leaf].pop()
                                
                graph[neighbor].remove(leaf)
                allNodes -= 1
                
                if len(graph[neighbor]) == 1:
                    nextLeaves.append(neighbor)
            
            leaves = nextLeaves                
                
                
        return leaves
            
            
            
            
                
        
        