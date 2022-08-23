class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        current = []
        
        temp = []  
        temp_sum = 1
        
        max_sum = 0
        
        for n in nums:
            if n == 0:
                if len(temp):
                    if temp_sum > 0:
                        max_sum = max(max_sum, len(temp))
                    else:
                        current.append(temp)
                    temp = []
                    temp_sum = 1
            else:
                temp.append(n)
                temp_sum *= n
        
        if temp_sum > 0:
            max_sum = max(max_sum, len(temp))
        else:
            current.append(temp)
                
        for cur in current:
                        
            prefix, suffix = 1, 1
            
            for i in range(len(cur)):
                if cur[i] < 0:
                    prefix = len(cur) - (i + 1)
                    break
            
            for i in range(len(cur) - 1, -1, -1):
                if cur[i] < 0:
                    suffix = i
                    break
                                        
            max_sum = max(max_sum, prefix, suffix)
            
        return max_sum
            
        
        