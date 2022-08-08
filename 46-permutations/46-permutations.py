from copy import copy
class Solution:
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def helper(self, nums, index):
                
        if index == len(nums):
            self.result.append(copy(nums))
    
        for i in range(index, len(nums)):
            self.swap(nums, i, index)
            self.helper(nums, index + 1)
            self.swap(nums, i, index)
        
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.helper(nums, 0)
        return self.result