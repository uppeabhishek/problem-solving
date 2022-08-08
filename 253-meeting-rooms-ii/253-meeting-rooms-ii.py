from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda k: k[0])
        
        result = []
        
        heappush(result, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if result[0] <= intervals[i][0]:
                heappop(result)
                
            heappush(result, intervals[i][1])
    
        return len(result)