class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left_i, right_i = -1, -2
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                left_i = i + 1
                right_i = i + 1
                break
        
        if left_i == -1:
            return 0
           
        current = nums[left_i]
        max_current_val = -sys.maxsize
        
        # find max after left index
        j = left_i
        
        while j < len(nums):
            if nums[j] < current:
                current = nums[j]
                left_i = j
            j += 1
    
        j = left_i
        
        # find min in left index
        while j > -1:
            if nums[j] > current:
                max_current_val = max(max_current_val, nums[j])
                left_i = j
            j -= 1
        
        # find max in right index
        nums[right_i] = max_current_val
        j = right_i
                
        while j < len(nums) - 1:
            if nums[j] > nums[j + 1]:
                nums[j + 1] = nums[j]
                right_i = j + 1
            j += 1
        
        return right_i - left_i + 1
                
                
        
        