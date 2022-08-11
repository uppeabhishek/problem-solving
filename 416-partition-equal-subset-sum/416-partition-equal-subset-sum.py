class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        current_sum = sum(nums)
        
        if current_sum & 1 == 1:
            return False
        
        half_sum = current_sum // 2
                
        @lru_cache(maxsize=None)
        def top_dp(index, result):
                        
            if index < 0 or result < 0:
                return False
            
            if result == 0:
                return True
            
            return top_dp(index - 1, result - nums[index - 1]) or top_dp(index - 1, result)
                        
        n = len(nums)
            
        def bottom_dp():
            
            dp = [[False for _ in range(n)] for _ in range(n)]
            
            for i in range(n + 1):
                for j in range(n + 1):
                    if i == 0 or j == 0:
                        continue
                    
            
        return top_dp(n - 1, half_sum)            
        