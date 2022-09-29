class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def helper(i):
            if i < 0:
                return 0
            
            return max(helper(i - 1), nums[i] + helper(i - 2))
        
        return helper(len(nums) - 1)