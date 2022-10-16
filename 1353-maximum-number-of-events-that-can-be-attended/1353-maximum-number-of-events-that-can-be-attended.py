from heapq import heappush, heappop

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        
        min_days, max_days = sys.maxsize, -sys.maxsize
        
        for i, j in events:
            min_days = min(min_days, i)
            max_days = max(max_days, j)
            
        
        heap = []
        index = 0
        result = 0
        
        for day in range(min_days, max_days + 1):
            
            while index < len(events) and events[index][0] == day:
                heappush(heap, events[index][1])
                index += 1
            
            while heap and heap[0] < day:
                heappop(heap)
            
            if heap:
                heappop(heap)
                result += 1
        
        return result
            
            
            
            
        