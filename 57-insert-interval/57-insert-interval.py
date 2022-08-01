class Solution:
    
    def mergeIntervals(self, intervals):
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
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not len(intervals):
            return [newInterval]
        
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                break
        
        while i > -1:
            if intervals[i][0] < newInterval[0]:
                break
            i -= 1
        
        start_i = max(0, i)
        
        while i < len(intervals):
            if newInterval[1] < intervals[i][0]:
                break
            i += 1
    
        end_i = i
                
        newIntervals = [newInterval] + intervals[start_i : end_i]
                
        return intervals[0 : start_i] + self.mergeIntervals(newIntervals) + intervals[end_i : ]
            
        