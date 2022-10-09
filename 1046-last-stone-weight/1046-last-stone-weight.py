from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
    
        for i in range(len(stones)):
            stones[i] = -stones[i]
    
        heap = stones
        
        heapify(heap)
        
        while len(heap) > 1:
            first, second = -heappop(heap), -heappop(heap)
            if first != second:
                heappush(heap, -abs(first - second))
        
        return -heap[0] if len(heap) else 0