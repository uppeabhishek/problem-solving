class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:    
        
        min_val, max_val = sys.maxsize, -sys.maxsize
        
        for num in nums:
            if num > 0:
                if num < min_val:
                    min_val = num
                if num > max_val:
                    max_val = num
        
        if min_val != 1:
            return 1
        
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:    
                nums[i] = 1
                
        for i in range(len(nums)):
            index = nums[i]
            nxt = nums[abs(index) - 1]
                        
            if nxt > 0:
                nums[abs(index) - 1] = -1 * nxt
        
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        
        
        return max_val + 1