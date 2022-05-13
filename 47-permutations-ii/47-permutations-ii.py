from copy import copy
class Solution:
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def helper(self, nums, index):
                
        if index == len(nums):
            self.result.add(tuple(nums))
    
        for i in range(index, len(nums)):
            self.swap(nums, i, index)
            self.helper(nums, index + 1)
            self.swap(nums, i, index)
        
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = set()
        self.helper(nums, 0)
        return self.result