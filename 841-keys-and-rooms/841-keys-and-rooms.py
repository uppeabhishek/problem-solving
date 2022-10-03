class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def getGraph(self):
        return self.graph
    
    def BFS(self, rooms):
        
        count = 0
        queue = deque([0])
        visited = set([0])
        
        while len(queue):
            top = queue.popleft()
            
            count += 1
            
            for room in rooms[top]:
                if room not in visited and room != top:
                    queue.append(room)
            
                visited.add(room)
        
        return count == len(rooms)
    
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        g = Graph()
        return g.BFS(rooms)
        
        
            