class Solution:
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        
        for key, value in c.items():
            c[key] = key * value
            
        max_num = max(c)
               
        @cache
        def dp(index):
            
            if index < 0:
                return 0
            
            ele = c[index] if index in c else 0
                
            first = dp(index - 1)
            second = ele + dp(index - 2)
            
            return max(first, second)
            
        
        return dp(max_num)