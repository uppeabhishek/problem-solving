class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(amount):            
            if amount == 0:
                return 0
            
            result = sys.maxsize
            
            for coin in coins:
                if coin <= amount:
                    currentResult = dp(amount - coin)
                    if currentResult != -1 and currentResult < result:
                        result = currentResult + 1
                    
            return result

        res = dp(amount) 
        
        return res if res != sys.maxsize else -1
        