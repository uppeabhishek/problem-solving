class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum, max_sum = sys.maxsize, -sys.maxsize
        
        for i in range(len(nums)):
            
            if current_sum == sys.maxsize:
                current_sum = 0
            
            current_sum += nums[i]
            
            max_sum = max(current_sum, max_sum)

            if current_sum < 0:
                current_sum = 0
            
            
        return max_sum
    
        