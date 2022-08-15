class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        @cache
        def helper(currentTarget):
            
            if currentTarget == 0:
                return 1
            
            result = 0
            
            for num in nums:
                if num <= currentTarget:
                    result += helper(currentTarget - num)
            
            return result
                
    
        return helper(target)