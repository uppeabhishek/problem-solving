class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        for i in range (1, n + 1):
            res = res * i 
            res = res * (2 * i - 1)
            res = res % (10 ** 9 + 7)
        return res