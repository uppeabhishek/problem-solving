class Graph:
    
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.root[x] == x:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        
        if x != y:
            if self.rank[x] == self.rank[y]:
                self.root[y] = self.root[x]
                self.rank[x] += 1
            elif self.rank[x] > self.rank[y]:
                self.root[y] = x
            else:
                self.root[x] = y

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        
        g = Graph(n)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    g.union(i, j)
        
        
        res = set()
        
        for i in range(n):
            res.add(g.find(i))
        
        return len(res)
                
            
            
            
            
        