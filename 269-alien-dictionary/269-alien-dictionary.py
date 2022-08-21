class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
    
    def addEdge(self, u, v):
        self.graph[u].add(v)

    def DFSHelper(self, v, result, visited, recursion):
        visited.add(v)
        recursion.add(v)

        for u in self.graph[v]:
            if u not in visited:
                if self.DFSHelper(u, result, visited, recursion):
                    return True
            elif u in recursion:
                return True

        result.appendleft(v)
        recursion.remove(v)
        return False
        
    def DFS(self):
        result = deque([])
        visited = set()
        recursion = set()
            
        for u in self.graph:
            if u not in visited:
                if self.DFSHelper(u, result, visited, recursion):
                    return ""
        
        return "".join(result)
    
    def getGraph(self):
        return self.graph
            
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        g = Graph()
        
        graph = g.getGraph()
        
        empty = True
        
        for w in words:
            for c in w:
                g.graph[c] = set()
        
        
        for i in range(len(words) - 1):
            l1, l2 = len(words[i]), len(words[i + 1])
            min_len = min(l1, l2)
            
            if l1 > l2 and words[i][0:min_len] == words[i + 1][0:min_len]:
                return ""
            
            for j in range(min_len):   
                current, nxt = words[i][j], words[i + 1][j]
                if current != nxt:
                    g.addEdge(words[i][j], words[i + 1][j])
                    break
            
        return g.DFS()
