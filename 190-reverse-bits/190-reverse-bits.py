class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        
        res = 0
        cnt = 0
        
        while n:
            if n & 1 == 1:
                current = 31 - cnt - 1
                if current < 0:
                    return res + 1
                res += (2 << current)
            n = n >> 1
            cnt += 1
        
        return res