class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n
        
    def addEdge(self, src, dest, dist):
        self.graph[src].append((dest, dist))
        
        
    def BFS(self, src, dest, k):
        
        min_distance = sys.maxsize
        
        queue = deque([(src, 0, -1)])
                
        stops = -1
        
        visited = defaultdict(int)
        visited[src] = 0
        
        while len(queue):
            
            node, distance, stops = queue.popleft()
            
            if node == dest:
                min_distance = min(min_distance, distance)
            
            if stops == k:
                continue
                        
            for current in self.graph[node]:
                nxt_node, nxt_distance = current

                if nxt_node not in visited or (nxt_node in visited and visited[nxt_node] > nxt_distance + distance):
                    queue.append((nxt_node, nxt_distance + distance, stops + 1))
                    visited[nxt_node] = nxt_distance + distance
        
        return -1 if min_distance == sys.maxsize else min_distance
    
    def getGraph(self):
        return self.graph

    
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
                        
        g = Graph(n)
        
        for flight in flights:
            g.addEdge(flight[0], flight[1], flight[2])
        
        return g.BFS(src, dst, k)