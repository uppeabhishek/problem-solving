class Graph:
    
    def __init__(self, n): 
        self.blueGraph = defaultdict(list)
        self.redGraph = defaultdict(list)
        self.n = n
    
    def addEdge(self, u, v, isRed = False):
        if isRed:
            self.redGraph[u].append(v)
        else:
            self.blueGraph[u].append(v)

    def BFS(self, start, end, isRed = False):
        
        queue = deque([(start, 0, isRed)])
        
        result = defaultdict(int)
        
        for i in range(self.n):
            result[i] = sys.maxsize
        
        if isRed:
            redVisited = set([start])
            blueVisited = set()
        else:
            redVisited = set()
            blueVisited = set([start])
                
        while len(queue):
            
            top, distance, isRed = queue.popleft()
            
            if top in end:
                result[top] = min(result[top], distance)
                        
            if isRed:
                for ele in self.blueGraph[top]:
                    if ele not in blueVisited:
                        queue.append((ele, distance + 1, False))
                    blueVisited.add(ele)
            else:
                for ele in self.redGraph[top]:
                    if ele not in redVisited:
                        queue.append((ele, distance + 1, True))
                    redVisited.add(ele)
        
        return result
                    
    
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        
        g = Graph(n)
        
        for i, j in redEdges:
            g.addEdge(i, j, True)    
        
        for i, j in blueEdges:
            g.addEdge(i, j)
        
        endResult = set([i for i in range(n)])
        
        redResult = g.BFS(0, endResult, True)
        blueResult = g.BFS(0, endResult)

        result = []
        
        for i in range(n):
            min_val = min(redResult[i], blueResult[i])
            if min_val == sys.maxsize:
                result.append(-1)
            else:
                result.append(min_val)
        
        return result
         
        