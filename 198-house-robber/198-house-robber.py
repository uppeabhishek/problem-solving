class Solution:
    
    def robHelper(self, nums, index, cache):
        
        if index in cache:
            return cache[index]
        
        if index == 0:
            return nums[index]
    
        if index == 1:
            return max(nums[index], nums[index - 1])
        
        first = self.robHelper(nums, index - 1, cache)
        second = nums[index] + self.robHelper(nums, index - 2, cache)
        
        cache[index] = max(first, second)
        
        return cache[index]
    
    def rob(self, nums: List[int]) -> int:
        cache = {}
        return self.robHelper(nums, len(nums) - 1, cache)