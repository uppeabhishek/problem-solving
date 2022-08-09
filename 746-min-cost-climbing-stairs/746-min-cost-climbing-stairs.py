class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = {}
        
        def dp(cost, index):
            
            if index in cache:
                return cache[index]
            
            if index < 2:
                return cost[index]
                        
            first = dp(cost, index - 1)
            second = dp(cost, index - 2)
                        
            cache[index] = cost[index] + min(first, second)
            
            return cache[index]
        
        return min(dp(cost, len(cost) - 1), dp(cost, len(cost) - 2))
            
            
                
            