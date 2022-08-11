from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
            
    def addNum(self, num: int) -> None:
        if not len(self.min_heap):
            heappush(self.min_heap, num)
        else:
            if num > self.min_heap[0]:
                heappush(self.min_heap, num)
                if len(self.min_heap) - len(self.max_heap) > 1:
                    heappush(self.max_heap, -heappop(self.min_heap))
            else:
                heappush(self.max_heap, -num)
                if len(self.max_heap) - len(self.min_heap) > 0:
                    heappush(self.min_heap, -heappop(self.max_heap))
                    
    def findMedian(self) -> float:        
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        
        return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()