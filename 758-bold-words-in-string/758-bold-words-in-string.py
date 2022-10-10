import re 

class Solution:
    
    def mergeIntervals(self, intervals):
        if not len(intervals):
            return []
        
        intervals.sort(key = lambda k: k[0])
        new_intervals = [intervals[0]]
        index = 0
                
        for i in range(1, len(intervals)):
            if intervals[i][0] <= new_intervals[index][1] or intervals[i][0] - new_intervals[index][1] == 1:
                if intervals[i][1] > new_intervals[index][1]:       
                    new_intervals[index][1] = intervals[i][1]
            else:
                new_intervals.append(intervals[i])
                index+=1
                
        return new_intervals
        
    
    def boldWords(self, words: List[str], s: str) -> str:
        
        array = []
        
        for word in words:
            start = 0
            
            for i in range(len(s)):
                i = s.find(word, start)
                if i != -1:
                    array.append([i, i + len(word) - 1])
                    start = i + 1
                else:
                    break      
                
        intervals = self.mergeIntervals(array)
                
        result = []
        index = 0
        n = len(intervals)
        
        for i in range(len(s)):
            if index < n:
                if intervals[index][0] == i:
                    result.append("<b>")
                elif intervals[index][1] + 1 == i:
                    result.append("</b>")
                    index += 1
            
            result.append(s[i])
        
        if index < len(intervals):
            result.append("</b>")
            index += 1
        
        return "".join(result)