class Solution:
    def myPow(self, x: float, n: int) -> float:

        cache = {}

        def helper(n1):

            if n1 in cache:
                return cache[n1]
            
            if n1 == 1:
                return x

            if n1 & 1 == 0:
                cache[n1] = helper(n1 // 2) * helper(n1 // 2)
                return cache[n1]

            cache[n1] = helper(n1 // 2) * helper(n1 // 2) * x
            return cache[n1]

        if n == 0:
            return 1
        
        if x == 0:
            return 0
        
        if n < 0:
            return 1 / helper(-n)
        return helper(n)