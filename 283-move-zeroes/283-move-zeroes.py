class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_index = sys.maxsize
        
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                zero_index = i
                break
            
        if zero_index == sys.maxsize:
            return
        
        zero_count = 0
        
        for i in range(n):
            if nums[i] != 0:
                if i > zero_index:
                    nums[zero_index] = nums[i]
                    zero_index = zero_index + 1  
            else:
                zero_count += 1
                    
        for i in range(n - zero_count, n):
            nums[i] = 0