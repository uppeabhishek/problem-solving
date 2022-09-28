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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        n = len(s)
        
        g = Graph(n)
        
        for x, y in pairs:
            g.union(x, y)
        
        char_dictionary = defaultdict(list)
        index_dictionary = defaultdict(list)
        
        for i, c in enumerate(s):
            find_index = g.find(i)
            current = s[find_index]  
                        
            char_dictionary[find_index].append(c)
            index_dictionary[find_index].append(i)
        
        result = [None] * n

        
        for key, value in char_dictionary.items():
            char_dictionary[key] = sorted(char_dictionary[key])
            for i, v in enumerate(index_dictionary[key]):
                result[v] = char_dictionary[key][i]
                
        return "".join(result)
            
        
        
        