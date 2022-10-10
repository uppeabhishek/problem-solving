from collections import defaultdict
from typing import List
from copy import copy

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.set1, self.set2 = set(), set()

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSHelper(self, u, visited, isSet1):

        visited.add(u)

        for v in self.graph[u]:
            if isSet1:
                if u in self.set2:
                    return False
                if v in self.set1:
                    return False

                self.set1.add(u)
                self.set2.add(v)
            else:
                if u in self.set1:
                    return False
                if v in self.set2:
                    return False

                self.set2.add(u)
                self.set1.add(v)

            if v not in visited:
                if not self.DFSHelper(v, visited, not isSet1):
                    return False

        return True

    def DFS(self):
        visited = set()
        
        for i in range(1, self.n + 1):
            if i not in visited:    
                if not self.DFSHelper(i, visited, True):
                    
                    self.set1, self.set2 = set(), set()
                    
                    visited = set()
                    
                    if not self.DFSHelper(i, visited, False):    
                        return False
                
        
        return True



class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = Graph(n)

        for u, v in dislikes:
            g.addEdge(u, v)

        return g.DFS()
    