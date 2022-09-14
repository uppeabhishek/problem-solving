class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def getDiff(first, second):
                        
            hour1, minute1 = list(map(int, first.split(":")))
            
            hour2, minute2 = list(map(int, second.split(":")))
                
            if minute2 < minute1:
                result = (hour2 - hour1) * 60 - (minute1 - minute2)
            else:
                result = (hour2 - hour1) * 60 + minute2 - minute1
                        
            return min(result, 1440 - result)
        
            
        n = len(timePoints)
        
        timePoints.sort()
        
        result = sys.maxsize
        
        for i in range(n - 1):
            result = min(result, getDiff(timePoints[i], timePoints[i + 1]))
        
        result = min(result, getDiff(timePoints[0], timePoints[i + 1]))
        
        return result