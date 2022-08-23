class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result = max(nums)
        
        curMin, curMax = 1, 1
        
        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            
            temp = curMax
            
            curMax = max(curMin * num, curMax * num, num)
            curMin = min(curMin * num, temp * num, num)
        
            result = max(result, curMin, curMax)
        
        return result