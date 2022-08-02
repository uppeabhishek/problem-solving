from heapq import heappush, heappop, heappushpop

class Solution:
    
    def distance(self, x1, y1, x2, y2):
        return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        x2, y2 = 0, 0
            
        
        for point in points:
            x1, y1 = point
            distance = self.distance(x1, y1, x2, y2)
                        
            if len(heap) == k:
                if -heap[0][0] > distance:
                    heappushpop(heap, (-distance, (point)))
            else:
                heappush(heap, (-distance, (point)))
            
        result = []
        
        for h in heap:
            result.append(h[1])
        
        return result
            