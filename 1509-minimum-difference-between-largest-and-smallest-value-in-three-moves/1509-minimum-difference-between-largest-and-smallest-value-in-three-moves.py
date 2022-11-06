class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 3:
            return 0
        
        nums.sort()
        
        i, j = 0, len(nums) - 1
                
        return min(nums[j] - nums[i + 3], nums[j - 3] - nums[i], nums[j - 2] - nums[i + 1], nums[j - 1] - nums[i + 2])
                
        
        