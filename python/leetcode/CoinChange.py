import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dp(amount):
            if amount == 0:
                return 0

            result = sys.maxsize

            for coin in coins:
                if coin <= amount:
                    currentResult = dp(amount - coin)

                    if currentResult != sys.maxsize and currentResult < result:
                        result = currentResult + 1

            return result

        print(dp(amount))


s = Solution()
s.coinChange([1,2], 11)
