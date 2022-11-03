class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        j = 0
        
        while i < len(nums) - 1:            
            if nums[i] != nums[i + 1]:
                nums[j] = nums[i]
                j += 1
            
            i += 1
        
        nums[j] = nums[i]
        
        return j + 1

                
            