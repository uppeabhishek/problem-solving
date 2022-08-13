from collections import deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(deque)
        
    def addEdge(self, a, b, name):
        self.graph[a].appendleft(b)
        self.graph[b].appendleft(a)
        
        self.graph[a].append(name)
        self.graph[b].append(name)
        
    def getGraph(self):
        return self.graph
    
    def DFSHelper(self, u, arr):
                
        arr.append(u)
        
        self.visited.add(u)
        
        if not self.name:
            self.name = self.graph[u][-1]
        
        for v in self.graph[u]:
            if v not in self.visited and v in self.graph:
                self.DFSHelper(v, arr)
        
    def DFS(self):
        self.visited = set([])
        
        result = []
                
        for key in self.graph.keys():
            if key not in self.visited:
                
                self.name = ''
                
                temp = []                
                self.DFSHelper(key, temp)
            
                temp.sort()
                
                temp = [self.name] + temp
                
                result.append(temp)

                
        return result
            
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        g = Graph()
        
        for account in accounts:
            for i in range(1, len(account) - 1):
                g.addEdge(account[i], account[i + 1], account[0])
        
        result = g.DFS()
                
        for account in accounts:
            if len(account) == 2:
                if account[1] not in g.getGraph():
                    result.append(account)
        
        return result
        
        