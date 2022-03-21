class Solution:
    def mergeIntervals(self, intervals):
        intervals.sort(key = lambda k: k[0])
        new_intervals = [intervals[0]]
        index = 0
                
        for i in range(1, len(intervals)):
            if intervals[i][0] <= new_intervals[index][1]:
                if intervals[i][1] > new_intervals[index][1]:       
                    new_intervals[index][1] = intervals[i][1]
            else:
                new_intervals.append(intervals[i])
                index+=1
        
        return new_intervals
           
                    
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i, c in enumerate(s):
            if c not in dic:
                dic[c] = [i, i]
            else:
                dic[c][1] = i
        
        intervals = []
        
        for _,value in dic.items():
            intervals.append(value)
        
        intervals = self.mergeIntervals(intervals)
        
        return [(interval[1] - interval[0] + 1) for interval in intervals]