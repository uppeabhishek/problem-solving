class Graph:
    
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.cnt = n

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
            
            self.cnt -= 1
            return True
        
        return False
            
    def getCount(self):
        return self.cnt
    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
                
        g = Graph(n)
        
        result = 0

        logs.sort(key = lambda k: k[0])
    
        for timestamp, x, y in logs:
            if g.union(x, y):
                result = timestamp
        
        return result if g.getCount() == 1 else -1            
        