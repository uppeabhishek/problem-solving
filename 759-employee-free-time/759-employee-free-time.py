"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        new_schedule = []
        
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                new_schedule.append(schedule[i][j])
        
        new_schedule.sort(key = lambda k: k.start)
        
        result = []
        
        max_end = 0
        
        for i in range(len(new_schedule) - 1):
            start, end, next_start = new_schedule[i].start, new_schedule[i].end, new_schedule[i + 1].start
            
            if end < next_start and next_start > max_end:
                result.append(Interval(start = max(max_end, end), end = next_start))
                
            max_end = max(end, max_end)
            
        return result
                
            