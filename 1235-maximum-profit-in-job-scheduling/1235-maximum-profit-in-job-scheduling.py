class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        startTime, endTime, profit = zip(*sorted(zip(startTime, endTime, profit)))
                
        n = len(startTime)
        
        def getNextJob(val, l, h):    
            result = n
            
            low, high = l,h
            
            while low <= high:
                mid = (low + high) // 2
                if startTime[mid] >= val:    
                    result = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            return result
        
        @cache
        def helperRecursion(index):
            if index == n:
                return 0
                        
            next_index = getNextJob(endTime[index], index + 1, n - 1)
            
            first = profit[index] + helperRecursion(next_index)
            second = helperRecursion(index + 1)
                        
            return max(first, second)
            
        return helperRecursion(0)            