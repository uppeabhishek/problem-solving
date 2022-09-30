class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        lastJump, maxJump, i = 0, 0, 0
        
        res = -1
        
        while i < n:
            
            maxJump = max(maxJump, min(n - 1, i + nums[i]))
                        
            if i == lastJump:
                lastJump = maxJump
                res += 1    
            
            i += 1
        
        return res
            
            