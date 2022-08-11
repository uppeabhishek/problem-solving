class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def swap(i1, j1):
            temp = nums[i1]
            nums[i1] = nums[j1]
            nums[j1] = temp
        
        i, j, k = 0, 0, len(nums) - 1
        
        while j <= k:
            if nums[j] == 0:
                swap(i, j)
                i += 1
                j += 1
            elif nums[j] == 2:
                swap(j, k)
                k -= 1
            else:
                j += 1
        
        
            
        