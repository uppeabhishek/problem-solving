from collections import defaultdict, deque


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

    def BFS(self):
        visited = set()
        queue = deque()
        for key in self.graph:
            if key not in visited:
                queue.append(key)
                visited.add(key)
                while len(queue):
                    top = queue.popleft()
                    print(top)
                    for ele in self.graph[top]:
                        if ele not in visited:
                            queue.append(ele)
                            visited.add(ele)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.DFS()
    print()
    g.BFS()
