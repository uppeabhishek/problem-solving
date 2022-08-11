class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        if not nums[0]:
            return False
        
        res = [False] * len(nums)
        
        res[0] = True
        
        last_max = 0
        
        for i in range(len(nums) - 1):
            if nums[i]:
                
                if last_max < i:
                    break
                    
                next_index = min(i + nums[i], len(nums) - 1)
                res[next_index] = True
                last_max = max(last_max, next_index)
        
                
        return res[-1]
                