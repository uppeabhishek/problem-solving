class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        @cache
        def helper(i, j):
            
            if i < j:
                return 0
            
            return max(helper(i - 1, j), nums[i] + helper(i - 2, j))
    
        return max(helper(n - 1, 1), helper(n - 2, 0))