class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        res = -1
        
        for i in range(len(nums)):
            
            nxt = abs(nums[i]) - 1
            
            
            if nums[nxt] < 0:
                res = nxt + 1
                break
                    
            nums[nxt] = nums[nxt] * -1
        
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        
        return res
                
            