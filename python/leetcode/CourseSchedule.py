from collections import defaultdict
from typing import List


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, u, visited):
        print(u)
        visited.add(u)
        for u in self.graph[u]:
            if u not in visited:
                self.DFSUtil(u, visited)

    def DFS(self):
        visited = set()
        for key in self.graph:
            if key not in visited:
                self.DFSUtil(key, visited)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = Graph()

        for p in prerequisites:
            print(p)
            g.addEdge(p[1], p[0])

        g.DFS()


s = Solution()
s.canFinish(2, [[1, 0]])
