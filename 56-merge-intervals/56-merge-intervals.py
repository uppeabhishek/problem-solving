class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda k: k[0])
        result = []
        prev = 0
        for i in range(len(intervals)):
            if i + 1 < len(intervals):
                if intervals[i + 1][0] > intervals[i][1]:
                    result.append([intervals[prev][0], intervals[i][1]]) 
                    prev = i + 1  
                else:
                    intervals[i + 1][1] = max(intervals[i + 1][1], intervals[i][1])
            else:
                result.append([intervals[prev][0], intervals[i][1]])
        
        return result
    
            
        