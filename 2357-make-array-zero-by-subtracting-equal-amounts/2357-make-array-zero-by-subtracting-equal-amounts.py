class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        nums.sort()
        cnt = 0
        
        for i in range(n):
            is_subtracted = False
            current = nums[i]
            for j in range(i, n):
                                
                if current > 0 and nums[j] - current >= 0:
                    is_subtracted = True

                nums[j] = max(0, nums[j] - current)
            
            if is_subtracted:
                cnt += 1
        
        return cnt