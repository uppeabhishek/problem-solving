class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        if n == 1:
            return 1
        
        nums.sort()
        
        i, j = 0, 1
        
        cnt = 1
        
        while j < n:
            if nums[j] - nums[i] <= k:
                j += 1
            else:
                cnt += 1
                i = j
        
        return cnt
        
        